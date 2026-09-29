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

Produce one complete campaign brief document. This is the operational handover document — it tells the execution team exactly what to make, to what specifications, by when, and to whose approval. It does not decide the campaign strategy; that is the role of `09-campaign-strategy`. Apply the `east-african-english` skill for tone throughout. Do not generate the brief until all Required Input has been confirmed.

**Distinction from 09-campaign-strategy:** Use `09-campaign-strategy` to decide WHAT campaign to run, who it is for, and what it needs to achieve. Use this skill (13-campaign-brief) to brief WHO will create the campaign content, HOW it should look and sound, and WHEN everything is due. The brief is a working document — it travels with the campaign from kickoff to sign-off.


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
|---|---|---:|---|
| Approved 09-campaign-strategy, production constraints, owners and deadlines | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Operational campaign brief with owners, deliverables and approvals | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified operational campaign brief with owners, deliverables and approvals. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Approved 09-campaign-strategy, production constraints, owners and deadlines is current and attributable | Produce the full operational campaign brief with owners, deliverables and approvals and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `09-campaign-strategy` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `09-campaign-strategy` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the operational campaign brief with owners, deliverables and approvals, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.
7. Complete the [reader-first content brief](references/reader-first-content-brief.md) and [content evidence and rights record](references/content-evidence-and-rights-record.md) for each production unit. Quarantine unsupported claims, missing rights, mismatched destinations or unassessed review states.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the operational campaign brief with owners, deliverables and approvals without approved 09-campaign-strategy. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `09-campaign-strategy` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified approved 09-campaign-strategy, the skill produces a operational campaign brief with owners, deliverables and approvals with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`09-campaign-strategy`](../09-campaign-strategy/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- [Reader-first content brief](references/reader-first-content-brief.md)
- [Content evidence and rights record](references/content-evidence-and-rights-record.md)
- [Finished campaign exemplars](../../../docs/world-class-exemplars/campaign-exemplars.md)
- [Creative review gate](../../../docs/quality-gates/creative-review-gate.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Input

Ask for the following before generating:

- **Campaign name** — the internal working title of the campaign
- **Campaign dates** — start and end date (including any pre-launch teaser period and post-campaign analysis window)
- **Client name** — trading name of the business
- **Target persona** — the persona name from `03-audience-personas` this campaign is aimed at
- **Key message** — the single sentence the audience must feel or understand after seeing this campaign
- **Deliverables required** — list all assets required (e.g., Facebook feed graphic ×4, Instagram reel ×2, WhatsApp broadcast copy ×3, caption set ×8)
- **Team and partner names and roles** — who is responsible for what (designer, copywriter, videographer, social media manager, client-side approver)
- **Approval contacts** — who reviews first drafts; who gives final sign-off
- **Budget per deliverable type** — amount allocated per asset type (e.g., graphic design: UGX 500,000; video production: UGX 1,200,000)
- **Country/city** — defaults to Kampala, Uganda

---

## Brief Document Structure

Generate all ten sections in order. Each section is clearly headed. Do not omit any section. The complete brief must read as a single, coherent document that any qualified team member could pick up and act on without further explanation.

---

### Section 1: Campaign Background and Objective

Write 3–4 sentences covering:
- What this campaign is about — the product, service, event, or message being promoted
- Why it is happening now — the business reason, seasonal moment, or strategic trigger
- What success looks like — the primary outcome the campaign must achieve
- How this campaign connects to the broader social media strategy or business goal

Write in plain, direct prose. Avoid marketing clichés. A new team member must understand the full context from this section alone.

---

### Section 2: Target Audience

State:
- **Persona name** — from `03-audience-personas`
- **3 defining characteristics relevant to this specific campaign** — not a full persona profile; only the characteristics that affect how this campaign should look, sound, or be delivered. Examples: "Price-sensitive; responds to value framing", "Mobile-first; consumes content in 15-second windows", "Aspirational; wants to see themselves in the brand"

Record evidence for the audience's use of each proposed channel and how it changes delivery. If account, survey or other audience evidence is absent, mark channel fit `NOT_ASSESSED`; do not infer preference or reach from Uganda/East Africa location alone.

---

### Section 3: Key Message

State one sentence only. This is the core message — what the audience must feel or understand after seeing this campaign. It is not the slogan or tagline; it is the strategic truth the creative must express.

Format:
> **Key message:** [One sentence]

Below the key message, add a two-sentence explanation: what this message achieves for the brand, and what it asks of the audience. This guides the creative team when making execution decisions.

---

### Section 4: Campaign Concept

Describe the creative idea in 2–3 sentences. State:
- What makes this campaign distinctive — the hook, the format, the storytelling approach
- The creative territory (emotional, functional, humorous, documentary, testimonial, etc.)
- Any specific creative device to be used consistently across all deliverables (e.g., a recurring character, a visual colour treatment, a campaign hashtag, a question-led structure)

This section does not produce design briefs — it sets the creative direction so all deliverables feel unified.

---

### Section 5: Deliverables List

Produce a table listing every asset required. Every deliverable mentioned in the Required Input must appear in this table.

| Deliverable | Platform and placement | Format | Official specification source and access date | Quantity | Due date | Owner |
|---|---|---|---|---|---|---|
| [Required asset from the approved strategy] | [Organic/paid placement] | [Text/image/video/etc.] | [Official source, version/page date, access date; or NOT_ASSESSED] | [Count] | [Agreed date] | [Named owner/role] |

List only deliverables required by the approved strategy. Do not assume that every channel or format is in scope. Do not copy fixed dimensions, durations, file limits, text limits, or format availability from an old brief. Populate the technical specification from the official current source for the exact platform, account and placement; if it cannot be verified, omit the value and mark it `NOT_ASSESSED`.

---

### Section 6: Content Specifications Per Deliverable

#### Platform specifications and copy

Do not embed default dimensions, file sizes, durations, aspect ratios, character limits, hashtag counts or "optimal" lengths in a campaign brief. They can vary by organic/paid placement, account, device, region and product change. Route current specifications through the canonical [Facebook](../../platforms/platform-facebook/SKILL.md), [Instagram](../../platforms/platform-instagram/SKILL.md), [LinkedIn](../../platforms/platform-linkedin/SKILL.md) or [TikTok](../../platforms/platform-tiktok/SKILL.md) skill, then verify the official source and intended account/placement when preparing production files. Record the source, source date or version where shown, access date, scope and recheck trigger. If a page or account cannot be checked, mark the specific specification `NOT_ASSESSED` and leave it out of the executable handoff.

Write copy to carry one audience need and one communication job. Do not force a word count, hashtag quota or CTA onto every unit. Include a CTA only when it follows from the approved offer, the destination works, and a named owner can handle the response. Check the live platform limit before final production; platform limits are not copy-length recommendations.

Treat accurate captions or an equivalent text alternative as a production accessibility requirement for spoken or audio-dependent video. Review automated captions for errors and test the rendered asset in its intended placement. This is an accessibility control for the deliverable, not a statement that every platform offers the same caption tool or that captions substitute for commercial, partnership or legal disclosure.

For graphics, use only approved brand assets and licensed or owned media. A logo is optional unless the approved identity or brief requires it. Keep essential information in accessible copy as well as the visual, and record alt text, contrast and render review with the design owner. Never imply that a visual has been reviewed when no render exists.

---

### Section 7: Brand Do's and Don'ts

Reference the `04-brand-voice-intake` document. Produce a campaign-specific summary — not a generic list that could apply to any brand.

**Do's — 5 rules for this campaign:**
1. [Specific to client and campaign — e.g., "Use the campaign hashtag on every post across all platforms"]
2. [Tone guidance — e.g., "Keep the tone warm and community-led; this audience responds to human stories, not corporate announcements"]
3. [Visual guidance — e.g., "Lead every graphic with a real person — no stock photography in this campaign"]
4. [Language guidance — e.g., "Use 'you' and 'we' — speak directly to the reader"]
5. [Platform-specific — e.g., "On WhatsApp, open every broadcast with a personal greeting; do not start with the product offer"]

**Don'ts — 5 rules for this campaign:**
1. [Specific restriction — e.g., "Do not reference competitor pricing — legal risk and off-brand"]
2. [Tone restriction — e.g., "Do not use pressure language: 'last chance', 'you're missing out' — this audience disengages from urgency tactics"]
3. [Visual restriction — e.g., "Do not use the hero image on a dark background — it loses detail at mobile resolution"]
4. [Language restriction — e.g., "Do not use the word 'cheap' — it conflicts with the premium brand positioning"]
5. [Platform restriction — e.g., "Do not post the same caption across Facebook and Instagram unchanged — adapt the tone for each platform"]

---

### Section 8: Timeline with Deadlines

Produce a table covering the full campaign lifecycle: pre-production, production, review, approval, and live dates.

| Milestone | Deliverable | Deadline | Owner |
|---|---|---|---|
| Campaign kickoff | Brief shared with all team members | [Date] | [Social media manager / account manager] |
| First drafts — graphics | Static images for all platforms | [Date] | [Designer name] |
| First drafts — copy | All captions and broadcast copy | [Date] | [Copywriter name] |
| First drafts — video | Raw cut of all video content | [Date] | [Videographer name] |
| Internal review | All first drafts reviewed by lead | [Date] | [Lead name] |
| Client review — Round 1 | All materials submitted to client | [Date] | [Account manager] |
| Revisions complete | All feedback incorporated | [Date] | [Designer / Copywriter / Videographer] |
| Final approval | Client signs off all materials | [Date] | [Client approver name] |
| Content scheduled | All posts scheduled in publishing tool | [Date] | [Social media manager] |
| Campaign goes live | First post published | [Date] | [Social media manager] |
| Campaign closes | Last post published | [Date] | [Social media manager] |
| Post-campaign report | Performance summary delivered | [Date + 7 days] | [Analytics lead] |

Populate dates from the campaign dates provided in the Required Input. If specific names are not yet confirmed, use role titles and add a note: "Assign names at kickoff meeting."

---

### Section 9: Approval Process

State clearly:

- **First reviewer** — [Name and role]: reviews all first drafts within [N] working days and returns consolidated feedback (not multiple rounds of partial feedback)
- **Final approver** — [Name and role]: gives final sign-off within [N] working days of receiving revised materials
- **Approval method** — [e.g., shared Google Drive folder with comment access / email sign-off / Trello card / WhatsApp confirmation followed by email confirmation]
- **If feedback is late:** If the client or approver does not respond within the agreed window, the campaign timeline moves by the same number of days. Document this in a brief note to the client. Pause production — do not guess what the client wants.
- **Emergency sign-off:** For time-sensitive reactive posts within the campaign, the account manager may approve with a voice note confirmation from the client, followed by written confirmation within 24 hours.

---

### Section 10: Success Metrics

State one primary KPI and three supporting KPIs. For each, provide the baseline (current performance before the campaign) and the target (what the campaign must achieve).

| KPI | Baseline | Target | How It Is Measured |
|---|---|---|---|
| **Primary KPI:** [e.g., Enquiries generated] | [e.g., 12 per month average] | [e.g., 40 during campaign period] | [e.g., WhatsApp enquiry count + form submissions] |
| Supporting KPI 1: [e.g., Post reach] | | | |
| Supporting KPI 2: [e.g., Engagement rate] | | | |
| Supporting KPI 3: [e.g., Link clicks] | | | |

Add a one-sentence note on how results will be reported: when the post-campaign report will be delivered, in what format, and to whom.

---

## Quality Criteria

- All ten sections are present and complete; no section is left blank or contains a placeholder without a note explaining what must be filled in at kickoff
- Deliverables table accounts for every asset mentioned in the Required Input — nothing is omitted
- Each technical platform specification has current official-source and intended-placement evidence, or is omitted and marked `NOT_ASSESSED`
- Spoken or audio-dependent video has reviewed captions or an equivalent text alternative; rendered accessibility and native-size preview evidence are recorded before production approval
- The key message is one sentence only and is clearly distinct from the campaign slogan or tagline
- Brand do's and don'ts are campaign-specific and reference the client's actual brand voice — not generic rules applicable to any campaign
- The timeline table covers the full lifecycle from kickoff to post-campaign report, with realistic sequencing between review and production stages
- The approval process states what happens when feedback is late — ambiguity here is a common cause of campaign delays
- Success metrics include baselines and targets; a KPI without a target is not a KPI

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

### How to apply at sign-off

Add a "Five Outcomes" subsection to the campaign brief. For each outcome, record `pass`, `fail` or `NOT_ASSESSED` and cite the evidence. The affected deliverable cannot ship unless every applicable outcome passes:

- Useful — [pass/fail/NOT_ASSESSED], because [persona goal and asset evidence]
- Easy — [pass/fail/NOT_ASSESSED], because [audience comprehension evidence or gap]
- Efficient — [pass/fail/NOT_ASSESSED], because [tested delivery context and equivalent text route where needed]
- Pleasing — [pass/fail/NOT_ASSESSED], because [approved visual reference and reviewed render]
- Accessible — [pass/fail/NOT_ASSESSED], because [image description, caption/text alternative and applicable contrast check evidence]

If an outcome fails, return the affected deliverable to the strategy, content or design owner to close the gap. If evidence is missing, retain `NOT_ASSESSED` and withhold release.

Accessibility evidence is part of production approval. If the asset has not been rendered or its relevant accessibility checks have not been reviewed, keep the outcome `NOT_ASSESSED` and do not present the deliverable as ready.

## Bounded example

See [the synthetic Ugandan small-retailer discussion example](examples/synthetic-retail-discussion-unit.md). It demonstrates channel adaptation and evidence boundaries; it is not an approved strategy, a complete campaign brief, or authority to publish.

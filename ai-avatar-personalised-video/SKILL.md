---
name: ai-avatar-personalised-video
description: >
  Generates an operational guide and all supporting content — tool selection
  rationale, avatar design brief, scripts, use-case plans, and distribution
  protocol — for deploying AI avatar video at scale in B2B outreach, client
  communications, and social content production. Invoke when a client wants
  to use AI-generated video for personalised outreach or branded video content,
  when production time on talking-head video needs to be reduced, or when a
  scalable video communications system is being built.
---
# AI Avatar Personalised Video

<!-- dual-compat:start -->
## Use when
- Generates an operational guide and all supporting content — tool selection rationale, avatar design brief, scripts, use-case plans, and distribution protocol — for deploying AI avatar video at scale in B2B outreach, client communications, and social content production. Invoke when a client wants to use AI-generated video for personalised outreach or branded video content, when production time on talking-head video needs to be reduced, or when a scalable video communications system is being built.
- Use this skill when it is the closest match to the requested deliverable or workflow.

## Do not use when
- Do not use this skill for graphic design, video production, software development, or legal advice beyond the repository's stated scope.
- Do not use it when another skill in this repository is clearly more specific to the requested deliverable.

## Workflow
1. Collect the required inputs or source material before drafting, unless this skill explicitly generates the intake itself.
2. Follow the section order and decision rules in this `SKILL.md`; do not skip mandatory steps or required fields.
3. Review the draft against the quality criteria, then deliver the final output in markdown unless the skill specifies another format.

## Anti-Patterns
- Do not invent client facts, performance data, budgets, or approvals that were not provided or clearly inferred from evidence.
- Do not skip required inputs, mandatory sections, or quality checks just to make the output shorter.
- Do not drift into out-of-scope work such as code implementation, design production, or unsupported legal conclusions.

## Outputs
- An AI-focused strategy, audit, system design, or prompt asset in markdown with human review and control points.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Purpose

Produce operational plans and production-ready scripts for AI avatar video
deployments using Synthesia, HeyGen, Tavus, D-ID, or Elai.io. Output covers
tool selection, avatar design, script writing, distribution, and disclosure
compliance. Every deliverable is sized for the East African market by default.

> Roth, H. and neuroflash Team (2024/2025) *AI Strategy 2025 for Marketing
> Teams*. neuroflash. [Statistics on video outreach performance cited below]

---

## Required Input

Before generating any deliverable, ask for:

1. **Client business name** and industry
2. **Country and city** (default: Uganda / Kampala)
3. **Primary goal** — outreach at scale, client communications, social content,
   or onboarding/training
4. **Volume required** — estimated number of videos per month and whether
   personalisation per recipient is needed
5. **Existing human presenter** — is there a real person whose voice and
   likeness the avatar should represent, or will a stock avatar be used?
6. **Budget tier** — indicative monthly budget in USD (see platform pricing below)

---

## Section 1 — Tool Selection Guide

### Platform Comparison

| Platform | Best for | Avatar creation | Languages | Free tier |
|---|---|---|---|---|
| Synthesia | Corporate training, branded explainers, polished templates | 230+ stock avatars; custom avatar from upload | 140+ | No (14-day trial) |
| HeyGen | B2B video outreach, language localisation, scalable personalisation | Instant from 60-second clip | 40+ | Yes (1 free video/month) |
| Tavus | 1:1 personalised video at scale (unique video per recipient) | Clone from 5-minute recording | English primary | No |
| D-ID | Talking-head from photo; fast turnaround; no minimum commitment | Animated photo or uploaded image | 119 | Yes (20 credits free) |
| Elai.io | Volume production at lower cost; best value for EA price point | Custom avatar from video upload | 75+ | Yes (1 free video/month) |

### Selection Rules

Apply these rules to select the right platform before starting production:

- **Outreach volume > 100 personalised videos/month:** Use Tavus. Each recipient
  receives a unique video with their name, company, and a personalised line.
- **Polished evergreen content (training, onboarding, explainers):** Use Synthesia.
  Templates are the strongest in the market; avatar quality is broadcast-standard.
- **Language localisation required (Swahili, French, Luganda voiceover):**
  Use HeyGen. Its translation feature re-lips the avatar in the target language
  from a single English recording.
- **Quick turnaround from a single photo, minimum budget:** Use D-ID. Ideal for
  one-off client communications or prototype testing.
- **Volume production on a constrained budget (under USD 50/month):** Use Elai.io.
  The price-to-output ratio is the strongest for high-frequency social content.

### EA Pricing Reference (March 2026)

| Platform | Entry paid plan | Approx. UGX/month |
|---|---|---|
| Synthesia | USD 29/month (Starter — 10 min video/month) | ~UGX 107,000 |
| HeyGen | USD 29/month (Creator — 15 credits) | ~UGX 107,000 |
| Tavus | USD 150/month (Starter) | ~UGX 555,000 |
| D-ID | USD 9/month (Lite — 10 min) | ~UGX 33,000 |
| Elai.io | USD 23/month (Basic — 15 min) | ~UGX 85,000 |

Flag: all platforms require payment by international card or PayPal. MTN Mobile
Money payment is not directly supported; use Payoneer or Wise to fund an
international card from a Mobile Money wallet.

---

## Section 2 — Avatar Design to Brand Specification

### Wardrobe and Visual Identity

- Specify wardrobe colour in the design brief using the client's primary brand
  colour hex code; most platforms allow uploading reference images.
- Avoid busy patterns or small checks — they compress poorly in MP4 output.
- Logo placement: Synthesia and HeyGen support branded backgrounds with logo
  overlays; for platforms that do not, use a branded frame in Canva applied
  in post-production.
- Professional register must match the sector: formal attire for financial
  services and legal; smart-casual for technology and creative sectors;
  branded casual (polo shirt with embroidery) for retail and FMCG.

### Background

- **Branded background:** Use the client's office, a branded set mockup, or a
  solid brand-colour background. Synthesia, HeyGen, and Elai.io all support
  custom background image uploads.
- **Neutral background:** A plain white, grey, or dark studio background works
  for B2B outreach where the message must carry the video, not the visual.
- D-ID does not support custom backgrounds natively; apply background via
  CapCut or Canva's video editor before distribution.

### Voice: ElevenLabs Integration

Where the client has a human presenter whose voice should match the avatar:

1. Record the presenter reading a 3–5 minute voice sample (clear, neutral pace,
   no background noise, on a phone in a quiet room is sufficient).
2. Upload to ElevenLabs Voice Cloning (Starter plan: USD 5/month).
3. Export the cloned voice as an MP3 and import into Synthesia, HeyGen, or
   Elai.io via their "custom voice" upload function.
4. Test with a 30-second sample video before full production.
5. Specify pace in the ElevenLabs settings: 0.9x speed is optimal for East
   African professional audiences; 1.0x can read as rushed.

### Approval Protocol

Obtain written client sign-off (email confirmation is sufficient) on:

1. Avatar appearance (screenshot from the platform's preview)
2. Voice sample (30-second MP3)
3. Disclosure language (see Section 6)
4. One full pilot video before any volume production begins

Do not proceed to volume production without approval at each stage.

---

## Section 3 — Script Writing for AI Avatars

Script quality is the primary determinant of avatar video quality. AI avatar
delivery requires a fundamentally different structure to live video.

### Core Rules

- **Sentence length:** 15 words maximum per sentence. Break longer sentences
  at natural breath points.
- **No compressed contractions:** Avoid "I'd've", "we'd've", "they'd've" — write
  "I would have", "we would have". Standard contractions (I'm, we're, it's) are
  acceptable.
- **No idioms:** Avoid "hit the ground running", "move the needle", "circle back".
  Write the plain meaning: "start immediately", "improve results", "follow up".
- **Pause markers:** Insert `[PAUSE]` wherever a human speaker would breathe,
  hesitate, or let a point land.
- **Emotional register instructions:** Open with a register instruction in
  parentheses — e.g. `(warm, direct)` or `(confident, measured)`. Insert a new
  instruction before any tonal shift — e.g. `(slight urgency)` before the CTA.
- **EA register:** Avoid English idioms that do not translate to the East African
  professional context. Write in the tone expected in an EA boardroom: direct,
  respectful, and specific.

### Length Limits

- **Outreach video (cold or warm B2B):** 60–90 seconds maximum. Anything longer
  loses the recipient before the CTA.
- **Client communications (e.g. monthly report summary):** 90–120 seconds.
- **Onboarding or training explainer:** Up to 3 minutes. Longer content must
  be broken into chapters (each chapter = a separate video file).
- **Social content (Reels, TikTok, Facebook short video):** 30–60 seconds.

### Script Template — B2B Outreach (60–90 seconds)

```
(warm, direct)
Hello [FIRST NAME]. [PAUSE]

My name is [PRESENTER NAME] from [COMPANY].

I noticed [ONE SPECIFIC, RESEARCHED OBSERVATION ABOUT THEIR BUSINESS]. [PAUSE]

We help [TARGET AUDIENCE DESCRIPTION] to [PRIMARY OUTCOME].

[PAUSE]

One of our clients, [CLIENT REFERENCE], achieved [SPECIFIC RESULT] in [TIMEFRAME].

(slight urgency)
I would like to show you how we could do the same for [THEIR COMPANY NAME].

[PAUSE]

Reply to this message and I will send you a 20-minute briefing. [PAUSE]

Thank you.
```

### Script Template — Monthly Report Summary (90–120 seconds)

```
(professional, warm)
Hello [CLIENT NAME] team. [PAUSE]

Here is your [MONTH] performance summary. [PAUSE]

This month, your top-performing content was [POST TITLE OR DESCRIPTION].
It reached [REACH FIGURE] people and generated [ENGAGEMENT FIGURE] interactions.

[PAUSE]

Your follower growth was [FIGURE] — [UP/DOWN] [PERCENTAGE] from last month.

(direct, confident)
Three priorities for [NEXT MONTH]: [PRIORITY 1]. [PAUSE] [PRIORITY 2].
[PAUSE] And [PRIORITY 3].

[PAUSE]

The full report is attached. [PAUSE]
I am available Thursday if you would like to discuss any of this.

Thank you.
```

---

## Section 4 — Use Cases with EA Application

### B2B Video Outreach

Personalised video emails achieve 75% open rates and up to 40% response rates,
compared to 21% average open rates for text-only emails (Roth and neuroflash
Team, 2024/2025).

- **Tool:** HeyGen (for variable personalisation with the recipient's name and
  company inserted via CSV) or Tavus (for fully unique video per recipient).
- **Personalisation variables:** First name, company name, one researched
  observation about their business (sourced from their LinkedIn or website).
- **Distribution:** LinkedIn InMail with video thumbnail embedded + follow-up
  email with GIF preview. Do not attach the raw MP4; host on Loom, Vimeo, or
  the platform's share link and embed the thumbnail.
- **EA application:** B2B outreach in Uganda/Kenya is relationship-led. Lead
  with a warm, specific observation before any product or service mention.
  A generic "I saw your company" opener will not perform in this market.

### Client Communications

- Monthly performance report as a 2-minute avatar video from the account
  manager. Replaces or supplements the PDF report.
- Use the account manager's own avatar (HeyGen custom avatar from a 60-second
  clip) so the client sees a familiar face.
- Distribute via WhatsApp (under 10MB MP4) and email (thumbnail link).
- EA application: personalised video report increases perceived value of the
  retainer. Clients who see a face presenting results are less likely to
  question the agency fee.

### Onboarding

- Welcome video for new clients: 90-second avatar video from the managing
  director, welcoming the client and confirming the first three steps.
- Platform training introduction: a 3-minute explainer on how to read their
  monthly dashboard or how to request content amendments.
- Use Synthesia for evergreen onboarding content — the polished templates
  are appropriate for a first impression.

### Social Content

- Short branded videos for Instagram Reels (30 seconds), TikTok (30–45 seconds),
  and Facebook (45–60 seconds).
- The avatar handles the talking-head element; pair with B-roll footage or
  branded graphics in CapCut or Canva.
- Production time: under 30 minutes per video once the script and avatar are
  approved.
- EA application: Ugandan audiences respond strongly to a recognisable,
  consistent presenter. A recurring avatar character builds familiarity over
  time in the same way a brand spokesperson does on television.

---

## Section 5 — Distribution Protocol

### LinkedIn

- Post the video directly to the LinkedIn feed (native video outperforms links
  in the algorithm).
- For outreach: send as an InMail with a thumbnail image embedded in the message
  body and the video URL beneath it.
- Add captions; LinkedIn auto-generates them — edit for accuracy before posting.

### Email

- Do not embed the MP4 file directly. Host the video and use a static thumbnail
  with a play-button overlay as the email image.
- A GIF preview of the video's first 3 seconds increases click-through rate
  by 26% (Roth and neuroflash Team, 2024/2025).
- Subject line format: "Video for [FIRST NAME]" or "[FIRST NAME] — 90 seconds
  on [TOPIC]" consistently outperforms generic subject lines.

### WhatsApp (EA Primary Channel)

- Compress the MP4 to under 10MB before sending (use HandBrake, free, or
  CapCut's export settings).
- Send directly to known contacts via WhatsApp Business.
- For broadcast to segments: use WhatsApp Business broadcast lists (maximum 256
  contacts per list). Do not broadcast unsolicited video; send only to contacts
  who have opted in to communications.
- A voice note teaser (15 seconds, human voice) sent before the video link
  increases video opens in the EA market — the voice note signals a genuine
  personal message rather than a mass broadcast.

---

## Section 6 — Disclosure Requirements

### Legal Obligation

Under EU AI Act Article 4 (effective August 2026) and emerging global norms,
any video using an AI avatar that is not a real person must be disclosed as
AI-generated.

This requirement applies to all clients regardless of their country of
operation, because:
- Content may be received by EU-based contacts or distributed on EU-regulated
  platforms.
- Non-disclosure is a reputational risk in any market; disclosure done well
  is a brand asset.

### Standard Disclosure Language

Include this line in every AI avatar video communication:

> "This message was delivered by an AI avatar on behalf of [FULL NAME],
> [TITLE] at [COMPANY NAME]."

Place the disclosure:
- As the final sentence of the video script (spoken by the avatar)
- In the email footer or LinkedIn message body beneath the video link
- In the video description on any platform that supports it

### Custom Avatar Disclosure

When the avatar uses a real person's likeness and voice (cloned via ElevenLabs
or a platform's custom avatar tool), add:

> "This is an AI-generated video using a digital likeness of [NAME], created
> with their consent."

### Client Approval

Obtain written client approval of the disclosure approach before any video is
sent to a third party. Document the approval in the client's folder.

---

## Quality Criteria

- The correct platform is selected using the selection rules in Section 1;
  the rationale is stated in one sentence referencing the client's primary goal
  and volume requirement
- The avatar design brief specifies wardrobe, background, voice, and pace with
  reference to the client's brand standards and sector register
- Every script follows the 15-word sentence limit, contains at least two
  `[PAUSE]` markers, and opens with a parenthetical register instruction
- Scripts are timed before production; outreach scripts are 90 seconds or under
  when read at the specified pace
- Distribution is specified per channel with file size limits and thumbnail
  instructions for email and WhatsApp
- Disclosure language is included in every deliverable and written client
  approval is required before volume production
- EA market context is reflected throughout: WhatsApp distribution, payment
  method feasibility, EA professional register, and relationship-led outreach
  norms
- Volume production does not begin until the pilot video has been approved
  in writing

---

## Related Skills

- **`biz-dev-video-outreach`** — use for the full video outreach sequence
  (messaging strategy, follow-up cadence, CRM tracking) that AI avatar videos
  feed into
- **`brand-voice-ai-training`** — use to establish the brand voice parameters
  before scripting avatars; the brand voice brief feeds directly into the
  register instructions in each script
- **`playbook-content-production`** — use for the full content production
  workflow that AI avatar social videos sit within

---

## References

- Roth, H. and neuroflash Team (2024/2025) *AI Strategy 2025 for Marketing
  Teams*. neuroflash. [Video outreach performance statistics; distribution
  CTR data]
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*.
  Pearson. [Channel strategy context for distribution sequencing]

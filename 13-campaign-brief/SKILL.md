---
name: 13-campaign-brief
description: Generates a complete campaign brief document for a specific campaign — used to brief an internal team or external creative partners with everything they need to execute. Invoke after 09-campaign-strategy has determined what to do; this skill translates that strategy into an operational brief covering who does what, how, and by when.
---

# Campaign Brief Generator

Produce one complete campaign brief document. This is the operational handover document — it tells the execution team exactly what to make, to what specifications, by when, and to whose approval. It does not decide the campaign strategy; that is the role of `09-campaign-strategy`. Apply the `east-african-english` skill for tone throughout. Do not generate the brief until all Required Input has been confirmed.

**Distinction from 09-campaign-strategy:** Use `09-campaign-strategy` to decide WHAT campaign to run, who it is for, and what it needs to achieve. Use this skill (13-campaign-brief) to brief WHO will create the campaign content, HOW it should look and sound, and WHEN everything is due. The brief is a working document — it travels with the campaign from kickoff to sign-off.

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

Add a one-sentence note on how the audience's platform behaviour in Uganda/EA affects campaign delivery (e.g., "This audience is primarily reached via Facebook and WhatsApp; Instagram secondary").

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

| Deliverable | Platform | Format | Dimensions / Specs | Quantity | Due Date | Responsible Party |
|---|---|---|---|---|---|---|
| Facebook feed graphic | Facebook | Static image | 1200 × 630 px, JPG/PNG | | | |
| Instagram feed graphic | Instagram | Static image | 1080 × 1080 px, JPG/PNG | | | |
| Instagram Stories graphic | Instagram | Static image / video | 1080 × 1920 px | | | |
| Instagram Reel | Instagram | Video | 1080 × 1920 px, MP4, max 60 sec | | | |
| LinkedIn graphic | LinkedIn | Static image | 1200 × 627 px, JPG/PNG | | | |
| TikTok video | TikTok | Video | 1080 × 1920 px, MP4, max 60 sec | | | |
| WhatsApp broadcast copy | WhatsApp | Text + image | Image: 800 × 800 px; copy: max 300 words | | | |
| Caption set | All platforms | Text | Per platform character limits (see Section 6) | | | |

Populate quantity, due date, and responsible party from the Required Input. Add rows for any additional deliverables not listed above.

---

### Section 6: Content Specifications Per Deliverable

#### Social Graphics

Use these standard specifications for all static image deliverables:

| Platform | Dimensions | File Format | Max File Size |
|---|---|---|---|
| Facebook feed | 1200 × 630 px | JPG or PNG | 8 MB |
| Instagram feed | 1080 × 1080 px | JPG or PNG | 8 MB |
| Instagram Stories | 1080 × 1920 px | JPG or PNG | 8 MB |
| LinkedIn feed | 1200 × 627 px | JPG or PNG | 8 MB |
| TikTok / Reels | 1080 × 1920 px | MP4 | 287 MB |
| WhatsApp image | 800 × 800 px | JPG or PNG | 2 MB |

**Key elements every graphic must include:**
- Brand logo (position: as per brand guidelines — typically top-left or bottom-right)
- Campaign headline or key message (legible at thumbnail size on mobile)
- Brand colours only — no off-brand colour use
- Clear visual hierarchy: one dominant image or graphic element, one headline, one CTA or supporting text

#### Video Specifications

| Platform | Duration | Aspect Ratio | Captions | Key Requirements |
|---|---|---|---|---|
| Instagram Reels | 15–60 seconds (30 sec optimal) | 9:16 vertical | Required | Hook in first 3 seconds; branding in last 5 seconds |
| TikTok | 15–60 seconds (30–45 sec optimal) | 9:16 vertical | Required | Native feel; avoid over-polished corporate aesthetic |
| Facebook video | 30–90 seconds | 16:9 or 1:1 | Required | Auto-plays without sound; first frame must carry the message |
| YouTube | 2–5 minutes (if in scope) | 16:9 | Required | Thumbnail must be designed separately |

**Captions are required on all video deliverables without exception.** A significant proportion of video on Facebook and Instagram in East Africa is watched without sound. Uncaptioned video fails a large part of the audience.

#### Captions

| Platform | Recommended Length | Max Length | Hashtags | CTA Required |
|---|---|---|---|---|
| Facebook | 40–80 words | 63,206 characters | 2–5 | Yes |
| Instagram | 100–150 words | 2,200 characters | 5–15 | Yes |
| LinkedIn | 100–200 words | 3,000 characters | 3–5 | Yes |
| TikTok | 1–3 sentences | 2,200 characters | 3–8 | Optional |
| WhatsApp broadcast | 100–200 words | 300 words recommended | None | Yes |
| X / Twitter | 1–2 sentences | 280 characters | 1–2 | Optional |

Every caption must include one clear CTA. Match the CTA to the campaign objective: awareness campaigns use "Share this", "Tag someone"; lead generation uses "Click the link", "Send us a message"; promotional campaigns use "Shop now", "Book your spot".

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
- All graphic specifications use the correct platform dimensions as listed; captions are required on all video deliverables without exception
- The key message is one sentence only and is clearly distinct from the campaign slogan or tagline
- Brand do's and don'ts are campaign-specific and reference the client's actual brand voice — not generic rules applicable to any campaign
- The timeline table covers the full lifecycle from kickoff to post-campaign report, with realistic sequencing between review and production stages
- The approval process states what happens when feedback is late — ambiguity here is a common cause of campaign delays
- Success metrics include baselines and targets; a KPI without a target is not a KPI

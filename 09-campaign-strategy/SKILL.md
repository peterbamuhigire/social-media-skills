---
name: 09-campaign-strategy
description: Generates a complete single-campaign strategy document — covering objective setting, audience targeting, campaign concept, channel plan, timeline, content production list, paid amplification, budget allocation, and success metrics. Invoke when a client needs to plan a focused marketing campaign: product launch, seasonal offer, awareness drive, or event promotion. Also produces a one-page campaign brief for briefing creative partners or clients.
---
# Campaign Strategy Generator

Produce a complete campaign strategy document for one focused marketing campaign. Every section must be populated with client-specific content — no generic filler. Apply British English throughout. Default to Uganda/East Africa context unless the client specifies otherwise.

A campaign is a time-bound, focused effort with a specific objective. It is distinct from always-on social media activity (covered in 05-social-media-strategy). This document governs one campaign only.

---

<!-- dual-compat:start -->
## Use when
- Generates a complete single-campaign strategy document — covering objective setting, audience targeting, campaign concept, channel plan, timeline, content production list, paid amplification, budget allocation, and success metrics. Invoke when a client needs to plan a focused marketing campaign: product launch, seasonal offer, awareness drive, or event promotion. Also produces a one-page campaign brief for briefing creative partners or clients.
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
- A structured onboarding, strategy, or planning document in markdown, ready to hand off to the next skill in the workflow.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Ask for all of the following before generating the campaign strategy document:

- **Client name** — trading name
- **Industry and sub-sector** — e.g. "retail — electronics", "hospitality — event venue"
- **Country/city** — defaults to Kampala, Uganda if not specified
- **Campaign type** — product launch / seasonal offer / brand awareness / event promotion
- **Campaign dates** — proposed start date and end date in day-month-year format
- **Target persona** — reference 03-audience-personas if available; otherwise describe the primary target (age, location, key motivations, platform habits)
- **Campaign budget** — total budget in UGX; split into: (a) production budget (content creation costs) and (b) paid spend (boosting, ads)
- **Available channels** — list all channels the client can activate: Facebook, Instagram, TikTok, WhatsApp broadcast, email list, YouTube, LinkedIn, X/Twitter
- **Primary business goal this campaign supports** — one sentence linking the campaign to a wider business objective

If the 03-audience-personas document is available, reference it explicitly. If not, ask the client to confirm the target audience before proceeding.

---

## Document Structure

Generate all ten sections in order. Use markdown headings. Do not omit any section.

### 1. Campaign Objective

State the primary campaign objective in SMART format. One primary objective only. Secondary objectives are listed separately.

**SMART objective format:**
- **Specific:** what exactly will be achieved
- **Measurable:** which number or metric defines success
- **Achievable:** is this realistic given the budget and timeframe?
- **Relevant:** how does this connect to the client's primary business goal?
- **Time-bound:** by what date must the objective be achieved?

Write the objective as a single sentence: "Achieve [measurable outcome] by [date] through [channel/approach], in order to [business goal]."

Example for a product launch: "Generate 200 pre-orders for [Product Name] by [launch date + 7 days] through a coordinated Instagram and WhatsApp campaign, in order to validate market demand before the full production run."

**Secondary objectives (list separately, not SMART):**
- [e.g. Grow Instagram following by 300 new followers during campaign period]
- [e.g. Generate 50 pieces of user-generated content via campaign hashtag]

Do not allow secondary objectives to dilute focus. The primary objective must remain the decision-making anchor for every campaign choice.

---

### 2. Target Audience

Identify explicitly which persona(s) from 03-audience-personas this campaign targets. State the reasoning.

If only one persona is targeted (recommended for most campaigns): name them, state their core motivation, and explain why this campaign is relevant to them.

If two personas are targeted: confirm that the core message works for both. Note if any element of the channel plan or content must be adapted for each.

State the following for the primary target:
- **Primary persona name:** [e.g. "Grace — urban professional, Kampala, 28–38"]
- **Why this campaign is for them:** [1–2 sentences linking the campaign offer or message to a known need, pain point, or aspiration from the persona profile]
- **Where to reach them:** [primary platform(s) and time of day they are most active; apply EAT, UTC+3]
- **What will motivate them to act:** [one sentence — the core behavioural driver: social proof / urgency / aspiration / saving money / belonging / status]

---

### 3. Campaign Concept and Core Message

Define the big idea that ties all campaign content together.

**Campaign name / working title:** [Short, memorable; 3–5 words]

**Tagline:** [One punchy line the audience will remember; can be used in graphics, captions, and CTAs]

**The big idea:** [One sentence describing the campaign concept — what it is and why it will resonate with the target audience]

**Core message:** [One sentence stating what the audience must take away from this campaign. Everything in the campaign serves this message. If an asset does not reinforce the core message, cut it.]

**Tone for this campaign:** [Reference 04-brand-voice-intake if available. Note if the campaign tone differs from the always-on brand tone — e.g. a campaign for a festive seasonal offer may be more playful than the brand's standard tone]

**Visual direction note:** [Brief description of the look and feel for campaign assets — not a design brief, but enough direction for a graphic designer or videographer to understand the aesthetic. Note: asset production is outside the scope of this skill.]

---

### 4. Channel Plan

Define how each channel will be used in this campaign. Show how channels work together — cross-channel sequencing is essential for campaign impact.

**Cross-channel sequencing principle:**
Build from teaser to announcement to amplification to close-out:
1. Tease on Stories (Instagram / Facebook) — generate curiosity before the launch
2. Announce on feed — hero content goes live at full quality
3. Amplify with WhatsApp broadcast — reach the most engaged existing audience
4. Follow up with email (if list available) — direct channel with highest intent audience
5. Sustain with supporting content — keep the campaign alive across the full period

**Channel plan table:**

| Platform | Role in Campaign | Content Type | Frequency | Timing (EAT, UTC+3) | Notes |
|---|---|---|---|---|---|
| Instagram | Announce + sustain | Feed post, Reel, Stories | [e.g. Daily during launch, 3x/week sustain] | [e.g. 07:00 / 12:00 / 19:00] | Hero visual on Day 1 |
| Facebook | Broad reach + community | Feed post, boosted post | [e.g. 3x/week] | [e.g. 08:00 / 13:00] | Boost launch post |
| TikTok | Entertainment + awareness | Short video | [e.g. 2x/week] | [e.g. 19:00–21:00] | UGC challenge if applicable |
| WhatsApp broadcast | Direct audience activation | Text + image message | [e.g. Day 1, Day 7, Day last] | [e.g. 09:00] | Personalised tone |
| Email | Nurture and convert | Campaign email | [e.g. 3 emails: announce / build / last chance] | [e.g. Morning sends 07:00] | Segment to leads and customers |
| YouTube | Tutorial or demonstration | Video | [e.g. 1 hero video] | [e.g. Publish Day 1] | If applicable |

Populate only channels available to this client. Remove rows for channels not in use.

---

### 5. Campaign Timeline

Structure across four phases. Populate with specific dates using the client's stated campaign dates.

**Phase 1 — Pre-launch (1–2 weeks before campaign start)**
Goal: build anticipation; warm existing audience; tease without revealing
- Content to publish: [list specific teasers — e.g. "countdown graphic on Stories", "behind-the-scenes video: 'something is coming'", "Instagram poll: 'Are you ready?'"]
- Community actions: [e.g. respond to all comments on teasers within 4 hours; DM engaged followers a sneak preview]
- Paid activity: [e.g. begin building warm Custom Audience for retargeting on Day 1 launch]
- Milestone: [e.g. 500 Story views on teaser content; 50 poll responses; WhatsApp broadcast list at target size]

**Phase 2 — Launch (Days 1–3)**
Goal: maximum visibility; drive first wave of action
- Content to publish: [list all launch assets — e.g. "hero feed post + Reel on Day 1", "Facebook boosted announcement", "WhatsApp broadcast at 09:00", "email to full list at 07:00"]
- Posting frequency: highest of the entire campaign; aim to be visible across all platforms in the first 24 hours
- Paid amplification: [specify which posts to boost and targeting notes — see Section 7]
- Community actions: [e.g. respond to every comment within 2 hours on Day 1; screenshot and share UGC in Stories]
- Milestone: [e.g. [X] impressions in first 48 hours; [Y] enquiries or clicks; [Z] orders or sign-ups]

**Phase 3 — Sustain (Week 2 through campaign close minus 48 hours)**
Goal: maintain momentum; deepen engagement; convert warm audiences
- Content to publish: [e.g. customer testimonials or UGC reposts, FAQ content, behind-the-scenes, reminder posts]
- UGC encouragement: actively invite customers to share their experience using the campaign hashtag
- Retargeting: serve content to people who engaged with Phase 2 posts but have not yet converted
- Email: send mid-campaign email to non-openers and non-clickers from Phase 2 send
- Milestone: [e.g. engagement rate sustained above baseline; UGC collected from [X] customers]

**Phase 4 — Close-out (Final 48 hours)**
Goal: urgency; last-chance messaging; finalise results
- Content to publish: [e.g. "Last 48 hours" countdown post, "Don't miss out" WhatsApp broadcast, final email: "last chance"]
- Urgency must be genuine — do not use artificial deadlines. If the offer has a real close date, state it clearly.
- After campaign ends: publish a results or thank-you post; acknowledge participants; share campaign outcome with the community
- Milestone: [primary KPI target achieved or documented; all results recorded for post-campaign report]

---

### 6. Content Production List

List every asset that must be created for this campaign. Group by type. Include specs and assign responsibility.

| Asset | Type | Specs | Quantity | Responsible | Due Date |
|---|---|---|---|---|---|
| Hero campaign graphic | Static image | 1080×1080px (feed), 1080×1920px (Stories) | 2 (feed + Stories version) | [Designer / in-house] | [Date] |
| Campaign Reel / TikTok video | Video | 9:16, 15–60 seconds, captions on-screen | 1 | [Videographer / in-house] | [Date] |
| Teaser graphic series | Static image | 1080×1920px Stories | 3 frames | [Designer] | [Pre-launch date] |
| Feed post captions | Copy | 150–300 words each | [Number] posts | [Copywriter / in-house] | [Rolling] |
| WhatsApp broadcast messages | Copy | 50–100 words each, no links in first message | 3 messages | [In-house] | [Phase dates] |
| Email campaign copy | Copy | Subject line + body (300–500 words) + CTA | 3 emails | [Copywriter] | [Phase dates] |
| Facebook boosted post creative | Static image or video | 1200×628px (link post), 1080×1080px (square) | 1–2 | [Designer] | [Launch date] |
| Campaign hashtag | Copy | Brand + campaign specific | 1 | [In-house] | [Pre-launch] |
| UGC brief (instructions for customers) | Copy | One short paragraph or 3-step instructions | 1 | [In-house] | [Launch date] |

Add or remove rows based on the client's channel plan. Reference the east-african-english and content-writing skills for copywriting standards.

Note: graphic design, video production, and visual asset creation are outside the scope of this skill suite. Provide briefs and specs; direct the client to a designer or videographer.

---

### 7. Paid Amplification Plan

This section covers high-level paid social strategy for this campaign. It is not a media buying plan or ad account setup guide.

**Which posts to boost:**
Prioritise for boosting:
- The hero launch post (Day 1) — highest quality asset, clearest message
- Any post that achieves above-average organic engagement in the first 24 hours
- The close-out post — re-serve the campaign offer to warm audiences before the deadline

**Audience targeting notes:**
- **Primary audience:** [Age range, gender if relevant, location (city/region), key interests aligned with persona]
- **Warm retargeting audience:** people who engaged with previous posts or visited the profile in the last 30 days (use Facebook/Instagram Custom Audience)
- **Lookalike audience (if budget permits):** Facebook's 1% lookalike of existing page engagers or customer list — effective for reach campaigns

For Uganda/EA: Kampala is typically the highest-density and highest-intent urban audience for consumer brands. Layer in Jinja, Mbarara, Entebbe, or other cities if the client operates nationally.

**Budget allocation per platform (paid spend only):**

| Platform | What to Boost | Duration | Audience | Allocated Spend (UGX) |
|---|---|---|---|---|
| Facebook | Hero launch post + close-out post | [Days] | [Primary + retargeting] | |
| Instagram | Hero Reel + Stories | [Days] | [Primary audience] | |
| TikTok | Hero TikTok video | [Days] | [Interest-based] | |
| Total | | | | |

Minimum effective boost spend on Facebook/Instagram in Uganda: approximately UGX 20,000–50,000 per day for meaningful reach (2,000–5,000 people). Below this threshold, results are negligible.

---

### 8. Budget Allocation

Present a complete budget summary covering both production costs and paid spend.

| Channel / Activity | Production Cost (UGX) | Paid Spend (UGX) | Total (UGX) |
|---|---|---|---|
| Graphic design (all assets) | | — | |
| Video production (if applicable) | | — | |
| Copywriting | | — | |
| Facebook / Instagram paid | — | | |
| TikTok paid | — | | |
| Email platform cost (incremental) | | — | |
| Influencer fee (if applicable) | | | |
| Contingency (10%) | | | |
| **Total campaign budget** | | | |

State clearly: total production cost / total paid spend / grand total. Verify the grand total matches the client's stated campaign budget. If there is a shortfall, flag which activities to prioritise and which to reduce.

---

### 9. Success Metrics

Define what success looks like before the campaign starts. Agree these with the client.

**Primary KPI:**
[One metric directly tied to the campaign objective. Example: "Number of product pre-orders" / "Number of event registrations" / "Number of qualified enquiries via DM or form"]
Target: [Specific number] by [Campaign end date]

**Supporting KPIs (3–4 maximum):**

| KPI | Target | Measurement Method |
|---|---|---|
| Total campaign reach | [e.g. 30,000 unique accounts] | Native analytics |
| Engagement rate (campaign posts) | [e.g. Above 4%] | Engagements ÷ reach |
| WhatsApp broadcast open/read rate | [e.g. Above 60%] | Manual count |
| Email campaign open rate | [e.g. Above 30%] | Email platform analytics |
| Discount code redemptions | [e.g. 50 redemptions] | Sales records |
| Website sessions from campaign | [e.g. 500 sessions] | Google Analytics UTM |

**Reporting:**
- During campaign: daily check on paid spend, reach, and engagement on launch days; every 2–3 days during sustain phase
- Post-campaign: full report within 5 working days of campaign close. Use meta-reporting skill for report structure.
- Document results against targets and record for future campaign benchmarking

---

### 10. One-Page Campaign Brief

Produce a summary brief for sharing with creative partners (graphic designers, videographers) or for presenting to the client for sign-off. This is a pull-out, standalone document.

---

**[Client/Brand Name] — Campaign Brief**
*Prepared by: [Consultant/Agency Name] | Date: [Day-Month-Year]*

**Campaign name:** [Working title]
**Campaign type:** [Launch / Seasonal / Awareness / Event]
**Campaign dates:** [Start] — [End]

**Objective:**
[One sentence — the SMART objective from Section 1]

**Target audience:**
[2–3 sentences from Section 2 — who they are, where to reach them, what motivates them]

**Core message:**
[One sentence — the single thing the audience must take away]

**Tagline / working campaign name:**
[From Section 3]

**Channels:**
[Bullet list of active channels from Section 4]

**Key dates:**
- Pre-launch: [Date range]
- Launch day: [Date]
- Campaign closes: [Date]

**Assets required:**
[Bullet list of the most critical deliverables from Section 6 — hero graphic, hero video, captions, emails]

**Budget:**
Total: UGX [X] | Production: UGX [X] | Paid spend: UGX [X]

**Primary KPI:**
[From Section 9 — the one number that defines success]

**Contact for questions:**
[Consultant name, WhatsApp / email]

---

## Quality Criteria

- Campaign objective is written as a complete SMART statement with a specific number, date, and link to a business goal
- Target persona is explicitly named and linked to 03-audience-personas where available
- Cross-channel sequencing shows how platforms work together — not just a list of channels
- Campaign timeline has specific dates (not relative weeks) derived from the client's stated campaign dates
- Content production list includes specs for every asset type — enough for a designer to work from
- Paid amplification notes include EA-specific minimum spend thresholds and audience targeting logic
- Budget table clearly distinguishes production costs from paid spend and totals to the client's stated budget
- Success metrics are agreed before the campaign starts — targets are specific numbers, not "increase" or "improve"
- One-page campaign brief is standalone and complete — a designer or client could act on it without reading the full document
- British English spelling throughout; EAT timezone applied to all scheduling references

# Book Synthesis Skills Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build 5 new skills and enhance 8 existing ones from knowledge synthesised from three books — Hahn (2003), Edwards et al. (1991), and Pinskey (1997).

**Architecture:** Each new skill is a standalone directory with a `SKILL.md` (YAML frontmatter + body under 500 lines). Enhancements are targeted additions to existing SKILL.md files — no rewrites. All content uses British English. All skills follow CLAUDE.md authoring rules.

**Tech Stack:** Markdown only. No code. Git for commits.

---

## PHASE 1 — New Skills (5 skills)

---

### Task 1: Create `playbook-pr-publicity`

**Files:**
- Create: `playbook-pr-publicity/SKILL.md`

**Content to write:**

```markdown
---
name: playbook-pr-publicity
description: Generate a complete PR and media relations strategy for a client — covering news release writing, media kit assembly, journalist pitching, publicity calendar, and earned media tracking. Use when a client wants press coverage, media exposure, or public credibility without a paid advertising budget.
---

# PR and Publicity Playbook

## Required Input

Before generating any deliverable, ask for:
- Client business name
- Industry / sector
- Country or city (default: Uganda / East Africa)
- Primary goal (e.g., launch coverage, sustained brand awareness, thought leadership)
- Any existing media relationships or past coverage

---

## Part 1 — What Counts as News

Not everything a business does is newsworthy. Apply this filter before writing any release.

**Genuinely newsworthy:**
- New product, service, or business launch
- Milestone (first client, 1,000 customers, anniversary, award)
- Survey, study, or data you commissioned or conducted
- A provable "first" or "biggest" in your category
- Tie to a current national or regional news trend
- Human-interest story (client transformation, founder origin, community impact)
- Controversy or contrarian take on an industry issue (handled carefully)
- Partnership, expansion, or change that affects the public

**Not newsworthy (do not pitch):**
- General promotions or price reductions
- Internal appointments with no public significance
- "We're excited to announce…" — without a reason for the reader to care
- Routine product updates

---

## Part 2 — The Standard News Release

Every news release follows this format exactly.

```
FOR IMMEDIATE RELEASE

[HEADLINE — active voice, benefit or outcome-led, present tense]
[SUBHEADLINE — one sentence that adds detail the headline omits]

[City], [Date] — [Lead paragraph: who, what, when, where, why — most important fact first.
Maximum two sentences. Never begin with the company name.]

[Second paragraph: supporting detail, context, and the "so what" for the reader.]

[Third paragraph: quote from a named spokesperson — not a generic statement.
Quote must add information not already in the body.]

[Fourth paragraph: further supporting detail, data, or background.]

[Boilerplate: one paragraph beginning "About [Company Name]:" —
describes the business in two to three sentences.]

For more information:
[Contact name]
[Email address]
[Phone number]
[Website]

###
```

**Rules for every release:**
- Lead with the most important fact — not the company name
- Active voice throughout
- Inverted pyramid structure (most important → least important)
- Maximum 400 words for the body
- One quote from a named person — never "a company spokesperson said"
- Every claim must be verifiable
- Send plain text or PDF — never Word documents
- Do not write the release as an advertisement

---

## Part 3 — The Publicity Kit

A publicity kit (media kit) is sent to journalists before or alongside a pitch. It contains:

| Component | Purpose |
|---|---|
| Biographical profile | Who you are — written in third person, 200 words |
| Company description | What the business does, for whom, since when — 100 words |
| Product/service overview | One page describing key offerings and differentiators |
| Fact sheet | Key figures: founding date, team size, clients served, notable results |
| High-resolution photography | Headshot + product/service images — minimum 300 dpi |
| Past coverage | Copies of any articles, features, or media mentions already published |
| Story hooks | 3–5 suggested story angles, written as headline-length ideas |
| Interview questions | 10–15 suggested questions a journalist could ask — provided as a courtesy |

**Delivery:** Send as a single PDF or a well-organised folder. Never email 10 individual attachments.

---

## Part 4 — Pitching Journalists

### The Query Letter Structure

Use this to pitch a feature article, interview, or column opportunity:

```
Paragraph 1 — The hook
Why this story, why now? Connect to a current news trend, season, or issue
that makes this timely. One to two sentences.

Paragraph 2 — The story
What exactly would the article or interview cover? What angle?
What will the reader learn or feel? Two to three sentences.

Paragraph 3 — Why you
Your credentials, expertise, or unique position to speak on this topic.
One to two sentences.

Paragraph 4 — Practical details
Proposed length, your availability for interview, any supporting materials
(data, case studies, photography) you can provide.

Sign-off: Name, title, phone, email.
```

**Length:** The query letter must fit on one printed page. Journalists are busy.

### 22 Ways to Get Your Story Published
*(Adapted from Hahn, 2003)*

1. Learn what journalists consider newsworthy — read the publication before pitching it
2. Find a news hook for every release — tie to current events or trends
3. Time releases to editorial calendars and news cycles
4. Write in inverted pyramid style — most important information first
5. Use the standard news release format (Part 2 above) without deviation
6. Target the right journalist — not the editor-in-chief; find the reporter who covers your beat
7. Send exclusives for major stories — one outlet gets first rights for 48–72 hours
8. Follow up by phone once only, 48 hours after sending
9. Build media relationships before you need them — comment on their articles, attend press events
10. Create a media kit and keep it permanently up to date (Part 3 above)
11. Capitalise on national news by making your business the local or specialist angle
12. Write opinion pieces (op-eds) as a named expert — 600–800 words, no advertising
13. Create an "expert source" positioning for your sector — be available for comment on breaking news
14. Use customer success stories as story angles — transformation, impact, and results
15. Anniversaries, milestones, and firsts are news — plan releases around them in advance
16. Create an award, index, or ranking in your category — data and recognition are both newsworthy
17. Sponsor a survey or publish original research — data is the most shareable PR asset
18. Host an event that creates news — a panel, launch, or public debate
19. Make yourself available immediately when journalists are on deadline — responsiveness is rare
20. Use trade press as a platform before targeting consumer press
21. Register with HARO (Help a Reporter Out) or regional equivalents as an expert source
22. Never lie, never spin — long-term media credibility is built over years and destroyed in a day

---

## Part 5 — Publicity Calendar

Generate a 12-month publicity calendar with these columns:

| Month | News Hook or Angle | Release / Pitch Type | Target Media | Lead Time Required |
|---|---|---|---|---|
| January | New year goals / resolutions | Opinion piece | Business press | 2 weeks |
| February | Upcoming campaigns (Valentine's) | Feature pitch | Lifestyle / consumer | 3 weeks |
| ... | ... | ... | ... | ... |

**Rules for the calendar:**
- Identify 2–3 newsworthy moments per quarter minimum
- Build in 3–4 weeks of lead time for print publications
- Flag national holidays and sector events that create natural hooks

---

## Part 6 — Earned Media Tracking

Track all media activity in a simple log:

| Date | Outlet | Story Type | Journalist | Status | Link / Clip | Estimated Reach |
|---|---|---|---|---|---|---|

Review monthly. Calculate:
- **Total earned media impressions** = sum of outlet reach figures for published coverage
- **Equivalent advertising value (EAV)** = estimated cost of buying equivalent space at rate card
- **Share of voice** = your mentions ÷ total category mentions in tracked outlets

---

## Quality Criteria

Good output from this skill:
1. Every news release passes the "would a journalist run this?" test — it is genuinely newsworthy
2. The release follows the standard format exactly — inverted pyramid, no advertising language
3. The publicity kit contains all 8 components, each at the specified word count
4. The query letter fits on one page and has a genuine time-sensitive hook
5. The 12-month calendar identifies real, specific news moments — not generic "brand awareness"
6. Media targets are named publications or outlet types relevant to the client's sector and geography
7. All content is written in the professional East African English register defined in `east-african-english`

---

## References

- Hahn, F.E. (2003) *Do-It-Yourself Advertising and Promotion*, 3rd edn. Hoboken: Wiley.
- Edwards, P., Edwards, S. and Douglas, L.C. (1991) *Getting Business to Come to You*. Los Angeles: Tarcher.
- Pinskey, R. (1997) *101 Ways to Promote Yourself*. New York: Avon Books.
```

**Steps:**
1. Create directory `playbook-pr-publicity/`
2. Write the content above to `playbook-pr-publicity/SKILL.md`
3. Verify line count is under 500
4. Commit: `git add playbook-pr-publicity/ && git commit -m "feat: add playbook-pr-publicity skill from book synthesis"`

---

### Task 2: Create `direct-mail-writer`

**Files:**
- Create: `direct-mail-writer/SKILL.md`
- Create: `direct-mail-writer/references/galletti-27-points.md`

**Content — SKILL.md:**

```markdown
---
name: direct-mail-writer
description: Write complete direct mail letters, postcard campaigns, and email campaigns for clients — covering offer design, list strategy, copy structure, and testing methodology. Use when a client wants to reach a known or purchased audience with a targeted, measurable written offer via post or email.
---

# Direct Mail Writer

## Required Input

Before generating any deliverable, ask for:
- Client business name
- Industry / sector
- Country or city (default: Uganda / East Africa)
- The specific offer being made (product, service, free consultation, etc.)
- The target audience (existing customers, prospects, a specific segment)
- The desired response action (phone call, website visit, WhatsApp message, in-store visit)
- Budget context (affects format recommendations)

---

## Part 1 — The Four Prerequisites

Before writing a word of copy, confirm all four conditions are met:
*(Adapted from Edwards, Edwards and Douglas, 1991)*

| # | Prerequisite | What to Verify |
|---|---|---|
| 1 | **The right list** | Is the audience targeted, current, and relevant? A mediocre piece to a great list outperforms a great piece to a poor list. |
| 2 | **The right offer** | Is the offer clear, compelling, and risk-reducing? A weak offer cannot be rescued by strong copy. |
| 3 | **The right copy** | Is the message benefit-led, action-oriented, and reader-focused? |
| 4 | **The right timing** | Does the mailing align with seasonal need, budget cycles, or purchasing windows? |

If any prerequisite is absent, resolve it before proceeding to copy.

---

## Part 2 — The Two-List Pre-Writing Process

Before writing, build two lists:

**List 1 — Features**
Every factual attribute of the product or service.

**List 2 — Benefits**
For each feature, ask: "What does this mean to the specific reader receiving this letter?"

Write the letter from **List 2 only**. Use List 1 as supporting evidence, never as the lead.

*"Features instruct. Benefits sell."* — Hahn (2003)

---

## Part 3 — The Three Tells

Every direct mail letter must address three questions — in the first paragraph AND again in the P.S.:

1. **What** are you offering?
2. **Why** should they want it?
3. **How** do they get it? (the response mechanism)

If any of the three is absent, the letter is incomplete.

---

## Part 4 — Letter Structure

```
[HEADLINE or opening hook — strongest benefit or most important fact]

[Opening paragraph: State the problem the reader has. Paint it vividly.
Then pivot: "There is a solution."]

[Second paragraph: Introduce the offer. State it clearly. Lead with the outcome,
not the features. Use specifics — not "great results" but "34% more enquiries
in the first month."]

[Third paragraph: Build credibility. Testimonial, case study, statistic,
or credential. One proof point is enough here; more can follow.]

[Fourth paragraph: Address the most likely objection. Do not wait for the reader
to think it — raise it and answer it.]

[Fifth paragraph: The offer in full. State exactly what they receive, what they
pay (or don't pay), and any time limitation or bonus.]

[Closing paragraph: The call to action. Exact next step. Make it frictionless.
State the deadline if applicable.]

[Signature — handwritten name, full title]

[P.S. — Restate the single strongest benefit and the call to action.
The P.S. is the second-most-read element after the headline. Never waste it.]
```

---

## Part 5 — The 27 Copywriting Points

See `references/galletti-27-points.md` for the full Galletti checklist. Apply before finalising any copy.

**The five most critical points:**
1. Move the best, most powerful thing you can say to the very beginning
2. Write to one specific person — not "our valued customers"
3. Use "you" and "your" far more than "I," "we," or "our"
4. Make the offer risk-free — a guarantee, a trial, or a free first step
5. Test the headline before anything else — if the headline fails, nothing else matters

---

## Part 6 — List Strategy and the FRAT Formula

When advising on mailing lists, apply the FRAT formula to prioritise who to contact first:
*(Adapted from Hahn, 2003)*

| Letter | Factor | Question |
|---|---|---|
| F | **Frequency** | How often has this contact bought or enquired? |
| R | **Recency** | How recently did they buy or enquire? |
| A | **Amount** | What is their average transaction value? |
| T | **Type** | What type of products or services do they purchase? |

Score each contact on all four criteria. Mail the highest-FRAT contacts first, most often, and with the most premium formats.

**For rented or purchased lists:**
- Require recency of contact within 90 days
- Match list demographics to the offer's target buyer
- Test with a small cell (minimum 500 pieces) before rolling out

---

## Part 7 — Budget Viability — The $20 Rule
*(Hahn, 2003)*

Before committing to a mailing programme:

> For every UGX 20,000 (or USD $20) of projected revenue per transaction, the client can reasonably invest up to UGX 1,000 (or USD $1) per piece in mailing costs.

If projected revenue per transaction is UGX 100,000 → affordable cost per piece = UGX 5,000.
If projected revenue per transaction is UGX 500,000 → affordable cost per piece = UGX 25,000.

Use this to guide format decisions: a UGX 5,000 budget points to a postcard or simple letter; UGX 25,000 allows for a folded brochure insert.

---

## Part 8 — Format Options

| Format | Best For | Cost Tier |
|---|---|---|
| Single A4 letter | Professional services, B2B offers, relationship selling | Low |
| Postcard (A5) | Event invitations, short offers, reminders | Low |
| Letter + insert | Product launches, complex offers with supporting evidence | Medium |
| Self-mailer (folded brochure) | Retail promotions, multiple products | Medium |
| Email (cold or warm list) | Digital-first audiences; fastest test vehicle | Very low |
| WhatsApp broadcast | Known contacts only; EA primary channel | Very low |

---

## Part 9 — Testing Methodology

- **Test one variable at a time only** — headline vs headline, offer vs offer, list A vs list B
- **Minimum test size:** 500 pieces per cell for digital; 2,000+ for print
- **Code every response mechanism:** different phone number, URL parameter, promo code, or reply address per test cell
- **Track:** response rate, cost per response, conversion rate, revenue per piece mailed
- **Never roll out without a test** — even a 50-piece email test beats no data

---

## Quality Criteria

Good output from this skill:
1. Copy leads with the strongest benefit — never the company name or "We are pleased to offer…"
2. The Three Tells appear in both the opening paragraph and the P.S.
3. "You" and "your" outnumber "we," "our," and "I" throughout the letter
4. The offer is specific and risk-reducing — not vague
5. At least one proof point (testimonial, statistic, case reference) appears in the letter
6. The call to action is a single, unambiguous instruction with a response mechanism
7. The P.S. restates the strongest benefit and the call to action
8. The $20 Rule has been checked before recommending any format

---

## References

- Hahn, F.E. (2003) *Do-It-Yourself Advertising and Promotion*, 3rd edn. Hoboken: Wiley.
- Edwards, P., Edwards, S. and Douglas, L.C. (1991) *Getting Business to Come to You*. Los Angeles: Tarcher.
- Pinskey, R. (1997) *101 Ways to Promote Yourself*. New York: Avon Books.
```

**Content — references/galletti-27-points.md:**

```markdown
# Galletti's 27 Copywriting Points

*Source: Carl Galletti, as documented in Pinskey, R. (1997) 101 Ways to Promote Yourself. New York: Avon Books.*

Apply this checklist before finalising any direct mail letter, sales letter, email campaign, or proposal document.

---

1. Take the best, most powerful, most effective thing you can say and move it to the very beginning.
2. Give your audience a reason to keep reading immediately.
3. Focus the entire piece on one main idea.
4. Know exactly who you are writing to — write as if to one specific person.
5. Make every word earn its place.
6. Write in conversational, natural language.
7. Use "you" and "your" far more than "I," "we," or "our."
8. Lead with a problem the reader already has.
9. Paint a picture of the world after the problem is solved.
10. Use specifics, not generalities. ("Increased revenue by 34%" not "increased revenue significantly.")
11. Build credibility early — credentials, testimonials, or case data in the first third of the piece.
12. Make an offer that removes risk — a guarantee, a trial, or a free first step.
13. Create urgency — a genuine reason to act now, not later.
14. Use subheadings so that a skimmer can understand the argument without reading every word.
15. Every paragraph must pull the reader into the next paragraph.
16. Use bullet points for lists of benefits — not for lists of features.
17. Make the call to action specific: what exactly should the reader do, when, and how.
18. Use simple words and short sentences. Write at a Grade 8 reading level.
19. The offer is more important than the copy — make an offer they cannot refuse.
20. Let the P.S. be your second headline — restate the key benefit and call to action.
21. Tell a story if possible — narrative outperforms argument.
22. Overcome objections before they are raised.
23. Use social proof — names, numbers, testimonials.
24. Use the active voice throughout.
25. Read it aloud before sending — if it sounds awkward, it reads awkward.
26. Have a second reader who does not know your business read it and describe what the letter is asking them to do. If they cannot say it in one sentence, rewrite.
27. Test the headline before anything else — if the headline fails, nothing else matters.
```

**Steps:**
1. Create directory `direct-mail-writer/` and `direct-mail-writer/references/`
2. Write SKILL.md and references/galletti-27-points.md
3. Verify SKILL.md is under 500 lines
4. Commit: `git add direct-mail-writer/ && git commit -m "feat: add direct-mail-writer skill from book synthesis"`

---

### Task 3: Create `playbook-networking`

**Files:**
- Create: `playbook-networking/SKILL.md`

**Content to write:**

```markdown
---
name: playbook-networking
description: Design a structured networking and referral programme for a client or for the consultancy itself — covering event networking, referral group creation, referral activation, and follow-up systems. Use when a client needs to generate leads through relationships rather than advertising, or when the consultancy needs a business development system for a market where personal trust precedes commercial transactions.
---

# Networking and Referral Playbook

## Required Input

Before generating any deliverable, ask for:
- Client business name
- Industry / sector
- Country or city (default: Uganda / East Africa)
- Primary goal (new client acquisition, referral activation, community presence, or all three)
- Current networking activity (if any)
- Budget and time available per week for networking activity

---

## Part 1 — Why Networking First

In the East African market — and for independent professional service businesses globally — word-of-mouth is the single most effective and lowest-cost marketing method available.

*"A satisfied customer tells three people about a positive experience over one month. An unhappy customer tells seven people about a bad experience within one week."* — Edwards, Edwards and Douglas (1991)

Networking is the deliberate, systematic management of the relationships that generate word-of-mouth.

The Time-Money Marketing Continuum (Edwards et al., 1991):
- **High time / low money:** Networking, speaking, referral cultivation, content creation
- **Low time / high money:** Paid advertising, direct mail, sponsored placement

New businesses and independent practitioners should start at the high-time/low-money end. Migrate toward paid channels only when revenue allows.

---

## Part 2 — Event Networking: 14 Rules

*(Adapted from Edwards, Edwards and Douglas, 1991)*

1. Set specific goals before each event — e.g., "I will have three substantive conversations and leave with two follow-up commitments."
2. Arrive early — groups have not yet formed; it is easier to meet people one-to-one.
3. Prepare and practise a clear 30-second answer to "What do you do?" (see USP Pitch in `biz-dev-positioning`).
4. Listen more than you talk — ask questions that draw the other person out.
5. Focus first on how you can help others — not on selling yourself.
6. Write a note on the back of every business card immediately after the conversation — what was discussed, what you promised to do.
7. Follow up within 24–48 hours. Not "we should have coffee sometime" but "I'll call you on Thursday."
8. Build a follow-up system — a spreadsheet or CRM with contact date, next action, and deadline.
9. Join organisations actively — volunteer for committees, not just attend as a passive member.
10. Refer others freely and specifically — reciprocity is the currency of networking.
11. Show up consistently — be known as someone who is always there, not someone who appears occasionally.
12. Choose organisations strategically — attend where your best clients and best referrers already are.
13. Do not hard-sell at networking events — the sale happens in the follow-up, not at the event.
14. Create your own group when existing options are inadequate (see Part 4).

---

## Part 3 — Referral Activation: Three Strategies

### Strategy 1 — Active Solicitation from Existing Clients

Do not wait for referrals. Ask for them explicitly and specifically.

**Script:**
> "I'm glad the work has been useful. I'm looking to work with more businesses like yours — specifically [describe the ideal client]. Do you know one or two people I should be speaking to?"

**Rules:**
- Ask at the peak of client satisfaction — immediately after a successful delivery, not at renewal time
- Be specific about who you are looking for — "anyone" produces nothing; a description produces names
- Follow up the referral immediately and report back to the referrer ("I spoke to James — thank you for the introduction")
- Express genuine gratitude — a handwritten note or a small gift is remembered

### Strategy 2 — Gatekeeper Cultivation

Gatekeepers are not clients; they are the people who connect you to clients — lawyers, accountants, architects, event organisers, trade association officers, journalists.

**Steps:**
1. List the five professional categories most likely to encounter your ideal client before you do
2. Identify 2–3 named individuals in each category
3. Make first contact through introduction or shared event — not a cold pitch
4. Build the relationship with value first: refer work to them, share useful information, invite them to relevant events
5. When the relationship is established, explain what you do and for whom — and ask if they know anyone who fits that description

### Strategy 3 — Reference Letters and Endorsements

A written reference from a respected client or partner functions as a referral that works without the referrer being present.

**What a useful reference letter contains:**
- Who the client is and what context they know you in
- The specific problem you solved
- The specific outcome you delivered (with numbers if possible)
- A direct statement that they would recommend you
- Permission to use it in proposals and on your website

**Collection process:** Ask for a reference letter within 2 weeks of completing a successful project. Provide a brief template to make it easy. Never wait 6 months — the experience will have faded.

---

## Part 4 — Creating a Referral Group: 7 Steps

*(Adapted from Edwards, Edwards and Douglas, 1991)*

A referral group is a small, structured gathering of non-competing professionals who refer business to each other systematically.

1. **Define the niche:** What sector or client type will this group serve? Be specific.
2. **Identify 8–12 founding members:** Each should bring a complementary (not competing) service. Example: social media consultancy, accountancy firm, legal practice, web design studio, print/branding supplier, business coach.
3. **Set a fixed, recurring meeting time:** Monthly is the minimum; fortnightly is optimal. Same day, same location.
4. **Create a referral-sharing structure:** At each meeting, each member describes their ideal client for the month and reports on referrals given and received.
5. **Keep meetings focused and short:** 90 minutes maximum. Assign a facilitator.
6. **Rotate hosting duties:** Distributes the commitment and builds ownership.
7. **Track referrals generated:** Record the source, the recipient, and the outcome. Quantify the value. This keeps members accountable and demonstrates the ROI of participation.

---

## Part 5 — The Follow-Up System

*"Follow-up is 80% of networking. Most people follow up zero times. One follow-up puts you in the top 20%. Two follow-ups puts you in the top 5%."* — Pinskey (1997)

**Minimum follow-up system:**

| Contact Type | Follow-Up Action | Timing |
|---|---|---|
| Event meeting | Personalised message referencing the conversation | Within 24 hours |
| Referral received | Acknowledgement to the referrer; introduction message to the lead | Within 48 hours |
| Proposal sent | One follow-up call | 5–7 business days after sending |
| Past client, inactive | Check-in message with relevant news or resource | Every 90 days |
| Referrer (gatekeeper) | Value touch — article, invitation, relevant introduction | Monthly |

**Tools:** A simple spreadsheet works for under 100 contacts. Any CRM (Hubspot Free, Notion database, Google Sheets) works for more.

---

## Part 6 — Deliverables This Skill Can Generate

1. **Networking action plan** — target organisations, events, and individuals for the next 90 days
2. **30-second USP pitch** — prepared answer to "what do you do?" (links to `biz-dev-positioning`)
3. **Referral activation script** — exact words to use when asking existing clients for referrals
4. **Gatekeeper target list** — 10–15 named referral sources with cultivation plan
5. **Referral group design document** — founding member profile, meeting structure, referral tracking log
6. **Follow-up schedule** — tailored to contact type, with message templates

---

## Quality Criteria

Good output from this skill:
1. The networking action plan names specific organisations and events — not generic "networking events"
2. The 30-second pitch is specific, benefit-led, and memorable — not a job title
3. Referral scripts are direct and comfortable to say aloud — not awkward or pressuring
4. The gatekeeper list identifies professionals in roles that actually precede the client's buying decision
5. The referral group design includes a tracking mechanism — not just a description of who attends
6. All follow-up timings are specific (24 hours, 48 hours) not vague ("soon")
7. Content is adapted to the Ugandan/East African relationship-first business culture

---

## References

- Edwards, P., Edwards, S. and Douglas, L.C. (1991) *Getting Business to Come to You*. Los Angeles: Tarcher.
- Pinskey, R. (1997) *101 Ways to Promote Yourself*. New York: Avon Books.
```

**Steps:**
1. Create directory `playbook-networking/`
2. Write SKILL.md
3. Verify under 500 lines
4. Commit: `git add playbook-networking/ && git commit -m "feat: add playbook-networking skill from book synthesis"`

---

### Task 4: Create `biz-dev-positioning`

**Files:**
- Create: `biz-dev-positioning/SKILL.md`

**Content to write:**

```markdown
---
name: biz-dev-positioning
description: Define the strategic market position for a client or for the consultancy itself — covering USP development, niche definition, the 15-second pitch, mission and vision statements, and preeminence strategy. Use when a client (or the consultancy) needs to articulate what makes them different, who they serve, and why prospects should choose them over alternatives.
---

# Business Development — Positioning

## Required Input

Before generating any deliverable, ask for:
- Business name
- Industry / sector
- Country or city (default: Uganda / East Africa)
- Current positioning (how they currently describe themselves, if at all)
- Primary competitor(s) — named or described
- Primary client type they want to attract
- What they most want to be known for

---

## Part 1 — The USP (Unique Selling Proposition)

The USP is the one specific thing that distinguishes a business, product, or personal brand from every alternative available to the target client.

*Original concept: Rosser Reeves (1950s). Applied here via Pinskey (1997).*

**The USP development process:**

1. List every service or product the business offers
2. For each service, list the specific, tangible outcomes it delivers to clients
3. Identify the one outcome that is both the most valuable to the target client AND the most differentiated from competitors
4. Express it in the language the ideal client would use — not internal jargon
5. Apply the test: **Could a direct competitor say this exact sentence?** If yes, it is not a USP. Refine.

**The USP formula:**

> "We [specific action] for [specific client type] so that [specific outcome] — without [key obstacle or pain the competition imposes]."

**Examples:**
- Weak: "We provide social media management services."
- Strong: "We manage social media for Ugandan food and beverage brands so that their Facebook and WhatsApp communities generate walk-in customers — without the owner spending a single hour on content."

---

## Part 2 — The 15-Second Pitch

The spoken version of the USP — used at networking events, in introductions, and in discovery calls.

**Structure:**
> "[What I/we do] + [for whom] + [the specific result they get] + [why us, not someone else]"

**Length:** 2–3 sentences. Delivered in under 15 seconds.

**Preparation process:**
1. Draft the pitch using the USP formula above
2. Say it aloud — does it sound natural, or like a brochure?
3. Revise until it sounds like something you would say in a casual conversation
4. Test it: deliver it at one networking event and note what follow-up questions it triggers

**Common mistakes:**
- Starting with a job title ("I'm a social media manager") — labels, not value
- Describing inputs ("We post three times a week") — outputs are what clients want
- Being too broad ("We help businesses grow") — no differentiation
- Being too long — if it takes more than 20 seconds, it is a sales pitch, not a pitch

---

## Part 3 — Niche Definition

*"For the self-employed individual, finding a niche is somewhat like establishing job security."* — Edwards, Edwards and Douglas (1991)

The most successful independent service businesses are highly specialised. A niche must be:
- **Small enough** to avoid heavy competition and be reachable within the business's time and budget
- **Large enough** to sustain the revenue the business requires

**Niche definition exercise:**

Answer these four questions:
1. Which type of client produces the most revenue per engagement?
2. Which type of client produces the most referrals?
3. Which type of work do you do best and find most interesting?
4. Where is competition least intense?

The intersection of all four answers is the natural niche.

**Niche levels (from broad to specific):**

| Level | Example |
|---|---|
| Sector | Healthcare |
| Sub-sector | Private hospitals and clinics |
| Role within sub-sector | Marketing teams in private hospitals |
| Geography | Kampala and Nairobi |
| Specific outcome | Patient acquisition through Facebook and WhatsApp |

The more specific, the more powerful the positioning.

---

## Part 4 — Mission and Vision Statements

**Mission Statement** — what the business does, for whom, and the value it delivers. Present tense. Action-oriented.

Formula: *"We [verb] [specific service or output] for [specific client type] so that [specific outcome]."*

Example: "We design and manage social media strategies for East African SMEs so that their online presence converts audiences into paying customers."

**Vision Statement** — where the business is heading. Future-tense. Aspirational but specific.

Formula: *"To be [specific position] in [specific market] by [specific timeframe]."*

Example: "To be the leading social media consultancy for the food and beverage sector across East Africa by 2028."

**Rules:**
- Mission and vision must be internally consistent — the vision is where the mission leads
- Both must be specific enough that you could describe what achieving them looks like
- Both should be written in plain English — not corporate jargon
- Both must be short enough to be memorised by every person in the business

---

## Part 5 — The Five Lessons of Successful Independents

*(Edwards, Edwards and Douglas, 1991 — synthesised from research into $100,000+ independent businesses)*

These five principles distinguish the most successful independent service businesses from the rest:

**Lesson 1 — Get people to beat a path to your door**
Build such a strong reputation for delivering a specific result that clients come to you, rather than you chasing them. Requires: a clearly defined offer, consistent visibility, and exceptional delivery.

**Lesson 2 — Establish a niche**
Specialise to the point where you are the obvious expert for a specific type of client with a specific problem. Generalists struggle; specialists dominate.

**Lesson 3 — Gain entrance through gatekeepers**
Identify the professionals and institutions that already have trusted relationships with your ideal clients — and build deliberate relationships with those gatekeepers. See `playbook-networking` for the gatekeeper cultivation process.

**Lesson 4 — Position yourself as preeminent in your field**
Three routes to preeminence:
- Further the knowledge in your field (publish, research, speak, teach)
- Assume a leadership role (association president, conference chair, award creator)
- Pioneer a new approach or methodology (be first, name it, own it)

**Lesson 5 — Become a premier marketeer**
Do not take out run-of-the-mill ads. Do not send customary mailings. Premier marketeers use the same tools as everyone else — but more creatively, more consistently, and with more understanding of what their specific audience responds to.

---

## Part 6 — Preeminence Strategy

For clients or the consultancy who want to be seen as the leading expert in their category:

| Route | Specific Actions |
|---|---|
| **Publish** | Monthly newsletter, LinkedIn articles, trade press column, annual industry report |
| **Speak** | Industry conferences, Chamber of Commerce events, university guest lectures |
| **Research** | Annual survey of your sector's clients or practitioners; publish the data |
| **Lead** | Volunteer for a leadership role in a trade or professional association |
| **Award** | Create a sector award (e.g., "Best Customer Service in Ugandan Banking") — judge and publish |
| **First** | Be the first to name a new problem, trend, or methodology in your category |

Preeminence is built over 12–36 months. It is an investment, not a campaign.

---

## Part 7 — Deliverables This Skill Can Generate

1. **USP statement** — one or two sentences, tested against the competitor test
2. **15-second pitch** — natural, spoken version of the USP
3. **Niche definition** — sector, sub-sector, role, geography, and specific outcome
4. **Mission statement** — 1–2 sentences
5. **Vision statement** — 1–2 sentences
6. **Positioning brief** — 1-page document combining all of the above for use in proposals and credentials
7. **Preeminence action plan** — 12-month visibility building programme

---

## Quality Criteria

Good output from this skill:
1. The USP fails the "competitor test" — a direct competitor could NOT say the same sentence
2. The 15-second pitch sounds natural when spoken aloud — not like marketing copy
3. The niche is specific enough to describe what it excludes, not just what it includes
4. The mission statement contains a subject, a verb, a client type, and an outcome
5. The vision statement names a specific position in a specific market with a specific timeframe
6. The preeminence plan names specific publications, events, and organisations — not generic categories
7. All content reflects the East African market context where relevant

---

## References

- Edwards, P., Edwards, S. and Douglas, L.C. (1991) *Getting Business to Come to You*. Los Angeles: Tarcher.
- Pinskey, R. (1997) *101 Ways to Promote Yourself*. New York: Avon Books.
```

**Steps:**
1. Create directory `biz-dev-positioning/`
2. Write SKILL.md
3. Verify under 500 lines
4. Commit: `git add biz-dev-positioning/ && git commit -m "feat: add biz-dev-positioning skill from book synthesis"`

---

### Task 5: Create `copywriting-brochure`

**Files:**
- Create: `copywriting-brochure/SKILL.md`

**Content to write:**

```markdown
---
name: copywriting-brochure
description: Write the complete copy for a client brochure — covering structure, headlines, benefits positioning, proof elements, and calls to action. Use when a client needs a printed or digital brochure for sales meetings, trade shows, direct mail inserts, or website downloads.
---

# Copywriting — Brochure

## Required Input

Before generating any deliverable, ask for:
- Client business name
- Industry / sector
- Country or city (default: Uganda / East Africa)
- Purpose of the brochure (what should the reader do after reading it?)
- Target audience (who will receive this brochure and in what context?)
- Format (trifold, A4 booklet, digital PDF, etc.)
- Services or products to be featured
- Any existing testimonials, case studies, or statistics available

---

## Part 1 — Purpose Before Writing

Define the single purpose of the brochure before writing a word.

**Ask:** What is the one action the reader should take after reading this?

| Answer | How It Changes the Copy |
|---|---|
| Call us for a consultation | Lead with the problem and the transformation; end with the call |
| Visit our website | Build curiosity — give enough to compel a visit, not enough to satisfy it |
| Approve us as a supplier | Lead with credentials, case studies, and proof |
| Buy at the point of sale | Lead with the offer and price — transactional, immediate |
| Refer us to someone else | Make it easy to understand who benefits and why |

If the client cannot define a single action, help them choose one. A brochure trying to do five things does none of them.

---

## Part 2 — The Eight Imprints Rule

*Adapted from Pinskey (1997)*

A prospect typically needs to encounter a brand or business name **eight times** before they will act.

The brochure is one imprint. It does not work as a standalone piece — it must be part of a system:
- Meeting (imprint 1) → Business card (2) → Brochure (3) → Follow-up email (4) → Article or post seen online (5) → Referral conversation (6) → Proposal (7) → Second meeting (8)

**Implication:** Design brochure copy to move the prospect to the *next step*, not to close the sale. The brochure's job is not to sell — it is to maintain and deepen interest.

---

## Part 3 — The Eight Elements Every Brochure Must Contain

1. **A headline that states the primary benefit** — not the company name, not the service category
2. **A clear description of who you serve** — the reader must immediately recognise themselves
3. **The problem you solve** — stated in the reader's language, not the business's
4. **Your solution (services)** — described in terms of outcomes, not processes
5. **Proof** — at least one testimonial, case result, or named client reference
6. **A clear call to action** — the single next step, stated explicitly
7. **Contact details** — minimum two channels (phone + email or WhatsApp)
8. **A reason to act now (if applicable)** — a deadline, limited availability, or bonus offer

---

## Part 4 — Features vs Benefits

*"Features instruct. Benefits sell."* — Hahn (2003)

Every service or product listed in the brochure must be translated from feature to benefit before it appears in copy.

**The translation process:**
- Feature: "We post 12 times per month across three platforms."
- Benefit: "Your brand stays in front of your audience every three days — without you lifting a finger."

**The test:** After every claim, ask: "So what does that mean for the reader?" The answer is the benefit.

**In a brochure, features are supporting evidence. Benefits are the message.**

---

## Part 5 — The Biggest Brochure Mistakes

1. **Leading with the company name and history** — the reader does not care yet; earn their interest first
2. **Featuring the company, not the client's outcomes** — "We were founded in 2015 and have 12 staff" is not a benefit
3. **No call to action** — a brochure without a next step is a pamphlet
4. **Listing services without outcomes** — "Social Media Management" tells the reader nothing; "More enquiries, more sales" tells them everything
5. **Jargon and industry terms** — write for the reader, not for peers
6. **No testimonials or proof** — claims without evidence are ignored
7. **Burying the headline** — the cover must state the most powerful benefit, not just the business name
8. **Trying to include everything** — a brochure with 12 services and 6 sections is unread

---

## Part 6 — Panel-by-Panel Structure (Trifold)

For a standard trifold brochure:

| Panel | Position | Content |
|---|---|---|
| **Cover** | Outside front | Headline (primary benefit) + business name + visual. Nothing else. |
| **Back** | Outside back | Contact details + brief boilerplate + secondary CTA |
| **Inside left** | First seen on opening | The problem — stated in the reader's language |
| **Inside centre** | Central panel | The solution — your services, outcome-led |
| **Inside right** | Third inside panel | Proof — testimonials, case results, credentials |
| **Back left flap** | Inside back | Call to action + contact details repeated |

**Rule:** Design the cover as the most powerful panel. It is the only panel the prospect sees if they are not yet interested.

---

## Part 7 — Design Instructions to Include

When briefing a designer, include these content-level design notes:

- Maximum two font families
- Body copy minimum 10pt for print; 14px for digital
- White space is deliberate — do not fill it with more copy or decorative elements
- Photography must show real results, real environments, or real clients — not generic stock
- Every image must serve a specific purpose (illustrate a benefit, provide social proof, or convey scale)
- The call to action must be visually distinct — boxed, coloured, or enlarged
- Separate editorial decisions from design decisions: write the full copy first, then brief the designer

---

## Quality Criteria

Good output from this skill:
1. The brochure has a single, clearly defined purpose and a single call to action
2. The cover headline states a primary benefit — not the company name alone
3. Every service is described in terms of outcomes, not processes or inputs
4. At least one proof element (testimonial, case result, statistic) appears inside
5. The copy avoids the eight most common brochure mistakes listed above
6. The panel-by-panel structure follows a logical journey from problem to solution to proof to action
7. All copy is written in British English using the register defined in `east-african-english`

---

## References

- Hahn, F.E. (2003) *Do-It-Yourself Advertising and Promotion*, 3rd edn. Hoboken: Wiley.
- Pinskey, R. (1997) *101 Ways to Promote Yourself*. New York: Avon Books.
```

**Steps:**
1. Create directory `copywriting-brochure/`
2. Write SKILL.md
3. Verify under 500 lines
4. Commit: `git add copywriting-brochure/ && git commit -m "feat: add copywriting-brochure skill from book synthesis"`

---

## PHASE 2 — Enhancements to Existing Skills (8 skills)

---

### Task 6: Enhance `content-writing`

**File:** `content-writing/SKILL.md`

**Action:** Read the file first. Then add a new section after the existing intro/overview section and before the first main content section. Add the following:

```markdown
## The WIIFM Principle

Every piece of content — before a word is written — must answer the reader's unspoken question: **"What's In It For Me?"**

*Edwards, Edwards and Douglas (1991)*

This is not a copywriting technique. It is a complete mental reorientation: stop thinking about what the client wants to say and start thinking about what the audience wants to hear, find, solve, or achieve.

**Apply before writing:**
- Who specifically is reading this?
- What do they want to accomplish, avoid, or understand?
- What is the one thing in this content that is most directly useful to them?
- Lead with that.

## Features vs Benefits Doctrine

*"Features instruct. Benefits sell."* — Hahn (2003)

| Feature | Benefit |
|---|---|
| Describes what a product/service IS or HAS | Describes what that feature DOES FOR the buyer |
| "12 posts per month" | "Your brand is visible to your audience every 2–3 days" |
| "24-hour response time" | "Your customers never wait overnight for an answer" |
| "Bilingual copywriting" | "You reach both English and Luganda-speaking customers without running two separate accounts" |

**Process:** For every feature in a piece of content, ask "So what does this mean to the reader?" The answer is the benefit. Lead with the benefit; use the feature as supporting evidence.

**Reference:** See `direct-mail-writer` for Galletti's 27 Copywriting Points — a full checklist applicable to any persuasive content.
```

**Steps:**
1. Read `content-writing/SKILL.md`
2. Add the WIIFM and Features vs Benefits section in the appropriate location
3. Verify the total file remains under 500 lines
4. Commit: `git add content-writing/SKILL.md && git commit -m "enhance: add WIIFM + features-vs-benefits doctrine to content-writing"`

---

### Task 7: Enhance `05-social-media-strategy`

**File:** `05-social-media-strategy/SKILL.md`

**Action:** Read the file first. Locate the strategic frameworks section (likely near the top or in an "Approach" section). Add the ARM framework as an additional lens:

```markdown
### ARM Content Testing Lens

Before approving any content plan or campaign, apply the ARM framework to verify balanced coverage:
*(Hahn, 2003)*

| Letter | Objective | Test Question |
|---|---|---|
| **A — Attract** | Bring in new audiences and prospects | Does this content reach people who do not yet know us? |
| **R — Retain** | Keep existing followers engaged and loyal | Does this content reward people who already follow us? |
| **M — Motivate** | Drive existing audiences to act, buy, or refer | Does this content give existing customers a reason to do something now? |

A healthy content plan addresses all three. A plan heavy on M (promotional) without A or R will shrink its audience over time. A plan heavy on A without M will grow an audience that never converts.
```

**Steps:**
1. Read `05-social-media-strategy/SKILL.md`
2. Add the ARM section to the frameworks section
3. Verify under 500 lines
4. Commit: `git add 05-social-media-strategy/SKILL.md && git commit -m "enhance: add ARM framework to 05-social-media-strategy"`

---

### Task 8: Enhance `biz-dev-credentials`

**File:** `biz-dev-credentials/SKILL.md`

**Action:** Read the file first. Add the Brand Asset Scorecard as an optional diagnostic tool — positioned as a pre-credentials self-assessment or a client brand audit tool:

```markdown
## Brand Asset Scorecard

*Killian, B., in Hahn (2003)*

Use this 16-criterion scorecard to assess brand health before building a credentials deck. Rate each criterion 1–10. Low scores reveal gaps the credentials should address or acknowledge.

| # | Criterion | Score (1–10) | Notes |
|---|---|---|---|
| 1 | Brand Name | | |
| 2 | Packaging / visual identity | | |
| 3 | Reach and frequency | | |
| 4 | Ad / content quality | | |
| 5 | Promotions and offers | | |
| 6 | Consistency across channels | | |
| 7 | Distribution / availability | | |
| 8 | Newsworthiness | | |
| 9 | Likeability | | |
| 10 | Trade / partner support | | |
| 11 | Sales team capability | | |
| 12 | User / customer profile clarity | | |
| 13 | Product / service performance | | |
| 14 | Repurchasing / retention rate | | |
| 15 | Actionable research / data | | |
| 16 | Perceived value | | |

**Scoring:** 130–160 = strong brand; 90–129 = functional but gaps present; below 90 = significant brand investment required.

When completing a credentials deck for a prospect client, use this scorecard to identify the brand strengths to emphasise and the gaps to offer as consultancy opportunities.
```

**Steps:**
1. Read `biz-dev-credentials/SKILL.md`
2. Add the scorecard section
3. Verify under 500 lines
4. Commit: `git add biz-dev-credentials/SKILL.md && git commit -m "enhance: add Brand Asset Scorecard to biz-dev-credentials"`

---

### Task 9: Enhance `07-email-marketing-strategy`

**File:** `07-email-marketing-strategy/SKILL.md`

**Action:** Read the file. Add the 11 Psychological Principles of Copywriting in the copy/content section:

```markdown
## Eleven Psychological Principles of Copywriting

Apply these principles when writing any email campaign, subject line, or marketing message:
*(Edwards, Edwards and Douglas, 1991)*

| # | Principle | Application |
|---|---|---|
| 1 | **Self-interest (WIIFM)** | Every subject line and opener leads with what the reader gets, not what the sender wants |
| 2 | **Specificity** | Specific claims are more credible than general ones ("34% more enquiries" beats "great results") |
| 3 | **Social proof** | Testimonials, named clients, or subscriber counts build trust before the ask |
| 4 | **Scarcity / urgency** | A genuine deadline or limited availability increases action rate |
| 5 | **Authority** | Credentials, publications, and client names signal expertise |
| 6 | **Reciprocity** | Give something of value first — a tip, a guide, a free audit — before making an offer |
| 7 | **Consistency** | People act in ways consistent with prior commitments — reference past interactions |
| 8 | **Liking** | Warm, human tone increases open and click rates; robotic copy reduces them |
| 9 | **Fear of loss** | Loss framing ("Don't miss…") outperforms gain framing ("You could gain…") |
| 10 | **Novelty** | "New" and "first" consistently attract attention in subject lines |
| 11 | **Story** | A brief narrative outperforms a list of facts in both engagement and recall |
```

**Steps:**
1. Read `07-email-marketing-strategy/SKILL.md`
2. Add the 11 principles in the copy/content section
3. Verify under 500 lines
4. Commit: `git add 07-email-marketing-strategy/SKILL.md && git commit -m "enhance: add 11 psychological copywriting principles to 07-email-marketing-strategy"`

---

### Task 10: Enhance `deck-strategy-presentation`

**File:** `deck-strategy-presentation/SKILL.md`

**Action:** Read the file. Add the following to the slide design / delivery guidance section:

```markdown
## The Case for Visuals — 3M/Wharton Data

*Cited in Pinskey (1997)*

- Presentations using visuals are **43% more persuasive** than those without
- Audiences retain information **65% better** when paired with a relevant visual
- A presenter using visuals is perceived as more prepared, more professional, and more credible

**Implication for strategy decks:** Every data point should have a chart. Every conceptual argument should have a diagram. Every case study should have a before/after visual. Text-only slides are an opportunity cost.

**Principles:**
- One idea per slide — never two arguments on the same slide
- Headline each slide with the **conclusion**, not the topic (Minto's Pyramid Principle — conclusion first, evidence below)
- Use images where possible, bullet lists only where genuinely required
- The handout must add value beyond the slide content — include supporting data, references, and action items the slide did not have room for
```

**Steps:**
1. Read `deck-strategy-presentation/SKILL.md`
2. Add the visuals section
3. Verify under 500 lines
4. Commit: `git add deck-strategy-presentation/SKILL.md && git commit -m "enhance: add 3M/Wharton visuals data to deck-strategy-presentation"`

---

### Task 11: Enhance `01-client-brief`

**File:** `01-client-brief/SKILL.md`

**Action:** Read the file. Locate the intake questions section. Add the following questions to the existing required input list:

```markdown
### Positioning Questions (add to intake form)

**USP / Differentiation:**
> "What is the one thing your business does or delivers that your closest competitor does not — or cannot — do as well?"

**Mission:**
> "In one sentence: what does your business do, for whom, and what outcome does it deliver?"

**Vision:**
> "Where do you want this business to be in three years? What does success look like specifically?"

**Niche:**
> "Describe your single most ideal client — their sector, size, location, and the specific problem they have that you solve best."

*These answers feed directly into `biz-dev-positioning` and all strategy and content work. Collect them at intake and store in the client file.*
```

**Steps:**
1. Read `01-client-brief/SKILL.md`
2. Add the four positioning questions to the intake section
3. Verify under 500 lines
4. Commit: `git add 01-client-brief/SKILL.md && git commit -m "enhance: add USP/mission/vision/niche intake questions to 01-client-brief"`

---

### Task 12: Enhance `meta-roi-framework`

**File:** `meta-roi-framework/SKILL.md`

**Action:** Read the file. Add the FRAT formula and $20 Rule to the measurement section:

```markdown
## FRAT — Customer List Prioritisation Formula

*Hahn (2003)*

When a client has a customer database and needs to prioritise who to contact first (for a campaign, a renewal, or a direct mail programme), apply FRAT scoring:

| Letter | Factor | Question |
|---|---|---|
| **F** | Frequency | How many times has this contact bought or enquired? |
| **R** | Recency | How recently did they last buy or enquire? |
| **A** | Amount | What is their average transaction value? |
| **T** | Type | What type of product or service do they purchase? |

Score each contact on all four criteria (1–5 per factor). Sort by total score descending. The highest-scoring contacts are the most responsive and should be contacted first, most often, and with the most effort.

## The $20 Rule — Campaign Budget Viability Test

*Hahn (2003)*

Before committing to any direct marketing campaign (email, direct mail, WhatsApp broadcast), check budget viability:

> For every UGX 20,000 (or equivalent USD $20) of projected revenue per transaction, the campaign can afford to invest UGX 1,000 (or USD $1) per contact reached.

**Examples:**
- Projected transaction value: UGX 200,000 → affordable spend per contact: UGX 10,000
- Projected transaction value: UGX 1,000,000 → affordable spend per contact: UGX 50,000

Use this to guide format decisions and campaign feasibility before recommending any outbound activity.
```

**Steps:**
1. Read `meta-roi-framework/SKILL.md`
2. Add the FRAT and $20 Rule sections
3. Verify under 500 lines
4. Commit: `git add meta-roi-framework/SKILL.md && git commit -m "enhance: add FRAT formula + $20 Rule to meta-roi-framework"`

---

### Task 13: Enhance `10-content-pillars`

**File:** `10-content-pillars/SKILL.md`

**Action:** Read the file. Add the 8 Imprints Rule to the frequency/volume section:

```markdown
## The 8 Imprints Rule — Why Frequency Matters

*Pinskey (1997)*

A prospect typically needs to encounter a brand or business name **8 times** before they will take action.

This is why content pillars and content frequency are not cosmetic — they are the engine of conversion.

**What counts as an imprint:**
- A social media post seen and processed
- A direct message received
- A referral conversation heard
- A brochure read
- An email opened
- A website visited
- A sign or poster noticed
- A face-to-face meeting held

**Implication for content pillars:** A single pillar producing once-monthly content is generating roughly 12 imprints per year — just above the minimum threshold. Content pillars that produce weekly content generate 52 imprints per year — making conversion significantly more likely.

**When presenting content pillars to a client:** use the 8 Imprints Rule to justify frequency recommendations. Posting three times per week is not vanity — it is the minimum required to reliably cross the threshold from awareness to action.

**Compatible reference:** The 10-4-1 rule (Bodnar and Cohen, 2012) defines the *type* of content across 15 posts; the 8 Imprints Rule explains *why* those 15 posts are necessary.
```

**Steps:**
1. Read `10-content-pillars/SKILL.md`
2. Add the 8 Imprints Rule section
3. Verify under 500 lines
4. Commit: `git add 10-content-pillars/SKILL.md && git commit -m "enhance: add 8 Imprints Rule to 10-content-pillars"`

---

## Final Commit

After all 13 tasks are complete:

```bash
git log --oneline -15
```

Verify all 13 commits are present. Then update `docs/gap-analysis-2026-03-new-books.md` or create a new `docs/gap-analysis-2026-03-advertising-books.md` to record what was built from these three books.

---

## Summary

| Phase | Tasks | Output |
|---|---|---|
| 1 — New Skills | 5 (Tasks 1–5) | `playbook-pr-publicity`, `direct-mail-writer`, `playbook-networking`, `biz-dev-positioning`, `copywriting-brochure` |
| 2 — Enhancements | 8 (Tasks 6–13) | 8 existing skills enhanced with new frameworks from Hahn, Edwards, and Pinskey |

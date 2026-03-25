---
title: LinkedIn Company Pages Skill — Design Document
date: 2026-03-25
status: approved
---

# LinkedIn Company Pages Skill — Design

## Decision

Create a new standalone skill: `platform-linkedin-company-pages`.

Do **not** modify the existing `platform-linkedin` skill. The new skill is complementary — `platform-linkedin` covers personal profiles and individual brand strategy; this skill covers the organisational Company Page asset.

## Source Material

Raymond, M.J. and Johnston, L. (2021) *Business Gold: Build Awareness, Authority, and Advantage with LinkedIn Company Pages*. 82 pages. Full book absorbed.

## Skill Metadata

- **Directory:** `platform-linkedin-company-pages/`
- **File:** `SKILL.md`
- **Frontmatter name:** `platform-linkedin-company-pages`
- **Frontmatter description:** Generates a complete LinkedIn Company Page strategy — page setup, admin structure, content approach, follower growth, Sub-Pages, and Events. Invoke when a client is an organisation (company, NGO, agency) that needs to build or optimise their Company Page as a credibility and lead generation asset. Complement with `platform-linkedin` for personal profile strategy.
- **Target length:** 380–420 lines (hard limit: 500)

## Required Input

- Client name and industry
- Country/city (default: Kampala, Uganda)
- Primary goal: brand credibility / B2B lead generation / talent acquisition / investor relations
- Current Company Page follower count (or "none — starting from zero")
- Target audience: 2–3 decision-maker job titles and industries
- Whether founding team / leadership are willing to post personally (yes/no)
- Budget band for paid: none / low / medium / high
- Outputs from `04-brand-voice-intake` if available

## Sections

### Section 1: Company Page Setup — 13-Step Checklist

Full setup walkthrough covering all 13 steps from the source:

- Logo: 300×300px, transparent background preferred
- Cover image: 1128×191px, include tagline + website + CTA
- Tagline: 120 characters — precise statement of what the business does and for whom
- About/Overview: 2,000 characters maximum, keyword-optimised
- Specialties: up to 20 — use specific service/product terms visible in search
- Page hashtags: 3 hashtags the Page follows (strategic selection by audience and content focus)
- Custom URL: set to linkedin.com/company/[brand-name]
- CTA button: configured for primary goal (Visit website / Contact us / Learn more)
- Featured content: pin most important post or resource
- Location and company size
- Page type and industry classification
- Linked personal profiles of admins
- Completeness check: complete pages receive 30% more weekly views (LinkedIn, cited in Raymond and Johnston, 2021)

Reality check stats to include:
- Pages reach approximately 3% of followers organically (vs ~10% for personal posts)
- Weekly posting delivers 2× engagement lift
- Traction threshold: 500–1,000 followers is the compounding point

### Section 2: Admin Roles

**Internal roles:**
- Super Admin — full control: edit page, manage admins, publish content, view analytics
- Content Admin — create and publish posts, respond to comments
- Curator — suggest content to post (no direct publish access)
- Analyst — view analytics only; no publishing rights

**Paid media roles (only relevant when paid budget exists):**
- Sponsored Content Poster — can boost posts and run sponsored content campaigns
- Lead Gen Forms Manager — create and manage lead gen forms attached to paid campaigns
- Pipeline Builder — access to Sales Navigator integration

Practical guidance: minimum viable structure (solo admin), small team structure (Super + Content), agency/communications team structure (all roles).

### Section 3: Content Strategy

**Know, Like and Trust framework** (Raymond and Johnston, 2021): content must move the audience through three stages — from awareness (Know) to affinity (Like) to confidence (Trust). All three must be present in the content mix; a page heavy on Trust content (case studies, credentials) without Know or Like content will not grow.

**Three content categories:**
- Big Picture — industry context, sector trends, world view; positions the brand as informed and relevant
- Human Interest — people, culture, behind-the-scenes, team stories; builds the Like stage
- Products & Services — what the brand offers, how it works, outcomes achieved; drives Trust and conversion

Cross-reference to established frameworks:
- 10-4-1 rule (Bodnar and Cohen, 2012): apply across all three categories
- Hero/Hub/Hygiene tier assignment per content type

**Content techniques:**
- Series: recurring formats on a schedule (e.g. weekly industry insight, monthly team spotlight)
- Repurposing: reformatting existing content — a blog post becomes a carousel; a webinar becomes clip posts
- Themes: monthly or seasonal content focus aligned to business calendar

**Five posting mistakes to avoid:**
1. Wall of text — use white space; one idea per paragraph
2. Over-promotion — Products & Services content should not dominate the mix; apply 10-4-1
3. Cross-posting without tailoring — content written for Instagram or Facebook reads as off-brand on LinkedIn
4. Too many hashtags — maximum 3–5 per post; more than 5 reduces reach
5. External links in the post body — LinkedIn suppresses reach for posts that send users off-platform; always paste the link in the first comment and note this at the end of the post

### Section 4: Follower Growth — Invite System and Growth Strategies

**Invite system mechanics:**
- 100 invite credits per month per Page (pooled across all admins)
- Credits are returned when an invitation is accepted — net cost of successful invites is zero
- Invitations can only be sent to first-degree connections of Page admins
- Accepted invitations do not consume a credit permanently; declined or ignored invitations do

**Three growth strategies:**

| Strategy | Description | Best for |
|---|---|---|
| Brand Awareness | Broad invite campaigns targeting all relevant first-degree connections; cross-promote Page on other platforms and in email signatures | Early stage: 0–500 followers |
| Niche Community | Targeted invites to specific job titles and industries; content tuned to a defined professional audience | Mid stage: building a focused, high-quality follower base |
| Account-Based Marketing | Target followers at specific named companies; content designed to resonate with decision-makers at priority accounts | B2B clients with a defined ICP |

**Employee amplification:**
- Ask all employees to follow the Page and to invite their own connections (using their own 100 credits)
- Share-ready post templates for employees to personalise and publish on their personal profiles
- Cross-reference `playbook-employee-advocacy` for full employee activation programme

### Section 5: Sub-Pages

**Showcase Pages**
- Up to 25 per Company Page
- Purpose: separate brand assets for distinct initiatives, audience segments, or product lines — e.g. a corporate social responsibility programme, a recruitment brand, a regional subsidiary
- Has its own follower count, content feed, and admin team
- Linked to the parent Company Page — visible in the "Affiliated pages" section
- When to use: when the initiative has a distinct audience that does not overlap with the main Page's audience
- When NOT to use: when follower counts are below 1,000 — creating sub-pages fragments the brand's presence before critical mass is reached

**Product Pages**
- Up to 35 per Company Page
- Require LinkedIn approval before going live
- Features: product name, description, logo, media (images/video), customer recommendations, featured customers
- Effectively a LinkedIn product catalogue — each product has its own page within the Company Page
- When to use: when the client has discrete, named products with distinct buyer audiences and wants social proof (recommendations) at product level
- When NOT to use: for service businesses with bespoke engagements where product pages would misrepresent the offering

**Subsidiary / Acquisition Pages**
- Enterprise-level feature; links acquired companies or subsidiaries to a parent Company Page
- Shows "Part of [Parent Company]" on the subsidiary's page
- Relevant for large organisations or conglomerates; not applicable to most SME clients

### Section 6: LinkedIn Events

**Two event types:**

| Type | Requirements | Registration |
|---|---|---|
| Off-platform event | No follower minimum; links to external registration page | External (Eventbrite, Google Forms, direct booking) |
| LinkedIn Live | 150+ followers; broadcasting tool required (StreamYard, Restream, etc.) | Internal LinkedIn registration |

**Registered vs non-registered events:**
- Registered: attendees opt in via LinkedIn; organisers can see attendee list and send follow-up messages
- Non-registered: awareness only; no attendee data captured — use only for broad awareness

**Promotion cadence:**
- 2 weeks before: announce the event with a post; send invitations to relevant connections
- 1 week before: reminder post with a key benefit or preview; target 1,000 invites per admin per week (platform limit)
- Day before: final reminder post
- Day of event: go live or publish event link; engage in event comments
- Post-event: recap post within 48 hours; connect with all registered attendees; share recording link

**Follow-up:**
Within 48 hours of the event, send personalised connection requests to all registered attendees who are not yet first-degree connections. Reference the event in the message.

### Section 7: 30-Day Company Page Content Plan

20 posts (5 per week) across four weeks. Each entry includes:
- Format (text post, document/carousel, native video, poll, event)
- Content category (Big Picture / Human Interest / Products & Services)
- Hook line
- Content brief (3–5 sentences)
- CTA

**Week 1 — Establish the Page:** company introduction, About section announcement, first carousel, team or founder post, industry observation.

**Week 2 — Demonstrate expertise:** case study or client result, product/service explainer carousel, Big Picture industry post, poll, testimonial.

**Week 3 — Engage the audience:** opinion post, Q&A or open question, behind-the-scenes, event announcement or webinar, employee spotlight.

**Week 4 — Convert and grow:** service promotion, month-in-review carousel, invite-focused post ("Follow us for…"), newsletter announcement, forward-looking preview of next month.

### Section 8: KPIs

**Company Page engagement rate formula** (Raymond and Johnston, 2021):
`(Likes + Comments + Shares + Clicks + Follows) ÷ Impressions × 100`

Note: this formula includes Clicks and Follows — broader than the formula commonly cited for personal posts, which typically counts only Reactions + Comments + Shares.

| KPI | Benchmark | Notes |
|---|---|---|
| Engagement rate | 2–4% organic | Below 2% for 4 consecutive weeks: audit content mix |
| Follower growth | 5–10% monthly (growth phase) | Track net new followers |
| Post impressions | Growing month-on-month | Segment by content category |
| Invite acceptance rate | 20–40% | Track accepted ÷ sent per month |
| Sub-Page follower growth | Growing relative to main Page | If sub-page is not growing, consolidate |
| Event registrations | Track per event | Registered events only; set a target per event type |
| Click-through rate | 1–3% for link posts | Links go in first comment; track via UTM |

Review monthly using `meta-reporting` skill. If engagement rate drops below 2% for 4 consecutive weeks, increase Big Picture and Human Interest content; reduce Products & Services ratio.

## Quality Criteria

1. The 13-step setup checklist covers all elements; completeness payoff stats (30% more views, 2× engagement) are cited
2. Admin roles section distinguishes internal roles from paid media roles; guidance on minimum viable structure for different team sizes is included
3. Know, Like and Trust framework is applied as the organising principle for the content strategy section — not just named but operationalised
4. The invite system mechanics are explained with the credit-return mechanic clearly stated; growth strategies are mapped to follower count stage
5. Sub-Pages section includes a decision framework (when to use / when NOT to use) not just a description of features
6. Events section distinguishes off-platform from LinkedIn Live with specific requirements for each; promotion cadence is specific (2 weeks / 1 week / day before / post-event)
7. The 30-day plan contains 20 posts with all required fields; content is client-specific, not generic
8. Engagement rate formula cited correctly from source; differs from personal post formula and the difference is noted
9. `platform-linkedin` is cross-referenced for personal profile strategy — this skill does not duplicate that content
10. British English throughout

## What This Skill Does NOT Cover

These topics remain in `platform-linkedin` and are cross-referenced, not duplicated:

- Personal profile optimisation (headline formula, About section, Featured section, custom URL)
- AIDA post structure for personal posts
- Connection request templates and warm-up tactics
- Boolean search and trigger-based prospecting
- Individual brand strategy (artists, politicians, creatives)
- Personal posting frequency and the 1.80 Dollar Strategy
- The 30-day personal profile content plan

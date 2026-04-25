---
name: playbook-paid-social-advertising
description: Produces a paid social media strategy and campaign brief for clients who have never run social ads or are running them poorly. Covers campaign objective selection, audience targeting tiers, Meta Pixel setup instructions, campaign structure, budget allocation, creative briefing, WhatsApp Click-to-Chat ads, performance metrics, and a monthly reporting template. Does not cover ad operations, bidding, creative production, or copywriting. Invoke this skill when a client wants to start paid social advertising, when a client's existing ads are underperforming, or when a consultant needs to design a paid social plan and hand off a brief to an ads operator.
---
# Paid Social Advertising Playbook

<!-- dual-compat:start -->
## Use when
- Produces a paid social media strategy and campaign brief for clients who have never run social ads or are running them poorly. Covers campaign objective selection, audience targeting tiers, Meta Pixel setup instructions, campaign structure, budget allocation, creative briefing, WhatsApp Click-to-Chat ads, performance metrics, and a monthly reporting template. Does not cover ad operations, bidding, creative production, or copywriting. Invoke this skill when a client wants to start paid social advertising, when a client's existing ads are underperforming, or when a consultant needs to design a paid social plan and hand off a brief to an ads operator.
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
- A structured markdown document, plan, playbook, or strategy ready for client-facing or internal use.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Ask for the following before generating the plan:

1. **Client business name and industry** — e.g., "Kampala Fresh — retail food & beverage"
2. **Country/city** — default is Uganda/East Africa if not specified
3. **Primary business objective** — state as a single SMART goal (e.g., "Generate 50 qualified leads per month by June 2026")
4. **Monthly paid social budget** — in UGX; see Section 4 for budget tier guidance
5. **Current paid activity** — what ads, if any, are running now; include the objective selected in Ads Manager, current monthly spend, and any results data available
6. **Website URL** — confirm whether the site is active and whether Meta Pixel is already installed
7. **WhatsApp Business number** — the number customers should message; confirm it is active and monitored
8. **Platforms in scope** — Facebook, Instagram, YouTube, or other; default for Uganda/EA is Facebook/Instagram (Meta)
9. **Who will operate the ads** — the client in-house, a media buyer, or a separate digital agency; this determines how detailed the creative brief must be

---

## Out of Scope

This skill produces a strategy and plan document. The following tasks are explicitly excluded:

- Ad bidding, targeting adjustments, or day-to-day campaign optimisation inside Ads Manager
- Creative production — graphic design, video editing, photography
- Ad copywriting — use the `caption-writer` skill for all ad copy and CTAs
- Audience research beyond the three-tier targeting framework below
- Influencer contracts or paid partnerships — refer to a legal professional

---

## Section 1 — Campaign Objective Selection

Select the campaign objective before building any other part of the plan. The objective determines how Meta's algorithm optimises delivery, who sees the ad, and how results are measured. Choosing the wrong objective is the single most common mistake in paid social — particularly using "Boost Post" when a direct-response result is required.

### The Three Objective Tiers

**Awareness objectives** — use when the client has low brand recognition and the immediate goal is reach, not action.
- Best for: new businesses, product launches, event promotion
- Meta objectives to use: Awareness → Brand Awareness or Reach
- Expected result: impressions, reach, cost per 1,000 impressions (CPM)
- Avoid awareness objectives when the client's budget is under UGX 200,000/month — the audience is too small to generate meaningful reach at that spend

**Consideration objectives** — use when the brand is known but prospects need a reason to engage or learn more.
- Best for: driving website traffic, increasing video views, generating DMs or WhatsApp conversations
- Meta objectives to use: Traffic, Engagement, Video Views, or Leads
- Expected result: link clicks, landing page views, cost per lead (CPL), cost per message
- The Leads objective (with an instant form) works well where the client lacks a landing page

**Conversion objectives** — use when the goal is a specific action: a purchase, a booking, a form submission, or a WhatsApp message from an interested buyer.
- Best for: e-commerce, service bookings, lead generation with a functioning website
- Meta objectives to use: Sales or Leads (with Pixel or Conversions API enabled)
- Requires Meta Pixel installed on the website — do not run conversion campaigns without it
- Expected result: cost per acquisition (CPA), cost per lead (CPL), return on ad spend (ROAS)

### When to Use Boost Post vs. Ads Manager

| Situation | Recommendation |
|---|---|
| Organic post performing well, objective is awareness only | Boost Post is acceptable — quick, simple, low cost |
| Client wants leads, sales, website traffic, or WhatsApp messages | Use Ads Manager — Boost Post does not optimise for these outcomes |
| Client wants to retarget previous visitors or warm audiences | Use Ads Manager — Boost Post has no retargeting capability |
| Client budget exceeds UGX 200,000/month on any single campaign | Use Ads Manager — the optimisation options justify the additional setup time |
| Client is testing a new creative or audience | Use Ads Manager — split testing is unavailable in Boost Post |

**Default recommendation for Uganda/EA SME clients:** use Ads Manager for all campaigns with a business objective. Reserve Boost Post only for event promotion and organic content amplification where no direct response is expected.

---

## Section 2 — Audience Targeting Tiers

Structure every campaign using three audience tiers. Each tier has a different level of brand familiarity and requires a different message and budget weighting.

### Tier 1 — Cold Audience (Interest-Based and Demographic)

Cold audiences have no prior relationship with the brand. Target them using:
- Demographics: age, gender, location (use city-level targeting for Kampala; national targeting for mass-market products)
- Interests: Meta's interest categories relevant to the client's industry — e.g., "small business owners", "health and wellness", "construction and real estate"
- Lookalike audiences: built from the client's existing customer list or Page fans (minimum 100 seed records for a usable lookalike in Uganda/EA)

**Message type for cold audiences:** brand introduction, problem-solution framing, social proof (testimonials, results, reviews). Do not lead with a hard offer — cold audiences need a reason to trust first.

**Budget allocation:** 50% of total paid social budget (see Section 4).

### Tier 2 — Warm Audience (Engaged Audience)

Warm audiences have interacted with the brand but have not converted. Build warm audiences from:
- People who have liked, commented on, or shared a post or ad in the last 30–90 days
- Page fans (Facebook Page followers)
- People who have watched 75% or more of any video ad or organic video on the Page — this is the most important warm audience for EA clients without a website or Pixel. A 15-second organic video can build a usable retargeting pool within 2–4 weeks at zero media cost. Target 75% viewers (not 25%) to qualify for genuine interest, not accidental exposure
- People who have watched 25% or more of a video ad (broader warm signal, appropriate for awareness-stage retargeting)
- People who have visited the website (requires Meta Pixel — see Section 3)
- People who have messaged the WhatsApp Business account (requires Pixel or Conversions API)

**Message type for warm audiences:** specific offer, case study, product demonstration, or testimonial that addresses the most common objection to purchase.

**Budget allocation:** 30% of total paid social budget.

### Tier 3 — Retargeting Audience (High-Intent Non-Converters)

Retargeting reaches people who showed strong buying intent but did not complete the desired action. Build retargeting audiences from:
- Website visitors who viewed a specific product or service page but did not submit a form or make a purchase (requires Meta Pixel)
- People who clicked a lead form ad but did not submit it
- People who initiated a WhatsApp conversation but did not complete a transaction

**Message type for retargeting:** urgency, limited offer, direct CTA, objection handling. These audiences are closest to conversion — the message should be direct and specific.

**Budget allocation:** 20% of total paid social budget.

**Note:** retargeting audiences in Uganda/EA are often small in the early months of a campaign. If the retargeting audience is under 1,000 people, hold the retargeting budget and reallocate it to Tier 1 until the audience grows.

---

## Section 3 — Meta Pixel: Setup and Purpose

### What the Meta Pixel Does

The Meta Pixel is a short snippet of tracking code installed on the client's website. Once installed, it records which pages visitors view, which actions they take (form submissions, purchases, button clicks), and which ads drove each visit. This data powers retargeting audiences (Section 2, Tier 3), enables conversion-optimised campaigns, and improves the accuracy of lookalike audience building.

Without the Pixel, the campaign operates on audience estimates only. With the Pixel, the algorithm learns from real customer behaviour.

### Consultant's Role in Pixel Setup

The consultant does not install the Pixel. Installation is a technical task for the client's web developer. The consultant's role is to:
1. Confirm whether a Pixel is already installed (use the Meta Pixel Helper browser extension to check)
2. Generate the Pixel ID from the client's Meta Business Manager account
3. Provide the developer with a written setup brief (template below)
4. Verify installation is correct once the developer confirms it is done

### Pixel Setup Brief for the Web Developer

Provide this to the client's web developer when no Pixel is installed:

> **Task:** Install the Meta Pixel on [Client Website URL]
>
> **Pixel ID:** [Insert from Meta Events Manager → Data Sources → Add]
>
> **Pages requiring the base code:** all pages (header installation preferred so every page visit is tracked)
>
> **Standard events to configure:**
> - `ViewContent` — fires when a user views a product or service page
> - `Lead` — fires when a user submits an enquiry form or contact form
> - `Purchase` — fires when a user completes a purchase (e-commerce clients only)
> - `Contact` — fires when a user clicks a WhatsApp or phone link
>
> **Verification method:** once installed, test using Meta Events Manager → Test Events, or using the Meta Pixel Helper Chrome extension. Confirm that the `PageView` event fires on every page.
>
> **Deadline:** [insert date — recommend 5 business days before the first Conversion campaign launches]

---

## Section 4 — Campaign Structure

Every Meta campaign follows a three-level hierarchy. Understanding this structure is essential for budget control and creative testing.

```
Campaign → Ad Set → Ad

Campaign: sets the objective and overall budget
Ad Set:   sets the audience, placement, schedule, and budget
Ad:       sets the creative (image, video, copy, CTA)
```

### Recommended Structure for a Standard SME Campaign

**Campaign level — one campaign per objective.** Do not run awareness and conversion objectives in the same campaign. Keep objectives separate so that performance data is clean.

**Ad Set level — one ad set per audience tier.** Create three ad sets in each campaign: one for the cold audience, one for the warm audience, and one for retargeting. Assign budget at the ad set level initially so you can see which audience tier is generating the lowest cost per result.

**Ad level — two to three ads per ad set.** Run two or three creative variants per ad set to identify which performs best. Test one variable at a time — either the image or the copy, not both. Use `meta-testing-framework` for structured creative testing.

### Campaign Budget Optimisation (CBO) vs. Ad Set Budget

- Use **Ad Set Budget** (ABO) for the first two to four weeks of a campaign — it gives you control over how much each audience tier spends and prevents Meta from concentrating all budget on the largest audience.
- Switch to **Campaign Budget Optimisation** (CBO) only after you have data showing which audience tier is converting best. CBO then allocates dynamically toward the best-performing set.

---

## Section 5 — Budget Allocation Principles

### UGX Budget Bands by Business Size

| Business Tier | Monthly Paid Social Budget | Recommended Starting Approach |
|---|---|---|
| Micro / sole trader | UGX 50,000 – 150,000 | Single ad set, Facebook only, one objective, boost best-performing organic post |
| Small SME | UGX 150,000 – 500,000 | Ads Manager, one campaign, two ad sets (cold + warm), Meta Leads objective |
| Mid SME | UGX 500,000 – 1,500,000 | Three-tier audience structure, Conversion or Leads objective, Pixel required |
| Large SME / Corporate | UGX 1,500,000 – 2,000,000+ | Full three-tier structure, split testing, Pixel mandatory, monthly optimisation cycle |

### Daily Budget vs. Lifetime Budget

**Use daily budgets when:**
- The campaign runs indefinitely with no fixed end date
- The client wants consistent daily delivery
- You are in a learning phase and want predictable spend

**Use lifetime budgets when:**
- The campaign has a fixed end date (event promotion, seasonal offer)
- You want Meta to distribute spend optimally across the campaign window
- Budget is tight and you want Meta to find the best-performing days and times

**Do not combine daily and lifetime budgets across ad sets in the same campaign** — it makes performance comparison unreliable.

### The 50/30/20 Audience Budget Split

Apply this split to the total paid social budget at the ad set level:

- **50% — Cold audience:** building awareness and filling the top of the funnel
- **30% — Warm audience:** converting engaged prospects
- **20% — Retargeting:** closing high-intent non-converters

Adjust the split after the first four weeks based on cost-per-result data. If cold audience CPL is significantly higher than warm, shift 10% from cold to warm. If retargeting audience is too small (under 1,000), reallocate the 20% to cold until the audience grows.

### Start Small, Prove, Scale

Follow this three-stage methodology before committing significant budget:

**Stage 1 — Test (Weeks 1–2):** Run UGX 50,000–150,000/week across the three audience tiers. Do not optimise during the learning phase — Meta needs approximately 50 conversion events per ad set to exit the learning phase. Simply let it run and collect data.

**Stage 2 — Prove (Weeks 3–4):** Identify the winning audience tier and creative variant. Calculate CPL or CPA. Confirm the cost per result is below the client's acceptable acquisition threshold.

**Stage 3 — Scale (Month 2 onwards):** Increase the budget of the proven ad set by no more than 20–30% per week. Sudden large budget increases reset the learning phase and destabilise performance.

---

## Section 6 — Creative Briefing

The consultant produces a creative brief; the designer and copywriter execute it. For all ad copy and CTAs, use the `caption-writer` skill.

### Ad Format Specifications (Meta Platforms, 2026)

| Format | Recommended Dimensions | File Size Limit | Video Length | Notes |
|---|---|---|---|---|
| Single image (Feed) | 1080 × 1080 px (square) or 1200 × 628 px (landscape) | 30 MB | — | Square performs best on mobile |
| Carousel (2–10 cards) | 1080 × 1080 px per card | 30 MB per card | — | Use for product range or step-by-step story |
| Video (Feed) | 1080 × 1080 px or 1080 × 1920 px (vertical) | 4 GB | 6–60 seconds recommended | Keep under 15 sec for EA audiences on mobile data |
| Stories / Reels | 1080 × 1920 px (9:16) | 4 GB | 15–60 seconds | First 3 seconds must hook — no slow intros |
| WhatsApp Click-to-Chat | As per Feed image/video specs | Same as Feed | Same as Feed | Destination is a WhatsApp conversation, not a website |

**Mobile data note:** the majority of Ugandan/EA users access Meta on mobile with variable data costs. Keep all video ads under 15 seconds. Lead with the key message in the first 3 seconds — do not use slow brand intros. Use captions on all video ads — most users watch without sound.

### Three Creative Principles for Facebook Ads (Marshall, 2024)

Apply all three to every ad creative brief. Ads that lack any of the three struggle to stop the scroll.

- **Contrast** — the ad must look different from surrounding News Feed content. Use motion, bold colour, unusual framing, or an unexpected subject. An ad that blends into the feed is invisible — users do not consciously skip it, they simply never see it.
- **Curiosity** — lead with an open loop the viewer wants to close: an unexpected data point, a counter-intuitive claim, or a question without an immediate answer on screen. Curiosity works for cold audiences because it creates a reason to stop without requiring any prior brand relationship.
- **Comedy / entertainment** — if the ad is genuinely entertaining, users share it without prompting. Shared ads generate organic reach that multiplies paid reach at no extra cost — this is uniquely possible on social media and unavailable in search or email.

**Customer Awareness Timeline:** match copy to the audience's current level of awareness. Cold audiences (unaware of the problem) need problem-identification copy, not product promotion. Warm audiences (aware of the problem, not the solution) need a product introduction. Retargeting audiences (know the product) need a specific offer, deadline, or testimonial to overcome the final objection (Marshall, 2024).

**Image text warning:** Facebook suppresses ad images that contain more than 20% text — the ad shows up to five times less often and costs up to three times as much per click. Keep ad images clean; place all copy in the primary text field, not the image (Cooper, 2019).

### Creative Brief Template

Complete one brief per ad format per campaign:

```
Client: [Client name]
Campaign objective: [Awareness / Consideration / Conversion]
Ad format: [Single image / Carousel / Video / Story]
Target audience tier: [Cold / Warm / Retargeting]
Platform placement: [Facebook Feed / Instagram Feed / Stories / Reels / All placements]

Headline: [Max 40 characters — from caption-writer]
Primary text: [Max 125 characters for feed — from caption-writer]
CTA button: [Send Message / Learn More / Shop Now / Sign Up — select one]

Visual direction:
- [Describe the scene, product, person, or concept to show]
- [Specify brand colours to use]
- [Note any elements to avoid]

WhatsApp number (if Click-to-Chat): [+256 XXX XXX XXX]
Landing URL (if website): [Full URL with UTM parameters — see meta-utm-tracking]
```

---

## Section 7 — WhatsApp Click-to-Chat Ads

WhatsApp Click-to-Chat ads are among the highest-performing ad formats for Uganda/East Africa. When a user clicks the ad, Meta opens a pre-filled WhatsApp conversation directly with the business — no website, no form, no login. This matches the dominant customer behaviour of using WhatsApp for all business enquiries.

### When to Use Click-to-Chat Ads

- When the client's primary sales channel is WhatsApp (most EA SMEs)
- When the client does not have a website or the website is not optimised for mobile conversion
- When the service requires a conversation before purchase (e.g., bespoke services, events, bulk orders)
- When the product category involves trust-building (healthcare, financial services, professional services)

### How to Set Up a Click-to-Chat Ad

1. In Ads Manager, create a new campaign with objective **Engagement → Messaging** or **Leads → Instant Forms or Messaging**.
2. At ad set level, under **Messaging apps**, select **WhatsApp** as the destination.
3. Connect the client's WhatsApp Business account to Meta Business Manager (requires the client's Business Manager admin to complete this — the consultant guides, does not execute).
4. At the ad level, set the CTA button to **Send Message**.
5. In the **Message Template** field, set the opening message the user sees pre-filled in WhatsApp. Keep it short, specific, and low-friction.

### Opening Message Templates

The opening message should remove the effort of composing a first message. Provide the client with one of the following templates, customised for their product or service:

> "Hi, I'm interested in [Product/Service Name]. Can you send me more details?"

> "Hello, I saw your ad and would like to get a quote."

> "Hi! I'd like to book an appointment. When are you available?"

Advise the client to respond to all WhatsApp enquiries from ads within 2 hours during business hours. Unanswered messages are wasted ad spend. If the volume exceeds the team's capacity, recommend the `playbook-chatbot-strategy` skill to set up automated WhatsApp responses.

---

## Section 8 — Performance Metrics and Optimisation

### Primary Metrics (Track Weekly)

| Metric | Definition | Benchmark for Uganda/EA |
|---|---|---|
| CPM (Cost per 1,000 impressions) | Cost to show the ad 1,000 times | UGX 5,000–20,000 is typical for Facebook/Instagram |
| CPL (Cost per lead) | Total spend ÷ number of leads generated | Target: below the client's acceptable acquisition cost |
| CPA (Cost per acquisition) | Total spend ÷ number of conversions | Depends on product margin — define with client at brief stage |
| CTR (Click-through rate) | Clicks ÷ impressions | Above 1% is healthy; below 0.5% signals a creative or audience problem |

### Secondary Metrics (Track Monthly)

- **Frequency:** average number of times one person sees the ad. Above 3.0 in a week signals audience fatigue — refresh the creative or broaden the audience.
- **Relevance score / Quality ranking:** Meta's assessment of how well the ad matches its audience. Below Average ranking requires creative or audience revision.
- **Landing page view rate:** of everyone who clicked the ad, what percentage loaded the landing page. Below 60% suggests the page is slow or the audience intent is weak.
- **WhatsApp response rate:** of all Click-to-Chat ad clicks, what percentage sent a message. Below 40% suggests the pre-filled message is not compelling or the audience targeting is off.

### Weekly Optimisation Checklist

Complete this checklist every 7 days during an active campaign:

- [ ] Review CPL or CPA for each ad set — compare against the target threshold defined at brief stage
- [ ] Check frequency — if above 3.0, expand the audience or refresh the creative
- [ ] Identify the top-performing ad creative in each ad set — pause the underperforming variants
- [ ] Confirm the campaign has exited the learning phase (50+ optimisation events per ad set)
- [ ] Check that the Pixel is still firing correctly (Meta Events Manager → Test Events)
- [ ] Report weekly results to the client using the metrics above

### Ads Troubleshooting Protocol — Eight-Step Diagnostic

Apply this sequence when a campaign underperforms. Change only one variable per diagnostic step — changing multiple variables simultaneously makes the root cause unidentifiable (Cooper, 2019).

1. **Check Quality Ranking** — view the Quality Ranking, Engagement Rate Ranking, and Conversion Rate Ranking columns in Ads Manager. "Average" on all three is acceptable; "Below Average" on Quality Ranking means the creative is the primary problem.
2. **Check CPC trend** — cost per click should fall below approximately UGX 1,100 (USD 0.30) by day 3. If it has not, proceed to Step 3.
3. **Quality high but CPC high?** → Audience is the problem. The audience is too small (under 50,000 for Uganda-wide campaigns), too saturated (too many advertisers using the same interests), or mismatched. Adjust the audience; do not change the creative.
4. **Quality low and engagement poor?** → Creative is the problem. Test a new image first (highest-impact variable), then primary text, then headline. One change at a time.
5. **Check result rate** — click-through rate should reach at least 2.5%; 4–6% is good; 10%+ is strong. If quality ranking is acceptable but CTR is below 2.5%, rework the headline and CTA.
6. **Check frequency** — above 1.5 over a 7–14 day window signals audience saturation. Expand target interests, duplicate the ad set to a new demographic, or introduce a fresh creative.
7. **Check demographic breakdown** — identify age or gender segments with disproportionately high cost per result and exclude them at the ad set level.
8. **Kill threshold** — pause the ad if: day 3 with CPC still above UGX 1,100, result rate persistently below 1%, or quality ranking remains Below Average after one creative revision. A second creative change is justified; a third means the audience is the problem.

### When to Kill a Campaign

Pause or stop an ad set when:
- CPL or CPA exceeds the client's acceptable threshold for two consecutive weeks and no creative or audience change has reduced it
- Frequency exceeds 4.0 and a fresh creative has not yet been produced
- The campaign has spent UGX 100,000 without generating a single result at the Conversion objective level — diagnose before scaling

### When to Scale a Campaign

Increase budget when:
- CPL or CPA is consistently below the acceptable threshold for two or more consecutive weeks
- The campaign has fully exited the learning phase
- A new creative has been tested and outperforms the control — scale the winner, pause the loser
- Increase budget by no more than 30% per week to avoid resetting the learning phase

---

## Section 9 — Monthly Paid Social Report Structure

Produce a monthly paid performance report for every client running paid social campaigns. The report covers one calendar month and is delivered within 5 business days of the month end.

### Report Sections

**1. Executive Summary (1 paragraph)**
State the campaign objective, total spend for the month, and the single most important result — CPL, CPA, or total leads generated.

**2. Spend Summary**

| Campaign | Objective | Monthly Spend (UGX) | Key Result | vs. Target |
|---|---|---|---|---|
| [Campaign name] | [Objective] | [Spend] | [CPL / CPA / Leads] | [Above / Below / On target] |

**3. Audience Performance**

| Audience Tier | Spend (UGX) | Results | CPL / CPA (UGX) | Recommendation |
|---|---|---|---|---|
| Cold | | | | |
| Warm | | | | |
| Retargeting | | | | |

**4. Creative Performance**
List the top three and bottom three ads by CPL or CTR. State which creatives are being paused and which are being carried forward.

**5. Key Insights**
Three to five bullet points on what the data showed this month — what worked, what did not, and why.

**6. Recommendations for Next Month**
Three to five specific, actionable changes to the campaign plan for the coming month. Each recommendation must include the rationale and the expected impact.

**7. Budget Plan for Next Month**
Updated 50/30/20 audience split with UGX amounts for the coming month, reflecting any reallocation based on this month's performance.

---

## Quality Criteria

Output meets production standard when all of the following are satisfied:

- The campaign objective is selected from the three-tier framework (Awareness / Consideration / Conversion) and the rationale for the choice is explicitly stated — "Boost Post" is recommended only where justified
- All three audience tiers (Cold, Warm, Retargeting) are defined with specific targeting signals and the 50/30/20 budget split is applied and stated in UGX
- The Meta Pixel section includes a complete developer brief with named standard events and a verification method — the consultant does not install the Pixel
- The campaign structure follows the Campaign → Ad Set → Ad hierarchy with one ad set per audience tier and two to three creative variants per ad set
- The creative brief template is completed for every ad format in scope, including WhatsApp Click-to-Chat where applicable, with correct 2026 format specifications
- WhatsApp Click-to-Chat ads are included in the plan for any Uganda/EA client whose primary customer communication channel is WhatsApp
- The monthly performance report structure is included with all seven sections and populated with the client's campaign names and targets
- The creative brief section covers the Three Cs (Contrast, Curiosity, Comedy), the Customer Awareness Timeline, and the image text warning — each ad brief is matched to the audience tier's awareness level
- The troubleshooting diagnostic is included and follows the eight-step sequence with specific UGX-denominated CPC benchmarks
- All content uses British English; all budget figures are stated in UGX; video ad guidance reflects mobile data constraints of the EA market

---

## References

Consult these linked skills when building or extending the paid social plan:

- `caption-writer/SKILL.md` — all ad copy, headlines, and CTAs; use for every ad creative brief
- `meta-budget-planner/SKILL.md` — overall digital marketing budget allocation across channels; use before setting the paid social budget if the client does not have a total budget plan
- `meta-testing-framework/SKILL.md` — structured A/B test design for creative and audience testing; use when more than two creative variants are being tested simultaneously
- `meta-utm-tracking/SKILL.md` — UTM parameter structure for tracking paid traffic in Google Analytics; use for all website destination ads
- `meta-reporting/SKILL.md` — full social media analytics and reporting framework; use when the paid report needs to be integrated with organic performance data
- `playbook-chatbot-strategy/SKILL.md` — WhatsApp automation setup; use when Click-to-Chat ad volume exceeds the team's manual response capacity

---

**Key citations used in this skill:**
- Cooper, M.D. (2019) *Help! My Facebook Ads Suck!* (2nd ed.)
- Marshall, P. (2024) *Ultimate Guide to Facebook Advertising* (4th ed.)

*Platform specifications and EA market benchmarks are calibrated for 2026. Confirm current Meta ad format specifications, CPM benchmarks, and UGX exchange rates before presenting any paid social plan to a client.*

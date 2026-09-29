# Paid social planning method

Moved from `SKILL.md` in Social Kaizen S09 (29 Sep 2026, start commit `0e0af8a`); wording tightened; every item, figure, rule and citation kept. Read when asking the intake questions, mapping the business goal to a Meta objective, setting the audience-temperature split, choosing budgets and pacing, designing click-to-WhatsApp ads or structuring the monthly report.

## Intake questions

1. Business name, industry and country/city (default Uganda/East Africa).
2. Primary objective as one SMART goal (e.g. "40 qualified enquiries a month from Wakiso parents by 30 November at no more than UGX [x] each").
3. Monthly paid budget in UGX and gross margin per sale or value per lead.
4. Current activity: objectives, spend, results; exports if available.
5. Destination: website (tracking status), lead form, or WhatsApp Business number (monitored, with response SLA).
6. Platforms in scope (default Meta for Uganda/EA; TikTok and LinkedIn by audience).
7. Special-category status and any regulated claims (health, finance, alcohol, betting, children, politics).
8. Who operates the account and who approves spend.

## Section 1: Objective selection

Meta's current objectives are Awareness, Traffic, Engagement, Leads, App promotion and Sales (AD-01, checked 2026-09-23). Map the business goal to the objective the platform should optimise for:

| Business goal | Objective | Notes |
|---|---|---|
| Be known in a new market | Awareness | Judge on reach, frequency and brand-lift or recall checks, not clicks |
| Qualified visits to content | Traffic | Only when the visit itself matters; watch landing-page views |
| Conversations on WhatsApp/Messenger, video views, engagement | Engagement | Click-to-WhatsApp sits here or under Leads depending on current setup options; check on the day |
| Enquiries via instant form or messaging | Leads | Add one qualifying question where sales capacity is limited |
| Purchases, bookings, qualified conversions | Sales | Requires working Pixel/Conversions API events |

Boosted posts suit amplification of proven organic posts (see `ad-testing-and-scaling`, references/organic-to-paid-amplification.md); business outcomes use Ads Manager campaigns.

## Section 2: Audience temperature and starting split

| Tier | Signals | Message | Starting share (heuristic) |
|---|---|---|---|
| Cold | Location, age, interests, broad targeting, lookalikes from consented buyer lists | Problem, story, proof; no hard offer first | ~50% |
| Warm | Video viewers, engagers, page/profile followers, WhatsApp conversation starters | Specific offer, demonstration, objection answer | ~30% |
| Retargeting | Site visitors (pixel), lead-form openers, abandoners | Proof for the objection, real deadline or incentive | ~20% |

The 50/30/20 split is an engine starting heuristic, not a benchmark; re-allocate from the client's cost per qualified result after the first read. Where retargeting pools are too small to deliver, hold that budget and grow warm pools with video.

Video viewers are the most practical warm pool for EA clients without a website pixel; set the view threshold per objective and check current audience options on the day.

## Section 3: Budget and pacing

- Use daily budgets for always-on programmes; lifetime budgets for dated campaigns (events, seasonal offers).
- Start with ad-set budgets while reading which tier performs; move to campaign-level (Advantage+ campaign budget) once one structure is proven; Advantage+ is on when audience, budget and placement automation are all enabled (AD-02).
- Platform behaviour after budget changes (learning periods, instability) is checked on the live help centre with the date; scale in steps via `ad-testing-and-scaling`.
- Micro budgets: one campaign, one objective, one or two ad sets; fewer, stronger ads.

## Section 4: Click-to-WhatsApp ads (East Africa)

Use when the business sells by conversation, has no strong website, or trust must be built before purchase (health, finance, professional services). Set a pre-filled opening message that is short and specific ("Hi, I'd like the price list for [service] in [area]"). Staff replies within an agreed SLA (the engine's default planning figure is two hours in business hours, adjustable per client); route to `playbook-chatbot-strategy` when volume outgrows the team. Business-initiated follow-up messages need opt-in and approved templates under the current WhatsApp Business policy (check on the day).

## Section 5: Monthly report structure

1. Executive summary: objective, spend, the one result that matters against its line.
2. Spend and results by campaign vs target.
3. Audience-tier performance with recommendations.
4. Creative performance: top and bottom three, what carries forward.
5. Downstream quality: leads to customers, response times.
6. Tests run and decisions.
7. Next month: plan, budget split in UGX, lines in the sand, required approvals.

## Sources

- Cooper, M.D. (2019) *Help! My Facebook Ads Suck!* (2nd ed.) and Marshall, P. (2024) *Ultimate Guide to Facebook Advertising* (4th ed.) — structural practices retained (objective discipline, awareness-matched creative, one variable per test, Three Cs of creative); their numeric thresholds and the retired 20% text rule are removed.
- Currentness register 2026-09-23: AD-01, AD-02, AD-03, AD-04, AD-06, AD-07, AD-08, AD-09, AD-10, PL-01, PL-02, PL-05, MK-01, MK-02, MK-03.

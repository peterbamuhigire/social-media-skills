# E-commerce and WhatsApp Conversion Diagnosis

Merged from skills/strategy/ecommerce-conversion-optimisation on 2026-09-29 at ce3299a; preservation map: [ecommerce-conversion-optimisation.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/ecommerce-conversion-optimisation.md)

## When to use this reference

Read this reference when traffic already reaches the client (posts, ads, broadcasts, referrals) but too few enquiries turn into paid orders, baskets are small or buyers drop out between the WhatsApp chat and payment. The parent [SKILL.md](../SKILL.md) builds the post-click path (bio links, `wa.me` links, landing pages, measurement and the cold-start audit); this reference diagnoses where an existing e-commerce or WhatsApp sales path loses buyers, prioritises tests and adds revenue boosters and a KPI dashboard.

Evidence status. The conversion targets, uplift percentages and take-rates below come from the source books and the engine's earlier East Africa calibration; none has a register record, so verify before stating them to a client and prefer the client's own baseline. WhatsApp follow-up follows the WhatsApp Business Messaging Policy (register WHATSAPP-BUSINESS-POLICY: opt-in provenance, opt-outs honoured, approved templates outside the 24-hour customer-service window). Drafting a message or test does not authorise sending, spending or changing a live shop.

## Inputs

Ask for these before producing a deliverable (in addition to the parent's required input):

1. Client business name and industry, for example "Kampala Fresh, organic food delivery".
2. Country and city; default Uganda/East Africa if not given.
3. Current traffic sources: organic social, paid ads, WhatsApp broadcasts, referrals, walk-in, or a mix.
4. Approximate monthly enquiries and conversion rate: how many enquiries a month, and how many become paid orders?
5. Average order value (AOV) in UGX or USD.
6. Primary drop-off point: product page, WhatsApp enquiry stage, payment step, or abandonment after a quote?
7. Tracking in place: Google Analytics, Meta Pixel, UTM parameters, a manual spreadsheet, or none.
8. Primary goal, for example raise conversion from 5% to 15%, cut cart abandonment, raise AOV or improve the WhatsApp close rate.

## Decision rules

| # | Condition | Action | Failure avoided |
|---|---|---|---|
| 1 | Traffic exists but purchase or enquiry completion is weak | Diagnose the highest-evidence friction point and specify one measurable test at a time | Changing brand strategy when the loss is in the transaction path |
| 2 | The business has fewer than 50 orders a month | Use a manual WhatsApp tracking sheet as the minimum viable tracking; add HotJar, Meta Pixel and GA4 only as volume grows | Buying tools the team will not maintain |
| 3 | Volume is too small for a significance test | Accept a winner only with at least a 20% relative improvement sustained over 2 weeks | Declaring a winner from noise |
| 4 | A recovery or re-engagement message would fall outside the 24-hour customer-service window or go to someone who has not opted in | Use an approved template to opted-in contacts only, and honour any opt-out (Uganda: register UG-DPPA-S26-DIRECT-MARKETING-2026) | Policy breach and number restriction |
| 5 | The recommendation is about brand positioning rather than the transaction path | Hand over to `ecommerce-brand-differentiation` | Fixing the wrong layer |

## The diagnostic system

Harris (2016) describes the Marketing Optimization System (MOS; the author's US spelling) with three modules:

1. **Customer mindset**: understand how visitors think, decide and buy.
2. **Gathering intelligence**: collect qualitative and quantitative data on actual behaviour.
3. **Optimisation process**: use the five-step process to test and scale improvements.

Do not skip to solutions. Diagnosis comes before treatment.

## Procedure

### 1. Gather intelligence

Qualitative research shows *why* customers behave as they do; it generates hypotheses. Quantitative data validates them.

| Qualitative tool | What it reveals | Cost |
|---|---|---|
| WhatsApp exit surveys | Why customers enquired but did not buy | Free |
| Customer interviews (3–5 a month) | Emotional motivations, objections, decision process | Free |
| HotJar (heatmaps, session recordings) | Where attention drops on a product page | Freemium (verify current tiers) |
| SurveyMonkey or Google Forms | Structured buyer feedback | Free |
| Competitor funnel hacking | Become a customer of 2–3 competitors and document their whole journey | Time only |

| Quantitative tool | What it reveals |
|---|---|
| Google Analytics 4 | Traffic sources, bounce rate, session duration, conversion funnel |
| Meta Pixel | Facebook/Instagram ad performance, retargeting audience data (pair with the Conversions API and deduplicate: register META-CAPI-DEDUP-2026) |
| WhatsApp Business analytics | Message open rates, response rate, catalogue views |
| Manual spreadsheet | Order-level conversion rate, enquiry source, AOV by product |

Minimum viable tracking for East African social commerce: a manual WhatsApp tracking sheet is enough below 50 orders a month. Log the enquiry source (which post or ad), product asked about, converted or not, and the reason if not. Review monthly. For UTM conventions see [measurement-tracking-plan](../../../meta-analytics-ops/measurement-tracking-plan/SKILL.md).

### 2. Read the customer mindset: four buyer modalities

Every customer approaches a purchase through one of four decision styles (Harris, 2016). Product pages and WhatsApp scripts should serve all four.

| Modality | Speed | Driver | What they need |
|---|---|---|---|
| Competitive | Fast | Logic | Results, proof, performance claims, specifications |
| Spontaneous | Fast | Emotion | Urgency, excitement, fear of missing out, striking visuals |
| Methodical | Slow | Logic | Detailed FAQs, ingredient or component lists, comparison tables |
| Humanistic | Slow | Emotion | Founder story, community impact, testimonials, relationship |

East Africa working default (the engine's assumption; confirm with the client's buyers): most Ugandan buyers lean Humanistic and Spontaneous. Open with trust signals and emotional resonance, and give the logical detail needed to close higher-value purchases (above UGX 200,000).

- Product captions open with an emotional hook (Spontaneous/Humanistic) and close with specific proof or specifications (Competitive/Methodical).
- WhatsApp scripts include a brief story or social proof before the price.
- Product pages and catalogue entries carry both a short emotional headline and a bullet list of specifications.

### 3. Find the buyer-legend gap

A buyer legend (Harris, 2016) exposes the gap between what the brand intends to communicate and what customers experience.

1. Write the ideal customer journey from first seeing a post to sending payment confirmation.
2. Walk the same journey as a new customer would, from a fresh social account or through a competitor's ad funnel.
3. Document every point of confusion, missing information or friction.
4. Treat each friction point as a conversion opportunity.

Run the walk with the parent's § 8 cold-start audit checklist.

### 4. Map the ideal click path (M.A.P., Marketing Along a Path)

| Stage | Touchpoint | Conversion event |
|---|---|---|
| Awareness | Social post, ad, referral | View product |
| Interest | Product page, Stories, catalogue | Send WhatsApp enquiry |
| Consideration | WhatsApp conversation, quote | Request payment details |
| Decision | Payment instructions sent | Payment confirmed |
| Retention | Post-purchase message | Second order |

For each stage, record the drop-off rate and the most common reason for drop-off.

### 5. Run the five-step optimisation process

Apply it to every conversion problem found (Harris, 2016):

1. **Discovery.** Combine qualitative and quantitative data to find the highest-impact friction point; prioritise by volume × severity.
2. **Hypothesis.** Write a specific, testable statement, for example: "Changing the product caption from price-first to story-first will increase WhatsApp enquiry rate by 20% within 4 weeks."
3. **Execution.** Change one variable at a time: one caption format, one CTA style, one Story layout or one WhatsApp script element. Run the test for at least 2 weeks or 200 impressions, whichever comes first (the source's minimum run rule; at low volume, 200 impressions rarely supports a significance test, so use decision rule 3).
4. **Review.** Compare with the baseline: did the metric improve, decline or stay flat? Require statistical significance (at least 95% confidence that the result is not random) before declaring a winner; for small-volume businesses, look for at least a 20% relative improvement sustained over 2 weeks.
5. **Scale.** Apply the winning variant across similar content and touchpoints, document the pattern so it becomes the new default, then return to step 1 with the next friction point.

### 6. Recover abandoned enquiries

An enquiry that did not convert is warm traffic, not a lost sale (Larsson, 2016). Structured recovery:

1. Within 30 minutes: WhatsApp follow-up, "Hi [name], just checking if you had any questions about [product]?"
2. Within 24 hours: resend the product image with a specific testimonial or trust signal.
3. At 48 hours: offer an incentive (free delivery, a bonus item or a 10% discount code). This falls outside the 24-hour customer-service window unless the customer has replied, so use an approved template (decision rule 4).
4. After 7 days: move the contact to the inactive broadcast list for monthly re-engagement, only if they opted in, and remove anyone who opts out.

Source target: recover 10–20% of abandoned enquiries (verify before stating; no register record).

## KPIs and targets

| Metric | Definition | Source's East Africa social-commerce target (verify; no register record) |
|---|---|---|
| Enquiry conversion rate | Orders ÷ WhatsApp enquiries | 30–50% |
| Post-reach-to-enquiry rate | Enquiries ÷ post reach | 1–3% for product posts |
| Abandoned enquiry rate | Enquiries with no follow-up response | Below 15% |
| Average order value (AOV) | Total revenue ÷ number of orders | Lift by 15–20% through upsells |
| Repeat purchase rate | Repeat customers ÷ total customers | 40%+ at 6 months |
| Bounce rate (web and link pages) | Single-page exits ÷ total visits | Below 55% |

## Revenue boosters

Tactics from Larsson (2016) to raise conversion rate and AOV. Uplift figures are the source's and have no register record: verify before stating.

- **Retargeting.** Install the Meta Pixel on any website or link-in-bio page to capture visitors. The source claims visitors are 70% more likely to convert after seeing a retargeting ad. Show a product-specific ad to people who viewed that product page but did not enquire. Retargeting needs consent and data-protection checks (see measurement-tracking-plan).
- **Landing pages.** A dedicated product landing page (even a single WhatsApp-linked link-in-bio page) is claimed to convert 5–10% better than sending buyers to a profile. Required elements: emotional headline; at least 3 product images; key features and benefits; at least one testimonial; price; one clear CTA. Build it to the parent's § 5 landing-page principles.
- **Mobile checkout.** Cut the WhatsApp order form to the minimum fields (name, item, delivery address, payment method). Offer a payment link (the source names Pesapal; verify availability and fees) for customers who prefer not to complete a Mobile Money transfer by hand. Guest-checkout principle: never require registration, an account or several steps before a customer can pay.
- **Free delivery threshold.** Set free delivery at 20% above current AOV to encourage larger baskets without much higher average fulfilment cost. Announce it in every product post: "Free delivery on orders above UGX [amount]."
- **Loss leaders and tripwires.** A low-cost or zero-margin entry product (loss leader) wins a first-time customer; upsell the margin-positive product in the follow-up. A tripwire is a deeply discounted, genuinely valuable first offer that turns cold traffic into buyers at scale.
- **Flash sales.** 24-hour flash sales with countdown timers in Stories create urgency and shorten the decision cycle. Run them on slow-moving stock first: discount the least popular 20% of SKUs, not the bestsellers. Announce 24 hours ahead, then remind at 6 hours, 2 hours and 30 minutes remaining.
- **Ride-alongs.** Put a printed insert, small bonus item or next-order discount code in every physical delivery. Cost is minimal; the source reports a 30–40% take-rate on a repeat-purchase incentive.

## KPI dashboard

Define and track these monthly. Report with simple visuals: a bar chart for trends, a table for current-period values.

- **Revenue**: total revenue, revenue by product, revenue by channel; gross margin % by product (source target 60%+); operating margin (EBITDA), tracked daily for any business doing 20+ orders a day.
- **Customers**: new versus repeat customers; customer acquisition cost (ad spend ÷ new customers from ads); customer lifetime value (average revenue per customer over 12 months).
- **Conversion**: enquiry conversion rate (orders ÷ enquiries); abandoned enquiry rate; AOV and its trend.
- **Traffic**: enquiries by source (which post, ad or channel); post reach-to-enquiry rate by content type.

Apply the RASTA standard to all client reporting (Phillips, 2015): Relevant, Accurate, Simple, Timely, Annotated.

## Release checklist

1. The specific conversion bottleneck is diagnosed before any solution is recommended.
2. Visitors are read against the four buyer modalities and copy recommendations adapted to them.
3. The full journey from first post to payment confirmation is mapped, with each drop-off point identified.
4. At least 3 conversion hypotheses are stated, each with a measurable success criterion.
5. A five-step testing plan (Discovery → Hypothesis → Execution → Review → Scale) covers the top-priority friction point.
6. A KPI dashboard tracks at least 5 metrics with baselines; any East Africa benchmark is labelled "verify" unless the client's data supports it.
7. A structured WhatsApp abandoned-enquiry recovery sequence is included and respects opt-in, templates and opt-outs.
8. Tools fit the client's scale: a manual spreadsheet for small volumes; HotJar, Meta Pixel and GA4 for larger operations.

## Related skills

- [social-commerce-strategy](../../../strategy/social-commerce-strategy/SKILL.md): East African social-commerce operations and platform set-up.
- [ecommerce-brand-differentiation](../../../strategy/ecommerce-brand-differentiation/SKILL.md): brand positioning and intangibles.
- [measurement-tracking-plan](../../../meta-analytics-ops/measurement-tracking-plan/SKILL.md): UTM, Pixel and consent set-up.

## Sources

- Harris, A. (2016) *Small Business Big Money Online*: Marketing Optimization System, four buyer modalities, five-step process.
- Larsson, T. (2016) *Ecommerce Evolved*: conversion tactics, traffic temperature, retargeting, flash sales, ride-alongs.
- Phillips, J. (2015) *Ecommerce Analytics*: KPI frameworks, dashboards, RASTA reporting.

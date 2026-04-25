---
name: ecommerce-conversion-optimisation
description: Produces a conversion rate optimisation (CRO) plan for a client's social commerce or ecommerce operation — diagnosing friction points, applying the 5-step Marketing Optimization System, segmenting visitors by buyer modality and traffic temperature, and building a structured A/B testing roadmap. Invoke this skill when a client has traffic or enquiries but low conversion, when cart or enquiry abandonment is high, when a client asks how to turn browsers into buyers, or when they want to improve their WhatsApp close rate or product page performance.
---
# Ecommerce Conversion Optimisation

<!-- dual-compat:start -->
## Use when
- Produces a conversion rate optimisation (CRO) plan for a client's social commerce or ecommerce operation — diagnosing friction points, applying the 5-step Marketing Optimization System, segmenting visitors by buyer modality and traffic temperature, and building a structured A/B testing roadmap. Invoke this skill when a client has traffic or enquiries but low conversion, when cart or enquiry abandonment is high, when a client asks how to turn browsers into buyers, or when they want to improve their WhatsApp close rate or product page performance.

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
- The primary deliverable requested by this skill, structured in markdown and ready for immediate use.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Ask the client for the following before generating any deliverable:

1. **Client business name and industry** — e.g., "Kampala Fresh, organic food delivery"
2. **Country/city** — default is Uganda/East Africa if not specified
3. **Current traffic sources** — organic social, paid ads, WhatsApp broadcasts, referrals, walk-in, or a combination
4. **Approximate monthly enquiries and conversion rate** — how many enquiries per month; how many convert to paid orders?
5. **Average order value (AOV)** — in UGX or USD
6. **Primary drop-off point** — where are most customers lost? (product page, WhatsApp enquiry stage, payment step, post-quote abandonment?)
7. **Existing tracking in place** — Google Analytics, Meta Pixel, UTM parameters, manual tracking in a spreadsheet, or none?
8. **Primary goal** — e.g., increase conversion rate from 5% to 15%, reduce cart abandonment, increase AOV, improve WhatsApp close rate

---

## Section 1 — The Marketing Optimization System (MOS)

The Marketing Optimization System (Harris, 2016) is a three-module framework for diagnosing and fixing conversion problems:

1. **Customer Mindset** — understand how visitors think, decide, and buy
2. **Gathering Intelligence** — collect qualitative and quantitative data on actual behaviour
3. **Optimisation Process** — use the 5-step process to test and scale improvements

Do not skip to solutions. Diagnosis comes before treatment.

---

## Section 2 — Customer Mindset

### 4 Buyer Modalities

Every customer approaches a purchase through one of four decision-making styles (Harris, 2016). Effective product pages and WhatsApp scripts serve all four.

| Modality | Speed | Driver | What They Need |
|---|---|---|---|
| Competitive | Fast | Logic | Results, proof, performance claims, specifications |
| Spontaneous | Fast | Emotion | Urgency, excitement, FOMO, striking visuals |
| Methodical | Slow | Logic | Detailed FAQs, ingredient/component lists, comparison tables |
| Humanistic | Slow | Emotion | Founder story, community impact, testimonials, relationship |

**EA audience default:** Most Ugandan buyers trend Humanistic and Spontaneous. Open with trust signals and emotional resonance; provide the logical detail needed to close higher-value purchases (above UGX 200,000).

**Application to content and copy:**
- Product captions should open with an emotional hook (Spontaneous/Humanistic) and close with specific proof or specifications (Competitive/Methodical)
- WhatsApp scripts should include a brief story element or social proof before presenting the price
- Product pages and catalogue entries should have both a short emotional headline and a bullet list of specifications

### Buyer Legends

A Buyer Legend (Harris, 2016) is the narrative gap between what your brand intends to communicate and what customers actually experience. To find the gap:

1. Write out the ideal customer journey from first seeing a post to sending payment confirmation
2. Walk the same journey as a new customer would — from a fresh social media account or via a competitor's ad funnel
3. Document every point of confusion, missing information, or friction
4. Each friction point is a conversion optimisation opportunity

### Ideal Click M.A.P. (Marketing Along a Path)

Map the full funnel from first touchpoint to post-purchase:

| Stage | Touchpoint | Conversion Event |
|---|---|---|
| Awareness | Social post, ad, referral | View product |
| Interest | Product page, Stories, catalogue | Send WhatsApp enquiry |
| Consideration | WhatsApp conversation, quote | Request payment details |
| Decision | Payment instructions sent | Payment confirmed |
| Retention | Post-purchase message | Second order |

For each stage, identify the drop-off rate and the most common reason for drop-off.

---

## Section 3 — Gathering Intelligence

### Qualitative Research Tools

Qualitative research reveals *why* customers behave as they do. Use these methods:

| Tool | What It Reveals | Free/Paid |
|---|---|---|
| WhatsApp exit surveys | Why customers enquired but didn't buy | Free |
| Customer interviews (3–5 per month) | Emotional motivations, objections, decision process | Free |
| HotJar (heatmaps, session recordings) | Where on a product page attention drops | Freemium |
| SurveyMonkey or Google Forms | Structured buyer feedback | Free |
| Competitor funnel hacking | Become a customer of 2–3 competitors; document their full journey | Time cost only |

Qualitative research generates hypotheses. Quantitative data validates them.

### Quantitative Research Tools

| Tool | What It Reveals |
|---|---|
| Google Analytics (GA4) | Traffic sources, bounce rate, session duration, conversion funnel |
| Meta Pixel | Facebook/Instagram ad performance, retargeting audience data |
| WhatsApp Business analytics | Message open rates, response rate, catalogue views |
| Manual spreadsheet tracking | Order-level conversion rate, enquiry source, AOV by product |

**Minimum viable tracking for EA social commerce:** A manual WhatsApp tracking sheet is sufficient for businesses under 50 orders per month. Log: enquiry source (which post or ad?), product enquired about, converted or not, reason if not converted. Review monthly.

---

## Section 4 — The 5-Step Optimisation Process

Apply this process for every conversion problem identified (Harris, 2016):

**Step 1 — Discovery:** Combine qualitative and quantitative data to identify the highest-impact friction point. Prioritise by volume × severity.

**Step 2 — Hypothesis:** Form a specific, testable statement. *"Changing the product caption from price-first to story-first will increase WhatsApp enquiry rate by 20% within 4 weeks."*

**Step 3 — Execution:** Implement the change in one variable at a time. For social commerce: test one caption format, one CTA style, one Story layout, or one WhatsApp script element. Run the test for a minimum of 2 weeks or 200 impressions, whichever comes first.

**Step 4 — Review:** Compare the results against the baseline. Did the metric improve, decline, or stay flat? Require statistical significance (a minimum 95% confidence that the result is not random) before declaring a winner. For small-volume businesses, look for at least 20% relative improvement sustained over 2 weeks.

**Step 5 — Scale:** Apply the winning variant across all similar content or touchpoints. Document the winning pattern so it becomes the new default. Then return to Step 1 with the next friction point.

---

## Section 5 — Key Conversion Metrics and Benchmarks

### Core KPIs

| Metric | Definition | EA Social Commerce Benchmark |
|---|---|---|
| Enquiry conversion rate | Orders ÷ WhatsApp enquiries | Target: 30–50% |
| Post-reach-to-enquiry rate | Enquiries ÷ post reach | Target: 1–3% for product posts |
| Abandoned enquiry rate | Enquiries with no follow-up response | Target: below 15% |
| Average order value (AOV) | Total revenue ÷ number of orders | Aim to lift by 15–20% via upsells |
| Repeat purchase rate | Repeat customers ÷ total customers | Target: 40%+ at 6 months |
| Bounce rate (web/link pages) | Single-page exits ÷ total visits | Target: below 55% |

### Abandoned Cart and Enquiry Recovery

An enquiry that did not convert is not lost — it is warm traffic (Larsson, 2016). Apply a structured recovery process:

1. Within 30 minutes: send a WhatsApp follow-up — "Hi [name], just checking if you had any questions about [product]?"
2. Within 24 hours: resend the product image with a specific testimonial or trust signal
3. At 48 hours: offer an incentive — free delivery, a bonus item, or a 10% discount code
4. After 7 days: move to the inactive broadcast list for monthly re-engagement

Target: recover 10–20% of abandoned enquiries through systematic follow-up.

---

## Section 6 — Conversion Tricks and Revenue Boosters

Apply these proven tactics (Larsson, 2016) to increase conversion rate and average order value:

### Retargeting
- Install the Meta Pixel on any website or link-in-bio page to capture all visitors
- Visitors are 70% more likely to convert after seeing a retargeting ad
- Use retargeting to show a product-specific ad to visitors who viewed that product page but did not enquire

### Landing Pages
- A dedicated product landing page (even a single WhatsApp-linked link-in-bio page) converts 5–10% better than sending buyers directly to a profile
- Required elements: emotional headline, product images (minimum 3), key features and benefits, at least one testimonial, price, and a single clear CTA

### Mobile Checkout Optimisation
- Simplify the WhatsApp order form to the minimum required fields (name, item, delivery address, payment method)
- Offer a payment link (Pesapal) for customers who prefer to pay without manually completing a Mobile Money transfer
- Guest checkout principle: never require registration, accounts, or multiple steps before a customer can pay

### Free Shipping Threshold
- Set free delivery at 20% above current AOV to incentivise larger baskets without significantly increasing average fulfilment cost
- Announce the threshold in every product post: "Free delivery on orders above UGX [amount]"

### Loss Leaders and Tripwires
- A low-cost or zero-margin entry product (loss leader) acquires a first-time customer; upsell the margin-positive product in the follow-up
- A tripwire is a deeply discounted, genuinely valuable first offer that converts cold traffic into buyers at scale

### Flash Sales
- 24-hour flash sales with countdown timers in Stories generate urgency and compress the decision cycle
- Run flash sales on slow-moving inventory first; apply the discount to the least popular 20% of SKUs, not the bestsellers
- Announce 24 hours in advance, then remind at 6 hours, 2 hours, and 30 minutes remaining

### Ride-Alongs
- Include a printed insert, a small bonus item, or a next-order discount code in every physical delivery
- Cost: minimal; effect: 30–40% take-rate on a repeat purchase incentive (Larsson, 2016)

---

## Section 7 — Ecommerce KPI Dashboard

Define and track these KPIs monthly. Report to the client using simple visualisations (bar chart for trends, table for current-period values):

**Revenue KPIs:**
- Total revenue, revenue by product, revenue by channel
- Gross margin % by product (target: 60%+)
- Operating margin (EBITDA) — track daily for any business doing 20+ orders per day

**Customer KPIs:**
- New customers vs. repeat customers
- Customer acquisition cost (ad spend ÷ new customers from ads)
- Customer lifetime value (LTV) — average revenue per customer over 12 months

**Conversion KPIs:**
- Enquiry conversion rate (orders ÷ enquiries)
- Abandoned enquiry rate
- AOV and trend over time

**Traffic KPIs:**
- Enquiries by source (which post, ad, or channel generated the enquiry?)
- Post reach-to-enquiry rate by content type

Apply the RASTA standard to all client reporting (Phillips, 2015): **Relevant, Accurate, Simple, Timely, Annotated**.

---

## Quality Criteria

Output from this skill meets the standard if it:

- Diagnoses the specific conversion bottleneck before recommending solutions
- Segments visitors into the 4 buyer modalities and adapts copy recommendations accordingly
- Maps the full customer journey from first post to payment confirmation, identifying each drop-off point
- Includes at least 3 specific conversion optimisation hypotheses with measurable success criteria
- Provides a 5-step testing plan (Discovery → Hypothesis → Execution → Review → Scale) for the top priority friction point
- Sets a KPI dashboard with at least 5 tracked metrics and baseline benchmarks for the EA market
- Includes a structured WhatsApp abandoned enquiry recovery sequence
- Names specific tools appropriate for the client's scale (manual spreadsheet for small volumes; HotJar, Meta Pixel, GA4 for larger operations)

---

## References

- Harris, A. (2016) *Small Business Big Money Online*. Marketing Optimization System, 4 Buyer Modalities, 5-Step Process
- Larsson, T. (2016) *Ecommerce Evolved*. Conversion tricks, traffic temperature, retargeting, flash sales, ride-alongs
- Phillips, J. (2015) *Ecommerce Analytics*. KPI frameworks, dashboarding, RASTA reporting
- `social-commerce-strategy/SKILL.md` — EA-specific social commerce operations and platform setup
- `ecommerce-brand-differentiation/SKILL.md` — Brand positioning and intangibles strategy

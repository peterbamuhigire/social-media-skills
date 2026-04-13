---
name: 07-email-marketing-strategy
description: Generates a complete standalone email marketing strategy — covering list building, segmentation, welcome sequences, newsletter planning, promotional emails, reactivation, KPIs, and subject line formulas. Invoke when a client has or wants an email list and needs a structured email programme, or when 06-digital-marketing-strategy has been commissioned and requires the email sub-strategy to be built out in full.
---
# Email Marketing Strategy Generator

Produce a complete email marketing strategy document. This is the authoritative email deliverable in the suite. Every section must be populated with client-specific content and guidance a non-specialist could follow. Apply British English throughout. Default to Uganda/East Africa context unless the client specifies otherwise.

Assume Mailchimp or Brevo as the email platform. Note differences between the two where relevant. Brevo (formerly Sendinblue) is often more cost-effective for EA clients due to send-volume pricing; Mailchimp is more widely known and has stronger third-party integrations.

---

<!-- dual-compat:start -->
## Use when
- Generates a complete standalone email marketing strategy — covering list building, segmentation, welcome sequences, newsletter planning, promotional emails, reactivation, KPIs, and subject line formulas. Invoke when a client has or wants an email list and needs a structured email programme, or when 06-digital-marketing-strategy has been commissioned and requires the email sub-strategy to be built out in full.
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

Ask for all of the following before generating the strategy document:

- **Client name** — trading name
- **Industry and sub-sector** — e.g. "retail — skincare", "professional services — accounting"
- **Country/city** — defaults to Kampala, Uganda if not specified
- **Primary product or service** — what the client sells or offers
- **Current email list size** — number of subscribers; state zero or none if starting from scratch
- **Email platform used** — Mailchimp / Brevo / other; if none, recommend based on list size and budget
- **Customer purchase cycle length** — how long from first contact to purchase (days / weeks / months); and how frequently customers typically re-purchase
- **Primary goal for email** — lead nurture / customer retention / promotional sales / all three
- **Monthly email marketing budget** — platform fees plus any content production costs

---

## Document Structure

Generate all eight sections in order. Use markdown headings. Do not omit any section.

### 1. List Building Strategy

Define how the client will grow their email list. For each opt-in mechanism, specify the incentive, placement, and expected conversion rate.

**Website sign-up form**
- Incentive: [match to industry — e.g. "Free guide: 5 skincare mistakes Kampala women make" / "10% discount on your first order" / "Free consultation booking"]
- Placement: homepage above the fold, blog sidebar, and exit-intent pop-up (implement via Mailchimp or Brevo embedded form)
- Expected conversion rate: 1–3% of website visitors for a well-positioned form with a strong incentive
- Platform note: Brevo offers unlimited contacts on the free plan; Mailchimp free plan caps at 500 contacts — factor into recommendation

**Social media lead magnet**
- Incentive: promote the same lead magnet via a pinned Facebook post, Instagram bio link (use Linktree or direct link), and a Facebook Lead Ad if budget permits
- Placement: Instagram bio link, Facebook pinned post, occasional story CTA
- Expected conversion rate: 2–5% of link clicks for a relevant, clearly communicated offer
- Note: Facebook Lead Ads allow in-app form submission without requiring a website visit — effective for mobile-heavy EA audiences

**WhatsApp broadcast opt-in**
- Incentive: invite existing WhatsApp contacts to opt into a broadcast list in exchange for exclusive offers or early access to new products/services
- Placement: include opt-in ask in every outbound WhatsApp message footer ("Reply YES to join our VIP broadcast list")
- Expected conversion rate: 15–30% of engaged WhatsApp contacts who see the ask
- Note: WhatsApp broadcasts are a parallel channel — co-ordinate messaging with email to avoid duplication

**In-store or event QR code**
- Incentive: printed QR code at checkout, reception, or event registration — links to a simple mobile-optimised sign-up form
- Placement: receipt slips, counter cards, event programmes, product packaging inserts
- Expected conversion rate: 5–15% of people who see the code and scan it; higher with a verbal ask from staff

For clients starting from zero: prioritise the website form and WhatsApp opt-in first. Set a Month 1 target of 50–100 subscribers as the initial milestone.

---

### 2. List Segmentation

Define four core segments. For each, state the definition, how to identify subscribers in it, and the communication approach.

**Segment 1 — Leads (subscribed but not yet purchased)**
- Definition: subscribers who have opted in but have not made a purchase or confirmed engagement
- How to identify: in Mailchimp — use a tag or group applied at sign-up; in Brevo — use a list or attribute field
- Communication approach: welcome sequence (see Section 3), then educational and value-driven content. Minimise hard sells. Nurture with proof points and testimonials. Frequency: weekly until purchase, then move to Active Customers segment.

**Segment 2 — Active Customers (purchased within the past 90 days)**
- Definition: subscribers who have made at least one purchase in the last 90 days
- How to identify: tag or label applied manually or via e-commerce integration at point of purchase
- Communication approach: deepen the relationship. Share usage tips, complementary products, behind-the-scenes content, and referral incentives. Frequency: weekly or fortnightly. Tone: warm and appreciative.

**Segment 3 — Lapsed Customers (no purchase in 90+ days)**
- Definition: previously active customers who have not purchased or engaged meaningfully in over 90 days
- How to identify: filter by last purchase date; or by email engagement (no opens in 90 days)
- Communication approach: reactivation sequence (see Section 6). After the sequence, move non-responders to a suppression list to protect sender reputation.

**Segment 4 — VIPs (top 20% by purchase frequency or value)**
- Definition: the client's highest-value customers — frequent buyers or high-spend individuals
- How to identify: manually tag the top 20% by purchase frequency or total spend; review quarterly
- Communication approach: early access, exclusive offers, personal thank-you messages, invitations to provide feedback or feature in testimonials. Frequency: as needed plus standard newsletter. Tone: personally addressed; never generic.

For clients with small lists (under 200 subscribers), simplified segmentation is acceptable: Leads and Customers only. Expand to four segments once the list exceeds 500.

---

### 3. Welcome Sequence

Define a 5-email onboarding flow. Every new subscriber enters this sequence automatically. For each email, provide the subject line formula, preview text approach, body structure, and CTA.

**Email 1 — Thank You and What to Expect**
Send timing: immediately on sign-up
Subject line formula: "Welcome to [Brand Name] — here's what happens next"
Preview text: "Your [incentive] is inside — plus what you can expect from us"
Body structure: (1) Deliver the lead magnet or promised incentive immediately. (2) One short paragraph introducing the brand — warm and human, not corporate. (3) Tell them what kind of emails they will receive and how often. (4) Invite a reply: "Hit reply and tell us one thing you'd like help with."
CTA: Download lead magnet / Visit website

**Email 2 — Your Story and Brand Introduction**
Send timing: Day 2
Subject line formula: "Why [Founder Name] started [Brand Name] (the honest version)"
Preview text: "It started with a problem we couldn't solve anywhere else"
Body structure: (1) Founder story or brand origin in 100–150 words — personal, specific, honest. (2) Connect the origin to the subscriber's problem. (3) Brief summary of what the brand offers.
CTA: [Most relevant product/service page or about page]

**Email 3 — Most Useful Content or Resource**
Send timing: Day 4
Subject line formula: "The [number] things every [target customer] should know about [topic]"
Preview text: "We wish someone had told us this sooner"
Body structure: (1) Brief introduction — why this content matters to the subscriber. (2) The resource itself (3–5 tips, a short guide, or a link to the most valuable blog post). (3) One sentence positioning the brand as the expert source for this topic.
CTA: Read the full guide / Watch the video / Book a call

**Email 4 — Social Proof and Community**
Send timing: Day 7
Subject line formula: "What [customer name or 'our clients'] say about [Brand Name]"
Preview text: "[Specific result or quote snippet]"
Body structure: (1) Share 2–3 testimonials or customer stories. Be specific — include names (with permission) and measurable outcomes. (2) Invite the subscriber to join the brand's community (WhatsApp group, Facebook group, or Instagram follow). (3) Short brand values statement.
CTA: Join the WhatsApp group / Follow on Instagram / Read more reviews

**Email 5 — Soft Offer and CTA**
Send timing: Day 10
Subject line formula: "A special welcome offer — just for you" or "[First name], this is for you"
Preview text: "We don't do this often — but you've earned it"
Body structure: (1) Acknowledge that the subscriber has been on the list for 10 days. (2) Present a genuine welcome offer: discount, free consultation, bonus, or priority booking. (3) Explain the terms clearly — expiry date, how to redeem. (4) Reassure them this is not a high-pressure sell.
CTA: Claim your offer / Book your session / Shop now

After Email 5: move the subscriber to the standard newsletter cadence. If they have not opened any of the 5 emails, move to the lapsed segment after 30 days.

---

### 4. Newsletter Strategy

Define the ongoing broadcast newsletter programme.

**Frequency recommendation:**
- Weekly: appropriate for e-commerce, news-driven industries, or clients with high content output
- Fortnightly: recommended for most service businesses — sustainable without overwhelming subscribers
- Monthly: minimum viable frequency; suitable for low-purchase-cycle industries (e.g. annual insurance, property)

Recommend frequency based on client's purchase cycle and content capacity. Default: fortnightly.

**Content mix:**
- 60% value: tips, how-to content, industry news, useful resources — no sales message
- 30% brand news: product updates, behind-the-scenes, team news, events, milestones
- 10% promotional: offers, sales, launches, special promotions — with a clear CTA

**Newsletter structure template:**
1. **Header:** brand logo and tagline
2. **Opening line:** personal, conversational — 1–2 sentences. Acknowledge something current (season, local event, shared experience).
3. **Main story or value piece:** 150–250 words. The core content of this issue.
4. **Secondary item(s):** 1–2 short items — news, tip, product spotlight, customer story
5. **CTA:** one clear call to action per newsletter. Do not include more than two links in the body.
6. **Footer:** unsubscribe link (mandatory), contact details, social media links

**Subject line approach — three proven styles:**
- Curiosity: "The one thing we stopped doing — and why" (works well for value-driven issues)
- Direct: "New arrivals: [Product name] is now in stock" (works for product businesses with time-sensitive content)
- Personal: "[First name], your [month] update from [Brand Name]" (works for service businesses with warm relationships)

Test subject line styles. Use Mailchimp's A/B testing (available on paid plans) or Brevo's A/B test feature. Test one variable at a time.

---

### 5. Promotional Email Framework

**Individual offer email structure:**
1. Subject line: benefit-first (e.g. "Save 20% on [Product] — this week only")
2. Preview text: reinforce urgency or secondary benefit
3. Opening: acknowledge the reader directly; one sentence
4. Offer: state it clearly in the first 50 words — what it is, what it costs, what they save
5. Product/service description: 50–100 words; benefits not features
6. Social proof: one testimonial or stat
7. CTA button: clear and specific (e.g. "Claim 20% discount" not "Click here")
8. Urgency line: "Offer expires [date]" — only use if genuine
9. Footer: standard

**Product launch sequence — 3 emails:**

Email 1: Announcement (Day 1 of launch)
Subject formula: "Introducing [Product Name] — [one-sentence benefit]"
Purpose: generate awareness and excitement; encourage early action
CTA: Pre-order / Join the waitlist / Shop now

Email 2: Build-up (Day 3)
Subject formula: "The story behind [Product Name]" or "Why we built [Product Name]"
Purpose: deepen interest; address objections; add social proof from early adopters
CTA: Read the full story / Buy now before stock runs out

Email 3: Last chance (Day 6 or 7)
Subject formula: "Last chance: [Product Name] offer ends tonight"
Purpose: urgency and FOMO; serve as the final push for those who have not yet acted
CTA: Buy now — offer ends at midnight

**Re-promotion of evergreen offers:**
For offers without an expiry date (e.g. consultations, memberships, standing discounts), re-promote to Leads segment every 8 weeks. Vary the framing — use a different angle each time (social proof, urgency, education, testimonial) to avoid appearing repetitive.

---

### 6. Reactivation Sequence

A 3-email series sent to lapsed subscribers (no purchase or email open in 90+ days).

**Email 1 — Re-engagement Hook**
Send timing: Day 1 of sequence
Subject formula: "We miss you, [First name]" or "Has something changed?"
Body: short and personal — 3–4 sentences. Acknowledge the gap. Offer a compelling reason to re-engage: a new product, a changed service, a relevant piece of content, or a special returning-customer offer.
CTA: Come back and see what's new

**Email 2 — What You Missed**
Send timing: Day 4
Subject formula: "Here's what happened while you were away"
Body: summarise 2–3 highlights from the past 90 days — new products, customer wins, useful content. Frame as genuinely useful updates, not a guilt trip.
CTA: Explore the updates / Book a catch-up call

**Email 3 — Last Chance to Stay**
Send timing: Day 8
Subject formula: "Should we say goodbye, [First name]?" or "One last thing before you go"
Body: honest and respectful — tell them this is the last email if they do not re-engage. Offer a final incentive if appropriate. Give them an easy way to update their preferences instead of unsubscribing.
CTA: Stay subscribed + claim offer / Update my preferences / Unsubscribe

After Email 3: suppress non-openers from future sends. Do not delete from the list — they may still be reached via other channels. Review suppressed contacts every 6 months.

---

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

---

### 7A. Strategic Email Programme Principles

**The 90/90 Rule (Bly, 2018):** 90% of email subscribers who will ever purchase do so within 90 days of joining the list. The first 90 days must be front-loaded with the highest-value, highest-frequency nurture content. Every email strategy must specify how send frequency and content intensity in weeks 1–12 differs from the steady-state cadence in months 4–12. For most EA clients: weeks 1–12 → 2 emails per week; months 4–12 → weekly or fortnightly. Do not apply a flat cadence across the full 12 months.

**Content-to-Sales Ratio (Bly, 2018):** A minimum of 50% of all emails sent must be pure content emails — educational, insightful, or entertaining with no promotional intent. If more than half of sends carry a sales message, opt-out rates rise and list health deteriorates. Track the content-to-sales ratio monthly. Report it to the client as part of list health monitoring, alongside bounce rate and opt-out rate.

**AI Send-Time Optimisation (Johnsen, 2024):** AI-driven per-subscriber optimal send time — rather than a single blast time for the whole list — produces measurable uplift in open rates and click-through rates. Define this as a distinct deliverable within the email strategy: specify which email platform supports per-subscriber send-time optimisation (Mailchimp: available on Standard plan and above; Brevo: available on Business plan), how to activate it, and how improvement is measured (compare CTOR pre and post activation over a 60-day period).

---

### 7. KPIs and Target Benchmarks

**Six Core Email KPIs (Bly, 2018):** Track all six metrics monthly. The CTR × conversion rate multiplier is the key revenue lever: optimising both produces compounding revenue gains.

| KPI | Target | Notes |
|---|---|---|
| Bounce rate (hard) | <1% | Remove hard bounces within 24 hours of each send |
| Opt-out rate | <0.1% per send | Rates above this indicate content-sales ratio imbalance or audience mismatch |
| Open rate | 10–15% (global floor) | EA benchmark higher — see below; use CTOR as primary quality indicator |
| Click-through rate (CTR) | 1–5% | Optimise subject line and preheader to lift open rate; optimise CTA placement to lift CTR |
| Conversion rate | Client-specific target | Set at onboarding based on current enquiry-to-sale rate; review quarterly |
| Gross revenue per email sent | Calculate from client data | Revenue attributed to send ÷ emails delivered; most important single email programme metric |

Target benchmarks calibrated for the East African market, where mobile-heavy audiences and Gmail/Android dominance affect open tracking behaviour.

| KPI | EA Benchmark Target | How to Measure | Platform |
|---|---|---|---|
| Open rate | 25–35% | Native analytics (note: Apple Mail Privacy Protection inflates open rates on iOS) | Mailchimp / Brevo |
| Click-through rate (CTR) | 2–5% | Clicks ÷ delivered emails | Mailchimp / Brevo |
| Click-to-open rate (CTOR) | 10–20% | Clicks ÷ opens — better indicator of content relevance | Mailchimp / Brevo |
| Unsubscribe rate | Under 0.5% per send | Unsubscribes ÷ delivered | Mailchimp / Brevo |
| Bounce rate (hard) | Under 2% | Hard bounces ÷ sent | Mailchimp / Brevo |
| List growth rate | 5–10% month-on-month (early stage) | Net new subscribers ÷ total list | Manual + platform |
| Revenue per email | Calculate based on client data | Revenue attributed to email send ÷ emails delivered | CRM + platform |

For e-commerce clients: track revenue per email and attribute via UTM links in all email CTAs.

Note: open rates are directional only due to email client privacy features. Use CTOR as the primary engagement quality indicator.

---

### 8. Twelve Subject Line Formulas with Uganda/EA Examples

Apply these formulas when writing subject lines. Test two at a time using A/B testing.

1. **The number list** — "[Number] things every [audience] needs to know about [topic]"
   EA example: "5 things every Kampala small business owner should know about cash flow"

2. **The direct benefit** — "[Do this] and [get result]"
   EA example: "Switch to mobile money reconciliation and save 3 hours a week"

3. **The curiosity gap** — "The [adjective] truth about [topic]"
   EA example: "The uncomfortable truth about why your Facebook posts aren't working"

4. **The personal address** — "[First name], [short statement or question]"
   EA example: "Sarah, have you tried this yet?"

5. **The how-to** — "How to [achieve outcome] without [common obstacle]"
   EA example: "How to grow your Instagram following without paying for ads"

6. **The social proof** — "How [customer or type] [achieved result]"
   EA example: "How a Ntinda bakery grew its orders by 40% using WhatsApp"

7. **The urgency** — "[Offer] ends [timeframe]"
   EA example: "End of month sale — closes Friday at midnight"

8. **The question** — "[Question the reader is already asking themselves]"
   EA example: "Is your business actually visible online?"

9. **The announcement** — "[New thing] is here"
   EA example: "Our Jinja branch is now open"

10. **The story hook** — "The day [something unexpected happened]"
    EA example: "The day we nearly lost our biggest client — and what we learned"

11. **The exclusive** — "For [segment] only: [offer or content]"
    EA example: "For our VIP customers only: first access to the new collection"

12. **The re-engagement** — "We haven't heard from you in a while, [First name]"
    EA example: "We haven't heard from you in a while, James — is everything okay?"

---

## Quality Criteria

- List building section provides specific opt-in mechanisms with incentives relevant to the client's industry, not generic examples
- Segmentation definitions are actionable — a non-specialist can identify which segment a subscriber belongs to
- Welcome sequence provides a usable subject line formula, preview text approach, and body structure for every email
- Promotional framework includes the 3-email launch sequence with subject lines and CTAs for each email
- Reactivation sequence concludes with a clear suppression instruction — not left open-ended
- KPI benchmarks are calibrated for the EA market and note the open rate limitation of iOS tracking
- Subject line formulas include Uganda/East Africa specific examples for every formula
- Platform differences between Mailchimp and Brevo are noted where they affect the client's decisions
- British English spelling throughout; all monetary values in UGX where referenced
- Frequency recommendation is justified based on the client's purchase cycle and content capacity

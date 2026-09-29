# Email Funnel Build Sequence

Merged from skills/playbooks/playbook-email-funnel on 2026-09-29 at cda737c (S04 tree); preservation map: [playbook-email-funnel.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/playbook-email-funnel.md)

## When to use this reference

Read this reference when the strategy is agreed and the delivery team needs an operating playbook to build and run the email funnel: a 30-day welcome sequence, a steady-state cadence by list size, CTA and mobile design standards, a subject-line testing log, a monthly list health review and a platform recommendation. It turns the SKILL.md strategy document into an email funnel operations brief with owners and checks.

For a timed offer, event, product drop, cohort or campaign window, also read [launch-sequence-operations.md](launch-sequence-operations.md). For the lead magnet that feeds the funnel, read [lead-magnets-and-list-building.md](lead-magnets-and-list-building.md).

## Inputs

Ask for the following before producing any output:

| # | Input | What to capture |
|---|---|---|
| 1 | Business name | Trading name of the client |
| 2 | Industry | Sector and niche |
| 3 | Country / city | Default Uganda/East Africa |
| 4 | Primary goal | What the programme ultimately drives: sales, bookings, enquiries or event registrations |
| 5 | Current list size | Number of subscribers and platform in use (Mailchimp, Brevo, etc.) |
| 6 | Sending frequency | How often the client sends now, if already established |
| 7 | Lead magnet in place | Yes/no; if yes, describe it. If no, build one first with [lead-magnets-and-list-building.md](lead-magnets-and-list-building.md) |

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| A subscriber has not consented or opts out | Suppress immediately and record the change | Unlawful or unwanted email |
| The welcome sequence is not yet live | Do not promote the lead magnet or the list | Subscribers who join, receive no onboarding and disengage |
| Planning weeks 1–12 of a subscriber's life | Front-load the best content, strongest case studies and clearest offers (90/90 rule) | Saving the best material for subscribers who have already decided |
| More than half of sends in a month are promotional | Rebalance to at least 50% pure content | Rising unsubscribes and a deteriorating list |
| List under 200 subscribers | Skip subject-line A/B tests; send one version | Reading meaning into results that are not statistically meaningful |
| Contact has not opened any email in 90 days | Send the three-email re-engagement sequence before removal | Deleting reachable contacts, or mailing dead ones indefinitely |
| Hard bounce notified | Remove within 24 hours; never send to it again | Sender reputation damage |

## Principles

**The 90/90 rule (Bly, 2018).** 90% of list subscribers who will ever buy do so within 90 days of joining. The welcome and early nurture period, the first 12 weeks, is therefore the highest-value part of the programme. The [strategy-document-sections.md § 7A. Strategic Email Programme Principles](strategy-document-sections.md) section sets the matching cadence; this reference applies it to the build.

**Content-to-sales ratio.** At least 50% of all emails sent must be pure content (education, insight, entertainment or community) with no promotional intent at all. Past that point unsubscribe rates rise and list health deteriorates. The ratio builds trust, which is the precondition for conversion.

**Clean beats big.** A clean, engaged list of 500 subscribers will generate more revenue than a dirty list of 5,000 unengaged contacts.

## Procedure

### 1. Build the welcome sequence (weeks 1–4)

Design and test this sequence before the lead magnet is promoted.

| Day | Email purpose | What to include |
|---|---|---|
| Day 1 | Lead magnet delivery and brand introduction | Deliver the promised resource; introduce the brand voice in 2–3 sentences; set expectations for what is coming |
| Day 3 | One actionable tip | A single, immediately usable tip tied to why they signed up; no promotion |
| Day 7 | Genuine expertise | One case study, client result or original insight the subscriber cannot find elsewhere |
| Day 14 | Soft offer | An invitation or low-commitment next step (free consultation, webinar, resource); not a direct purchase push |
| Day 30 | Direct ask | One question: "What is your biggest challenge with [topic]?" Replies inform future content and qualify prospects |

After day 30 the subscriber moves to the steady-state cadence. This build schedule is an alternative to the Day 0–10 welcome series in [strategy-document-sections.md § 3. Welcome Sequence](strategy-document-sections.md): use that series where the purchase cycle is short and the offer is ready early; use this 30-day series where the sale is considered and replies are needed to qualify prospects. Record which one was chosen and why.

### 2. Set the steady-state cadence

Set frequency by content capacity and audience expectation, then hold it without interruption.

| List size | Recommended frequency |
|---|---|
| Under 500 subscribers | Weekly |
| 500–5,000 subscribers | Weekly or twice-weekly |
| Over 5,000 subscribers | Twice-weekly, with segmented sends |

Mark every planned send as content or sales so the 50% ratio can be checked.

### 3. Apply CTA placement rules

Every email carries a call to action. No exceptions.

- At least two CTAs per email: one after the first paragraph, one at the close.
- Emails of 500+ words: add a third CTA in the middle of the body.
- One ask per placement: never put two different asks in the same CTA position; one email, one primary action.
- Specific instructions only: "Click here to book a 30-minute call" or "Reply to this email with your biggest question about X", not "Learn more" or "Get in touch".
- CTAs are hyperlinked text, a button or both. In mobile-optimised emails, use a button for the primary CTA: at least 44px high, high-contrast colour, centred.

### 4. Apply mobile email design standards

The source skill states that 85%+ of emails in Uganda and East Africa are opened on mobile; verify before stating (no register record). Design for mobile first and check desktop second.

| Element | Standard |
|---|---|
| Layout | Single column only; no multi-column grids |
| Body text | Minimum 14px |
| Headlines | Minimum 22px |
| CTA buttons | Minimum 44px high; high-contrast colour; centred |
| Image width | Maximum 600px; avoid text embedded in images |
| Preview text | 40–90 characters; key message first |
| Line length | 50–75 characters per line |

Test every email on a real mobile device before sending, not only in a desktop client preview.

### 5. Run the subject-line A/B testing protocol

Test on every send where the list allows it (minimum 200 subscribers for a meaningful result). Change one variable per send; changing two makes the result impossible to attribute.

Variables, one at a time:

1. Length: short (under 40 characters) against long (60+ characters).
2. Question against statement: "Are you making this mistake?" against "The mistake most businesses make with email".
3. Personalisation: first-name token against none.
4. Emoji against no emoji; test with the primary audience demographic first.
5. Benefit-led against curiosity-led: "How to double your email open rate" against "The counterintuitive truth about email open rates".

Log every test. After 10 tests, identify the winning pattern and make it the default subject-line formula.

### 6. Track the six KPIs from the first send

Set client-specific targets before launch; do not wait for data to accumulate. Review all six monthly. Never report open rate on its own: without CTR and conversion it is vanity data. Targets and definitions match [strategy-document-sections.md § 7. KPIs and Target Benchmarks](strategy-document-sections.md) (Bly, 2018); the signal column below is the operating addition.

| KPI | Target | What it signals |
|---|---|---|
| Bounce rate | Under 1% | List quality; a high rate points to stale or purchased contacts |
| Opt-out rate | Under 0.1% per send | Content relevance; persistently high opt-out means content does not match audience expectations |
| Open rate | 10–15% benchmark (Bly, 2018) | Subject-line effectiveness and sender reputation |
| Click-through rate | 1–5% benchmark | Content-to-CTA fit; weak CTR despite a good open rate means the body copy or CTA is unclear |
| Conversion rate | Client-specific target per campaign | Bottom-of-funnel effectiveness; define what conversion means before launch |
| Revenue per email sent | Track from the first sale | The bottom-line KPI: total revenue attributed to email ÷ total emails sent in the period |

### 7. Hold a monthly list health review

1. Bounce rate: flag any send above 1%; if bounces spike, investigate where new subscribers are coming from.
2. Opt-out rate: flag any send above 0.1%; review that send's content and subject line.
3. Inactive subscribers: identify contacts with no opens in the past 90 days.
4. Re-engagement: send a three-email sequence to inactive contacts before removing them: "We miss you", "Here is our best content", "Last chance — shall we remove you?" ([strategy-document-sections.md § 6. Reactivation Sequence](strategy-document-sections.md) gives full copy structure).
5. Hard bounces: remove within 24 hours of notification; never send to a confirmed hard bounce.

Bounce and opt-out rates must be within target before the following month's sends begin.

### 8. Recommend one platform

Recommend by the client's technical confidence and list size, not personal preference. Plan limits and prices change; verify before stating (no register record).

| Platform | Best for | Cost as recorded in the source skill |
|---|---|---|
| Mailchimp | Lists under 500 subscribers; beginners | Free up to 500 contacts |
| Brevo (formerly Sendinblue) | Lists of any size; automation-heavy programmes | Generous free tier; pay per send |
| ConvertKit | Creator-focused businesses; tag-based segmentation | Free up to 1,000 subscribers |

The source skill records that all three include basic automation (welcome sequences, trigger-based sends) on their free tiers; confirm on the current plan page before advising.

## Template: email funnel operations brief

Produce for the client:

1. Welcome sequence: five emails in the client's brand voice, following the schedule above.
2. Steady-state calendar: a four-week rolling content plan with each send marked content or sales.
3. KPI dashboard template: the six KPIs with client-specific targets and a monthly review date.
4. Subject-line testing log (blank):

   | Date | Variable tested | Winning version | Open-rate difference | CTR difference |
   |---|---|---|---|---|

5. List health review checklist: the monthly actions above in tickable form.
6. Platform recommendation: one platform with setup notes.

## Release checklist

- [ ] 90/90 rule applied: the welcome sequence is written and tested before any list promotion, and the first 12 weeks of content are outlined.
- [ ] All six KPIs tracked from the first send, with client-specific targets set before launch.
- [ ] Content-to-sales ratio monitored monthly and held at a minimum of 50% pure content.
- [ ] Every email has at least two specific, actionable CTAs; no generic "learn more".
- [ ] Every email tested on a mobile device before sending; mobile standards are non-negotiable.
- [ ] Subject-line A/B protocol set up and logged from the first send.
- [ ] List health reviewed monthly; bounce and opt-out within target before the next month's sends.

## Sources

- Bly, R.W. (2018) *The Digital Marketing Handbook: A Step-by-Step Guide to Creating Websites That Sell*, Entrepreneur Press.

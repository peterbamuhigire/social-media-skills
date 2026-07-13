---
name: playbook-email-funnel
description: Use when designing or improving a Email Funnel operating playbook with roles, ordered actions, controls and measures. Use platform skills for channel plans and strategy skills for upstream direction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Email Funnel Operations Playbook

<!-- dual-compat-start -->
## Use When
- Build or improve a repeatable Email Funnel workflow for a client or delivery team.
- Turn an approved objective into roles, controls, handoffs and measurable actions.

## Do Not Use When
- The task is a single-channel presence plan; use the closest `platform-*` skill.
- The task is upstream positioning or channel choice; use the closest `strategy-*` skill.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience and success measure | Approved client brief or accountable owner | Yes | Stop and request the missing decision |
| Current workflow, assets and performance evidence | Team records, platform exports or supplied artefacts | Conditional | Label the baseline unassessed and use a minimum viable workflow |
| Roles, budget, timing and approval limits | Delivery owner | Yes for execution | Produce a draft only; do not schedule, spend or publish |

## Capability and Permission Boundaries
Read supplied artefacts and search relevant evidence. Treat review, audit and planning as read-only. Editing the requested draft is allowed; publishing, messaging, production changes, personal-data processing, spending, destructive actions and certification claims require explicit authority. Use network access only for authorised verification.

## Degraded Mode
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Email Funnel playbook plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| A subscriber has not consented or opts out | Suppress immediately and record the change | Unlawful or unwanted email |
| Inputs and authority are complete | Produce an execution-ready playbook | Unowned actions and hidden assumptions |
| Evidence or tooling is incomplete | Produce the narrowest qualified draft and a gap list | Treating an unassessed check as passed |
| Action publishes, spends, contacts people or changes production state | Require explicit approval before action | Unauthorised external impact |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply the decision rules, preserve useful existing material and draft the Email Funnel playbook.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Email Funnel playbook | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
| Assumption and gap register | Approver or next workflow | Every missing source, unassessed check and required approval has an owner or next action |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and verification record | Inline table or appendix | Each material choice traces to an input, source or labelled assumption |
| Release-gate result | Completed checklist | No blocking policy, factual, permission or anti-slop finding remains |

## Quality Standards
Use British English and the specified market context. Recommendations must be executable with the stated capacity, current claims must be verified or qualified, and acceptance conditions must be observable. A worked example must use a labelled scenario, not fabricated client evidence.

## Anti-Patterns
- Inventing a client fact, benchmark, budget or approval. Fix: cite the source or label the assumption and its effect.
- Copying one channel or client pattern unchanged. Fix: tie each choice to the named audience, objective and evidence.
- Stating volatile platform or legal details from memory. Fix: verify the current official source or omit the claim.
- Treating an inaccessible account, file or metric as healthy. Fix: mark it `not assessed` and bound the conclusion.
- Publishing, spending, messaging or changing production state from planning authority. Fix: obtain explicit action authority.
- Delivering actions without owner, timing or acceptance. Fix: assign all three or return the item as an unresolved gap.

## References
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- [East African English standard](../../language/east-african-english/SKILL.md)
- Use the directly cited sources and companion skills in the domain guidance below; verify time-sensitive claims before use.
<!-- dual-compat-end -->

## Required Inputs

Ask for the following before generating any output:

1. **Business name** — trading name of the client
2. **Industry** — sector and niche
3. **Country / city** — default is Uganda/East Africa
4. **Primary goal** — what the email programme is ultimately driving (sales, bookings, enquiries, event registrations)
5. **Current list size** — number of subscribers and platform in use (Mailchimp, Brevo, etc.)
6. **Sending frequency** — how often the client currently sends (if already established)
7. **Lead magnet in place** — yes/no; if yes, describe it (links to `playbook-lead-magnet-system`)

---

## The 90/90 Rule

Bly (2018) establishes a critical operational principle: **90% of email list subscribers who will ever purchase do so within 90 days of joining the list.**

This means the welcome and early nurture sequence — the first 12 weeks — is the highest-value section of the entire email programme. Front-load the best content, the most compelling case studies, and the clearest offers into weeks 1–12. Do not save the strongest material for later; most subscribers will have made their purchase decision before they reach it.

---

## Welcome Sequence Structure (Weeks 1–4)

Design this sequence before the lead magnet is promoted. A subscriber who joins before the sequence is live will receive no onboarding and will disengage.

| Day | Email Purpose | What to Include |
|---|---|---|
| Day 1 | Lead magnet delivery + brand introduction | Deliver the promised resource; introduce the brand voice in 2–3 sentences; set expectations for what is coming next |
| Day 3 | One actionable tip | A single, immediately applicable tip directly related to why they signed up — no promotion |
| Day 7 | Genuine expertise | One case study, client result, or original insight — something the subscriber cannot find anywhere else |
| Day 14 | Soft offer | An invitation or low-commitment next step (a free consultation, a webinar, a resource) — not a direct purchase push |
| Day 30 | Direct ask | Ask the subscriber one question: "What is your biggest challenge with [topic]?" — replies inform future content and qualify prospects |

After day 30, the subscriber transitions to the steady-state nurture cadence.

---

## Steady-State Cadence

After the welcome sequence, maintain a consistent sending rhythm. Frequency should be set based on content capacity and audience expectation — and held without interruption.

**Recommended cadence by list size and resource:**

| List Size | Recommended Frequency |
|---|---|
| Under 500 subscribers | Weekly |
| 500–5,000 subscribers | Weekly or twice-weekly |
| Over 5,000 subscribers | Twice-weekly, with segmented sends |

**Content-to-sales ratio:** A minimum of 50% of all emails sent must be pure content — education, insight, entertainment, or community — with no promotional intent whatsoever. If more than half of sends are promotional, unsubscribe rates rise and list health deteriorates. The ratio enforces trust, which is the precondition for conversion.

---

## Six Email KPIs

Track all six from the first send. Set client-specific targets before the programme launches — do not wait for data to accumulate before establishing benchmarks.

| KPI | Target | What It Signals |
|---|---|---|
| Bounce rate | Under 1% | List quality; high bounce rate indicates stale or purchased contacts |
| Opt-out rate | Under 0.1% per send | Content relevance; persistent high opt-out means content is misaligned with audience expectations |
| Open rate | 10–15% benchmark (Bly, 2018) | Subject line effectiveness and sender reputation |
| Click-through rate | 1–5% benchmark | Content-to-CTA alignment; weak CTR despite good open rate signals the body copy or CTA is unclear |
| Conversion rate | Set client-specific targets per campaign | Bottom-of-funnel effectiveness; define what conversion means before the campaign launches |
| Revenue per email sent | Track from first sale | The ultimate bottom-line KPI; calculated as total revenue attributed to email ÷ total emails sent in the period |

Review all six KPIs monthly. Do not report open rate in isolation — open rate without CTR and conversion is vanity data.

---

## CTA Placement Rules

Every email must contain a call to action. No exceptions. Apply these rules:

- **Minimum two CTAs per email** — once after the first paragraph, once at the close
- **Emails of 500+ words** — include a third CTA in the middle of the body
- **One CTA per placement** — never include two different asks in the same CTA position; one email, one primary action
- **Specific instruction required** — "Click here to book a 30-minute call" or "Reply to this email with your biggest question about X" — not "Learn more" or "Get in touch"

CTAs must be written as hyperlinked text, a button, or both. In mobile-optimised emails, use a button for the primary CTA — minimum 44px height, high-contrast colour, centred.

---

## Mobile Email Design Standards

In Uganda and East Africa, 85%+ of emails are opened on mobile devices. Design for mobile first; check desktop second.

| Element | Standard |
|---|---|
| Layout | Single-column only — no multi-column grid layouts |
| Body text | Minimum 14px |
| Headlines | Minimum 22px |
| CTA buttons | Minimum 44px height; high-contrast colour; centred |
| Image width | Maximum 600px; avoid text embedded in images |
| Preview text | 40–90 characters; front-load the key message |
| Line length | 50–75 characters per line for comfortable mobile reading |

Test every email on a mobile device before sending. Use a real device, not only a desktop email client preview.

---

## Subject Line A/B Testing Protocol

Run an A/B test on every send where list size permits (minimum 200 subscribers required for statistically meaningful results). Test one variable per send only — changing two variables simultaneously makes it impossible to attribute the result.

**Variables to test (one at a time):**

1. Subject line length — short (under 40 characters) vs. long (60+ characters)
2. Question vs. statement — "Are you making this mistake?" vs. "The mistake most businesses make with email"
3. Personalisation — first name token vs. no personalisation
4. Emoji vs. no emoji — test with the primary audience demographic first
5. Benefit-led vs. curiosity-led — "How to double your email open rate" vs. "The counterintuitive truth about email open rates"

Record every test result in a testing log: date, variable tested, winning version, open rate differential, CTR differential. After 10 tests, identify the winning pattern and apply it as the default subject line formula.

---

## List Health Review

Conduct a formal list health review every month. The review covers:

1. **Bounce rate** — flag any send above 1%; investigate the source of new subscribers if bounce rate spikes
2. **Opt-out rate** — flag any send above 0.1%; review the email content and subject line for that send
3. **Inactive subscribers** — identify contacts who have not opened any email in the past 90 days
4. **Re-engagement sequence** — send a 3-email re-engagement sequence to inactive contacts before removing them: "We miss you", "Here is our best content", "Last chance — shall we remove you?"
5. **Hard bounces** — remove within 24 hours of the bounce notification; never send to a confirmed hard bounce

A clean, engaged list of 500 subscribers will generate more revenue than a dirty list of 5,000 unengaged contacts.

---

## Platform Recommendations for EA Clients

| Platform | Best For | Cost |
|---|---|---|
| Mailchimp | Lists under 500 subscribers; beginners | Free up to 500 contacts |
| Brevo (formerly Sendinblue) | Lists of any size; automation-heavy programmes | Generous free tier; pay per send |
| ConvertKit | Creator-focused businesses; tag-based segmentation | Free up to 1,000 subscribers |

All platforms above include basic automation (welcome sequences, trigger-based sends) on their free tiers. Recommend the platform based on the client's technical confidence and list size, not personal preference.

---

## Output: Email Funnel Operations Brief

Generate the following for the client:

1. **Welcome sequence** — 5 emails written in the client's brand voice, one per day as per the schedule above
2. **Steady-state calendar** — 4-week rolling content plan with content-to-sales ratio marked for each send
3. **KPI dashboard template** — six KPIs with client-specific targets and a monthly review schedule
4. **Subject line testing log** — blank template for recording A/B test results
5. **List health review checklist** — monthly actions in a tickable format
6. **Platform recommendation** — one recommended platform with setup notes

---

## Quality Criteria

Output meets the standard when:

1. The 90/90 rule is applied — the welcome sequence is fully written and tested before any list promotion begins, and the first 12 weeks of content are outlined
2. All six KPIs are tracked from the first send, with client-specific targets set before launch — not after results arrive
3. Content-to-sales ratio is monitored monthly and maintained at a minimum of 50% pure content sends
4. Every email contains a minimum of two CTAs, each specific and actionable — no generic "learn more" instructions
5. All emails are tested on a mobile device before sending — mobile design standards are non-negotiable
6. Subject line A/B testing protocol is established and logged from the first send
7. List health is reviewed monthly — bounce rate and opt-out rate are within targets before the following month's sends begin

---

## Reference

Bly, R.W. (2018) *The Digital Marketing Handbook: A Step-by-Step Guide to Creating Websites That Sell*. Entrepreneur Press.

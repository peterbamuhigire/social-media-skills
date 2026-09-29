---
name: playbook-reputation-management
description: 'Use when a brand''s standing online is weak or under attack: poor Google or Facebook ratings, negative reviews, damaging search results or local gossip; produces the reputation audit and score, review-response protocol and 90-day recovery plan; not for proactive review and referral programmes (use `strategy-ewom-reviews`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Reputation Management Playbook

Audits, defends and rebuilds how a brand looks online (ratings, reviews, search results and local press) for Ugandan and East African businesses, from a weighted reputation score through to a 90-day recovery plan.

<!-- dual-compat-start -->
## Use When
- Audit what people see when they search the company name: ratings, reviews, press and forums, with a reputation score and red flags.
- Angry customers are posting after a service failure or billing mistake: reply templates for negative and positive reviews, who answers, and when to bring in legal or PR.
- Push down damaging search results with stronger content and Google Business Profile authority.
- Plan a recovery: stabilise in the first two weeks, run a review drive, publish positive content and keep monitoring by month three.
- Handle East African specifics: reviews sent by WhatsApp, Facebook recommendations versus Google reviews, local press, and Uganda DPPA 2019 limits on using customer data.

## Do Not Use When
- `strategy-ewom-reviews` for review generation, testimonials and referral programmes when nothing is wrong.
- `playbook-crisis-communications` for a fast-moving incident with media attention.
- `meta-social-listening` for setting up ongoing mention and sentiment monitoring.
- Stop before posting fake or paid-for reviews, threatening reviewers or asking platforms to remove content without evidence and client approval.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business name, industry and country/city | Client | Yes | Default the market to Uganda/East Africa; stop if the business cannot be identified. |
| Current star ratings and review counts on Google Business Profile, Facebook and other active review profiles | Client; incognito search and platform pages | Yes | Run the audit checklist from public pages and mark any platform you cannot see `not assessed`. |
| Negative press, viral complaints and incidents in the last 24 months, with how they were handled | Client; local press search | Yes | Search the five local outlets and record "none found" with the date searched. |
| Focus: Proactive, Reactive or Recovery | Client lead | Yes | Derive it from the weighted score (below 3.9 means Recovery) and label it provisional. |
| Lawful basis and consent record for customer contact data | Client data owner | For review outreach | Hold all review-request outreach; deliver the audit and response protocols only. |
| Response owners, named contacts and approval limits | Delivery owner | For execution | Produce templates as drafts with placeholder owners; do not post replies. |

## Workflow

1. Ask the intake questions and confirm the focus (Proactive, Reactive or Recovery); stop if the business, market or response owner is missing. See [the method](references/reputation-audit-and-recovery-method.md#required-input).
2. Run the audit checklist across Google Business Profile, Facebook, other directories and page-1 search results before recommending anything.
3. Calculate the weighted score (GBP 50 %, Facebook 30 %, other platforms 20 %), read it against the bands below and tick the red flags.
4. Build the proactive layer: WhatsApp review requests, positive-review replies, GBP authority actions and the monthly reputation content mix.
5. Build the reactive layer: the complaint decision tree, negative-review protocol, suppression list where negative results rank on page 1, escalation thresholds and the do-not-do list.
6. Where the score is below 3.9 or a significant incident has occurred, lay out the 90-day recovery plan (Week 1–2, Week 3–4, Month 2, Month 3) with owners and dates.
7. Check every outreach step against Uganda DPA 2019 consent and every reply against platform review policies; stop and escalate to legal or `playbook-crisis-communications` when a threshold is met.
8. Run the quality and anti-slop gates; correct any failed template or action and rerun the check before hand-off.

## Score bands

| Weighted score | Reading | Response |
|---|---|---|
| 4.5–5.0 | Strong | Maintenance and volume growth |
| 4.0–4.4 | Acceptable | Targeted improvement |
| 3.5–3.9 | Weak | Proactive recovery required |
| Below 3.5 | Critical | Launch the reputation recovery plan |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Reputation audit table with weighted score and red flags | Client owner | Every platform in scope has a rating, count and date or is marked `not assessed`; red flags ticked before any recommendation. |
| Review request and response templates (WhatsApp request, positive reply, 1-star reply) | Client response team | British English with an East African tone; personalised fields marked; no public offer of compensation. |
| Complaint, escalation and suppression protocol | Client owner; legal or PR adviser when triggered | Each escalation threshold names its trigger and the owner who takes over. |
| 90-day recovery plan or maintenance cadence | Client owner and delivery team | Each task has a responsible party, channel and timeline; plan depth matches the stated focus. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Page-1 search baseline (titles and URLs) with the search date | Table or screenshots | Recorded in Week 1 and re-run at month 3 for comparison. |
| Review outreach tracker | Spreadsheet: name, date sent, date reviewed, platform | No contact is listed without a recorded lawful basis. |
| Escalation and evidence log for coordinated attacks or false claims | Dated log with screenshots | Evidence is preserved before any report or response. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Posting replies, sending review requests and reporting content to platforms each need that authority separately.

## Degraded Mode

Without current ratings and page-1 search results, return the narrowest qualified result and mark the affected checks `not assessed`. The response templates, do-not-do list and escalation thresholds can still be delivered as drafts.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A damaging claim is credible and unresolved | Preserve evidence, respond proportionately and move resolution to the right owner | Defensive deletion that compounds distrust |
| A public complaint appears | Acknowledge publicly within 2 hours, move to a private channel, resolve within 24 hours where possible, close publicly | A visible unanswered complaint that lowers trust more than the complaint itself |
| Weighted score below 3.9 or a significant public incident | Run the full 90-day recovery plan and fix the operational root cause first | A recovery that fails because the cause is still live |
| A negative result ranks on page 1 of Google for the business name | Start the prioritised suppression list and track weekly; expect 60–120 days | Promising quick removal of search results |
| False factual claims in press or on a high-traffic platform, or defamation | Engage a lawyer before responding publicly; do not counter publicly | Legal exposure from a public rebuttal |
| Several 1-star reviews in a short window from accounts with no other activity | Treat as a coordinated attack: document evidence and report to Google | Answering fake accounts one by one |
| Crisis with media coverage | Hand over to `playbook-crisis-communications` immediately | Managing a media crisis through review-response protocols |
| Review outreach is proposed | Confirm Uganda DPA 2019 lawful basis and consent; never offer incentives or use bought lists | Privacy breach and review-policy violation |

## Quality Standards

- A completed audit table with a weighted score and documented red flags comes before any recommendation.
- At least one customised WhatsApp review request and one Google review response template, both in British English with an East African tone.
- Proactive and reactive components are balanced to the stated focus: a recovery-stage client gets the full 90-day plan; a maintenance-stage client gets a content cadence and review system.
- Uganda DPA 2019 is named explicitly wherever review outreach is recommended, with a clear compliance checkpoint.
- Specific local publications and platforms for the Ugandan/EA context are named, not generic global examples.
- A concrete, prioritised suppression list is included whenever negative search results are identified.
- Escalation thresholds are explicit: the consultant knows exactly when to move from social media response to legal or PR intervention.
- Every action item is assignable, with a responsible party, a channel and a timeline.

## Anti-Patterns

- Arguing with a reviewer or complainant in a public thread. Fix: acknowledge, move to a private channel and close publicly once resolved.
- Offering a refund, discount or free service in a public reply. Fix: make any compensation offer privately.
- Deleting a Facebook complaint comment. Fix: leave it and respond; deletion is logged, can be screenshotted first and signals guilt.
- Asking friends, staff or associates to post positive reviews to counter negative ones. Fix: run the genuine review drive; counter-posting is review manipulation and breaks platform policies.
- Ignoring a negative review in the hope it disappears. Fix: answer it with the negative-review protocol.
- Offering incentives, discounts or gifts in exchange for reviews. Fix: ask within 24–48 hours of a positive experience, with one follow-up only.
- Sending the same pasted reply to every review. Fix: vary the language and reference the reviewer's specific comment.

## References

- [Reputation audit, defence and recovery method](references/reputation-audit-and-recovery-method.md): read when running the audit, drafting templates, planning suppression, building the recovery plan or applying Uganda and East African specifics.
- [`playbook-crisis-communications`](../playbook-crisis-communications/SKILL.md): read when an incident involves media coverage, coordinated attacks or a business-threatening public controversy.
- [`meta-social-listening`](../../meta-analytics-ops/meta-social-listening/SKILL.md): read when setting up ongoing monitoring of brand mentions, keywords and competitor activity.
- [`platform-google-business-profile`](../../platforms/platform-google-business-profile/SKILL.md): read when doing detailed GBP setup, post strategy and Q&A management.
- [`strategy-ewom-reviews`](../../strategy/strategy-ewom-reviews/SKILL.md): read when nothing is wrong and the need is proactive review and referral programmes.
- [`blog-writer`](../../content-writing/blog-writer/SKILL.md): read when drafting suppression and case-study blog posts.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when replies or plans make legal, privacy or defamation claims.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting templates and replies.
- [East African English standard](../../language/east-african-english/SKILL.md): read when setting tone for WhatsApp and review replies.
<!-- dual-compat-end -->

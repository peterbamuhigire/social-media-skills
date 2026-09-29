---
name: email-copywriter
description: Use when a client needs a specific email written, such as a newsletter, promotional offer, welcome or reactivation email; produces send-ready email copy with subject lines, preview text, body and call to action; not for designing the email programme, lifecycle sequences or list strategy (use `07-email-marketing-strategy`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Email Copywriter

Writes send-ready newsletter, promotional, welcome and reactivation emails: subject lines, preheader, body and one CTA, mobile-first and in British English. Core principle: emails must earn the right to sell; value first, sell second.

<!-- dual-compat-start -->
## Use When
- We need this month's newsletter written for our customers or members.
- A sale, launch or event needs a promotional email with a clear offer and one call to action.
- New subscribers should get a welcome email that sets expectations and makes a first offer.
- Lapsed customers need a reactivation email to bring them back.
- Our open rates are low and we want subject line and preview text options to test.

## Do Not Use When
- `07-email-marketing-strategy` for the lifecycle programme, segmentation and measurement plan.
- `direct-response-funnel-copy` for multi-step sales sequences inside a launch funnel.
- `caption-writer` for social post copy.
- Stop before sending or scheduling in Mailchimp or any email platform, and before emailing anyone who has not opted in.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client business name (the inbox sender name), industry and country/city | Client brief | Yes | Default the market to Uganda/East Africa; ask for the sender name before writing. |
| Email type (newsletter, promotional, welcome, reactivation) and primary goal (awareness, relationship, conversion, reactivation) | Account manager or `07-email-marketing-strategy` | Yes | Stop and ask; the structure depends on the type. |
| Audience segment (leads, active customers, lapsed customers, VIPs) and its opt-in status | Client CRM or email platform export | Yes | Write for the named segment only; stop if the list's consent is unknown. |
| Key message (one sentence), offer or content to feature, and the CTA | Approved brief | Yes | Draft the key message from the brief and flag the assumed CTA for confirmation. |
| Brand tone (3 words) and banned vocabulary | `04-brand-voice-intake` | No | Take tone from recent client emails and apply the engine's banned-word list. |
| Offer terms, prices, deadlines, testimonials and metrics | Client source pack or authorised owner | Conditional | Hold urgency and social proof lines unless they are genuine and traceable. |

The full intake list is in the [email type templates](references/email-type-templates.md#required-input).

## Workflow

1. Confirm the email type, segment, goal and sending boundary; route to `07-email-marketing-strategy` for the lifecycle programme or to `direct-response-funnel-copy` for multi-step launch-funnel sequences.
2. Inventory the offer facts, proof, deadlines and consent status; stop if the goal, segment or opt-in basis is unknowable.
3. Pick 3 subject line approaches from the [12 subject line formulas](references/email-type-templates.md#12-subject-line-formulas) that suit the type and audience, and write a preheader of 40–90 characters that extends the subject line rather than repeating it.
4. Build the body to the type's structure in the [email type templates](references/email-type-templates.md): newsletter (value first, 150–250-word feature), promotional (desire-led hook, four-element offer, one proof line, 3 button options, genuine urgency only, PS), welcome (specific thanks, three what-to-expect bullets, first gift) or reactivation (honest acknowledgement, re-engagement hook, explicit opt-out).
5. For welcome sequences, launches, waitlists, event promotion or reactivation flows, sequence the emails with [launch and sequence copy](references/launch-and-sequence-copy.md); for premium or high-ticket offers apply `premium-commercial-writing`.
6. Apply the writing standards (British English, sentences under 20 words on average, 2–3-sentence paragraphs, one CTA, written to one person, mobile-first, personal sign-off) and run the direct-marketing ethics filter on selling emails.
7. Run the `anti-ai-slop` humanising passes and the quality checks below; correct any failing section and rerun the checks before delivery.
8. Deliver send-ready copy with the claim register and the approval step; the client or an authorised owner schedules it.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| 3 subject line options and 1 preheader | Client approver; email platform operator | Three genuinely different approaches; preheader 40–90 characters, complementing not repeating. |
| Email body with one CTA and personal sign-off | Client approver | Follows the type's structure; value before any ask; scannable on a smartphone. |
| CTA button options (promotional) and PS line | Client approver | Three action-led button texts; the PS restates the benefit differently or answers the likeliest objection. |
| Sequence copy, when requested | `07-email-marketing-strategy` owner | Each email progresses the sequence; no two emails do the same job. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Claim, proof and urgency register | Inline table | Every price, saving, deadline, place count, testimonial and metric traces to a source or is removed. |
| Consent and segment note | One line per send | States the segment and its opt-in basis, or marks it `not assessed`. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Sending or scheduling in Mailchimp or any email platform, and emailing anyone who has not opted in, is out of scope.

## Degraded Mode

Without a confirmed email type, segment or opt-in basis, return the narrowest qualified result and mark the affected checks `not assessed`. Subject line options and a draft body for the most likely type can still be delivered, with assumptions flagged.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The email is a newsletter | Give value first; use a reply or resource CTA, never a sales CTA unless the brand has built significant trust with this list. | Readers who learn to ignore the newsletter. |
| Urgency, a deadline or scarcity is proposed | Include it only if genuine and stated plainly ("Offer closes [date]", "Only [N] places remaining"); use a "Last chance" subject only if the list is genuinely being cleaned. | False urgency and lost trust. |
| Subscribers have not opened or clicked in 60 or more days | Send a reactivation email before any further promotion, with an explicit, guilt-free opt-out. | Damaged sender reputation and spam reports. |
| A reactivation offer is being considered | Use one only if relevant and authentic; never manufacture an offer purely to reactivate. | A cynical offer that damages trust. |
| Social proof is needed | Use one specific, traceable customer result, testimonial or metric. | Vague claims ("our clients love us") or invented numbers. |
| The offer is premium or high-ticket | Show proof, value and risk reduction with one appropriately weighted CTA; apply `premium-commercial-writing`. | Discount-led copy that cheapens the offer. |

## Quality Standards

- Subject line options are genuinely different in approach, not three versions of the same formula; the preheader complements the subject line without repeating it.
- The opening earns attention before requesting or selling anything; no "we are pleased to announce" or "I hope this email finds you well" opener.
- One clear CTA throughout; no competing actions in the same email.
- British English throughout (organisation, colour, recognise, programme); no banned vocabulary in any section.
- Scannable on mobile: short paragraphs, no walls of text, white space between sections.
- Tone matches the brand voice and suits the EA professional register: warm but not unprofessional.
- Premium or high-ticket emails show proof, value, risk reduction and one appropriately weighted CTA.
- Passes the `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns

- Opening a promotional email with the product ("We are excited to offer you…"). Fix: open with the reader's desire or problem and lead with the benefit.
- Two competing CTAs in one email. Fix: keep one action; move the second to a later email.
- Addressing "dear subscribers" or "hello everyone". Fix: write to one person.
- Sending further promotions to inactive subscribers. Fix: run reactivation first and let them leave cleanly.
- Adding a price, result, quotation or metric without a traceable source. Fix: verify it or qualify/remove it.
- Sending or scheduling from drafting authority alone, or emailing people who have not opted in. Fix: obtain explicit action-specific authority and confirm consent.

## References

- [Email type templates](references/email-type-templates.md): read when asking the intake questions, building a newsletter, promotional, welcome or reactivation email, applying the writing standards or choosing subject line formulas.
- [Launch and sequence copy](references/launch-and-sequence-copy.md): read when writing a welcome sequence, timed launch, waitlist sequence, event promotion or reactivation flow.
- [Human, professional phrase bank](../references/human-professional-phrase-bank.md): read when shaping sentence patterns for emails, posts, ads, pages, rate cards and plans.
- [Direct-marketing ethics filter](../references/direct-marketing-ethics-filter.md): read before releasing any selling email; the screen is mandatory.
- [`07-email-marketing-strategy`](../../pipeline/07-email-marketing-strategy/SKILL.md): read when the lifecycle programme, segmentation or measurement plan is in question.
- [`premium-commercial-writing`](../premium-commercial-writing/SKILL.md): read when the email sells a premium or high-ticket offer.
- [`caption-writer`](../caption-writer/SKILL.md): read when routing is unclear; it is the nearest neighbour.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting and before client delivery.
- [Repository agent guide](../../../AGENTS.md): read when an email raises a market, safety or consent question the engine-wide gates cover.
<!-- dual-compat-end -->

---
name: 07-email-marketing-strategy
description: Use when a client wants to build, grow or revive an email list, including lead magnets, welcome and win-back sequences and a lapsed-customer reactivation push; produces the email marketing strategy and lifecycle sequence map; not for writing the finished emails themselves (use `email-copywriter`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Email Marketing Strategy Generator

Produces the authoritative email marketing strategy document in the suite: eight client-specific sections a non-specialist can follow, defaulting to Uganda/East Africa and to Mailchimp or Brevo as the platform.

<!-- dual-compat-start -->
## Use When

- The client has customer emails but never sends anything, and needs a plan for list growth, segmentation, newsletters, sequences, promotions and how to judge results.
- Customers have not bought in a year or more and the client wants to win them back: a thank-you message, a comeback or returning-customer offer, a refer-a-friend ask and a WhatsApp win-back follow-up sequence.
- The email funnel needs running rules: welcome sequence timing, steady cadence, CTA placement, mobile layout and a subject-line A/B test log.
- The client wants a lead magnet such as a free checklist, report, quiz or webinar, with website pop-ups, exit-intent placements, WhatsApp delivery and double opt-in.
- A timed launch, event or product drop needs its own email sequence plan.

## Do Not Use When

- `email-copywriter` for the finished subject lines and email copy.
- `playbook-marketing-automation` for building triggers and workflows in the automation tool.
- `06-digital-marketing-strategy` when email is one channel in a wider digital plan.
- Stop before mailing any list without proof of consent and an unsubscribe route under Uganda's DPPA 2019 or the law that applies.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, industry and sub-sector, primary product or service, country/city | Client brief or `01-client-brief` | Yes | Default the location to Kampala, Uganda; return the intake questions for the rest. |
| Current list size and email platform | Client; dated platform export | Yes | Treat the list as zero and recommend Mailchimp or Brevo on list size and budget. |
| Consent basis and unsubscribe route for every list | Client; sign-up records | Yes | Stop before any send plan for that list; design double opt-in and plan only new, consented growth. |
| Purchase cycle length and re-purchase frequency | Client or sales records | Yes | Default the newsletter to fortnightly and label the cadence provisional. |
| Primary goal for email (lead nurture, retention, promotional sales or all three) | Client lead | Yes | Plan for all three and ask the client to rank them. |
| Monthly budget (platform fees plus content production) | Client | Yes | Recommend within free-plan limits and state which paid features (A/B tests, send-time optimisation) are excluded. |

## Workflow

1. Ask the intake questions in [strategy-document-sections](references/strategy-document-sections.md) § Intake questions; route to `06-digital-marketing-strategy` when email is one channel in a wider plan, or to `email-copywriter` for finished copy.
2. Confirm consent and an unsubscribe route for every list; stop the send plan for any list without proof of consent under Uganda's DPPA 2019 or the law that applies.
3. Write sections 1–6 (list building, segmentation, welcome sequence, newsletter, promotional framework, reactivation) with the section method; use simplified segmentation under 200 subscribers.
4. Apply section 7A: a front-loaded weeks 1–12 cadence, a separate months 4–12 cadence, the 50 % content floor and the send-time optimisation deliverable.
5. Set section 7 KPIs with East African benchmarks and section 8 subject-line formulas with Uganda/EA examples.
6. Add the conditional packs the decision rules trigger (win-back, funnel operations brief, launch sequence, lead magnet).
7. Check the document against the quality standards; correct any failing section and rerun the check before hand-off.
8. Run the anti-slop ship gate and hand the strategy to the client lead; withhold release while a consent, figure or evidence defect remains.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Email marketing strategy document (sections 1–8 with 7A) | Client lead; `email-copywriter` | All eight sections present and client-specific; no generic examples left. |
| Lifecycle sequence map (welcome, newsletter, launch, reactivation) with send timings | `playbook-marketing-automation`; delivery team | Every email has timing, subject-line formula, body structure and CTA; reactivation ends in a suppression instruction. |
| KPI and list-health plan | Client lead | Six core KPIs with EA targets, CTOR as the primary quality indicator and a monthly content-to-sales ratio check. |
| Conditional packs (win-back brief, funnel operations brief, lead magnet plan) | Client lead; delivery team | Produced only when a decision rule triggers them, each with owners. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Consent and list-source record | Table: list, source, consent basis, unsubscribe route | Every list planned for sending has a recorded consent basis; unknown bases are marked `not assessed`. |
| Benchmark and platform-feature register | Table: figure or feature, source, date | Each benchmark and plan-tier claim (for example send-time optimisation tiers) is dated or labelled unverified. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Importing contacts, building automations or sending to any list is out of scope for this strategy.

## Degraded Mode

Without the list size, consent basis or purchase cycle, return the narrowest qualified result and mark the affected checks `not assessed`. A list-building, lead magnet and welcome-sequence plan for new consented subscribers can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A list has no proof of consent or unsubscribe route | Stop sends to it; plan only double opt-in growth and a consent refresh. | Unlawful mailing under the DPPA 2019 and sender-reputation damage. |
| The client holds a dormant past-customer list it has stopped contacting | Build the four-part win-back campaign and sign-off brief with [win-back-and-reactivation](references/win-back-and-reactivation.md); send Message 1 only to numbers without opt-in. | Cold-ad spend while a warm list sits unused; messaging without consent. |
| The strategy is agreed and the team must build and run the funnel | Produce the operations brief with [email-funnel-build-sequence](references/email-funnel-build-sequence.md) (add [launch-sequence-operations](references/launch-sequence-operations.md) for a timed launch). | A strategy nobody can operate; promotion before onboarding is live. |
| The list is small or growing slowly and there is no specific opt-in offer | Design the lead magnet, placements and double opt-in with [lead-magnets-and-list-building](references/lead-magnets-and-list-building.md). | Generic newsletter sign-ups and unconsented list additions. |
| Setting send frequency (three figures in this engine answer different questions) | New subscribers, weeks 1–12: 2 emails a week (Bly, 2018). Steady state, months 4–12: start B2C newsletters at 1–2 a month (B2B at most 2 a month) per [owned-media-assets](../../strategy/peso-integrated-strategy/references/owned-media-assets.md), and raise towards the list-size ceiling in [email-funnel-build-sequence](references/email-funnel-build-sequence.md) (weekly under 500 subscribers) only when open rates hold above 25 % and content capacity exists. State the chosen cadence and its reason. | A flat 12-month cadence that misses the 90/90 buying window, or East African unsubscribes from over-mailing. |
| More than half of sends in a month carry a sales message | Rebalance to at least 50 % pure content and report the ratio monthly with bounce and opt-out rates. | Rising opt-outs and a deteriorating list. |
| The plan sends marketing mail at volume, uses a new sending domain, or the client asks whether lifecycle flows add revenue | Add the Gmail and Yahoo sender checklist (SPF, DKIM, DMARC at least `p=none`, one-click unsubscribe, spam rate below 0.10 %), warm-up and a persistent random holdout per [deliverability-and-lifecycle-holdouts](references/deliverability-and-lifecycle-holdouts.md) (registers `GMAIL-SENDER-GUIDELINES`, `YAHOO-SENDER-REQUIREMENTS`). | Mail rejected or foldered under bulk-sender enforcement; flows credited with sales they did not cause. |
| The list is under 200 subscribers | Use Leads and Customers segments only; expand to four segments once the list exceeds 500. | Segments too small to act on. |
| Email is one channel in a wider digital plan | Route to `06-digital-marketing-strategy` and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Quality Standards

- List building gives specific opt-in mechanisms with incentives relevant to the client's industry, not generic examples.
- Segmentation definitions are actionable: a non-specialist can identify which segment a subscriber belongs to.
- The welcome sequence gives a usable subject line formula, preview text approach and body structure for every email, and the promotional framework includes the 3-email launch sequence with subject lines and CTAs for each email.
- The reactivation sequence concludes with a clear suppression instruction, not left open-ended.
- KPI benchmarks are calibrated for the EA market and note the open rate limitation of iOS tracking.
- The frequency recommendation is justified on the client's purchase cycle and content capacity, with a distinct weeks 1–12 cadence.
- Subject line formulas include Uganda/East Africa specific examples for every formula, and platform differences between Mailchimp and Brevo are noted where they affect the client's decisions.
- British English spelling throughout; all monetary values in UGX where referenced.

## Anti-Patterns

- Applying one flat cadence across the full 12 months. Fix: specify how weeks 1–12 differ from months 4–12 (90/90 rule).
- Judging performance on open rate alone. Fix: treat opens as directional (Apple Mail Privacy Protection inflates them) and use CTOR as the primary quality indicator.
- Deleting non-openers after reactivation. Fix: suppress them, keep them reachable through other channels and review suppressed contacts every 6 months.
- Writing "Offer expires" lines for offers with no real deadline. Fix: use urgency only when genuine; re-promote evergreen offers every 8 weeks with a new angle.
- Promoting the lead magnet before the welcome sequence is live. Fix: build and test the welcome sequence first.
- Running subject-line A/B tests on a list under 200. Fix: send one version until the list is large enough; test one variable at a time.
- Sending, importing or automating in a live account during planning. Fix: hand the strategy over; live actions need separate authority.

## References

- [Email strategy document method](references/strategy-document-sections.md): read when asking the intake questions or writing sections 1–8 and 7A, the eleven copywriting principles, the KPI tables and the subject-line formulas.
- [win-back-and-reactivation](references/win-back-and-reactivation.md): read when a dormant past-customer list needs a reactivation campaign.
- [email-funnel-build-sequence](references/email-funnel-build-sequence.md): read when building and operating the funnel after the strategy is agreed.
- [launch-sequence-operations](references/launch-sequence-operations.md): read when the funnel serves a timed offer, event, product drop or cohort.
- [lead-magnets-and-list-building](references/lead-magnets-and-list-building.md): read when designing the opt-in offer, placements and double opt-in.
- [deliverability-and-lifecycle-holdouts](references/deliverability-and-lifecycle-holdouts.md): read when setting sender authentication, unsubscribe handling, spam-rate monitoring, warm-up or a lifecycle holdout test.
- [`06-digital-marketing-strategy`](../06-digital-marketing-strategy/SKILL.md): read when email is one channel in a wider digital plan.
- [`email-copywriter`](../../content-writing/email-copywriter/SKILL.md): read when the finished subject lines and email copy are needed.
- [`playbook-marketing-automation`](../../playbooks/playbook-marketing-automation/SKILL.md): read when triggers and workflows must be built in the automation tool.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when the strategy makes consent, DPPA or benchmark claims.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

---
name: strategy-ewom-reviews
description: 'Use when a business wants more reviews, testimonials and recommendations: asking happy customers, a social-proof register, superfans and referral rewards via WhatsApp codes or Mobile Money; produces the reviews and word-of-mouth plan; not for damage control after public criticism (use `playbook-reputation-management`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# eWOM and Reviews Strategy

Designs a proactive electronic word-of-mouth (eWOM) programme that gets satisfied East African customers to review, share and refer honestly, using the GST framework (Hanlon and Tuten, 2022) and measuring advocacy rather than follower counts.

<!-- dual-compat-start -->
## Use When

- Satisfied customers stay silent; we want more Google, Facebook, TripAdvisor or Jumia reviews without faking or buying them.
- Testimonials, results, certifications and endorsements need collecting, permission checks and placing on the website, proposals and WhatsApp sales chats, with a proof asset register.
- We want superfans and a referral programme: Connectors, Mavens and Salespeople, WhatsApp referral codes and Mobile Money rewards.
- We need to measure electronic word of mouth (eWOM) and advocacy, not just follower counts.

## Do Not Use When

- `playbook-reputation-management` for responding to bad reviews, complaints and criticism.
- `08-influencer-marketing-strategy` for paid creator and influencer programmes.
- `strategy-customer-value-journey` for the full funnel from awareness to advocacy.
- Stop before fabricating, buying or gating reviews, or offering incentives that break platform or consumer-protection rules.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business name, industry, country/city and primary goal (Google review volume, referral programme, first NPS) | Client | Yes | Default to Uganda / East Africa; ask for the goal before choosing tactics. |
| Active review platforms and current monthly review volume | Client; platform profiles | Yes | Count visible reviews on Google and Facebook and mark velocity a baseline estimate. |
| Current NPS or CSAT score | Client survey data | If measured | Confirm none exists and make an NPS survey to all active clients the month-one action. |
| Primary customer communication channel (WhatsApp, email, phone) | Client | Yes | Default to WhatsApp for review and referral requests. |
| Existing reviews, testimonials, social mentions and consent records | Client files; public profiles | Yes | Run the proof audit first; publish no testimonial without recorded consent. |
| CRM or enquiry-source records | Client | If available | Add a CRM source field before reporting referral rate. |

## Workflow

1. Confirm the goal is proactive advocacy, not a response to live complaints (`playbook-reputation-management`) or paid creators (`08-influencer-marketing-strategy`); run the intake in the [eWOM programme method](references/ewom-programme-method.md).
2. Audit current proof: inventory reviews, testimonials and mentions, and identify the client's own peak satisfaction moments; stop any testimonial or proof asset from being placed until consent is recorded.
3. Design Give, Seek and Transmit activation: a single-tap review link sent by WhatsApp within 48 hours of each peak moment, visible reviews where seekers look, and shareable assets for transmitters.
4. Identify transmitters through social listening (`meta-social-listening`), the NPS recommendation question and CRM data, and build the Advocate List from promoters (score 9–10).
5. Design incentives for referrals and social sharing only, with every reward disclosed; for a full superfan or referral programme apply the [referral design reference](references/word-of-mouth-and-referral-design.md), and for proof placement the [proof asset register](references/social-proof-asset-register.md).
6. Set the negative-review response routine and the six monthly eWOM metrics, ranking platforms Google first, Facebook second.
7. Check every request, incentive and proof asset against platform and consumer-protection rules; correct any incentivised Google review request or unconsented proof and rerun the check, then run the anti-slop gate before hand-off.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| eWOM programme plan covering Give, Seek and Transmit with the client's peak satisfaction moments | Client lead; customer-facing team | All three behaviours activated; peak moments specific to the client, not generic timing. |
| WhatsApp review request template, short review links and team briefing | Customer-facing team | 48-hour window stated; links tested on a mobile device. |
| Referral and advocacy incentive design with the Advocate List criteria | Client lead | Incentives target referrals and social sharing, never Google reviews; rewards disclosed. |
| Negative-review response routine and templates | Named team member | Response within 24 hours, private resolution channel, invitation to update the review. |
| Monthly eWOM measurement dashboard spec | Client lead; analytics owner | All six metrics with definitions, targets and monthly cadence. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Proof inventory and consent register | Table | Every testimonial or proof asset has source, date and consent status. |
| eWOM baseline | Table of the six metrics | Each value is sourced from a platform count, survey or CRM, or marked `not assessed`. |
| Incentive compliance check | Checklist | Each incentive is checked against Google's review guidelines and disclosure rules. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Sending review requests, NPS surveys or referral messages to customers is outreach and personal-data processing.

## Degraded Mode

Without the client's current review counts and customer contact channel, return the narrowest qualified result and mark the affected checks `not assessed`. The GST design, request template, response routine and metric definitions can still be delivered with a baseline to be filled in month one.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The goal is new advocacy rather than incident response | Design ethical prompts and proof capture; route active damage control to reputation management. | Manipulated reviews or a growth plan built on unresolved complaints. |
| An incentive is proposed for a Google review | Redirect it to referrals and social sharing; Google's review guidelines prohibit incentivised reviews. | Review removal and platform penalties. |
| The client wants to hide negative reviews to show a perfect rating | Display them alongside positive ones and respond professionally (a 4.3-star mixed record is more trusted than 5.0, Rageh, 2026). | A record that reads as manipulation or selective deletion. |
| eWOM effort is spread across many platforms | Focus on Google and Facebook first; expand only after review velocity on both is strong. | Thin, stale reviews everywhere. |
| The client needs proof collected, consented, placed by touchpoint or governed as a register | Apply [social-proof-asset-register.md](references/social-proof-asset-register.md): six proof sources, at least three per conversion page, consent before publishing. | Unconsented, expired or single-source proof. |
| The client needs a full organic word-of-mouth or referral programme | Apply [word-of-mouth-and-referral-design.md](references/word-of-mouth-and-referral-design.md): five pillars, advocate types, referral loop, dark-social tracking; disclose every reward. | Accidental referrals, undisclosed incentives or untracked WhatsApp advocacy. |
| Evidence is contradictory or materially incomplete | Pause the affected recommendation and request the accountable source. | Confident advice built on an unresolved premise. |
| Authority is limited to analysis or planning | Deliver a read-only plan and approval checklist. | Unauthorised publication, spend, outreach, or data use. |

## Quality Standards

- The GST Framework (Give / Seek / Transmit) is applied — the strategy activates all three eWOM behaviours, not just review generation.
- Peak satisfaction moments are identified for the specific client — not generic timing recommendations.
- The 48-hour review request window and WhatsApp-first request channel are specified.
- The objectivity principle is applied — the strategy includes negative review response, not just positive review generation.
- All six eWOM measurement metrics are included with monthly tracking cadence.
- Google's prohibition on incentivised reviews is flagged — incentives are directed at referrals and social sharing.
- Platform priority is ranked with EA context: Google first, Facebook second.
- Language is British English throughout; imperative in all instructional sections; `ai-marketing/anti-ai-slop` is applied during drafting and release is blocked on an F from `ai-marketing/ai-slop-audit`.

## Anti-Patterns

- Fabricating, buying or gating reviews. Fix: engineer authentic, voluntary advocacy from real customers.
- Asking for a review weeks after delivery or making the customer search for the platform. Fix: send a single-tap link by WhatsApp within 48 hours of the peak moment.
- Assuming top reviewers are the people who share. Fix: identify transmitters separately through listening, the NPS recommendation question and CRM data.
- Arguing with a negative reviewer in public. Fix: acknowledge without defensiveness and move resolution to WhatsApp or email.
- Measuring advocacy by follower counts. Fix: track review velocity, sentiment ratio, NPS, share rate, referral rate and platform spread.
- Stating the 80 % response-rate drop after 48 hours as fact. Fix: treat it as a legacy figure and verify before stating.
- Treating a missing consent record as a pass. Fix: mark the asset `not assessed` and hold it.

## References

- [eWOM programme method](references/ewom-programme-method.md): read when running the intake, applying GST, finding transmitters, planning review requests and incentives, handling negative reviews, setting metrics and platform priority, or building a programme from zero.
- [Social proof asset register](references/social-proof-asset-register.md): read when collecting, verifying, placing or governing testimonials, endorsements, certifications and other proof.
- [Word-of-mouth and referral design](references/word-of-mouth-and-referral-design.md): read when designing a word-of-mouth, superfan or referral programme and its tracking.
- [`meta-social-listening`](../../meta-analytics-ops/meta-social-listening/SKILL.md): read when monitoring unprompted brand mentions to find transmitters.
- [`playbook-reputation-management`](../../playbooks/playbook-reputation-management/SKILL.md): read when complaints or criticism are already live.
- [AGENTS.md](../../../AGENTS.md): read when routing to a neighbour skill or engine.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting request templates, response templates and referral messages.
<!-- dual-compat-end -->

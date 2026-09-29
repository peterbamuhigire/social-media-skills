---
name: direct-response-funnel-copy
description: 'Use when a client wants copy that sells: launch funnels, offer ladders, long sales letters or pages, email and WhatsApp sales sequences, webinar scripts and direct-mail letters; produces funnel copy with offer, proof and honest urgency, plus mailing-list selection; not for short ad headlines or hooks (use `ad-copy-and-hook-lab`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Direct-Response Funnel Copy Skill (Brunson + Kennedy)

Designs direct-response campaigns that produce measurable sales, applications or sign-ups, applying the value ladder and funnel logic (Brunson) and sales-letter discipline with the five propositions (Kennedy). This is a conversion-economics skill: every asset serves a funnel step with a target and a test.

<!-- dual-compat-start -->
## Use When
- The client wants a social, email or WhatsApp campaign that sells a course, coaching programme, event, membership or high-ticket service.
- We need a funnel that moves buyers from a free offer to a low-price entry and up to the core and premium offers.
- A long sales page or sales letter, webinar script or launch sequence needs writing with a clear offer, guarantee and a deadline that is true.
- Our funnel gets leads but few sales and we need to find the weak step and rewrite it.
- We are sending a direct mail letter, postcard or self-mailer and need the P.S., list selection by FRAT scoring and a cost-per-piece check.

## Do Not Use When
- `ad-copy-and-hook-lab` for short paid ad headlines, hooks and primary text.
- `email-copywriter` for a single newsletter or promotional email.
- `05-social-media-strategy` for brand-building work with no conversion goal.
- Stop where regulated claims (financial, health or education results) appear until legal review clears them; never use fake scarcity or invented testimonials.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Funnel-design answers: who the buyer is, where they gather, what attracts them, which offer the funnel sells | Client workshop or brief | Yes | Stop; ask the funnel-design questions before any copy is written. |
| Offer range: entry, core, back-end and any recurring option | Client or `biz-dev-pricing-menu` | Yes | Map what exists and state which ladder steps are missing; do not invent offers or prices. |
| Traffic today: owned list sizes, paid spend, organic reach | Client analytics and CRM | Yes | Mark the traffic plan `not assessed` and size the funnel test on stated assumptions. |
| Revenue goal (UGX or stated currency) and period | Client lead | Yes | Stop the revenue maths; deliver the funnel map without targets. |
| Current conversion data: ad → lead, lead → customer, average order value | Client export | No | Use labelled assumptions and replace them after the small-batch test. |
| Brand voice from `04-brand-voice-intake`; testimonials, results and guarantees with consent | Client source pack | Conditional | Hold any testimonial, result or guarantee without consent or evidence. |

## Workflow

1. Answer the funnel-design questions in writing; all copy is built against them ([funnel architecture](references/funnel-architecture-and-scripts.md) §1). Stop if the brief has no conversion goal, offer or call to action and route to `05-social-media-strategy`.
2. Work the revenue maths backwards from the goal to entry buyers and visitors; if the numbers cannot close, change the offer or model before writing.
3. Map the offer ladder (free → low-cost → core → premium → recurring) and give every post, email and broadcast one ladder step to serve; classify traffic as rented, borrowed or owned and plan the consented route into owned lists (WhatsApp opt-in in most East African cases).
4. Set the public voice: one persona stance with a true backstory, admitted weaknesses and a clear point of view, within the agreed brand voice.
5. Design the offer and Kennedy's five propositions before copy ([offer and price integrity](references/offer-proposition-and-price-integrity.md)).
6. Draft the main long-form asset with the persuasion arc ([long-copy system](references/long-copy-sales-letter-system.md) for drafting and editing), or the direct-mail letter with [direct-mail letters and packs](references/direct-mail-letters-and-packs.md); then the five-message story sequence or three-message follow-up, the post-purchase offer and, where relevant, the live-presentation script and two-call close.
7. Specify honest urgency (real deadlines and limits with reasons), run the [ethics filter](../references/direct-marketing-ethics-filter.md) and the [pre-release copy checklist](references/galletti-27-points.md); stop any asset that fails.
8. Plan the small-batch funnel test with pre-set targets per step before any spend is scaled; recover by fixing the weakest step and rerunning the test.

The full eleven-step method, script toolkit, offer and trust layer, integrations and East Africa notes are in [funnel method and toolkit](references/funnel-method-and-toolkit.md).

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Funnel-design answers, revenue maths and offer-ladder diagram (steps, prices, margin per step, upgrade triggers) | Client lead; `09-campaign-strategy` | Every funnel step has a target rate and volume; the ladder has at least three steps and a clear upgrade path. |
| Persona brief and main long-form asset (sales letter, video script or landing copy) | Client approver; landing-page builder | The asset follows the persuasion arc with the five propositions visible. |
| Launch sequence, ongoing nurture calendar (12 or more notes) and post-purchase offer script | `07-email-marketing-strategy`; WhatsApp broadcast owner | Scripted message by message, each tied to one ladder step. |
| Urgency specification with reasons and small-batch test plan with per-step targets | Client lead; `advertising/direct-response-economics` | At least two genuine urgency mechanics, each provable; targets set before spend. |
| Integration notes | `13-campaign-brief` | Name the assets, channels and test gates the campaign brief must carry. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Claim, testimonial and urgency register | Inline table | Every result, testimonial, deadline and limit has evidence, consent or a stated reason. |
| Ethics-filter and pre-release checklist record | Checklist per asset | Each asset shows a pass, or the failing item and the fix. |
| Revenue-maths workings | Table: traffic → leads → entry buyers → core and recurring buyers | Assumptions labelled; replaced by test data when available. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Sending broadcasts or mailings to a list also needs the list's consent basis on record.

## Degraded Mode

Without the funnel-design answers, offer range or revenue goal, return the narrowest qualified result and mark the affected checks `not assessed`. A funnel map with the weak step identified and draft copy for one ladder step can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The revenue maths cannot close at realistic conversion rates | Change the offer or model before writing any copy. | Polished copy for a funnel that cannot pay back. |
| Regulated claims (financial, health or education results) appear | Stop those claims until legal review clears them. | Regulatory action and client liability. |
| A hard-sell register conflicts with the voice agreed in `04-brand-voice-intake` | Keep the agreed voice; adapt the persuasion arc to it or return the conflict to the client. | Copy that damages the brand it sells for. |
| A deadline, limit or scarcity claim is not true and provable | Remove it; use only real mechanics with the reason why, and never extend a deadline publicly. | Fake scarcity and destroyed future urgency. |
| High-consideration or B2B buyer | Use the three-message follow-up (full offer → "did this reach you?" with the top objection answered → final honest notice). | A single send with no follow-up. |
| The funnel ends in a call, chat or meeting | Apply the consultative stages before, during and after the conversation. | Scripted pressure that loses the qualified buyer. |
| The deliverable is a direct-mail letter, postcard, self-mailer or letter-style email/WhatsApp broadcast to a list | Apply the four prerequisites, two-list process, Three Tells, letter structure, FRAT list scoring, $20 Rule and test design in [direct-mail letters and packs](references/direct-mail-letters-and-packs.md). | A mailing sent to the wrong list, in a format the transaction value cannot pay for, or rolled out untested. |
| Scaling is proposed before the small-batch test meets its targets | Hold the spend; fix the weakest step and rerun the test. | Paying for expensive qualified clicks into a broken funnel. |

## Quality Standards

- Funnel-design questions answered specifically; revenue maths worked backwards with a target rate and volume for every step.
- Offer ladder has at least three steps and a clear upgrade path; traffic sources are classified with a consented plan to move buyers into owned lists.
- Persona stance declared and consistent across assets.
- Main long-form asset follows the persuasion arc, adapted to channel and awareness, with the five propositions visible and an honest concession.
- Launch sequence scripted message by message.
- At least two genuine urgency mechanics, each with its reason.
- Small-batch funnel test planned before spend is scaled.
- Ethics filter passed for every asset; British English; names, figures and quotations verified; the `anti-ai-slop` gate passed.

## Anti-Patterns

- An "awareness campaign" with no conversion goal, offer or call to action. Fix: route to `05-social-media-strategy` or set the goal and offer first.
- Posts ending with a link but no explicit next step. Fix: state one action and what happens after it.
- Long copy with no honest concession, so it reads as hype. Fix: name the obvious weakness first ("We are not the cheapest; here is why").
- A value stack with no clear price moment, or values that were never real prices. Fix: substantiate each value and make the price moment explicit.
- Deadlines extended publicly. Fix: honour the deadline; it protects future urgency.
- Boosting a post "to see what happens" instead of building a funnel. Fix: plan the small-batch test with per-step targets.
- A premium offer given away free "for marketing", or a single send with no follow-up sequence. Fix: keep the premium priced and script the follow-up.

## References

- [Funnel method and toolkit](references/funnel-method-and-toolkit.md): read when you need the full eleven-step method, script toolkit, offer and trust layer, honest urgency mechanics, integrations, deliverable list or Uganda / East Africa notes.
- [Funnel architecture and scripts](references/funnel-architecture-and-scripts.md): read when making funnel-design decisions and drafting the persuasion arc, sequences, post-purchase offer, live-presentation closes or call close.
- [Long-copy sales letter system](references/long-copy-sales-letter-system.md): read when researching the reader, drafting, editing and testing any long sales asset or sequence.
- [Offer, proposition and price integrity](references/offer-proposition-and-price-integrity.md): read when designing the offer, the propositions, discount rules or the price section.
- [Consultative sales and positioning](references/consultative-sales-and-positioning.md): read when the funnel ends in a call, chat or meeting.
- [Direct-mail letters and packs](references/direct-mail-letters-and-packs.md): read when writing a direct-mail letter, insert, postcard or self-mailer, choosing a mailing list, checking cost per piece or designing a mail test.
- [Direct-mail pre-release copy checklist](references/galletti-27-points.md): read when finalising any direct-mail letter, sales letter, email or WhatsApp broadcast before release.
- [Direct-marketing ethics filter](../references/direct-marketing-ethics-filter.md): read before releasing every asset; the filter is mandatory.
- [`premium-commercial-writing`](../premium-commercial-writing/SKILL.md): read when direct-response copy must stay credible and premium-fee worthy.
- [`caption-writer`](../caption-writer/SKILL.md): read when only the promoting social posts are needed.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when financial, health or education claims appear.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting any asset.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

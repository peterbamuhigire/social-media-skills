---
name: direct-response-funnel-copy
description: Use when Direct-Response Funnel Copy Skill (Brunson + Kennedy) is needed to produce a publication-ready copy for social-media or digital-marketing work; use `caption-writer` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Direct-Response Funnel Copy Skill (Brunson + Kennedy)

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **publication-ready copy** and the supplied brief falls within direct-response funnel copy skill (brunson + kennedy).

## Do Not Use When
- Use `caption-writer` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Content brief, channel, audience, message, format and call to action | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified publication-ready copy; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Channel, format and audience commitment level are known | Choose the hook, structure and call to action native to that context. | Copy that could be pasted unchanged onto any channel or brand. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact publication-ready copy, consumer, market, channel and approval boundary; route to `caption-writer` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete publication-ready copy; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Publication-ready copy | Requester, client reviewer or delivery team | The publication-ready copy addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
| Decision and gap note | Approver or next workflow | Names the chosen route, evidence used, unresolved inputs and any action requiring authority. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Source/assumption register and completed release checklist | Inline table, checklist or linked source note | Every material claim, decision and unavailable check is traceable. |

## Quality Standards
- Preserve the domain guidance and East African market context below; replace it only when the requester names another market.
- Use British English unless the target language or market requires otherwise, and verify names, figures, quotations and platform rules before use.
- Make the key choice visible, cover failure and edge cases, and keep the result ready for its named consumer.
- Run the repository's `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested publication-ready copy, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [caption-writer](../caption-writer/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

## Overview
Design direct-response campaigns that produce measurable sales, applications or sign-ups — not just awareness. The skill applies named frameworks with brief attribution — the value ladder and funnel logic (Brunson), sales-letter discipline and the five propositions (Kennedy) — through the engine's own workflow, templates and ethics filter, across social campaigns, email, WhatsApp broadcasts and long-form landing content.

This is a **conversion-economics** skill: every asset serves a funnel step with a target and a test.

## Use When
- The client wants a social, email or WhatsApp campaign that *sells*, not one that only posts.
- Launching a course, coaching programme, high-ticket service, membership, event, webinar or book.
- Building a lead funnel that moves buyers up an offer ladder (free → low-cost → core → premium → recurring).
- Diagnosing a funnel that converts poorly (small-batch test, lead-progression review).
- Designing WhatsApp or email broadcast sequences for launch, evergreen selling or reactivation.
- High-ticket selling where awareness content alone will not close.

## Do Not Use When
- The brief is brand-building with no conversion goal (use `05-social-media-strategy` and `10-content-pillars`).
- A hard-sell register conflicts with the voice agreed in `04-brand-voice-intake`.
- Regulation forbids the claims involved (financial services, health, other regulated categories) until legal review clears them.

## Required Inputs
- **Funnel-design answers:** who the buyer is, where they gather, what attracts them, which offer the funnel sells.
- **Offer range:** entry offer, core offer, back-end and any recurring option (or state what is missing).
- **Traffic today:** owned list sizes, paid spend, organic reach.
- **Brand voice** from `04-brand-voice-intake`.
- **Revenue goal** (UGX or stated currency) and period.
- **Current conversion data:** ad → lead, lead → customer, average order value (or labelled assumptions).

## Workflow
1. **Answer the funnel-design questions** in writing; all copy is built against them ([funnel architecture](references/funnel-architecture-and-scripts.md) §1).
2. **Work the revenue maths backwards** from the goal to entry buyers and visitors; if the numbers cannot close, change the offer or model before writing.
3. **Map the offer ladder**; give every post, email and broadcast one ladder step to serve.
4. **Classify traffic** as rented, borrowed or owned and plan the consented route into owned lists (WhatsApp opt-in in most East African cases).
5. **Set the public voice**: one persona stance with a true backstory, admitted weaknesses and a clear point of view.
6. **Design the offer and propositions** before copy ([offer and price integrity](references/offer-proposition-and-price-integrity.md)).
7. **Draft the main long-form asset** with the persuasion arc ([funnel architecture](references/funnel-architecture-and-scripts.md) §3; [long-copy system](references/long-copy-sales-letter-system.md) for the drafting and editing stages).
8. **Draft the sequences**: a five-message story sequence after opt-in, or a three-message follow-up for high-consideration and B2B buyers; then ongoing notes.
9. **Draft the post-purchase offer** and, where relevant, the live-presentation script and two-call close.
10. **Specify honest urgency** (real deadlines and limits with reasons) and run the [ethics filter](../references/direct-marketing-ethics-filter.md); stop any asset that fails it.
11. **Plan the small-batch funnel test** with pre-set targets per step before any spend is scaled; recover by fixing the weakest step and rerunning.

## Script Toolkit (choose by job)

| Job | Pattern | Where it lives |
|---|---|---|
| Long sales letter, video script, webinar pitch, one-page broadcast | Persuasion arc: stop the reader → desire and stalled attempts → one promise → who is speaking → the mechanism → evidence → offer → value then price → risk reversal → honest urgency → result and action → after-action and P.S. | [Funnel architecture](references/funnel-architecture-and-scripts.md) §3 |
| Launch after opt-in | Five-message story sequence (welcome → story to the obstacle → the realisation → unexpected benefits → offer with real deadline) | Same, §3 |
| High-consideration or B2B follow-up | Three messages: full offer → "did this reach you?" with top objection answered → final honest notice (after Kennedy) | Same, §3; [long-copy system](references/long-copy-sales-letter-system.md) stage 7 |
| Ongoing nurture | Rotate a real incident, a lesson and a how-to, each with a light product link | Same, §3 |
| Straight after purchase | One named add-on, offered once, easy to decline | Same, §3 |
| Webinar or live session | Perfect Webinar structure (Brunson) with closing moves chosen by the buyer's objection | Same, §3 |
| High-ticket application | Two calls: qualify with four commitments (time, learning, investment, decision-maker), then confirm and close | Same, §3 |
| Call or meeting-led sale | Consultative stages before, during and after the conversation | [Consultative sales](references/consultative-sales-and-positioning.md) |

## Offer and Trust Layer
- **Propositions:** build Kennedy's five propositions (distinctive reason to choose, value beyond price, hard-to-refuse offer, safety, experience) into every long-form asset.
- **P.S. lines:** one to three, each with one job — restate offer and deadline, add a bonus, answer the top objection, or add a consented testimonial.
- **Honest selectivity:** state real qualification criteria ("for owners already selling weekly"); never manufacture exclusivity.
- **Price handling:** change the comparison, cost per use, substantiated value stacks, instalments (mobile money where permitted), discounts only in exchange for something, and an open admission of price.
- **Honest concession:** name the obvious weakness first ("We are not the cheapest; here is why") to pre-empt scepticism.

## Honest Urgency
Use only mechanics that are true and provable, with the reason why (see the ethics filter). Where genuine limits exist, combine two:
- A specific deadline (date, time, time zone).
- A proven limited quantity or cohort size.
- An early-response bonus with its own sub-deadline.
- A real consequence of waiting (the price does rise; the offer is withdrawn).
- A strong, honoured guarantee.

## Integration With Other Skills
| Skill | Integration |
|---|---|
| `04-brand-voice-intake` | The public persona must respect the brand voice |
| `05-social-media-strategy` | This skill builds the direct-response layer; strategy defines the awareness layer above it |
| `07-email-marketing-strategy` | Story, follow-up and nurture sequences slot in directly |
| `09-campaign-strategy` | This skill handles copy; campaign strategy handles the mix |
| `ai-whatsapp-chatbot-design` | WhatsApp is usually the main owned channel in East Africa |
| `biz-dev-proposal`, `biz-dev-reactivation-campaign` | The same methods apply to B2B proposals and win-back |
| `premium-commercial-writing` | Premium layer for proof density, value framing, price integrity and high-ticket tone |
| `advertising/direct-response-economics` | Break-even targets for the small-batch test |

## Quality Bar
- Funnel-design questions answered specifically.
- Revenue maths worked backwards; every funnel step has a target rate and volume.
- Offer ladder has at least three steps and a clear upgrade path.
- Traffic sources classified, with a consented plan to move buyers into owned lists.
- Persona stance declared and consistent across assets.
- Main long-form asset follows the persuasion arc, adapted to channel and awareness.
- Launch sequence scripted message by message.
- Five propositions visible in the long-form asset.
- At least two genuine urgency mechanics, each with its reason.
- Small-batch funnel test planned before spend is scaled.
- Ethics filter passed for every asset.

## Common Failures
- An "awareness campaign" with no conversion goal, offer or call to action.
- Posts ending with a link but no explicit next step.
- Long copy with no honest concession (reads as hype).
- A value stack with no clear price moment, or values that were never real prices.
- Deadlines extended publicly (destroys future urgency).
- Boosting a post "to see what happens" instead of building a funnel.
- A premium offer given away free "for marketing".
- A single send with no follow-up sequence.

## Deliverables
- Funnel-design answers.
- Revenue maths from traffic to entry buyers to core and recurring buyers.
- Offer-ladder diagram (steps, prices, margin per step, upgrade triggers).
- Persona brief (stance, backstory, admitted weaknesses, point of view, voice rules).
- Main long-form asset (sales letter, video script or landing copy).
- Launch sequence (five-message story sequence or three-message follow-up).
- Ongoing nurture calendar (12 or more notes).
- Post-purchase offer script.
- Urgency specification with reasons.
- Small-batch test plan with per-step targets.
- Integration notes for `13-campaign-brief`.

## References
- [Funnel architecture and scripts](references/funnel-architecture-and-scripts.md) — read when making funnel-design decisions and drafting the persuasion arc, sequences, post-purchase offer, live-presentation closes or call close.
- [Long-copy sales letter system](references/long-copy-sales-letter-system.md) — read when researching the reader, drafting, editing and testing any long sales asset or sequence.
- [Offer, proposition and price integrity](references/offer-proposition-and-price-integrity.md) — read when designing the offer, the propositions, discount rules or the price section.
- [Consultative sales and positioning](references/consultative-sales-and-positioning.md) — read when the funnel ends in a call, chat or meeting.
- [Direct-marketing ethics filter](../references/direct-marketing-ethics-filter.md) — apply to every asset before release.
- **Premium commercial writing layer:** see `../premium-commercial-writing/SKILL.md` when direct-response copy must stay credible and premium-fee worthy.

## Uganda / East Africa Notes
- **WhatsApp is usually the main owned channel.** Opt-in lists often outperform email for consumer offers in the region — an unverified practitioner heuristic; test against the client's own data.
- **Story sequences map well to a five-day WhatsApp broadcast:** voice notes for the story messages, text plus image for the benefit messages, and a combined text, voice and image call to action at the end.
- **Three-message follow-up** works on LinkedIn, email or WhatsApp for B2B decision-makers.
- **Test before you scale:** qualified clicks are expensive; do not scale a broken funnel.
- **Study what already works:** Kenyan, Nigerian and South African offer pages and ad libraries — structure only, never wording.
- **Cohort limits** ("50 seats, closes 30 November") tied to a real event or venue suit many Ugandan buyers — only when true.
- **Payment:** mobile money (MTN, Airtel) is expected; a card-only checkout is a likely barrier — test and measure rather than assume a figure.

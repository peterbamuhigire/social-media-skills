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
Design direct-response campaigns that convert — not just "build awareness." Applies Russell Brunson's DotComSecrets Ignite funnel framework (Secret Formula, Value Ladder, 3 traffic types, 7 phases of a lead, Star-Story-Solution, Perfect Webinar, Soap Opera sequence) and Dan Kennedy's sales letter sequencing and takeaway selling disciplines to social media campaigns, email sequences, WhatsApp broadcasts, and long-form landing content.

This is a **conversion-economics** skill. It assumes the campaign must produce measurable sales, applications, or signups — not impressions.

## Use When
- The client wants a social/email/WhatsApp campaign that *sells*, not one that just posts
- Launching an info-product, coaching programme, mastermind, high-ticket service, membership, event, webinar, or book
- Building a lead funnel that ascends prospects up a Value Ladder (free → low-ticket → high-ticket → continuity)
- Diagnosing why a current funnel converts poorly (apply the 100-Visitor Test and 7-phase framework)
- Designing WhatsApp / email broadcast sequences for launch, evergreen, or reactivation
- The client faces a high-ticket selling motion where awareness-only content is not enough

## Do Not Use When
- The primary brief is brand-building with no conversion goal (use `05-social-media-strategy` + `10-content-pillars` instead)
- Hard-sell direct-response tone conflicts with the brand voice already established in the `04-brand-voice-intake`
- Legal/regulatory constraints forbid direct-response claims (financial services, healthcare claims, regulated categories — always check)

## Required Inputs
- **Dream customer definition** — who, where, what bait, where you'll take them (Brunson's Secret Formula)
- **Offer**: front-end product/SLO + backend + continuity (or state if missing)
- **Current traffic sources** — owned list size, paid spend, organic reach
- **Brand voice and tone** — inherited from `04-brand-voice-intake`
- **Revenue goal** (absolute UGX/USD) and timeline
- **Conversion benchmarks** — current ad → lead rate, lead → customer rate, AOV

## Workflow
1. **Build the Secret Formula answer** (4 questions): dream customer / where / bait / where to take them. All subsequent copy is built against this.
2. **Reverse-engineer the revenue math** (Brunson): monthly revenue goal → continuity members OR backend sales needed → SLO sales needed (at ~30% upsell) → monthly traffic needed (at ~5% conversion).
3. **Map the Value Ladder** — free bait → front-end / SLO → core offer → premium → continuity. Every post/email/broadcast must serve one ladder rung.
4. **Classify each traffic source** — Controlled (paid), Uncontrolled (SEO/social reach), Owned (email/WhatsApp). **Goal of every campaign: convert Controlled/Uncontrolled → Owned.**
5. **Design the Attractive Character** (posture choice): Leader / Adventurer-Crusader / Reporter-Evangelist / Reluctant Hero. Pick one and apply consistently across backstory, parables, character flaws, polarity.
6. **Write the primary long-form asset** using the Star-Story-Solution script (see Scripts section below).
7. **Write the launch sequence** (Soap Opera 5-day → Seinfeld ongoing) or single-letter + 2 follow-ups (Kennedy).
8. **Write the upsell / OTO script** (Brunson 14-step bump).
9. **Specify scarcity / deadline mechanics** — the campaign dies without urgency (Kennedy Step 13).
10. **Plan the 100-Visitor Test** — test the funnel at small scale before scaling paid spend. Diagnose weakest step first.

## The Scripts
### Primary Long-Form Script — Star, Story, Solution (Brunson, 35 beats)
Use for: long-form sales letter, VSL, webinar pitch, broadcast one-pager, launch email #3.

```
1. Pattern Interrupt opening
2. Core Desire Questions ("have you ever wanted to…?")
3. Agitate Past Failures ("why hasn't it happened yet?")
4. Big Promise (the ONE thing they'll discover)
5. Intro the Attractive Character
6. High Drama opening line
7. Backstory & Wall
8. Identify the Problem
9. Epiphany / Declaration of Independence
10. The Path (what you tried)
11. First Signs of Success
12. Conspiracy (why you'd failed before)
13. Big Lie ("it's not your fault")
14. Common Enemy
15. Rapid Growth
16. Case Studies
17. Hidden Benefits
18. Formal Introduction of the offer
19. Pain + Cost of creation
20. Ease / Speed / "So" Benefits
21. Social Proof
22. Make the Offer
23. Build Value (stack)
24. Fake Price / "total value of $$$"
25. "If All's" Emotional Close
26. Reveal Real Price
27. Guarantee (logic)
28. Inject Scarcity (fear)
29. Future Pacing
30. CTA
31. Post-Selling
32. Take-Away / Warning
33. Close with Reminder
34. P.S. (restate, bonus, deadline)
35. P.P.S. (testimonial, handle top objection)
```

### Launch Sequence — Soap Opera (5 days)
| Day | Purpose | Content |
|---|---|---|
| 1 | Set the Stage | Welcome, intro Attractive Character, what's coming |
| 2 | High Drama → Backstory → Wall | Story, build bond, tease resolution |
| 3 | Epiphany → The ONE Thing | Ah-ha, tie to offer |
| 4 | Hidden Benefits | Unexpected upsides |
| 5 | Urgency CTA | Scarcity + call to buy |

### Kennedy Three-Letter Sequence (for high-consideration / B2B)
- **Letter 1** — full pitch, strong offer, deadline
- **Letter 2** — "Did you receive my letter?" + top objection handled + restate
- **Letter 3** — final deadline + strongest incentive + urgency

Response typically 2–3× a single send. Works in email, WhatsApp broadcast, SMS, direct mail.

### Ongoing — Seinfeld Emails (3 styles, cycled)
- **Episode** — "something happened today…" + product tie
- **Epiphany** — teaching moment + product tie
- **Educational** — direct how-to + product tie

### OTO Bump Script (immediately post-purchase)
14 steps, compressed: Confirm Decision → 3X/2X → Smart+Why → Question → Exclusive → Fast/Results/Speed → The ONE Thing → Future Cast → CTA → Guarantee → Value Stack → Scarcity → 2nd CTA → Testimonial Rush.

### Perfect Webinar Close (for webinar-driven campaigns)
Intro ("How to __ without __") → 3 Secrets (each with Reveal + Reframe) → The Stack close → 20+ mini-closes (If/All's, Money-is-good, Disposable Income, Money Replenishes, Break Old Habits, Money or Excuses, 2 Choices, Us vs Them, Hand Hold, Say Goodbye, Now & Later, Only Excuses, Reluctant Hero, If You Only Got, Close Close).

### Two-Step Phone Close (for high-ticket application funnels)
Set call: qualify → 4 commitments (Time, Teachable, Investment, Decision-Maker).
Close call: confirm commitments → finalise sale.

## Kennedy Overlays
Brunson gives the *structure*. Kennedy adds the *discipline*:

### Five Propositions (stack into every long-form asset)
1. USP (why choose you?)
2. UVP (why far more valuable than the price?)
3. Irresistible Offer (discount + premiums + fast-bonus + deadline penalty)
4. Unique Safety Proposition (guarantee, warranty, risk reversal)
5. Unique Experience Proposition (theme, ritual, celebrity, event)

### The Creative P.S.
The P.S. is the second-most-read element after the headline. Multiple P.S. lines (P.S., P.P.S., P.P.P.S.) each serving a distinct purpose:
- Restate offer + deadline
- Add a bonus
- Handle top objection
- Add a testimonial

### Takeaway Selling
Disqualify. "This isn't for everyone. Only apply if you can commit to X." Paradoxically increases demand.

### Beat the Price Bugaboo
- Apples-to-oranges comparison shift
- Cost-per-day / cost-per-use reframe
- Value-stack bundling
- Payment plan reframe
- Quid pro quo if discounting
- Damaging admission about price ("yes, this costs more; here's why")

### Damaging Admission
Concede the obvious weakness first. "I'm not the cheapest. My programme isn't for beginners." Pre-empts skepticism.

## Scarcity / Urgency Mechanics (Kennedy Step 13)
Every campaign needs at least two:

- Specific deadline (date + time + timezone)
- Limited quantity (with proof)
- Fast-action bonus (expires at a sub-deadline)
- Penalty for missing deadline (price rises / offer withdrawn)
- Risk reversal (strong guarantee = easier decision)

## Integration With Other Skills
| Skill | Integration |
|---|---|
| `04-brand-voice-intake` | Attractive Character must respect brand voice |
| `05-social-media-strategy` | This skill produces the *direct-response layer*; the strategy skill defines the *awareness layer* above it |
| `07-email-marketing-strategy` | Soap Opera + Seinfeld + 3-letter sequences slot directly in |
| `09-campaign-strategy` | Use together — this skill handles the copy; campaign strategy handles the mix |
| `ai-whatsapp-chatbot-design` | WhatsApp is the primary "owned traffic" channel in EA |
| `biz-dev-proposal`, `biz-dev-reactivation-campaign` | Same frameworks apply to B2B proposals and win-back |
| `premium-commercial-writing` | Apply as the premium quality layer for proof density, value framing, price integrity, and high-ticket tone control |

## Quality Bar
- Secret Formula is answered specifically (dream customer / where / bait / destination)
- Revenue math is reverse-engineered — every funnel step has a target conversion rate and volume
- Value Ladder has at least 3 rungs with a clear ascension path
- Traffic sources map to the Controlled / Uncontrolled / Owned framework, with a plan to convert to Owned
- Attractive Character is declared and consistent across assets
- Primary long-form asset follows Star-Story-Solution (35 beats, adapted)
- Launch sequence (Soap Opera or 3-letter) is scripted day-by-day
- 5 Propositions are visible in the long-form asset
- At least 2 scarcity mechanics are live
- 100-Visitor Test is planned before scaling spend

## Anti-Patterns
- "Brand awareness campaign" with no conversion goal, no offer, no CTA
- Social posts that end with a link but no explicit next step
- Long-form copy without damaging admission (reads as hype)
- Stack offer without reveal-price moment
- Deadlines that get extended publicly (kills future urgency)
- "We'll boost this post and see what happens" in place of a funnel
- Premium offering given away free "for marketing"
- Single-send launches with no follow-up sequence

## Outputs
- Completed Secret Formula (4 questions answered specifically)
- Reverse-engineered revenue math (traffic → SLO → continuity/backend)
- Value Ladder diagram (rungs, prices, margin per rung, ascension triggers)
- Attractive Character brief (archetype, backstory, character flaws, polarity, voice rules)
- Primary long-form asset (sales letter / VSL script / landing page copy)
- Launch sequence (5-day Soap Opera OR 3-letter Kennedy sequence)
- Seinfeld email calendar (12+ ongoing posts)
- OTO bump script
- Scarcity/urgency mechanics specification
- 100-Visitor Test plan with per-step conversion targets
- Integration notes for the campaign brief (`13-campaign-brief`)

## References
- **Brunson primary source**: See `../book-extractions/brunson-dotcomsecrets-ignite-extraction.md` — Secret Formula, Value Ladder, 3 traffic types, 7 phases of a lead, 100-Visitor Test, 9 Core Funnels, Inception Awareness levels, Star-Story-Solution script, OTO Bump, Perfect Webinar, 2-Step Phone Close, Soap Opera, Seinfeld, EA/Uganda adaptation notes.
- **Kennedy sales letter primary source**: See `../book-extractions/kennedy-ultimate-sales-letter-extraction.md` — the 28-step system, the Power of a Sequence, the Creative P.S., Beat the Price Bugaboo.
- **Kennedy sales success**: See `../book-extractions/kennedy-no-bs-sales-success-extraction.md` — Positioning-Not-Prospecting, 5 Propositions, Takeaway Selling, Damaging Admission, 6-Step Sales Process.
- **Kennedy price strategy**: See `../book-extractions/kennedy-no-bs-price-strategy-extraction.md` — discount discipline, price presentation, competing with free.
- **Premium commercial writing layer**: See `../premium-commercial-writing/SKILL.md` and its references when direct-response copy must stay credible, premium-fee worthy, and search/authority aware.

## Uganda / East Africa Notes
- **WhatsApp is the primary "traffic you own" channel.** WhatsApp broadcast lists outperform email by 3–10× on open rate and 2–5× on conversion for most consumer and prosumer offers.
- **Soap Opera maps to a 5-day WhatsApp broadcast** — use voice notes for Day 1 and Day 2 (storytelling), text+image for Day 3–4, and a combined text+voice+image CTA on Day 5.
- **Kennedy 3-letter sequence** works on LinkedIn InMail, email, or WhatsApp for B2B decision-makers.
- **100-Visitor Test is essential** — traffic in EA is expensive per qualified click. Don't scale a broken funnel.
- **Model what works** — study Kenyan/Nigerian/SA info-product pages and Facebook ad libraries before inventing. Brunson's "model, don't invent" discipline applies.
- **Scarcity mechanics** — Ugandan buyers respond especially well to cohort-based scarcity ("only 50 seats, closes 30 Nov") tied to an event or launch date.
- **Payment mechanics** — mobile money (MTN, Airtel Money) integration is non-negotiable; any funnel requiring card-only payment cuts conversion by 50%+.

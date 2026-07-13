---
name: email-copywriter
description: Use when Email Copywriter is needed to produce a publication-ready copy for social-media or digital-marketing work; use `caption-writer` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Email Copywriter

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **publication-ready copy** and the supplied brief falls within email copywriter.

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

## How to Use This Skill
Collect the Required Input below. Identify the email type. Generate complete, send-ready copy for the specified email type: subject lines, preheader, body, and CTA. Apply British English, mobile-first formatting, and the principle that every email must give value before it asks for anything.

Core principle: emails must earn the right to sell. Value first, sell second.

## Required Input
Ask for the following before writing:

- **Client business name** — the sender name as it appears in the inbox
- **Industry** — sector (e.g. retail, professional services, health, NGO)
- **Country / city** — default Uganda/East Africa
- **Primary goal** — what this email should achieve (awareness / relationship / conversion / reactivation)
- **Email type** — newsletter / promotional / welcome / reactivation
- **Audience segment** — leads / active customers / lapsed customers / VIPs
- **Key message** — the single most important thing this email communicates (one sentence)
- **Offer or content to feature** — what the email is about (product, discount, event, article, tip)
- **CTA desired** — what the reader should do (reply / click link / visit store / book a call)
- **Brand tone (3 words)** — from 04-brand-voice-intake
- **Any banned vocabulary** — words or phrases to avoid

## Writing Standards (All Email Types)
Apply these standards to every email generated:

- British English throughout: organisation, colour, programme, behaviour, recognise, analyse
- Sentences under 20 words on average — short sentences are easier to read on mobile
- Short paragraphs: 2–3 sentences maximum per paragraph; one idea per paragraph
- Active voice: "We offer" not "great service is offered by us"
- One CTA per email — never two competing actions
- Write to one person — not "dear subscribers" or "hello everyone"
- Mobile-first: assume most East African readers open on a smartphone; short paragraphs, generous white space
- No banned vocabulary: leverage, game-changing, revolutionary, paradigm shift, groundbreaking, delve, tapestry
- No filler openers: do not begin with "I hope this email finds you well", "We are pleased to announce", or "In today's digital world"
- Personal sign-off: not "Best regards" — use "Talk soon", "To your success", "Warmly", or a variation that fits the brand tone

## Email Type 1: Newsletter
**When to use:** Regular value-first communication — weekly, fortnightly, or monthly. Builds relationship and trust over time. Does not primarily sell.

**Output structure:**

**Subject lines: 3 options**
Generate 3 genuinely different approaches — not 3 variations of the same formula:
- Option A: Curiosity-driven (creates a knowledge gap the reader wants to fill)
- Option B: Direct (tells the reader exactly what is inside)
- Option C: Personal (first-person or conversational — feels like a message from a person, not a brand)

**Preheader text: 1 option**
The preheader appears next to the subject line in most email clients. It must complement the subject line — not repeat it. 40–90 characters. It should extend the subject line's promise or add new information.

**Opening: 2 sentences**
Warm, personal. Tell the reader what you are sharing and why — today, this week, right now. Do not open with a sales line.

**Feature section: 150–250 words**
The main value: a practical tip, insight, case story, or behind-the-scenes piece. One topic only. Use a subheading. Write it so the reader takes something useful away even if they never click.

**Secondary content (optional)**
One sentence + one link. A brief additional recommendation or resource. If there is nothing genuinely worth adding, omit this section.

**CTA: one action**
"Reply to this email and tell me [question]" works well for relationship-building. "Click here to [read / watch / download]" for resource-driven newsletters. Never a sales CTA in a newsletter unless the brand has built significant trust with this list.

**Sign-off**
Warm, personal. Sender's name. Optional: one line that sets up the next email ("Next week, I will share [topic]").

## Email Type 2: Promotional Email
**When to use:** Announcing a specific offer, product, event, or time-limited opportunity. Every promotional email must open with the reader's desire or problem — not the product.

**Output structure:**

**Subject lines: 3 options**
- Option A: Urgency-led (deadline, scarcity, or limited availability — only use if genuine)
- Option B: Benefit-led (what the reader gains — not what the product is)
- Option C: Curiosity-led (something surprising or unexpected about the offer)

**Preheader text: 1 option**
Complements the subject line. Adds a second reason to open.

**Opening hook: 2 sentences**
Acknowledge the reader's situation, desire, or problem. Lead with the benefit — not the product name. Do not open with "We are excited to offer you…"

**Offer presentation**
Four elements, each clearly stated:
- What is on offer (product, service, event, discount)
- What is included (scope, features, components)
- What is the price or saving
- Why now (what makes this the right moment)

**Social proof**
One sentence: a customer result, testimonial, or metric. Specific is more credible than vague. ("127 Kampala businesses have used this service since January" beats "our clients love us".)

**CTA button text: 3 options**
Action-led alternatives for the primary CTA button:
- Option A: e.g. "Claim your discount"
- Option B: e.g. "Reserve your place"
- Option C: e.g. "Get started today"

**Urgency note**
Include only if the deadline or scarcity is genuine. State it plainly: "Offer closes [date]" or "Only [N] places remaining." Do not manufacture false urgency.

**PS line**
Always include a PS. It is consistently the second most-read element of an email, after the subject line. Use it to restate the key benefit in a different way — or to address the reader's most likely objection.

## Email Type 3: Welcome Email (Single Email)
**When to use:** Sent immediately when someone joins the mailing list, signs up for a service, or downloads a lead magnet. Sets the tone for the entire relationship. This is the most-opened email in any sequence — write it accordingly.

**Output structure:**

**Subject lines: 3 options**
- Option A: Warm welcome (acknowledges who they are and what they signed up for)
- Option B: What to expect (previews the value they will receive)
- Option C: First gift (if there is a lead magnet or resource to deliver — lead with the gift)

**Opening**
Thank them. Be specific about what they signed up for — not a generic "thank you for subscribing." 2 sentences.

**What to expect**
Three bullets. Keep each to one line:
- What they will receive
- How often they will receive it
- Why it is useful to them specifically

**First gift**
Deliver the promised resource, lead magnet, or welcome offer. If there is a link, make it prominent. If there is a discount code, state it clearly and separately from the surrounding text.

**CTA**
Low-pressure. "Hit reply and tell me [one question about them]" builds immediate two-way engagement. Alternatively: "Click here to [access / read / watch]" if delivering a resource.

**Warm close**
First name sign-off. One sentence that expresses genuine welcome — not a legal disclaimer.

## Email Type 4: Reactivation Email
**When to use:** For subscribers who have not opened or clicked in 60 or more days. Goal: re-engage them with value, or let them leave cleanly. Do not send further promotional content to inactive subscribers without attempting reactivation first — it harms sender reputation.

**Output structure:**

**Subject lines: 3 options**
- Option A: "We miss you" approach — warm and personal
- Option B: "Are you still there?" — direct and honest
- Option C: "Last chance" — only if the list is being cleaned and this is genuinely the final email

**Opening**
Acknowledge the gap directly. Do not pretend nothing happened. Two sentences, honest and warm — not passive-aggressive.

**Re-engagement hook**
Something new or genuinely valuable they have missed since going quiet: a new product, an insight, a result, or a piece of content they would have found useful. Make it relevant to why they subscribed in the first place.

**Offer (optional)**
An exclusive reactivation offer — discount, free resource, early access — if relevant and authentic. Do not manufacture an offer purely to reactivate; it damages trust if it feels cynical.

**Opt-out option**
Include this explicitly and without guilt. Example: *"If you would rather not hear from us, you can unsubscribe below — no hard feelings. We would rather you leave than stay and find us irrelevant."* Including this increases trust, reduces spam reports, and keeps the list healthy.

## 12 Subject Line Formulas
Apply these when generating subject line options. Each formula is a different psychological approach — select the 3 most relevant to the email type and audience.

| # | Formula | Uganda/EA Example |
|---|---|---|
| 1 | The Question: *[Question your reader asks themselves]?* | "Is your business invisible on WhatsApp?" |
| 2 | The Number: *[N] ways to [benefit]* | "3 ways Kampala retailers are cutting delivery costs in 2025" |
| 3 | The Secret: *The secret to [outcome] most [industry] owners miss* | "The secret to retaining customers most salon owners miss" |
| 4 | The Warning: *Before you [common action], read this* | "Before you boost that post, read this" |
| 5 | The Story: *How [relatable person] [achieved result] in [timeframe]* | "How a Ntinda boutique doubled its WhatsApp enquiries in 6 weeks" |
| 6 | The Name-drop: *What [respected source] taught us about [topic]* | "What our top-performing client taught us about Facebook reach" |
| 7 | The Specific: *[Specific number] [specific thing] that [specific outcome]* | "12 captions that generated over 400 enquiries last quarter" |
| 8 | The Curiosity gap: *This one thing is keeping your business [problem]* | "This one thing is keeping your restaurant invisible on Instagram" |
| 9 | The Confession: *I was wrong about [commonly held belief]* | "I was wrong about posting every day" |
| 10 | The Exclusive: *For our [list name / VIP label] only:* | "For our Kampala clients only:" |
| 11 | The Timely: *[Month/season/event]: how to [action] before [deadline]* | "Back to school: how to reach parents before August rush" |
| 12 | The Direct: *[Exactly what is in the email, no frills]* | "Your September content calendar is ready" |

## Human Authenticity Gate
All content produced using this skill must pass through the `ai-content-humaniser` before client delivery. AI-generated or AI-assisted email copy must meet the Golden Rule: every email must look, feel, and sound as if it was written by the most skilled human copywriter with deep knowledge of the target audience and their relationship with the brand. Generic, flat, or culturally misaligned output is not acceptable regardless of how efficiently it was produced.

## Quality Criteria
- [ ] Subject line options are genuinely different in approach — not three versions of the same formula
- [ ] Preheader text complements the subject line without repeating it
- [ ] Opening earns attention before requesting or selling anything — no "we are pleased to announce" opener
- [ ] One clear CTA throughout — no competing actions in the same email
- [ ] British English throughout — organisation, colour, recognise, programme
- [ ] No banned vocabulary in any section
- [ ] Email is scannable on mobile — short paragraphs, no walls of text, white space between sections
- [ ] Tone matches the brand voice and suits the EA professional register — warm but not unprofessional
- [ ] Premium or high-ticket emails show proof, value, risk reduction, and one appropriately weighted CTA

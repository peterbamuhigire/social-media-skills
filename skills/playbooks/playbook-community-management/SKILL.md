---
name: playbook-community-management
description: Use when designing or improving a Community Management operating playbook with roles, ordered actions, controls and measures. Use platform skills for channel plans and strategy skills for upstream direction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Community Management Playbook

<!-- dual-compat-start -->
## Use When
- Build or improve a repeatable Community Management workflow for a client or delivery team.
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
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Community Management playbook plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| A comment creates safety, legal or credible crisis risk | Preserve evidence and escalate under the response matrix | Casual replies that worsen harm |
| Inputs and authority are complete | Produce an execution-ready playbook | Unowned actions and hidden assumptions |
| Evidence or tooling is incomplete | Produce the narrowest qualified draft and a gap list | Treating an unassessed check as passed |
| Action publishes, spends, contacts people or changes production state | Require explicit approval before action | Unauthorised external impact |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply the decision rules, preserve useful existing material and draft the Community Management playbook.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Community Management playbook | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
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

## Required Input

Collect the following before generating the playbook:

- **Client name** and business type (product/service/both)
- **Platforms managed** (select all that apply: Facebook, Instagram, WhatsApp Business, LinkedIn, X/Twitter, Google Business Profile, TikTok)
- **Business hours** (days and times, e.g. Monday–Friday 08:00–17:30 EAT)
- **WhatsApp Business number** — used as the escalation CTA in all templates
- **Client escalation contact** — name, title, and preferred channel (WhatsApp/email/phone) for Level 2+ issues
- **Brand tone** — pull from the completed 04-brand-voice-intake output; summarise in three adjectives if not available (e.g. warm, professional, direct)
- **Country/city** — defaults to Uganda/East Africa if not specified

---

## 1. Response Time SLAs by Platform

Populate this table for the client. Defaults are provided; adjust to business hours supplied.

| Platform | Comment Response Time | DM / Message Response Time | Escalation to Client |
|---|---|---|---|
| Facebook | 2 hours (business hours) | 4 hours (business hours) | Within 30 minutes of trigger |
| Instagram | 3 hours (business hours) | 4 hours (business hours) | Within 30 minutes of trigger |
| WhatsApp Business | N/A | 1 hour (business hours) | Within 30 minutes of trigger |
| LinkedIn | 24 hours | 24 hours | Within 2 hours of trigger |
| X / Twitter | 2 hours (business hours) | 2 hours (business hours) | Within 30 minutes of trigger |
| Google Business Profile | 24–48 hours | N/A | Within 2 hours of trigger |
| TikTok | 4 hours (business hours) | 4 hours (business hours) | Within 30 minutes of trigger |

**X/Twitter exception:** if a mention is trending, has been shared by a journalist or public figure, or has 50+ interactions, treat as Level 2 and escalate within 30 minutes regardless of time of day.

**Outside business hours:** Away messages and auto-replies acknowledge receipt. The WhatsApp Business away message must confirm: "We have received your message and will respond by [next business day opening time] EAT." Responses resume at the next business day opening. Do not leave customers without acknowledgement overnight.

---

## 2. Response Templates by Scenario

Use these templates as written. Replace bracketed fields with client-specific details. Adapt tone to match the brand voice supplied in Required Input.

### a. Positive Comment or Compliment
> "Thank you so much, [Name] — this genuinely made our day! We are glad you had a great experience. We look forward to welcoming you again. Feel free to tag a friend who would love [product/service]!"

### b. Product or Service Enquiry
> "Hello [Name], thank you for your interest! [Answer the specific question in one sentence if straightforward.] For full details and to place an order, please send us a WhatsApp message on [WhatsApp number] — our team will assist you promptly. We look forward to hearing from you!"

### c. General Complaint (Product or Service)
> "Hello [Name], thank you for letting us know. We are sorry to hear your experience did not meet the standard you deserved — and the standard we aim to deliver. Please send us a direct message [or WhatsApp us on [number]] with your order details so we can resolve this for you promptly. We want to make this right."

### d. Shipping or Delivery Complaint
> "Hello [Name], we are sorry to hear your order has not arrived as expected. We take delivery issues seriously. Please WhatsApp us directly on [number] with your order number and we will investigate and update you within [timeframe]. Thank you for your patience — we appreciate it."

### e. Offensive or Abusive Comment
> "We appreciate feedback and welcome all views on our page. However, we ask that all comments remain respectful. We have noted your concern and will address it through the appropriate channel. Please send us a direct message if you would like us to assist you."
> *(Moderation action: if the comment contains personal abuse, hate speech, or profanity, hide it after responding. Screenshot before hiding. Do not delete unless it violates platform community standards egregiously — document the action.)*

### f. Comment from a Competitor
> *(Do not engage publicly. Screenshot and forward to client noting the account. Delete only if the comment is clearly promotional spam — i.e. advertising their product/service in your comments. If it is a veiled negative comment, treat as a general complaint and take offline.)*

### g. Media or Press Enquiry
> "Hello [Name], thank you for getting in touch. For media enquiries, please contact [spokesperson name] directly on [email address]. They will be happy to assist you. Thank you."
> *(Flag to client immediately — this is an automatic escalation trigger regardless of level.)*

### h. Positive Review (Google / Facebook)
> "Thank you, [Name]! We truly appreciate you taking the time to share your experience. Reviews like yours mean the world to our team. We look forward to serving you again at [Client Name]!"

### i. Negative Review (Google / Facebook)
> "Hello [Name], thank you for taking the time to share your feedback. We are genuinely sorry to read about your experience — this is not the standard we hold ourselves to. Please contact us directly on [WhatsApp number] or [email] so we can understand what happened and make this right. We look forward to resolving this for you."
> *(Never argue publicly. Never contradict the reviewer's account in a public reply. The prospective customers reading the exchange are judging your professionalism, not the complaint itself.)*

---

## 3. Escalation Protocol

### When to Escalate to the Client Directly

Escalate immediately — within 30 minutes — for any of the following:

- A comment names a specific staff member negatively
- Any language suggesting legal action ("I will sue", "my lawyer", "consumer tribunal")
- Any identification as media or press ("I am a journalist", "I write for [outlet]")
- Any safety concern, emergency, or reference to physical harm
- Any comment that reaches 50+ likes or reactions and is negative in nature
- Level 2 or Level 3 crisis threshold reached (see playbook-crisis-communications)

### Escalation Process

1. Social media manager screenshots the comment/message in full (including timestamp and account name).
2. Sends screenshot to client via WhatsApp within 30 minutes of identification, with a one-line summary: "Level [X] issue — [brief description]. Holding response until your direction."
3. Holds all public responses until the client confirms the approach.
4. Client directs: approve drafted response, provide alternative wording, or take over response directly.
5. Social media manager logs the incident in the Monthly Community Health Scorecard.

---

## 4. Handling Negative Reviews: Four-Step Process

Apply this process to every negative review on Google Business Profile or Facebook.

**Step 1 — Acknowledge**
"We are sorry to read about your experience."

**Step 2 — Empathise**
"This is not the standard we aim to deliver at [Client Name]."

**Step 3 — Take Offline**
"Please contact us on [WhatsApp number] or [email] so we can resolve this for you directly."

**Step 4 — Do Not Argue**
Never contradict the reviewer publicly. Never ask them to prove their experience. Never explain why the situation was their fault. The audience reading the response is not the unhappy customer — it is every prospective customer researching the business. A calm, professional response to a negative review builds more trust than ten positive reviews left unanswered.

**Priority note:** responding to negative reviews publicly is more valuable than responding to positive ones. Prioritise accordingly.

---

## 5. Growing Community Engagement (Proactive Management)

Community management is not only reactive. Build engagement proactively with these methods.

### Conversation Starters
Post a genuine question for the community twice per week. Generate 10 question ideas tailored to the client's industry. Examples for a food business: "What is your go-to comfort meal on a rainy Kampala evening?" Examples for a fashion brand: "Which colour are you wearing most this season — and why?"

### Engagement Relationships
Identify 5–10 complementary businesses or professionals in the same city or sector with whom to engage consistently — genuine comments, shares, and reciprocal interaction. This builds organic reach without paid spend. Document the list and review monthly.

### Pinned Content
Use pinned posts or pinned comments to drive ongoing discussion on evergreen topics. A pinned question with weekly replies keeps older posts active in the algorithm.

### Community Milestones
Celebrate follower milestones (500, 1,000, 5,000), positive review counts, and business anniversaries publicly with the community. Acknowledge the community's role in the growth. This deepens loyalty and generates genuine engagement at no cost.

---

## 6. Monthly Community Health Scorecard

Complete this table at the end of each calendar month. Share with the client in the monthly report (see deck-monthly-report).

| Metric | Target | Actual | Rating |
|---|---|---|---|
| Followers — end of month | [Set target] | | G / A / R |
| Average engagement rate | ≥3% (EA benchmark) | | G / A / R |
| Comments received | — | | — |
| DMs / messages received | — | | — |
| Average response time | Within SLA above | | G / A / R |
| Reviews received (positive) | — | | — |
| Reviews received (negative) | — | | — |
| Issues escalated to client | — | | — |
| Notes | | | |

**Rating key:**
- **Green (G):** On or above target
- **Amber (A):** Within 10% below target — monitor
- **Red (R):** More than 10% below target — action required; note corrective steps

---

## Quality Criteria

Output meets production standard when it satisfies all of the following:

- Every response template is complete and ready to copy-paste — no generic filler text, no "[write something here]" placeholders
- SLA table is populated with the client's actual business hours and platforms, not the default placeholders
- Escalation protocol names the actual client contact and channel supplied in Required Input
- Negative review four-step process is explained with rationale, not just the steps
- Proactive engagement section includes at least 10 question ideas tailored to the client's specific industry and Ugandan/EA market context
- Monthly scorecard includes targets relevant to the client's current follower count and platform mix
- All templates use British English and match the brand tone adjectives supplied; no American spellings appear in any deliverable
- No out-of-scope elements are included (no graphic design, no paid ad guidance, no influencer contracts)

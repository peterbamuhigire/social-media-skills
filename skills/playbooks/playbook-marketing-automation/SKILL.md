---
name: playbook-marketing-automation
description: Use when designing or improving a Marketing Automation operating playbook with roles, ordered actions, controls and measures. Use platform skills for channel plans and strategy skills for upstream direction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Marketing Automation Playbook

<!-- dual-compat-start -->
## Use When
- Build or improve a repeatable Marketing Automation workflow for a client or delivery team.
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
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Marketing Automation playbook plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| A journey trigger is ambiguous or untested | Keep the step manual until the trigger and rollback are proven | Wrong-message automation |
| Inputs and authority are complete | Produce an execution-ready playbook | Unowned actions and hidden assumptions |
| Evidence or tooling is incomplete | Produce the narrowest qualified draft and a gap list | Treating an unassessed check as passed |
| Action publishes, spends, contacts people or changes production state | Require explicit approval before action | Unauthorised external impact |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply the decision rules, preserve useful existing material and draft the Marketing Automation playbook.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Marketing Automation playbook | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
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
4. **Primary goal** — what automation must achieve (convert leads to enquiries, nurture to first purchase, re-engage lapsed customers, onboard new clients)
5. **Current follow-up method** — how the business currently follows up with leads (manual calls, sporadic emails, nothing formal)
6. **Primary communication channel** — email, WhatsApp, or both
7. **Technology in use** — any CRM, email platform, or automation tool already deployed
8. **Sales cycle length** — how long from first enquiry to purchase on average

---

## What Marketing Automation Is

Marketing automation is a system that sends the right message to the right person at the right time — automatically, triggered by that person's behaviour. The alternative — manual follow-up — is inconsistent, does not scale, and depends on the availability and memory of individual team members. Automation does not replace human relationships; it ensures that no lead falls through the gaps between human touchpoints.

---

## The Four Trigger Categories

Map the client's business against all four categories before designing any sequences. A trigger event that is skipped now becomes a gap in the nurture system later.

### 1. Acquisition Triggers
Events that create a new contact in the system.

| Trigger | Response |
|---|---|
| Form submission (website, landing page) | Immediate confirmation + lead magnet delivery |
| Lead magnet download | Welcome sequence begins |
| First WhatsApp message | Greeting message + sequence entry |
| Webinar or event registration | Registration confirmation + pre-event nurture |
| Referral introduction | Personalised welcome acknowledging the referral source |

### 2. Engagement Triggers
Events that indicate the contact is active and interested.

| Trigger | Response |
|---|---|
| Email opened but not clicked | Follow-up within 48 hours with a different angle on the same topic |
| Link clicked in email | Send deeper content on the specific topic clicked |
| Webinar attended | Post-event follow-up sequence (within 24 hours) |
| Webinar registered but did not attend | "You missed it" sequence with recording access |
| Pricing page visited (if trackable) | High-intent follow-up — offer consultation or next step |

### 3. Purchase Triggers
Events that confirm a transaction has occurred.

| Trigger | Response |
|---|---|
| First purchase | Onboarding sequence — confirm order, set expectations, introduce the relationship |
| Repeat purchase | Loyalty acknowledgement — thank the customer and reinforce the relationship |
| Abandoned cart / lapsed enquiry | Re-engagement sequence — 3 messages over 7 days with decreasing urgency |
| Subscription or retainer signed | Welcome + onboarding pack delivery |

### 4. Lifecycle Triggers
Events triggered by the passage of time rather than an action.

| Trigger | Response |
|---|---|
| 30 days of inactivity (no opens, no clicks) | Re-engagement sequence |
| 90 days since last purchase | Win-back sequence |
| Anniversary of first purchase | Relationship moment — thank the customer, share what has changed |
| Subscription renewal approaching | Renewal reminder sequence (14 days, 7 days, 1 day before) |

---

## Sequence Architecture

Apply this timing structure to all new sequences. Adapt the content for the specific trigger and audience; hold the timing model constant.

| Stage | Timing | Purpose |
|---|---|---|
| Trigger event | Immediate (within 5 minutes) | Welcome / confirmation / deliver the promised resource |
| Early value | Day 1–3 | The lead magnet, the follow-up resource, or the post-event material |
| Deeper value | Day 4–7 | A related insight, case study, or practical tip — no promotion |
| Soft introduction | Day 8–14 | Introduce the next logical offer — not a hard sell; a signpost |
| Direct offer | Day 15–30 | A specific invitation to take the next step; clear CTA |
| Steady-state | Day 31 onwards | Educational content, product updates, community content — see `playbook-email-funnel` |

---

## WhatsApp Automation for EA Clients

For most clients in Uganda and East Africa, WhatsApp automation runs alongside or instead of email automation. Design both paths wherever possible; allow the contact to self-select their preferred channel.

**WhatsApp automation requires one of:**
- WhatsApp Business App with manual quick replies (suitable for low-volume, single-operator businesses)
- WhatsApp Business API via an approved Business Solution Provider — required for automated sequences, broadcast scheduling, and multi-agent inbox management

**Approved platforms for EA context:**
- Twilio (WhatsApp API)
- Vonage (WhatsApp API)
- 360dialog (API access, used by many African businesses)
- Brevo (combined email and WhatsApp automation)

**WhatsApp sequence structure:**
Trigger → Auto-reply confirmation (within 5 minutes) → Day 1 value message → Day 3 follow-up → Day 7 soft offer → Day 14 direct ask. Keep WhatsApp messages shorter than emails: 50–150 words per message, one clear point, one link or CTA.

Note: broadcast automation at scale requires the WhatsApp Business API. The free WhatsApp Business App does not support scheduled broadcasts or automated sequences beyond the three built-in messages (greeting, away, quick replies).

---

## Message Timing Rules

Apply without exception. Automated messages that arrive at 2am or during weekends feel intrusive and increase opt-out rates.

1. **Business hours only** — all automated messages must be queued for delivery between 8am and 8pm in the recipient's local time zone (EAT for Uganda, Kenya, Tanzania)
2. **Minimum 24-hour gap** — no two automated messages in any sequence may be sent within 24 hours of each other
3. **Human handover on reply** — if the contact replies to any automated message at any point, remove them from the automated sequence immediately and assign the conversation to a human within 2 hours. Automation that continues after a human reply is experienced as disrespectful and robotic.

---

## Personalisation Tokens

Use merge fields to personalise every automated message. Minimum personalisation for every sequence:

- First name (required — never send an automated message addressed to "Hello there" if the first name is captured)
- Company name (B2B sequences)
- Specific product or content engaged with (referencing what the contact actually did)
- Location / city (where captured)

Personalised subject lines increase email open rates by 20–40% (Zahay et al., 2024). In WhatsApp messages, beginning with the first name increases read rate and reply rate.

---

## Quarterly Sequence Review

Automation sequences are not "set and forget." Review every active sequence quarterly.

**Review checklist:**
- Remove or update any offer that has expired or changed
- Update case studies and client examples with more recent results
- Check all links — broken links in automated sequences create poor first impressions at scale
- Review open rates and click rates for each message in the sequence — a message with consistently low engagement should be rewritten or removed
- Compare sequence conversion rates quarter on quarter

---

## Output: Marketing Automation Brief

Generate the following for the client:

1. **Trigger map** — all four trigger categories mapped against the client's business model; mark which triggers are in scope for the first phase
2. **Sequence architecture** — one fully written sequence per in-scope trigger, following the timing model above
3. **WhatsApp sequence** — parallel WhatsApp version of the primary sequence (if the client uses WhatsApp as a primary channel)
4. **Personalisation token list** — all merge fields required for each sequence; confirm which are captured in the current sign-up flow
5. **Platform recommendation** — one recommended tool with setup notes
6. **Quarterly review schedule** — dates for the first four quarterly reviews

---

## Quality Criteria

Output meets the standard when:

1. Trigger events are fully mapped before sequence content is written — the automation logic is confirmed before a single message is drafted
2. All four trigger categories are assessed for relevance to the client's business; sequences are designed only for triggers that are actually in use
3. WhatsApp automation path is designed alongside email path for all EA clients — do not default to email-only
4. All automated messages are timed for delivery within local business hours (8am–8pm EAT)
5. Manual handover protocol is in place for contacts who reply to any automated message — the team knows the process before the first sequence goes live
6. Personalisation tokens are tested and confirmed functional in the chosen platform before any sequence is activated
7. Quarterly review schedule is booked and confirmed — sequences without a review date will decay and go stale

---

## References

Hanlon, A. and Tuten, T. (2022) *The SAGE Handbook of Social Media Marketing*. SAGE Publications.

Pidsley, R. (2023) *Social Media Marketing for Business: Scaling an Integrated Social Media Strategy Across Your Organisation*. Kogan Page.

Zahay, D. et al. (2024) *Digital Marketing Management: A Handbook for the Current (or Future) CEO*. 3rd edn. Business Expert Press.

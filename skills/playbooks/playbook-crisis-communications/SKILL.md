---
name: playbook-crisis-communications
description: Use when designing or improving a Crisis Communications operating playbook with roles, ordered actions, controls and measures. Use platform skills for channel plans and strategy skills for upstream direction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Crisis Communications Playbook

<!-- dual-compat-start -->
## Use When
- Build or improve a repeatable Crisis Communications workflow for a client or delivery team.
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
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Crisis Communications playbook plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| Facts are incomplete during a live incident | Issue a verified holding statement and set the next update time | Speculation under pressure |
| Inputs and authority are complete | Produce an execution-ready playbook | Unowned actions and hidden assumptions |
| Evidence or tooling is incomplete | Produce the narrowest qualified draft and a gap list | Treating an unassessed check as passed |
| Action publishes, spends, contacts people or changes production state | Require explicit approval before action | Unauthorised external impact |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply the decision rules, preserve useful existing material and draft the Crisis Communications playbook.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Crisis Communications playbook | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
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

- **Client name** and business type
- **Social media manager** — name and WhatsApp/phone number
- **Client approver** — name, title, and WhatsApp/phone number (the person who approves all public statements during a crisis)
- **PR or legal contact** — name and contact details (note if not applicable; advise the client to identify one before a crisis occurs)
- **WhatsApp number** for crisis-related customer contact (may be the same as main business number)
- **Platforms in scope** (Facebook, Instagram, WhatsApp Business, LinkedIn, X/Twitter, TikTok, Google Business Profile)
- **Country/city** — defaults to Uganda/East Africa if not specified

---

## Foundational Principle

Apply the acknowledge → investigate → update cadence to every crisis at every level. The first response acknowledges the issue and signals seriousness. The second response (4–8 hours later) confirms an investigation is under way and provides any available facts. The third response (within 24 hours) provides resolution or a detailed update. Never go silent between updates.

---

## 1. Crisis Severity Classification

### Level 1 — Minor Complaint or Negative Post

**Definition:** An unhappy customer posts publicly. Under 50 interactions. No media involvement. Isolated to one or two posts.

**Response:** Community management team handles within 2 hours. Use the standard complaint template from playbook-community-management. Take the conversation offline via DM or WhatsApp. No public statement required.

**Escalation:** Notify client within 4 hours by WhatsApp. No pause to the content calendar. Monitor for 24 hours in case the post gains further traction.

---

### Level 2 — Viral Negative Post or Media Attention

**Definition:** A post has reached 200+ interactions or is spreading via shares, OR a media account (journalist, news outlet, public figure) has shared or commented on it. Could include a local journalist tweeting about the brand.

**Response:** Pause all scheduled posts immediately. Social media manager alerts client within 30 minutes. Client and social media manager prepare a holding statement together within 1 hour of identification. Do not post any further content until the holding statement is agreed.

**Escalation:** Client leads all public responses from this point. Social media manager executes, monitors, and tracks all mentions and interactions. Social media manager does not craft or publish responses independently.

---

### Level 3 — Major Reputational Threat

**Definition:** National or regional media coverage, significant public figure or government official involved, legal implication or allegation, public safety issue, or criminal allegation against the company or a named employee.

**Response:** Pause all social activity across all platforms immediately. Client contacts PR counsel and/or legal counsel before any public statement is issued. A holding statement is issued within 2 hours. 24-hour monitoring is put in place. Social media manager does not act independently under any circumstances.

**Escalation:** Client and external counsel lead all communication. Social media manager is operational support only — monitoring, reporting, and executing approved responses.

---

## 2. Response Protocol by Level

### Level 1 Response Timeline

**First 30 minutes:**
- [ ] Community manager identifies the complaint
- [ ] Assess interaction count — confirm it is under 50
- [ ] Draft a response using the standard complaint template
- [ ] Publish the response and take the conversation offline

**First 2 hours:**
- [ ] Monitor the post for further activity
- [ ] Confirm the customer has been contacted via DM or WhatsApp
- [ ] Note the incident in the community management log

**First 24 hours:**
- [ ] Notify client with a brief summary via WhatsApp
- [ ] Confirm resolution or note if still in progress
- [ ] Continue monitoring the post for 24 hours post-response

---

### Level 2 Response Timeline

**First 30 minutes:**
- [ ] Social media manager identifies the escalation trigger (200+ interactions or media involvement)
- [ ] Screenshot all posts, shares, and comments — timestamped
- [ ] Pause all scheduled content immediately (Buffer/Hootsuite draft mode — do not delete content)
- [ ] WhatsApp the client approver: "Level 2 crisis identified. [One-sentence summary]. Awaiting your direction. Holding all responses."
- [ ] Do not publish anything

**First 2 hours:**
- [ ] Client and social media manager agree on the holding statement (use template below)
- [ ] Social media manager publishes the holding statement across all affected platforms
- [ ] Set a monitoring window — check every 30 minutes for new developments
- [ ] Social media manager tracks all mentions, shares, and new comments in a live log

**First 24 hours:**
- [ ] Client and social media manager issue a second update with any new facts or resolution steps
- [ ] Continue monitoring all platforms
- [ ] If media involvement increases, re-classify to Level 3
- [ ] Do not resume normal content calendar until client approves

---

### Level 3 Response Timeline

**First 30 minutes:**
- [ ] Social media manager pauses all social activity across all platforms
- [ ] Screenshots all content — posts, comments, shares, media articles
- [ ] Contacts client approver by phone (not WhatsApp only) immediately
- [ ] Does not publish anything, does not respond to any comments

**First 2 hours:**
- [ ] Client contacts PR and/or legal counsel
- [ ] Holding statement is drafted by client and counsel (use template below as starting structure only)
- [ ] Social media manager publishes the approved holding statement — no edits without approval
- [ ] Monitoring begins — social media manager reports to client every 30 minutes

**First 24 hours:**
- [ ] Client and counsel issue a full update or resolution statement
- [ ] Social media manager continues 24-hour monitoring and logs all activity
- [ ] No normal content resumes until client gives explicit approval
- [ ] Social media manager compiles a full incident log for the post-crisis review

---

## 3. Holding Statement Templates

### Level 1 Holding Statement
> "Thank you for bringing this to our attention. We are sorry to hear about your experience. Please send us a direct message so we can resolve this for you."

### Level 2 Holding Statement
> "We are aware of the concern raised about [topic]. We take this seriously and are looking into it urgently. We will share an update within [timeframe — recommend 4–6 hours]. If you have been personally affected, please contact us directly on [WhatsApp number]."

### Level 3 Holding Statement
> "We are aware of the reports circulating regarding [topic]. We are taking this very seriously and are working urgently to understand the full situation. We will provide a comprehensive update by [specific date and time]. [If applicable: we have engaged the relevant authorities.] We appreciate your patience and understanding."

**Customisation note:** Replace bracketed fields with specifics before publishing. Never publish a holding statement with placeholder text visible. The client approver must sign off on every Level 2 and Level 3 statement before it goes live.

---

## 4. What NOT to Do in a Crisis

Follow these rules without exception during any Level 2 or Level 3 event:

- **Do not delete negative comments.** Deletion signals guilt, inflames the audience, and creates a Streisand effect — the post will be screenshotted and shared more widely. Delete only clear hate speech or harassment, and document each deletion.
- **Do not go silent.** Silence reads as guilt or indifference. Even if you have no resolution yet, a holding statement is better than nothing.
- **Do not be defensive or blame the customer publicly.** The audience is not only the complainant — it is every potential customer reading the exchange.
- **Do not use humour in a serious crisis.** Levity in a Level 2 or Level 3 situation is almost always misread and amplifies the reputational damage.
- **Do not post normal content while the crisis is unfolding.** A cheerful promotional post during a public controversy is tone-deaf and will be screenshot and mocked.
- **Do not let multiple people respond differently.** Agree one voice and one message before any statement goes out. Contradictory responses are more damaging than a delayed response.
- **Do not over-promise on resolution timelines.** If you cannot resolve in 24 hours, say "we are committed to resolving this and will provide updates as we have them." Do not say "we will fix this today" if you cannot.

---

## 5. Platform-Specific Crisis Actions

### All Platforms
Pause all scheduled content immediately on identification of Level 2 or Level 3. Use Buffer or Hootsuite draft mode — do not delete scheduled content, only pause it. Resume only with client approval.

### Facebook
For Level 3: consider enabling the strong profanity filter (Settings → Privacy → Profanity Filter → Strong). For specific posts under heavy negative attack, comments can be turned off on that post via the three-dot menu. Use this only when comments have become abusive or coordinated — not to suppress legitimate criticism.

### Instagram
Use the restricted words list (Settings → Privacy → Hidden Words) to automatically hide comments containing abusive language. Hide — not delete — specific comments that are threatening or contain personal abuse. Document all hidden comments.

### WhatsApp Business
Pause all pending broadcast messages immediately. Update the away message to: "We are aware of the current situation and are working to address it. For urgent enquiries, please message us here and we will respond as soon as possible."

### X / Twitter
Mute notifications from the specific viral post to allow focused monitoring without being overwhelmed. Do not deactivate the account — deactivation reads as fleeing and amplifies the story. Monitor all mentions via the search function for the brand name, not just notifications.

### LinkedIn
Level 2 and 3 crises rarely originate on LinkedIn in the East African context but can spread there. Monitor comments on all recent posts. Pause any scheduled articles or posts.

---

## 6. Post-Crisis Review

Conduct this review 48–72 hours after the crisis is resolved. The social media manager compiles it; the client approves it.

Answer these questions in writing:

1. What triggered the crisis — what happened and when?
2. At what point was it identified, and by whom?
3. Could it have been prevented? If yes, what would have prevented it?
4. How did the response go? What worked well?
5. What did not work — slow response, unclear ownership, missing contact details?
6. What needs to change in policies, products, or communications as a result?
7. Are there any outstanding customer issues still to resolve?

Document the answers in a one-page incident report. File it. Use it to update this playbook annually.

---

## 7. One-Page Crisis Quick Card

Generate this as a standalone section the client can print and keep accessible. Fill in all fields with the client's actual details before delivering.

---

**[CLIENT NAME] — SOCIAL MEDIA CRISIS QUICK CARD**

### Crisis Levels at a Glance

| Level | Trigger | First Action |
|---|---|---|
| 1 — Minor | Under 50 interactions; no media | Community manager responds within 2 hours |
| 2 — Viral | 200+ interactions OR media involved | Pause all posts; alert client within 30 minutes |
| 3 — Major | National media, legal, safety, public figure | Pause everything; call client and counsel immediately |

### First 30-Minute Checklist (Level 2 / 3)
- [ ] Screenshot everything with timestamps
- [ ] Pause all scheduled content (Buffer/Hootsuite draft mode)
- [ ] WhatsApp or call client approver immediately
- [ ] Publish nothing until client approves
- [ ] Begin monitoring log

### Holding Statements (Ready to Use)

**Level 1:** "Thank you for bringing this to our attention. We are sorry to hear about your experience. Please send us a direct message so we can resolve this for you."

**Level 2:** "We are aware of the concern raised about [topic]. We take this seriously and are looking into it urgently. We will share an update within [timeframe]. Please contact us on [WhatsApp number] if you have been personally affected."

### Escalation Contacts

| Role | Name | WhatsApp / Phone |
|---|---|---|
| Social Media Manager | [Name] | [Contact] |
| Client Approver | [Name] | [Contact] |
| PR / Legal Contact | [Name] | [Contact] |

### What NOT to Do
- Do not delete comments (screenshots first if you must)
- Do not go silent — always issue a holding statement
- Do not post normal content during a crisis
- Do not blame the customer publicly
- Do not let multiple people respond with different messages

---

## Quality Criteria

Output meets production standard when it satisfies all of the following:

- All three crisis levels are defined with clear, quantifiable triggers — no vague language such as "significant" without a threshold
- Each level has a distinct, actionable timeline checklist in tick-box format, not prose instructions
- All three holding statement templates are complete, customised with client details, and contain no visible placeholder text before delivery
- The "What NOT to Do" section includes the rationale for each prohibition, not just the rule
- Platform-specific actions are tailored to the platforms listed in Required Input — unused platforms are omitted
- The Crisis Quick Card is formatted as a genuinely standalone, printable section — not a summary of the main document
- Post-crisis review questions are specific enough to produce a usable incident report, not generic reflection prompts
- All content uses British English; no American spellings appear anywhere in the deliverable

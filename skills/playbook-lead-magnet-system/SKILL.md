---
name: playbook-lead-magnet-system
description: >
  Guides the design, placement, and optimisation of lead magnets to build owned email
  and WhatsApp subscriber lists. Invoke when a client needs to grow a permission-based
  audience asset — replacing reliance on platform algorithms with a list the business
  controls. Source: Bly (2018) The Digital Marketing Handbook.
---
# Lead Magnet System Playbook

<!-- dual-compat:start -->
## Use when
- Guides the design, placement, and optimisation of lead magnets to build owned email and WhatsApp subscriber lists. Invoke when a client needs to grow a permission-based audience asset — replacing reliance on platform algorithms with a list the business controls. Source: Bly (2018) The Digital Marketing Handbook.
- Use this skill when it is the closest match to the requested deliverable or workflow.

## Do not use when
- Do not use this skill for graphic design, video production, software development, or legal advice beyond the repository's stated scope.
- Do not use it when another skill in this repository is clearly more specific to the requested deliverable.

## Workflow
1. Collect the required inputs or source material before drafting, unless this skill explicitly generates the intake itself.
2. Follow the section order and decision rules in this `SKILL.md`; do not skip mandatory steps or required fields.
3. Review the draft against the quality criteria, then deliver the final output in markdown unless the skill specifies another format.

## Anti-Patterns
- Do not invent client facts, performance data, budgets, or approvals that were not provided or clearly inferred from evidence.
- Do not skip required inputs, mandatory sections, or quality checks just to make the output shorter.
- Do not drift into out-of-scope work such as code implementation, design production, or unsupported legal conclusions.

## Outputs
- A structured markdown document, plan, playbook, or strategy ready for client-facing or internal use.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Inputs

Ask for the following before generating any output:

1. **Business name** — trading name of the client
2. **Industry** — sector and specific niche (e.g. financial services / personal loans)
3. **Country / city** — default is Uganda/East Africa
4. **Primary goal** — what the client wants subscribers to ultimately do (purchase, book, enquire)
5. **Current list size** — email subscribers and WhatsApp contacts (if any)
6. **Existing lead magnet** — describe any current free offer or sign-up mechanism in use
7. **Primary capture channel** — website, social media bio, WhatsApp, or a combination

---

## What Is a Lead Magnet

A lead magnet is a free, high-value offer exchanged for a prospect's contact details — an email address, WhatsApp number, or both. Its purpose is to build an owned audience asset that no platform algorithm, account suspension, or policy change can remove from the business.

**Bly's Lead Magnet Specificity Formula (Bly, 2018):**

A lead magnet must satisfy all four criteria:

| Criterion | What It Means |
|---|---|
| Specific outcome | Promises one concrete result, not a vague benefit |
| High perceived value | The audience would pay for this if it were not free |
| Instantly deliverable | Received immediately — no waiting |
| Unique expertise | Demonstrates knowledge only this business can offer |

Generic sign-up prompts ("subscribe to our newsletter") fail because they offer no exchange of value. The audience has no reason to hand over their contact details in return for updates they did not ask for.

---

## Six Lead Magnet Formats

Select the format that best matches audience behaviour and client capability. Produce one format at a time — do not attempt multiple formats simultaneously.

**1. Special Report or White Paper**
Detailed research or analysis on a topic the audience is actively investigating. Best for B2B clients and professional services. Length: 5–12 pages. Example: *The 2025 Uganda SME Digital Marketing Report: What Is Working and What Is Not.*

**2. Checklist**
A step-by-step process the audience can apply immediately. Best for practical, action-oriented audiences. Length: one page. Example: *The 10-Step WhatsApp Business Setup Checklist for Ugandan Retailers.*

**3. Video Training**
A recorded demonstration of a skill, tool, or process. Best for audiences who prefer visual learning. Length: 10–20 minutes. Example: *How to Set Up a Facebook Business Page in Under 20 Minutes.*

**4. Quiz or Assessment**
A personalised diagnosis of the audience's current situation, delivered as a scored result. Best for clients whose audience needs to understand their own gap before purchasing. Example: *Is Your Business Ready for Social Media Advertising? Take the 5-Minute Assessment.*

**5. Free Tool or Template**
A plug-and-play resource that saves the audience significant time. Best when the client's expertise is practical and process-driven. Example: *The Monthly Social Media Content Calendar Template (Excel/Google Sheets).*

**6. Webinar or Live Workshop**
An interactive session with Q&A. Highest perceived value of any format; requires the most preparation. Best for established clients with an existing audience ready to attend live. Example: *Free 60-Minute Workshop: How to Get Your First 10 Clients Using WhatsApp.*

---

## Placement Sequence

Implement placements in this order. Do not drive paid traffic to the lead magnet until all four placements are live.

**Position 1 — Hero Section (above the fold)**
The lead magnet offer must appear at the top of the website homepage without scrolling. Include: headline stating the specific outcome, one-sentence description, an image of the lead magnet (cover mockup or screenshot), and a single input field (email or WhatsApp number).

**Position 2 — Sidebar or Pop-up**
Trigger: after 30 seconds on page OR after 50% scroll depth — whichever comes first. Do not trigger immediately on page load. Keep the pop-up dismissible; a forced interstitial damages trust.

**Position 3 — Post-Content**
Place the lead magnet offer at the close of every blog post, article, or YouTube video description. The audience who reads to the end is the most engaged; they are the highest-probability opt-ins.

**Position 4 — Exit Intent**
Triggered when the cursor moves towards the browser close button (desktop) or the back button is pressed (mobile). Present a different angle or headline from the hero section — the audience has already seen the primary message.

---

## East Africa Adaptation: WhatsApp-First Lead Capture

For EA clients, WhatsApp number capture is often more valuable than email capture. WhatsApp messages achieve open rates of 80%+ versus email's 20–40% in the region.

**Design the delivery flow for both channels:**

- **WhatsApp delivery:** Configure WhatsApp Business auto-reply to send the lead magnet link or PDF attachment immediately upon the prospect sending a trigger message (e.g. "SEND CHECKLIST" to the business WhatsApp number). Promote this trigger message in the bio link, social posts, and Stories.
- **Email delivery:** Standard email automation — trigger on form submission, deliver within 5 minutes, follow with the welcome sequence (see `playbook-email-funnel`).

Where the client has both channels, offer the audience a choice: "Get the checklist by WhatsApp or by email." This respects channel preference and improves opt-in rates.

---

## Double Opt-In Requirement

All lead magnet sign-ups must trigger a confirmation step before the contact is added to any list or broadcast group.

- **Email:** Confirmation email with a single click to confirm. The lead magnet is delivered after confirmation, not before.
- **WhatsApp:** The prospect must initiate contact by sending a message to the business number (this constitutes explicit opt-in). Never add a contact to a WhatsApp broadcast list unless they have initiated contact first.

**Legal basis:** Uganda's Data Protection and Privacy Act 2019 and Kenya's Data Protection Act 2019 require informed, freely given, specific consent before processing personal data for marketing purposes. Double opt-in is the most defensible consent mechanism available.

---

## List Hygiene Protocol

A clean, engaged list outperforms a large, disengaged one. Apply this protocol from day one.

| Action | Trigger | Timeline |
|---|---|---|
| Remove hard bounces | Automatic bounce notification | Within 24 hours |
| Re-engagement campaign | 90 days of inactivity | Send 3-email sequence: "Are you still there?" |
| Remove unresponsive contacts | No engagement after re-engagement sequence | After sequence completes |
| Review list health | Monthly | Check open rate, click rate, unsubscribe rate |

Benchmark: a healthy EA email list should maintain an open rate of at least 20%. A WhatsApp broadcast list should maintain a read rate of at least 60%.

---

## Output: Lead Magnet System Brief

Generate the following document for the client:

1. **Recommended format** — with rationale based on audience and goal
2. **Lead magnet title** — applying the specificity formula: specific outcome + audience + timeframe
3. **Content outline** — what the lead magnet will contain (headings and key points)
4. **Delivery mechanism** — WhatsApp flow, email automation sequence, or both
5. **Placement plan** — where each of the four positions will be implemented and by whom
6. **Opt-in compliance summary** — confirming consent mechanism and regulatory alignment
7. **List hygiene schedule** — dates for first review, re-engagement trigger, and monthly audit

---

## Quality Criteria

Output meets the standard when:

1. Lead magnet format is chosen based on audience research and client capability — not defaulted to whichever is quickest to produce
2. Bly's specificity formula is fully applied — the lead magnet title promises a concrete, singular outcome, not a general benefit
3. Double opt-in is configured and tested for both email and WhatsApp delivery paths before any promotion begins
4. All four placement positions are identified, assigned to a responsible party, and scheduled for implementation
5. List hygiene protocol is documented with specific triggers and timelines, not left as a vague instruction to "clean the list occasionally"
6. Delivery mechanism is tested end-to-end — a real opt-in journey is completed and confirmed working before traffic is driven
7. EA regulatory compliance is noted explicitly — consent mechanism aligns with the Data Protection and Privacy Act 2019 (Uganda) or equivalent

---

## Reference

Bly, R.W. (2018) *The Digital Marketing Handbook: A Step-by-Step Guide to Creating Websites That Sell*. Entrepreneur Press.

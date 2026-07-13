---
name: biz-dev-beyond-agency-offer
description: Use when The Risk-Free "First Date" Engagement Offer is needed to produce a beyond agency offer deliverable for social-media or digital-marketing work; use `biz-dev-positioning` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# The Risk-Free "First Date" Engagement Offer

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **beyond agency offer deliverable** and the supplied brief falls within the risk-free "first date" engagement offer.

## Do Not Use When
- Use `biz-dev-positioning` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Commercial brief, target buyer, offer, proof and requested next step | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified beyond agency offer deliverable; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Buyer problem, proof strength and commercial objective align | Choose the offer and proof sequence that supports the requested buying decision. | A generic sales asset with unsupported claims or the wrong ask. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact beyond agency offer deliverable, consumer, market, channel and approval boundary; route to `biz-dev-positioning` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete beyond agency offer deliverable; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Beyond agency offer deliverable | Requester, client reviewer or delivery team | The beyond agency offer deliverable addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
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
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested beyond agency offer deliverable, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [biz-dev-positioning](../biz-dev-positioning/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

> **The principle:** Traditional agencies ask clients to commit to a
> monthly retainer while hoping for results. The Beyond Agency model
> inverts this — results come first, payment follows. The consultant
> "bakes a bigger pie" for the client first, then takes a slice. The
> client has zero financial risk on the test campaign; the consultant
> demonstrates capability before asking for a long-term commitment. This
> removes the biggest objection in any agency sales conversation: "How do
> I know you can deliver?" (Fihn, 2025)

## Required Input
Ask for the following before producing the offer:

1. **Prospect business name and industry** — trading name and sector
2. **Country / city** — defaults to Uganda/Kampala if not specified
3. **Prospect's primary pain point** — the specific problem they have
   described (not what you assume; use their exact words)
4. **What they have already tried** — previous agency, ads, referrals,
   or organic efforts that have underperformed
5. **Their customer base** — do they have a dormant customer list? An
   active WhatsApp database? A Facebook Group? A physical address file?
   (The answer determines which test campaign type is most appropriate)
6. **The offer / service** — what product or service will the test
   campaign promote?
7. **Revenue metric** — how do they define success? (New bookings / leads
   generated / WhatsApp enquiries / sales revenue)
8. **Preferred fee structure** — profit-share (30–50% of revenue
   generated above baseline), flat test fee, or deferred payment
9. **Timeframe** — how many days for the test campaign? (Default: 7–10)
10. **Outreach method** — was this prospect approached via video audit,
    referral, white-label partner, or inbound? (Affects the tone and
    framing of the offer)

## Section 1 — The Five Offer Structures
Select the most appropriate offer structure based on the client's
situation and appetite for risk:

**Structure 1 — Result guarantee**
*"We will generate [specific number] of [leads / bookings / enquiries]
in the next [7/10/14] days. If we do not reach that number, you pay
nothing."*

Best for: businesses with a clear, measurable conversion action (bookings,
sign-ups, WhatsApp enquiries). Requires the consultant to be confident
in the campaign type.

**Structure 2 — Guaranteed appointment booking**
*"We will fill [X] appointment slots in the next [X] days using your
existing customer list / our targeting. You only pay for the
appointments that show up."*

Best for: service businesses (salons, clinics, coaches, consultants)
where a booked appointment is the primary revenue driver.

**Structure 3 — Specific desirable lead types**
*"We will deliver [X] qualified enquiries from [specific audience
description] in [X] days. Qualified means: [define criteria]."*

Best for: B2B and high-value services where lead quality matters more
than volume.

**Structure 4 — Combine value**
*"We are not just running a campaign — we will also provide [add-on:
a WhatsApp welcome sequence / a referral programme / a customer
reactivation campaign / a social media month plan] as part of the
test. Our goal is to make this the best [X] days of marketing your
business has ever had."*

Best for: clients who are sceptical of the specific campaign alone;
adding bundled value raises perceived worth and reduces price sensitivity.

**Structure 5 — Revenue sharing**
*"We invest our time in the test campaign at no upfront cost to you.
If the campaign generates revenue above your normal baseline, we take
[30–50]% of the excess. You keep the other [50–70]%. If it does not
generate excess revenue, you owe us nothing."*

Best for: clients who genuinely cannot afford a fee but have a strong
customer base. This is the highest-trust offer and the highest-reward
model. Requires a written agreement specifying the baseline revenue
figure (Fihn recommends including a legal disclaimer).

## Section 2 — The Written Offer Document
Generate a one-page offer document. Replace all brackets with the
client-specific information from the Required Input stage.

**[CLIENT BUSINESS NAME]**
**[CONSULTANT NAME / AGENCY NAME]**
**7-Day Marketing Test — No Upfront Commitment**
Proposed start date: [DD Month YYYY]

**What we are proposing**

A focused 7-day test campaign targeting [specific audience: past
customers / Facebook followers / WhatsApp contacts / paid audience].
The campaign will promote [specific offer/service] with the goal of
generating [specific result: X bookings / X enquiries / UGX X in
revenue] by [end date].

This is not a proposal for a monthly retainer. It is an invitation
to see what we can do together before either party makes a larger
commitment. You will have results — or you will have a clear answer —
within 7 days.

**What we will do**

- [Campaign activity 1 — e.g., Write and send a 4-part reactivation sequence to your existing customer list]
- [Campaign activity 2 — e.g., Set up a WhatsApp Click-to-Chat campaign to your warm Facebook audience]
- [Campaign activity 3 — e.g., Optimise your Instagram profile and pin a campaign-specific Story]

**What we will not do**

- We will not ask for access to your bank account, payment processors,
  or business systems beyond what is required for the campaign
- We will not make any public-facing change to your brand without your
  approval
- We will not commit you to any ongoing obligation at the end of the
  7 days

**What we need from you**

- [Requirement 1 — e.g., Access to your customer email list or WhatsApp contacts (names and numbers)]
- [Requirement 2 — e.g., One hour of your time at the start to brief us on your best offer]
- [Requirement 3 — e.g., Prompt responses to our questions during the campaign window]

**What success looks like**

We define the test as successful if: [specific measurable result —
e.g., "a minimum of 5 confirmed bookings" or "UGX 500,000 in new
enquiries"].

**What happens at the end of the 7 days**

If the campaign achieves or exceeds the success target, we will
present a proposal for an ongoing engagement. You are under no
obligation to accept it. If the campaign does not achieve the target,
you owe us [nothing / the agreed flat test fee only].

**The fee**

[Select one:]
- Option A (risk-free): No upfront cost. If the campaign generates
  results above your baseline, we retain [35]% of the excess revenue
  for a period of [30] days. After that, we agree new terms or part
  as friends.
- Option B (flat test fee): UGX [amount] covers the 7-day test in full.
  No profit-share. If results exceed expectations, we discuss ongoing
  terms.
- Option C (deferred): No payment during the test. If you proceed to
  an ongoing engagement after the test, the test fee of UGX [amount]
  is included in Month 1.

Agreed by: _________________________ Date: ___________
[Client name, title]

Proposed by: _________________________ Date: ___________
[Consultant name, agency name]

## Section 3 — The Verbal / Written Pitch (Phoneless Close)
Use this script for written outreach (email, LinkedIn, WhatsApp) or
as the basis for a short video audit message. The goal is to produce
a response — not to close on first contact.

**Opening hook (written or video):**
> "I was looking at your [website / Facebook Page / Instagram] and
> noticed [specific, genuine observation: 'your customer reviews are
> excellent but there's no way for new visitors to contact you quickly'
> / 'you have 4,000 Facebook followers but I couldn't see a WhatsApp
> link anywhere']. I filmed a 3-minute walkthrough of what I noticed —
> would it be useful if I sent it to you?"

Do not pitch services in the opening message. The goal is to get a
"yes, send it."

**The video audit (Loom or WhatsApp voice note):**
- 3–5 minutes maximum
- Screen-record their digital presence while narrating what you see
- Identify 2–3 specific, genuine improvements (do not manufacture
  problems)
- End with: *"I have an idea for how to test this quickly — would
  you be open to a short message or a quick chat to see if it makes
  sense for you?"*

**The close message (sent after the audit is viewed):**
> "[Name], thanks for watching. Based on what I saw, I think a focused
> 7-day test on [specific tactic] could generate [estimated result].
> I've put together a one-page outline — no commitment needed to read
> it. Happy to send it over?"

By the time the one-page offer document lands, the prospect has already
engaged twice and seen the consultant's thinking. The "yes" to the offer
document is the natural next step — not a hard sell.

## Section 4 — The Expectations Sign-Off Document
Produce this one-page document at the start of every engagement to
prevent misalignment, scope creep, and disappointing client experiences.
Have it signed before any campaign begins (Fihn, 2025: the four
key expectation areas).

**[CLIENT BUSINESS NAME] — Engagement Expectations**
Agreed on: [DD Month YYYY]

**Results**

What we are working towards: [specific goal agreed in the offer document]

Realistic timeframe for seeing early results: [e.g., 3–5 days for
reactivation enquiries; 14–21 days for organic social growth]

What results depend on: [list factors the client controls — e.g.,
"prompt responses to WhatsApp enquiries received from the campaign;
approval of copy within 24 hours"]

What is not guaranteed: No marketing campaign can guarantee a specific
revenue outcome. We guarantee our effort, our process, and our
professional standard — not a specific number. (If a guarantee was
agreed in the offer, it is stated in the offer document above.)

**Time**

Our typical turnaround for campaign materials: [e.g., 48 hours for
copy; 5 business days for full strategy documents]

Your expected turnaround for approvals: [e.g., 24 hours on weekdays]

Campaign launch date: [DD Month YYYY]
Campaign end date: [DD Month YYYY or "ongoing — reviewed monthly"]

**Cost**

Agreed fee structure: [from the offer document]
Payment schedule: [e.g., "35% profit-share collected monthly on
the 10th" or "UGX X invoiced on campaign completion"]
Late payment terms: [e.g., "Invoices unpaid after 14 days incur
a UGX X late fee"]

**Communication**

Our primary contact point: [name, WhatsApp number, email]
Your primary contact point: [client name, number, email]
Response time commitment (us): [e.g., "WhatsApp replies within 4
hours during business hours EAT; emails within 24 hours"]
Response time expectation (client): [e.g., "Copy approvals within
24 hours; campaign queries within 2 hours when campaign is live"]
Scheduled check-in: [e.g., "Brief WhatsApp update every Monday
morning; full written report on Day 7 or Day 30"]

Signed: _________________________ Date: ___________
[Client name, title]

Signed: _________________________ Date: ___________
[Consultant name]

## Quality Criteria
Output meets the standard for this skill when:

- The offer document is complete, ready to send, and contains no
  unfilled placeholders — every bracket is replaced with
  client-specific information
- One of the five offer structures is selected and its terms are
  clearly stated including the specific measurable success target,
  the timeframe, and the fee structure in UGX (or local currency)
- The written pitch script produces two touchpoints before the offer
  document is sent — opening hook, then video audit response request
- The expectations document covers all four areas (Results, Time, Cost,
  Communication) with dates and names filled in — not generic
- The revenue-sharing or flat-fee terms are unambiguous; the skill
  includes a note recommending legal review for any profit-share
  agreement over UGX 500,000
- British English throughout; no American spelling variants

## References
- Fihn, F. (2025) *Beyond the Agency Box: The Phoneless Meet*

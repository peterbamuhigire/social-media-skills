---
name: meta-sales-marketing-alignment
description: Use when sales and marketing disagree about lead quality, follow-up or targets and need shared lifecycle stages, handover rules, a lead score and a joint review; produces the sales-marketing SLA, KPI ownership map and lead-scoring model; not for finding and contacting new prospects (use `biz-dev-lawful-prospecting-outreach`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Sales–Marketing Alignment Framework

Source: Kahan (2022) *High-Velocity Digital Marketing*. Sets shared KPIs, lead handover rules, a lead score and a monthly joint review so that marketing and sales are both held to revenue.

<!-- dual-compat-start -->
## Use When

- Sales complains about lead quality and marketing complains about follow-up; both need agreed stages and definitions.
- Handover rules are missing: when a lead passes to sales, how fast sales responds and what happens if nobody does.
- The client wants a lead scoring model built with sales: fit and behaviour points, score decay, MQL threshold, BANT qualification and CRM set-up.
- An owner-managed business needs one CRM as the source of truth and a monthly joint review meeting.

## Do Not Use When

- `biz-dev-lawful-prospecting-outreach` for sourcing contact lists and running cold or warm outreach.
- `playbook-marketing-automation` for building nurture workflows in the automation tool.
- `meta-roi-framework` for calculating return on marketing spend.
- Stop before changing live CRM fields or scoring rules without the sales owner's sign-off.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| CRM system in use and adoption state (HubSpot, Zoho, Salesforce, spreadsheet, none) | Sales owner or CRM administrator | Yes | Recommend Zoho CRM (free tier up to 3 users) or HubSpot CRM (free tier, unlimited users); hold scoring and attribution work until the CRM is adopted. |
| Current funnel stages and lead definitions | Marketing and sales leads | Yes | Draft MQL, opportunity and deal definitions for joint sign-off; mark them provisional. |
| Sales team size, or confirmation that the owner handles all sales | Client | Yes | Apply the owner-managed business scenario and ask. |
| Current monthly lead volume and average sales cycle length (days) | CRM export or client estimate | Yes | Record the client's estimate as an assumption; set the joint review to measure it in month 1. |
| Response-time evidence (MQL delivery to first contact) | CRM activity log | If an SLA already exists | Mark SLA compliance `not assessed` and start logging first-contact times. |
| Client name, industry, country/city and primary goal | Client brief | Yes | Default to Uganda / East Africa; ask for the goal (for example reduce lead wastage, improve MQL-to-deal conversion). |

The intake questions are in [alignment method](references/alignment-method.md) § Required Inputs.

## Workflow

1. Confirm the intake and name the core problem in the client's terms (wasted leads, missing credit, attribution disputes); stop and route to `meta-roi-framework`, `biz-dev-lawful-prospecting-outreach` or `playbook-marketing-automation` when the request is theirs.
2. Map KPI ownership (marketing-owned, sales-owned, jointly-owned) and get it agreed in writing before any reporting or scoring work.
3. Check the three CRM conditions (100% adoption, daily updates, marketing access); stop scoring and attribution work until they are met, using a spreadsheet CRM only as a transitional tool.
4. Write the lead handover SLA with the 4-hour rule and the escalation protocol, and share it with both teams.
5. Set the starter lead score (fit and intent points, WhatsApp signals for EA clients, 50-point MQL threshold); build the full design with [lead-scoring-model](references/lead-scoring-model.md) when calibration, decay or BANT is needed.
6. Set the 60-minute monthly joint review agenda and the 24-hour write-up rule.
7. Adapt the SLA and tracking for owner-managed businesses where there is no sales team.
8. Review conversion at each joint review; if MQLs convert below 20%, correct the threshold or criteria and rerun the scoring for the next period.

KPI lists, CRM rules, the full SLA, scoring points, meeting agenda and the owner-managed scenario are in [alignment method](references/alignment-method.md).

## Handover SLA and starter score

| Stage | Owner | Timeline |
|---|---|---|
| MQL generated | Marketing | Real-time (automated delivery to CRM) |
| First contact attempt | Sales | Within 4 hours of MQL delivery during business hours |
| If no contact within 4 hours | Marketing (re-nurture) | Lead reverts to marketing nurture, not lost |
| Follow-up attempts | Sales | Days 2, 4, 7 after initial contact |
| MQL rejection (sales disputes quality) | Joint review | Within 48 hours; resolve with data |

Starter MQL threshold in this skill: a lead reaching 50+ points is classified as an MQL and handed to sales. The full design in [lead-scoring-model](references/lead-scoring-model.md) proposes 60 points for a standard B2B model and 40 points for the East Africa starter model; both sets are practitioner starting points to calibrate with the client's data.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| KPI ownership map | Marketing lead, sales lead, owner | Every KPI is marketing-owned, sales-owned or jointly-owned, and both teams have signed it. |
| Lead handover SLA with escalation protocol | Sales manager and marketing lead | States the 4-hour first contact, re-nurture on breach, follow-up days and the three-breaches escalation. |
| Lead-scoring model (starter or full design) | Sales and marketing; CRM administrator | Fit and intent points, threshold with rationale and review date; full design follows the reference template. |
| Monthly joint review agenda | Both teams | Six agenda items, a 60-minute slot and a written outcome within 24 hours. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| CRM prerequisite check | Table: adoption, daily updates, marketing access, each pass or `not assessed` | Scoring and attribution work starts only after all three pass. |
| SLA compliance record | Monthly count of MQLs contacted within 4 hours and breaches per rep | Reviewed monthly; breaches trigger the escalation protocol. |
| Threshold calibration log | Table: date, threshold, MQL-to-deal conversion, change made | Each change cites conversion data, not opinion. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Changing live CRM fields, scoring rules or automated replies needs the sales owner's sign-off.

## Degraded Mode

Without an adopted CRM and current funnel stage definitions, return the narrowest qualified result and mark the affected checks `not assessed`. The KPI ownership map, a draft SLA, the joint review agenda and a CRM adoption recommendation can still be delivered; lead scoring and attribution wait.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The CRM is not fully adopted or marketing cannot read deal data | Stop lead scoring and attribution work; recommend a CRM and allow a spreadsheet CRM only if the client cannot commit to software within 30 days. | Scoring built on records held in inboxes, WhatsApp chats and notebooks. |
| KPI ownership is disputed | Agree and document ownership in writing before building any report or scoring system. | The most common cause of failed alignment initiatives. |
| A rep misses the 4-hour contact three times in a month | Marketing escalates to the sales manager; if the pattern continues, review whether the scoring model identifies qualified leads. | Leads going cold within 24 hours of initial contact. |
| MQLs convert below 20% | Lower the threshold or revise the scoring criteria at the quarterly review. | Sales losing trust in marketing leads. |
| The client is in East Africa and sells through WhatsApp | Add WhatsApp behavioural points: question in reply to a broadcast (+15), price-list request (+20). | Missing the strongest local intent signals. |
| The business is owner-managed with no sales team | Apply the SLA to the owner's response on WhatsApp, email and phone; use WhatsApp Business automated replies and a simple tracking sheet. | A process designed for a sales team nobody staffs. |
| The client needs a full lead scoring design (explicit and behavioural points, decay, calibrated threshold, BANT) rather than the starter model | Build it with [lead-scoring-model](references/lead-scoring-model.md), after the CRM prerequisites are met. The starter model in [alignment-method](references/alignment-method.md) uses a 50-point MQL threshold; the full model calibrates 60 points (B2B) or 40 (EA starter). Name the model and threshold in use and do not mix their point tables. | Uncalibrated thresholds, stale high scores and unqualified MQLs reaching sales. |
| The requested outcome belongs to `meta-roi-framework` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Quality Standards

- KPI ownership is clearly mapped: marketing-owned, sales-owned and jointly-owned metrics are distinguished.
- The 4-hour lead response SLA is documented with an escalation protocol for non-compliance.
- CRM adoption is treated as a prerequisite; no lead scoring or attribution work proceeds without it.
- The monthly joint review meeting has a documented agenda and output format.
- WhatsApp is addressed as both an acquisition channel and a lead follow-up channel for EA clients.
- The EA owner-managed business context is addressed as a distinct scenario with adapted recommendations.
- The ROI formula (Bodnar and Cohen, 2012) is applied to marketing KPI reporting.
- Language is British English throughout; imperative in all instructional sections.

## Anti-Patterns

- Resolving attribution disputes by opinion. Fix: settle lead source with CRM data at the joint review.
- Building lead scoring before the CRM is adopted. Fix: meet the three CRM conditions first.
- Treating an uncontacted MQL as lost. Fix: return it to marketing nurture after 4 hours without contact.
- Setting the MQL threshold once and leaving it. Fix: adjust quarterly from conversion data; recalibrate the full model at 60 days.
- Letting each team optimise only its own metrics. Fix: hold both to jointly-owned KPIs (CLV, NPS, revenue by acquisition channel).
- Leaving WhatsApp enquiries unacknowledged while the owner is busy. Fix: set WhatsApp Business automated replies and log every enquiry.
- Absorbing `meta-roi-framework` into this workflow. Fix: route the neighbouring output and hand over verified inputs.

## References

- [Alignment method](references/alignment-method.md): read when running the intake, listing KPIs by owner, checking CRM conditions, writing the SLA, setting starter score points, running the joint review or adapting for an owner-managed business.
- [lead-scoring-model](references/lead-scoring-model.md): read when designing, calibrating or auditing a lead scoring model and MQL handover threshold.
- [`meta-roi-framework`](../meta-roi-framework/SKILL.md): read when marketing ROI or CAC needs calculating for the KPI map.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the SLA and meeting documents.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

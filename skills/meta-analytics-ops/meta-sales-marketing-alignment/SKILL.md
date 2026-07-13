---
name: meta-sales-marketing-alignment
description: "Use when defining shared lifecycle stages, ownership, handover rules and review cadence. Produces sales-marketing service-level agreement and KPI map; use `meta-lead-scoring` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Sales–Marketing Alignment Framework

**Source:** Kahan (2022) *High-Velocity Digital Marketing*

---


<!-- dual-compat-start -->
## Use When

- Use this skill for defining shared lifecycle stages, ownership, handover rules and review cadence.
- Confirm that `meta-lead-scoring` is not the closer route before proceeding.

## Do Not Use When

- Use `meta-lead-scoring` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Current funnel stages, crm ownership and response-time evidence | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Sales-marketing service-level agreement and kpi map | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified sales-marketing service-level agreement and KPI map. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Current funnel stages, crm ownership and response-time evidence is current and attributable | Produce the full sales-marketing service-level agreement and KPI map and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `meta-lead-scoring` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `meta-lead-scoring` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the sales-marketing service-level agreement and KPI map, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the sales-marketing service-level agreement and KPI map without current funnel stages. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `meta-lead-scoring` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified current funnel stages, the skill produces a sales-marketing service-level agreement and KPI map with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`meta-lead-scoring`](../meta-lead-scoring/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Inputs

Ask for the following before generating any deliverable:

1. **Client business name**
2. **Industry**
3. **Country / city** (defaults to Uganda / East Africa)
4. **Primary goal** (e.g. reduce lead wastage, improve MQL-to-deal conversion, establish attribution clarity)
5. **Sales team size** (number of sales staff, or confirm if owner handles all sales)
6. **CRM system in use** (HubSpot, Zoho, Salesforce, spreadsheet, none — critical to know before recommending process changes)
7. **Current monthly lead volume** (approximate)
8. **Average sales cycle length** (days from first contact to signed contract or purchase)

---

## The Core Problem

Marketing generates leads; sales does not follow up promptly or considers them unqualified. Sales closes deals; marketing does not receive credit for sourcing them. Both functions optimise for their own metrics and neither is held accountable for revenue. The result: wasted leads, duplicate effort, and attribution disputes that undermine both teams.

---

## KPI Ownership Map

### Marketing-Owned KPIs
- Website visitors per month
- Lead volume per month (by channel)
- Cost per lead per channel
- Marketing Qualified Lead (MQL) volume
- Marketing-sourced pipeline value (UGX/KES value of opportunities that marketing generated)
- Customer Acquisition Cost (CAC)
- Marketing ROI — apply the formula: **(Total Lifetime Value − CAC) ÷ CAC** (Bodnar and Cohen, 2012)

### Sales-Owned KPIs
- Total revenue (monthly and cumulative vs. target)
- Pipeline coverage ratio: total pipeline value ÷ quarterly revenue target (target: 3–4×)
- Lead-to-opportunity conversion rate
- Opportunity-to-deal conversion rate
- Average sales cycle length (days)
- Average revenue per account

### Jointly-Owned KPIs
- Customer Lifetime Value (CLV)
- Net Promoter Score (NPS)
- Revenue by acquisition channel (first-touch attribution)

Agree and document KPI ownership in writing before implementing any reporting or scoring system. Disputes about KPI ownership are the most common cause of failed alignment initiatives.

---

## CRM as Single Source of Truth

All leads, opportunities, and deal records must exist in one CRM system — not in email inboxes, WhatsApp conversations, spreadsheets, or individual sales reps' notebooks. Before implementing any lead scoring or attribution model, ensure the CRM meets three conditions:

1. **100% adoption** — every sales team member logs every lead and activity. No exceptions.
2. **Daily updates** — activity records (calls made, messages sent, meetings held) must be logged same-day.
3. **Marketing access** — marketing must have read access to opportunity and deal data to report on marketing-sourced revenue.

**For EA clients without a CRM:** Recommend Zoho CRM (free tier supports up to 3 users) or HubSpot CRM (free tier, unlimited users). Do not implement lead scoring or attribution analysis until the CRM is adopted. A spreadsheet-based CRM is acceptable as a transitional tool if the client cannot commit to a software platform within the next 30 days.

---

## Lead Handover SLA

Apply Kahan's (2022) lead handover SLA as the operational standard:

| Stage | Owner | Timeline |
|---|---|---|
| MQL generated | Marketing | Real-time (automated delivery to CRM) |
| First contact attempt | Sales | Within **4 hours** of MQL delivery during business hours |
| If no contact within 4 hours | Marketing (re-nurture) | Lead reverts to marketing nurture — not lost |
| Follow-up attempts | Sales | Days 2, 4, 7 after initial contact |
| MQL rejection (sales disputes quality) | Joint review | Within 48 hours — resolve with data |

**The 4-hour rule (Kahan, 2022):** Leads go cold within 24 hours of initial contact. Research across B2B markets consistently shows response time is the single biggest predictor of lead conversion. Document the 4-hour SLA in writing, share with both teams, and review compliance monthly.

**Escalation protocol:** If a sales rep fails to contact an MQL within 4 hours three times in a month, the marketing team escalates to the sales manager. If the pattern continues, review whether the lead scoring model is correctly identifying qualified leads.

---

## Lead Scoring Foundation

Before implementing lead scoring, confirm the CRM is fully adopted (see above). Then build a simple scoring model:

**Demographic score (fit):**
- Correct industry: +10
- Correct company size: +10
- Decision-maker title: +15
- Located in target geography: +5

**Behavioural score (intent):**
- Visited pricing page: +20
- Downloaded lead magnet: +10
- Attended webinar: +15
- Opened 3+ emails in past 30 days: +10
- Requested a demo or quote: +25

**MQL threshold:** A lead reaching 50+ points is classified as an MQL and handed to sales. Adjust thresholds quarterly based on conversion data — if MQLs are converting at below 20%, lower the threshold or revise the scoring criteria.

For EA clients, include WhatsApp engagement in behavioural scoring: responding to a WhatsApp broadcast with a question (+15) or requesting a price list (+20) are strong intent signals.

---

## Monthly Joint Review Meeting

Marketing and sales must meet for 60 minutes each month. Structure:

1. **Lead volume and quality (marketing presents):** MQL volume, cost per MQL, top-performing channels
2. **Funnel conversion rates (joint review):** MQL → opportunity → deal at each stage
3. **Revenue by channel (joint review):** Which marketing channels produced closed revenue this month?
4. **Attribution disputes:** Resolve any disagreements about lead source with CRM data, not opinion
5. **Scoring model review:** Are the leads marketing delivers genuinely qualified? Adjust scoring if conversion rate is below 20%
6. **Next month targets:** Agree lead volume targets and channel allocation for the next period

Document meeting outcomes in writing and share with both teams within 24 hours.

---

## EA-Specific Context: Owner-Managed Businesses

Many EA businesses do not have a formal sales team — the business owner or one account manager handles all sales enquiries. Apply the same principles:

- The "alignment" is between marketing activity and the owner's follow-up behaviour
- The 4-hour SLA applies to the owner's response to WhatsApp, email, and phone enquiries
- Design marketing content to reduce the barrier to first contact: WhatsApp CTA buttons, pre-answered FAQs, pricing visible online
- Use WhatsApp Business automated replies to acknowledge enquiries instantly, even when the owner cannot respond immediately
- Track all enquiries in a simple CRM or Google Sheet — minimum fields: name, contact, source, date, status (contacted / pending / converted / lost)

---

## Quality Criteria

Output meets the standard for this skill if:

- KPI ownership is clearly mapped — marketing-owned, sales-owned, and jointly-owned metrics are distinguished
- The 4-hour lead response SLA is documented with an escalation protocol for non-compliance
- CRM adoption is treated as a prerequisite — no lead scoring or attribution work proceeds without it
- The monthly joint review meeting has a documented agenda and output format
- WhatsApp is addressed as both an acquisition channel and a lead follow-up channel for EA clients
- The EA owner-managed business context is addressed as a distinct scenario with adapted recommendations
- The ROI formula (Bodnar and Cohen, 2012) is applied to marketing KPI reporting
- Language is British English throughout; imperative in all instructional sections

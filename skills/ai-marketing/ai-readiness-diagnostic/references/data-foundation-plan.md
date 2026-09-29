# Data Foundation Plan

Merged from skills/ai-marketing/ai-data-foundation-plan on 2026-09-29 at 7c60138; preservation map: [ai-data-foundation-plan.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/ai-data-foundation-plan.md)

## When to use this reference

Use it when the client needs an implementation plan to build their data foundation — Canvas Step 1 of Venkatesan and Lecinski (2026) *The AI Marketing Canvas*, 2nd edn — rather than a one-off audit. It suits larger East African clients (banks, NGOs, telecoms, universities) that hold data but make no structured marketing use of it. For a quick SME hygiene audit and 30-day clean-up, use [data-foundation-audit.md](data-foundation-audit.md) first.

AI is only as good as the data it is trained on. A client with poor data will get poor AI outputs regardless of which tools they buy. The most common reason AI marketing fails at Step 2 is not tool quality — it is data quality. The four customer moments that AI marketing serves — Acquisition, Retention, Growth and Advocacy — each need specific, clean, structured data. This reference delivers the inventory, quality assessment, schema and 90-day plan that build that foundation.

After the plan, re-run the 41-item diagnostic in the parent skill to confirm Canvas step progression, and use [meta-tools-stack-evaluation](../../../meta-analytics-ops/meta-tools-stack-evaluation/SKILL.md) for a full CRM or AI tool selection process. For data-product ownership, lineage, freshness, audience boundaries and AI marketing controls, read [data-product-and-ai-foundation-principles.md](data-product-and-ai-foundation-principles.md).

## Inputs to collect before any output

1. **Client business name** — trading name and legal entity if different.
2. **Industry** — financial services, NGO, telecom, education, retail, etc.
3. **Country and city** — defaults to Uganda/Kampala if not specified.
4. **Organisation size** — approximate staff count and customer/contact count.
5. **Current data sources** — every source, including spreadsheets, WhatsApp contact lists, paper records and legacy software.
6. **Primary marketing goal** — the AI capability the client wants to enable (for example segmented email, churn prediction, personalised WhatsApp messaging).
7. **Current Canvas step** — from the 41-item diagnostic; if it has not been run, ask the client to describe their AI marketing activity to date.
8. **Existing CRM or data tool** — name and version, or "none".

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| A source is below 50 % completeness or updated less than monthly | Flag it as a priority gap in the inventory. | Building segments on stale or empty records. |
| A source misses a quality target (see Step 2) | Rate the cell Red or Amber and add a remediation task. | Treating a failing source as fit for AI use. |
| Fewer than 200 contacts and no budget | Recommend Google Sheets + AppSheet. | Paying for a CRM the team cannot sustain. |
| 200–2,000 contacts and some budget | Recommend HubSpot or Zoho free tier. | Outgrowing a spreadsheet mid-programme. |
| Client is an NGO or CSO | Apply for Salesforce Nonprofit first. | Missing a donated-licence route. |
| Complex relational data needs | Recommend Airtable. | Forcing relational data into a flat contact list. |
| More than 1,000 records processed | Appoint a Data Protection Officer (reasonable internal threshold for larger clients). | Processing at scale without accountable oversight. |
| Customer base is not primarily English-speaking | Translate the consent notice into Luganda or Swahili. | Consent that is not informed. |

## Procedure

### Step 1 — Data asset inventory

Map all current data sources across five categories:

- **Contact data** — customer name, phone number, email address, location.
- **Transaction data** — purchase history, amounts (UGX), dates, payment method (Mobile Money / bank transfer / cash).
- **Engagement data** — social media interactions, email opens, website visits, WhatsApp message responses.
- **Behavioural data** — content consumed, products viewed but not purchased, pages visited, app activity.
- **Feedback data** — survey responses, Google/Facebook reviews, complaint records, WhatsApp conversation threads.

For each source, record:

| Attribute | Description |
|---|---|
| Location | Where it lives: spreadsheet, CRM, WhatsApp contacts, paper ledger, POS system |
| Owner | Which department or individual controls it |
| Currency | How often it is updated: daily / weekly / monthly / never |
| Completeness | Estimated % of records with all required fields populated |

Present the inventory as a table. Flag any source below 50 % completeness or updated less than monthly as a priority gap.

### Step 2 — Data quality assessment

Rate each source on four dimensions; flag any source below target.

| Dimension | Definition | Target |
|---|---|---|
| **Completeness** | Are all required fields populated? | 80 %+ of records |
| **Accuracy** | Is the data correct? Spot-check 10 records per source. | < 5 % error rate |
| **Consistency** | Same customer in multiple systems — do records match? | 90 %+ match rate |
| **Currency** | When was it last updated? | Within 30 days |

Check explicitly for these East African data problems:

- **SIM swapping** — customers in Uganda frequently change SIM cards; a contact may have 2–4 phone numbers on file, not all current.
- **Mobile Money numbers** — MTN MoMo and Airtel Money numbers may differ from the customer's primary voice SIM; record both separately.
- **Name variations** — Luganda and English forms of the same name are often recorded inconsistently (for example "Nakato Sarah" vs "Sarah Nakato" vs "S. Nakato"); flag duplicates.
- **Unrecorded cash transactions** — particularly common in retail and financial services; a customer's LTV is systematically underestimated if cash sales are not captured.
- **WhatsApp as de facto CRM** — WhatsApp contact lists are valuable but unstructured; they must be exported and cleaned before any AI tool can use them.

Produce a quality scorecard with one row per source and one column per dimension. Assign RAG status (Red / Amber / Green) per cell.

### Step 3 — Minimum viable customer schema

Design the client's minimum viable customer record — the fields their stated marketing goal requires. Do not produce a generic schema; tailor fields to the client's industry and goal.

**Core fields — required for any AI use**

| Field | Notes |
|---|---|
| Customer ID | Unique identifier; generate if none exists |
| Full name | Standardised format: First Last |
| Primary phone | With country code (+256 for Uganda) |
| Mobile Money number | MTN or Airtel; note network |
| Email address | Where available; not mandatory for all EA segments |
| Location | District and sub-county minimum; full address where possible |
| Date of first contact | Transaction date or sign-up date |
| Customer type | Individual / Business / NGO / Government |

**Behavioural fields — required for the Retention and Growth moments**

| Field | Notes |
|---|---|
| Last transaction date | Enables churn scoring |
| Total lifetime value (LTV) | Cumulative spend in UGX |
| Average transaction value | LTV ÷ transaction count |
| Preferred contact channel | WhatsApp / Facebook / Email / In-person / SMS |
| Content preferences | If trackable from engagement data |
| Complaint history | Boolean Y/N; resolved Y/N |

**Segmentation fields — required for the Acquisition moment**

| Field | Notes |
|---|---|
| Acquisition source | Referral / Social media / Walk-in / Event / Paid ad |
| Referrer name | Critical for word-of-mouth tracking in EA; link to the referrer's Customer ID |
| Industry / Sector | B2B clients only |
| Organisation name | B2B clients only |

For each field note (a) whether it exists in a current source, (b) the source location and (c) the action needed to populate it.

### Step 4 — 90-day data foundation plan

Produce a task-level plan with named deliverables per 30-day block. Assign a responsible role (for example Marketing Manager, IT Officer, Data Analyst) to each task. Milestones must be concrete and measurable, not vague objectives.

**Days 1–30: Audit and clean**
- Week 1 — Complete the data asset inventory (Step 1). Produce the inventory table and share it with senior management for sign-off.
- Week 2 — Run the data quality assessment (Step 2) on the top three sources by customer record count. Produce the RAG scorecard.
- Weeks 3–4 — Identify and close the single most damaging data gap. For most EA clients this is either (a) deduplicating phone numbers or (b) exporting and structuring WhatsApp contacts.
- Week 4 — Select a CRM or data management tool (see below). Complete sign-up and configure the minimum viable schema as the record template.

**Days 31–60: Consolidate**
- Migrate all customer records from existing sources into the chosen CRM.
- Apply the minimum viable schema to all migrated records; flag incomplete records for follow-up.
- Write and circulate a one-page data entry standard specifying exactly how new customer records are created (format, required fields, who enters data).
- Set up a consent capture process (see the compliance section). Every new customer record created from Day 31 onward must have documented consent.

**Days 61–90: Connect and test**
- Connect the clean data source to the first AI or automation tool named in the client's marketing goal (for example Mailchimp for email segmentation; Africa's Talking for SMS broadcast; HubSpot workflows for lead nurturing).
- Run the first segmented campaign using the clean data.
- After the campaign, measure: was the data clean enough to run without manual correction? Which fields were missing or incorrect?
- Produce a **data health score**: the % of records meeting the full minimum viable schema. Target 70 %+ by Day 90 and 90 %+ by Month 6.

### Step 5 — Uganda Data Protection and Privacy Act 2019 compliance

Address these obligations explicitly in the plan output:

- Obtain explicit, informed consent before storing any personal data.
- Inform customers what data is collected, the purpose, how it is used, how long it is retained and who it may be shared with.
- Honour opt-out requests within 48 hours.
- WhatsApp broadcast lists require opt-in from each recipient — do not add contacts without consent.
- Appoint a Data Protection Officer if processing data at scale (> 1,000 records is a reasonable internal threshold for larger clients).

These are the source skill's operating rules; confirm current statutory wording with qualified counsel before presenting them as legal requirements.

**Consent capture template** — include in the output, adapted to the client's name and service:

> **[CLIENT NAME] — Data Consent Notice**
>
> By sharing your contact details with us, you agree that [Client Name] may store and use your name, phone number, and purchase history to:
> - Send you relevant updates, offers, and service information via WhatsApp, SMS, or email
> - Improve our products and services based on your feedback
> - Contact you about your account or orders
>
> Your data will not be sold or shared with third parties without your separate consent. You may withdraw consent at any time by messaging "STOP" to [WhatsApp number] or emailing [email address].
>
> Data is retained for [X] years or until you request deletion.
> This notice complies with the Uganda Data Protection and Privacy Act 2019.

Adapt the retention period and contact channels to the client's actual practice. Translate into Luganda or Swahili if the primary customer base is not English-speaking.

## Recommended CRM tools for the EA market

Recommend one tool based on client size and budget, with a brief rationale (see the decision rules). Verify current free-tier limits and payment options before quoting.

| Tool | Type | Free tier | Payment method | Best for |
|---|---|---|---|---|
| HubSpot CRM | Full CRM | Yes — generous free tier | USD card required | SMEs with 500+ contacts |
| Zoho CRM | Full CRM | Yes — up to 3 users | USD card required | Growing SMEs |
| Airtable | Flexible database | Yes — limited records | USD card required | Custom data structures |
| Google Sheets + AppSheet | Low-code CRM | Yes | Google account / USD | Very small teams, no budget |
| Salesforce Nonprofit Success Pack | Full CRM | Donated — 10 licences | Requires application | NGOs and civil society |

## Output format

Deliver the plan in five clearly labelled sections:

1. Data Asset Inventory (table)
2. Data Quality Assessment (RAG scorecard table)
3. Minimum Viable Customer Schema (table with current-state notes)
4. 90-Day Data Foundation Plan (three 30-day blocks, task-level)
5. Compliance and Consent (DPA 2019 notice, adapted)

Close with a one-paragraph **Next Step** statement confirming the client's current Canvas step, what the 90-day plan will enable, and what to run next (re-score with the 41-item diagnostic, or begin full canvas development with [ai-marketing-canvas-scoring.md](ai-marketing-canvas-scoring.md)). The output is a structured text document suitable for sharing with the client's senior leadership team as a standalone briefing paper.

## Quality checklist

- [ ] The data asset inventory is exhaustive — it includes WhatsApp contacts, paper records and POS systems where present, not only digital CRM sources.
- [ ] All four quality dimensions (completeness, accuracy, consistency, currency) are scored in a RAG table, not described generically.
- [ ] The minimum viable schema is tailored to the client's industry and marketing goal — not a copy-paste generic template.
- [ ] The 90-day plan has named, measurable tasks in each 30-day block with an assigned responsible role; no block contains only vague objectives.
- [ ] Uganda DPA 2019 compliance is addressed, with the consent template adapted to the client's name, channels and retention period.
- [ ] The CRM recommendation is specific to the client's size and budget, with a brief rationale — not a list of all options.
- [ ] EA-specific data problems — SIM swapping, Mobile Money number duplication, Luganda/English name variations, unrecorded cash transactions — are identified where relevant to the client's sources.
- [ ] The output closes with the data health score target and the Canvas step the client will be ready to attempt once it is met.

## Sources

- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd edn. Stanford Business Books.
- Mohan, S. *Designing the AI-Driven Data Foundations: Architecture, Principles, and Practice* — synthesised in [data-product-and-ai-foundation-principles.md](data-product-and-ai-foundation-principles.md).

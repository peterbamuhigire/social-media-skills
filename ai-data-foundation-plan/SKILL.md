---
name: ai-data-foundation-plan
description: >
  Audits a client's existing data assets, designs a customer-focused minimum
  viable data schema, and produces a 90-day action plan to build the data
  infrastructure required for AI marketing. Invoke this skill when a client at
  Canvas Step 1 (Foundation) needs to structure their data before any AI tools
  can function, or when a client at Step 2–3 discovers data gaps that limit AI
  effectiveness. Based on Venkatesan and Lecinski (2026) The AI Marketing
  Canvas, 2nd edition, Stanford Business Books.
---
# AI Data Foundation Plan

<!-- dual-compat:start -->
## Use when
- Audits a client's existing data assets, designs a customer-focused minimum viable data schema, and produces a 90-day action plan to build the data infrastructure required for AI marketing. Invoke this skill when a client at Canvas Step 1 (Foundation) needs to structure their data before any AI tools can function, or when a client at Step 2–3 discovers data gaps that limit AI effectiveness. Based on Venkatesan and Lecinski (2026) The AI Marketing Canvas, 2nd edition, Stanford Business Books.
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
- An AI-focused strategy, audit, system design, or prompt asset in markdown with human review and control points.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Purpose

Produce a structured data foundation action plan grounded in Canvas Step 1 of
Venkatesan and Lecinski's *The AI Marketing Canvas* (2nd ed., 2026). AI is
only as good as the data it is trained on. A client with poor data will get
poor AI outputs regardless of which tools they purchase. The most common reason
AI marketing fails at Step 2 is not tool quality — it is data quality.

The four customer moments that AI marketing serves — Acquisition, Retention,
Growth, and Advocacy — each require specific, clean, structured data to
function. This skill delivers the audit, schema, and plan to build that
foundation.

Primarily relevant for larger East African clients (banks, NGOs, telecoms,
universities) with existing data but no structured marketing use of it.

After completing this plan, refer the client to `ai-readiness-diagnostic` to
confirm their Canvas step progression, and to `ai-vendor-evaluation` when
selecting CRM or AI tools.

---

## Required Inputs

Ask for the following before generating any output:

1. **Client business name** — trading name and legal entity if different
2. **Industry** — financial services, NGO, telecom, education, retail, etc.
3. **Country and city** — defaults to Uganda/Kampala if not specified
4. **Organisation size** — approximate staff count and customer/contact count
5. **Current data sources** — list every source, including spreadsheets,
   WhatsApp contact lists, paper records, and legacy software
6. **Primary marketing goal** — what AI capability the client wants to unlock
   (e.g., segmented email, churn prediction, personalised WhatsApp messaging)
7. **Current Canvas step** — from `ai-readiness-diagnostic`; if not run, ask
   the client to describe their AI marketing activity to date
8. **Existing CRM or data tool** — name and version, or "none"

---

## Step 1 — Data Asset Inventory

Map all current data sources across five categories. For each source identified,
record the four attributes listed below.

**Five data categories to map:**

- **Contact data** — customer name, phone number, email address, location
- **Transaction data** — purchase history, amounts (UGX), dates, payment
  method (Mobile Money / bank transfer / cash)
- **Engagement data** — social media interactions, email opens, website visits,
  WhatsApp message responses
- **Behavioural data** — content consumed, products viewed but not purchased,
  pages visited, app activity
- **Feedback data** — survey responses, Google/Facebook reviews, complaint
  records, WhatsApp conversation threads

**For each data source, record:**

| Attribute | Description |
|---|---|
| Location | Where it lives: spreadsheet, CRM, WhatsApp contacts, paper ledger, POS system |
| Owner | Which department or individual controls it |
| Currency | How frequently it is updated: daily / weekly / monthly / never |
| Completeness | Estimated % of records with all required fields populated |

Present the inventory as a table. Flag any source rated below 50% completeness
or updated less than monthly as a priority gap.

---

## Step 2 — Data Quality Assessment

Rate each data source on four dimensions. Target scores are noted; flag any
source below target.

| Dimension | Definition | Target |
|---|---|---|
| **Completeness** | Are all required fields populated? | 80%+ of records |
| **Accuracy** | Is the data correct? Spot-check 10 records per source. | <5% error rate |
| **Consistency** | Same customer appearing in multiple systems — do records match? | 90%+ match rate |
| **Currency** | When was it last updated? | Within 30 days |

**EA-specific data problems to check for explicitly:**

- **SIM swapping** — customers in Uganda frequently change SIM cards; a
  contact may have 2–4 phone numbers on file, not all current
- **Mobile Money numbers** — MTN MoMo and Airtel Money numbers may differ from
  the customer's primary voice SIM; record both separately
- **Name variations** — Luganda and English name forms of the same person are
  often recorded inconsistently (e.g., "Nakato Sarah" vs "Sarah Nakato" vs
  "S. Nakato"); flag duplicates
- **Unrecorded cash transactions** — particularly common in retail and
  financial services; a customer's LTV is systematically underestimated if
  cash sales are not captured
- **WhatsApp as de facto CRM** — WhatsApp contact lists are valuable but
  unstructured; they must be exported and cleaned before any AI tool can
  use them

Produce a quality scorecard table with one row per data source and columns for
each dimension. Assign RAG status (Red / Amber / Green) per cell.

---

## Step 3 — Minimum Viable Customer Schema

Design the client's minimum viable customer record — the specific fields
required for their stated marketing goal. Do not produce a generic schema;
tailor fields to the client's industry and goal.

**Core fields — required for any AI use:**

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

**Behavioural fields — required for Retention and Growth AI moments:**

| Field | Notes |
|---|---|
| Last transaction date | Enables churn scoring |
| Total lifetime value (LTV) | Cumulative spend in UGX |
| Average transaction value | LTV ÷ transaction count |
| Preferred contact channel | WhatsApp / Facebook / Email / In-person / SMS |
| Content preferences | If trackable from engagement data |
| Complaint history | Boolean: Y/N; resolved: Y/N |

**Segmentation fields — required for Acquisition AI moment:**

| Field | Notes |
|---|---|
| Acquisition source | Referral / Social media / Walk-in / Event / Paid ad |
| Referrer name | Critical for word-of-mouth tracking in EA; link to referrer's Customer ID |
| Industry / Sector | B2B clients only |
| Organisation name | B2B clients only |

For each field in the schema, note: (a) whether it currently exists in a data
source, (b) the source location, and (c) what action is needed to populate it.

---

## Step 4 — 90-Day Data Foundation Plan

Produce a task-level plan with named deliverables per 30-day block. Assign a
responsible role (e.g., Marketing Manager, IT Officer, Data Analyst) to each
task. Milestones must be concrete and measurable — not vague objectives.

### Days 1–30: Audit and Clean

- **Week 1** — Complete the data asset inventory (Step 1). Produce the
  inventory table and share with senior management for sign-off.
- **Week 2** — Run the data quality assessment (Step 2) on the top three data
  sources by customer record count. Produce the RAG scorecard.
- **Week 3–4** — Identify and close the single most damaging data gap. For
  most EA clients this will be either: (a) deduplicating phone numbers, or
  (b) exporting and structuring WhatsApp contacts.
- **Week 4** — Select a CRM or data management tool (see recommendations
  below). Complete tool sign-up and configure the minimum viable schema as
  the record template.

### Days 31–60: Consolidate

- Migrate all customer records from existing sources into the chosen CRM.
- Apply the minimum viable schema to all migrated records; flag incomplete
  records for follow-up.
- Write and circulate a data entry standard — one-page document specifying
  exactly how new customer records are created (format, required fields,
  who enters data).
- Set up a consent capture process (see Uganda DPA 2019 requirements below).
  Every new customer record created from Day 31 onward must have documented
  consent.

### Days 61–90: Connect and Test

- Connect the clean data source to the first AI or automation tool identified
  in the client's marketing goal (e.g., Mailchimp for email segmentation;
  Africa's Talking for SMS broadcast; HubSpot workflows for lead nurturing).
- Run the first segmented campaign using the clean data.
- After the campaign, measure: Was the data clean enough to run without
  manual correction? What fields were missing or incorrect?
- Produce a **data health score**: calculate the % of records meeting the
  full minimum viable schema. Set a target of 70%+ by Day 90, 90%+ by
  Month 6.

---

## Uganda Data Protection and Privacy Act 2019 — Compliance

Address the following requirements explicitly in the plan output.

**Obligations relevant to marketing data:**

- Obtain explicit, informed consent before storing any personal data.
- Inform customers of: what data is collected, the purpose, how it is used,
  how long it is retained, and who it may be shared with.
- Honour opt-out requests within 48 hours.
- WhatsApp broadcast lists require opt-in from each recipient — do not add
  contacts without consent.
- Appoint a Data Protection Officer if processing data at scale (>1,000
  records is a reasonable internal threshold for larger clients).

**Consent capture template — include this verbatim in the output, adapted to
the client's name and service:**

---

> **[CLIENT NAME] — Data Consent Notice**
>
> By sharing your contact details with us, you agree that [Client Name] may
> store and use your name, phone number, and purchase history to:
> - Send you relevant updates, offers, and service information via WhatsApp,
>   SMS, or email
> - Improve our products and services based on your feedback
> - Contact you about your account or orders
>
> Your data will not be sold or shared with third parties without your
> separate consent. You may withdraw consent at any time by messaging
> "STOP" to [WhatsApp number] or emailing [email address].
>
> Data is retained for [X] years or until you request deletion.
> This notice complies with the Uganda Data Protection and Privacy Act 2019.

---

Adapt the retention period and contact channels to the client's actual
practice. Translate into Luganda or Swahili if the client's primary customer
base is not English-speaking.

---

## Recommended CRM Tools for the EA Market

Recommend one tool from this table based on client size and budget. Cross-
reference with `ai-vendor-evaluation` for a full tool selection process.

| Tool | Type | Free Tier | Payment Method | Best For |
|---|---|---|---|---|
| HubSpot CRM | Full CRM | Yes — generous free tier | USD card required | SMEs with 500+ contacts |
| Zoho CRM | Full CRM | Yes — up to 3 users | USD card required | Growing SMEs |
| Airtable | Flexible database | Yes — limited records | USD card required | Custom data structures |
| Google Sheets + AppSheet | Low-code CRM | Yes | Google account / USD | Very small teams, no budget |
| Salesforce Nonprofit Success Pack | Full CRM | Donated — 10 licences | Requires application | NGOs and civil society |

**Selection guidance:**
- If the client has fewer than 200 contacts and no budget: Google Sheets +
  AppSheet.
- If the client has 200–2,000 contacts and some budget: HubSpot or Zoho free
  tier.
- If the client is an NGO or CSO: apply for Salesforce Nonprofit first.
- If the client has complex relational data needs: Airtable.

---

## Quality Criteria

Assess the output against these criteria before delivering to the client:

- The data asset inventory is exhaustive — it includes WhatsApp contacts,
  paper records, and POS systems if present, not only digital CRM sources.
- All four data quality dimensions (completeness, accuracy, consistency,
  currency) are assessed and scored in a RAG table, not described generically.
- The minimum viable schema is tailored to the client's industry and stated
  marketing goal — it is not a copy-paste generic template.
- The 90-day plan contains named, measurable tasks for each 30-day block with
  an assigned responsible role; no block contains only vague objectives.
- Uganda DPA 2019 compliance is addressed with the consent capture template
  adapted to the client's name, channels, and retention period.
- The CRM recommendation is specific to the client's size and budget, with a
  brief rationale, not a list of all options.
- EA-specific data problems — SIM swapping, Mobile Money number duplication,
  Luganda/English name variations, unrecorded cash transactions — are
  explicitly identified where relevant to the client's data sources.
- The output closes with a clear statement of the data health score target
  and what Canvas step the client will be ready to attempt once that target
  is met.

---

## Output Format

Deliver the plan in five clearly labelled sections matching the steps above:

1. Data Asset Inventory (table)
2. Data Quality Assessment (RAG scorecard table)
3. Minimum Viable Customer Schema (table with current-state notes)
4. 90-Day Data Foundation Plan (three 30-day blocks, task-level)
5. Compliance and Consent (DPA 2019 notice, adapted)

Close with a one-paragraph **Next Step** statement confirming: what Canvas step
the client is currently at, what the 90-day plan will unlock, and which skill
to invoke next (`ai-readiness-diagnostic` to re-score, or
`ai-marketing-canvas-assessment` to begin full canvas development).

Output is a structured text document suitable for sharing with the client's
senior leadership team as a standalone briefing paper.

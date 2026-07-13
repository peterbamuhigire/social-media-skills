---
name: ai-data-foundation-audit
description: Use when AI Data Foundation Audit is needed to produce an evidence-backed audit report for social-media or digital-marketing work; use `ai-readiness-diagnostic` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Data Foundation Audit

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **evidence-backed audit report** and the supplied brief falls within ai data foundation audit.

## Do Not Use When
- Use `ai-readiness-diagnostic` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| AI marketing use-case brief, intended human control point and success measure | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Issue a qualified finding and identify the evidence needed. |

## Capability and Permission Boundaries
Default to read-only: inspect supplied material and report findings. Editing, publishing, contacting people, spending, or changing live systems requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified evidence-backed audit report; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Data readiness, AI maturity and risk support the proposed operating level | Choose the lowest viable automation level and define its human approval gate. | Automating an unsafe or unevaluable marketing process. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact evidence-backed audit report, consumer, market, channel and approval boundary; route to `ai-readiness-diagnostic` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete evidence-backed audit report; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Evidence-backed audit report | Requester, client reviewer or delivery team | The evidence-backed audit report addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
| Decision and gap note | Approver or next workflow | Names the chosen route, evidence used, unresolved inputs and any action requiring authority. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Finding-to-source register and unassessed-check list | Inline table, checklist or linked source note | Every material claim, decision and unavailable check is traceable. |

## Quality Standards
- Preserve the domain guidance and East African market context below; replace it only when the requester names another market.
- Use British English unless the target language or market requires otherwise, and verify names, figures, quotations and platform rules before use.
- Make the key choice visible, cover failure and edge cases, and keep the result ready for its named consumer.
- Run the repository's `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested evidence-backed audit report, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [ai-readiness-diagnostic](../ai-readiness-diagnostic/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

## Required Input
Ask for the following before generating any deliverable:

1. **Client business name** — trading name as it appears to customers
2. **Industry** — e.g. retail, hospitality, healthcare, professional services
3. **Country/city** — default: Uganda / East Africa if not specified
4. **All customer data sources currently in use** — tick all that apply:
   WhatsApp chat history | Facebook Page DMs and comments | Email (Gmail /
   Outlook) | CRM software (name it) | Excel / Google Sheets | Accounting
   software (e.g. QuickBooks, Wave) | Other (describe)
5. **Primary AI use case the data will support** — select one:
   Content personalisation | Chatbot knowledge base | Predictive analytics |
   Audience segmentation
6. **Approximate number of customer records** — total across all systems
   (even a rough estimate is useful)

## Why Data Quality is Step 1
Three independent books converge on the same conclusion: data quality is the
single most important prerequisite for any AI marketing investment (Venkatesan
and Lecinski, 2026; Lamplugh, 2024; Ltifi, 2025). AI tools amplify what they
receive — clean data produces better outputs; dirty data produces worse outputs
at speed.

For East African clients specifically, the data challenge is structural.
Customer data is fragmented across WhatsApp chat histories, Facebook Page DMs,
manual Excel spreadsheets, phone contacts, and verbal records. Before any AI
tool can add value, this fragmentation must be addressed.

The investment in data hygiene is not a technical exercise — it is the
commercial prerequisite for every AI use case. Skipping this step does not
save time; it wastes the cost of the AI tool.

## The EA Data Reality
Map the typical Ugandan SME data environment honestly before proceeding:

- **WhatsApp** — customer enquiries, orders, and complaints are stored in chat
  history; rarely exported or structured; impossible to query or analyse at
  scale
- **Facebook Page** — post comments, DM threads, and page insights are
  exportable via Meta Business Suite but rarely exported; valuable for
  sentiment and engagement data
- **Email** — enquiries and newsletter replies sit in Gmail or Outlook, rarely
  in a CRM; no linkage to purchase data
- **Excel spreadsheets** — customer names, phone numbers, and purchase history
  recorded manually; often incomplete, inconsistent formatting, and not
  regularly updated
- **Verbal / in-person** — walk-in customers and cash transactions frequently
  go unrecorded entirely
- **Result** — the same customer may appear in three or four separate systems
  with different name spellings, no unique identifier, and no purchase history
  linkage. AI tools cannot perform matching, personalisation, or segmentation
  on this data without prior consolidation.

## Data Hygiene Checklist (20 Items)
Complete this checklist for the client. Score each item Yes / No / Partial.
Flag any No or Partial item as a remediation priority.

### Completeness
- [ ] Are all customer records complete — name, contact detail, and transaction
  history at minimum?
- [ ] Are there records with missing phone numbers or email addresses?
- [ ] Are product and service names consistently recorded — not "cake" in some
  rows and "birthday cake" in others?
- [ ] Are dates recorded in a consistent format (DD/MM/YYYY throughout)?

### Accuracy
- [ ] Are phone numbers in the correct format for Uganda (+256 or 0)?
- [ ] Are prices recorded in UGX consistently — not a mix of UGX and USD?
- [ ] Are customer names spelled consistently across all systems?
- [ ] Are inactive or churned customers flagged and separated from active
  customer records?

### Consistency
- [ ] Is each customer recorded once across all systems — not duplicated
  across WhatsApp, Excel, and email?
- [ ] Are product categories consistent — not "electronics" in one place and
  "gadgets" in another?
- [ ] Are campaign names consistent across Meta, email, and CRM records?
- [ ] Are staff names or salesperson records consistent for attribution
  purposes?

### Accessibility
- [ ] Is data stored in a format the AI tool can read — CSV, Excel, or plain
  text — not only in printed records or chat messages?
- [ ] Can the data be exported from its current system? Some WhatsApp and
  Facebook data requires manual export steps.
- [ ] Is the data accessible to the team members who will operate the AI
  tools?
- [ ] Are data access credentials documented and stored securely?

### Governance
- [ ] Is there a named data owner — one person responsible for data quality?
- [ ] Is there a documented process for adding new customer records?
- [ ] Is customer data held in compliance with Uganda's Data Protection and
  Privacy Act (2019)? Confirm that consent has been obtained and data is not
  shared without permission.
- [ ] Is there a data retention policy — documenting how long customer records
  are kept and when they are deleted?

## Data Mapping Framework
Follow this step-by-step process to consolidate fragmented data into a single
master customer list:

1. **List all data sources** — WhatsApp, Facebook, email, Excel, accounting
   software, and any others identified in the Required Input.
2. **For each source, record:** what data it contains; its format; estimated
   record count; date last updated.
3. **Identify the primary identifier** — the field that will link records
   across systems. Phone number is the most reliable identifier in Uganda,
   because it is more consistent than email across both urban and peri-urban
   customers.
4. **Export all sources to Excel or CSV** — request exports from WhatsApp
   (chat export), Meta Business Suite (contacts and insights), Gmail
   (contacts), and any CRM or accounting software in use.
5. **Standardise the phone number field** across all exports — remove spaces,
   remove hyphens, ensure all numbers use the +256 international format.
6. **Use VLOOKUP or a de-duplication tool** to identify records appearing in
   multiple sources. Google Sheets has a built-in Remove Duplicates function;
   Excel has a Remove Duplicates tool under the Data tab.
7. **Build a master customer list** — one row per customer, linking all data
   points: name, phone number, email (if available), source systems, last
   transaction date, and any segment tags.

## 30-Day Remediation Plan Template
Apply this plan after the hygiene checklist is complete and the top three
issues are identified:

**Week 1 — Map and assess**
Complete the data mapping framework. Run the hygiene checklist for all 20
items. Identify the top three issues (typically: missing contact details,
duplicate records, and inconsistent product naming). Assign a named owner for
each issue.

**Week 2 — Fix completeness**
Fill missing contact details by following up with customers via WhatsApp or
in-person. Add missing transaction dates from accounting records or receipts.
Ensure all product and service names follow a single agreed naming convention.

**Week 3 — Fix accuracy**
Standardise all phone numbers to +256 format. Correct misspellings in customer
names. Merge duplicate records into the master list. Flag and separate inactive
customers.

**Week 4 — Implement governance**
Assign the named data owner formally. Document the new record process: how new
customers are added, which fields are required, and who is responsible.
Confirm Uganda Data Protection and Privacy Act (2019) compliance — consent
records in place, retention policy documented. Export the final master customer
list and confirm it is ready for AI tool import.

**Output:** a clean master customer list ready for import into the AI tool of
choice, plus a documented data governance process that prevents regression.

## Tool Options
| Tool | Use | EA accessibility | Approx. cost |
|---|---|---|---|
| Google Sheets | Data consolidation and de-duplication | Yes — free | Free |
| Airtable | Structured database with easy import/export | Yes — free tier | Free tier available |
| HubSpot Free CRM | Customer database with basic automation | Yes — free | Free |
| Notion | Flexible database and knowledge base | Yes — free tier | Free tier available |
| Excel | Standard spreadsheet de-duplication | Yes | Included in Office 365 |

For most Ugandan SMEs, Google Sheets is the recommended starting point: it is
free, collaborative, accessible on mobile, and sufficient for up to several
thousand customer records.

## Handoff — Connecting Clean Data to AI Tools
Once the audit and remediation are complete, connect the master customer list
to the relevant AI tools:

- **RAG knowledge base** (see `ai-rag-brand-knowledge-base`) — upload the
  product catalogue and FAQs derived from the clean data
- **Chatbot knowledge base** (see `ai-whatsapp-chatbot-design`) — upload
  approved response templates and policies built from the structured data
- **Segmentation tool** — import the master customer list with segment tags
  for audience targeting
- **Predictive analytics tool** (see `ai-predictive-analytics-social`) —
  import transaction history and engagement history for churn and upsell
  modelling

Do not connect any AI tool until the Week 4 governance step is complete. A
tool connected to unclean data will produce unreliable outputs and undermine
client confidence in AI marketing.

## Quality Criteria
Good output from this skill meets all of the following standards:

- All customer data sources mapped — no source overlooked, including informal
  sources such as verbal records and WhatsApp chat histories
- Data hygiene checklist completed in full — all 20 items scored Yes, No, or
  Partial with priority flags applied to every No and Partial item
- Data mapping framework completed — master customer list built using phone
  number as the primary identifier, with all sources consolidated
- Top three hygiene issues identified with a specific, actionable remediation
  step for each — not generic advice, but concrete next actions for this client
- 30-day remediation plan documented with named owner and weekly milestones —
  not a suggestion but a committed plan
- Data governance framework in place — named data owner, new record process
  documented, and responsibility assigned
- Uganda Data Protection and Privacy Act (2019) compliance confirmed — consent
  documented for all records, data sharing restrictions understood, retention
  policy set
- Clean data handed off to at least one AI tool with a verification step
  confirming that outputs have improved compared to pre-audit baseline

## References
- Venkatesan, R. and Lecinski, J. (2026) *The AI Marketing Canvas*, 2nd edn.
  Stanford University Press.
- Lamplugh, M. (2024) *The AI Marketing Playbook*, 2nd edn. Mercury Learning.
- Ltifi, M. (ed.) (2025) *Advances in Digital Marketing in the Era of
  Artificial Intelligence*. CRC Press.

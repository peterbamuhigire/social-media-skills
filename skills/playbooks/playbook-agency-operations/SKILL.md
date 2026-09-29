---
name: playbook-agency-operations
description: 'Use when an agency needs to run its own business: onboarding, approvals, invoicing, team roles and certifications, QC, client audits of media billing, growth, or white-label and sub-contracted delivery; produces the agency operating manual and partner terms; not for one client''s scope and renewal (use `playbook-client-retainer-management`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Agency Operations Playbook

Produces the agency's own operating manual (onboarding, retainers, approvals, invoicing, QC, reporting, team, growth) and partner terms for white-label or sub-contracted delivery, calibrated to a Uganda and East Africa practice of one to ten people.

<!-- dual-compat-start -->
## Use When
- A new client is signing on: 30-day onboarding checklist, communication channels and the first publishing cycle.
- The agency needs a project management system, a content approval protocol, a quality-control checklist and a reporting rhythm that work across every client.
- Invoicing rules, cash-flow controls, margins, client-concentration limits and the tax obligations to check.
- A client contract lets the client inspect our media bills, rebates and principal-media deals, or our staff's Google and Meta certificates are lapsing: records, disclosures and a renewal register must stand up to scrutiny.
- Our team of two to ten people needs role definitions, delegation rules, hiring stages and a growth roadmap, including AI revenue models such as database reactivation.
- Another agency asks for content delivered white-label under its brand, or work is being sub-contracted out: pricing, NDA, briefing standard, payment terms and exit.

## Do Not Use When
- `playbook-client-retainer-management` for one client's scope, scope creep, monthly check-ins and renewal.
- `playbook-daily-operations-routine` for a manager's daily and weekly working blocks across accounts.
- `biz-dev-pricing-menu` for the priced service menu offered to prospects.
- Stop before signing contracts, sending invoices or committing to a white-label partner without the agency owner's written approval; deliver the draft terms for sign-off.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Agency name, team size (solo, 2–5, 5–10) and new or existing operation | Agency owner | Yes | Ask the intake questions; do not size tools or roles until answered. |
| Client count and typical retainer range (UGX) | Owner's invoices or client list | Yes | Build on a stated assumption and label every money figure illustrative. |
| Tools in use (project management, invoicing, communication) | Owner or delivery lead | Yes | Recommend the tool for the stated team size and mark current state unassessed. |
| Primary challenge (client management, cash flow, team coordination or quality control) | Owner | Yes | Deliver the standard manual without an expanded section and ask again. |
| Partner or sub-contractor terms, brief and end-client data handling | Partner agency or owner | If white-label | Stop partner work; return the evaluation checklist from the white-label reference. |
| Current tax figures and revenue-authority guidance | `chwezi-accounting-doctrine`; URA or KRA | If tax is asked | State no figure; route the question to the finance engine. |

## Workflow

1. Run the intake questions and calibrate: size tools by team size, expand the section for the primary challenge, and note whether systems are being built or refined. Stop if the owner or objective is missing.
2. Build the 30-day onboarding checklist (Day 1–3, 4–7, 8–14, 15–30), retainer tiers, billing protocol and contract essentials from [agency operating procedures](references/agency-operating-procedures.md).
3. Set the project management tool, weekly workflow, content approval protocol (48-hour approval, two revision rounds) and the nine-item quality-control checklist.
4. Write invoicing and cash-flow rules (mandatory invoice fields, Day 8/15/30 chase, one-month float) and the tax note that routes every figure to the finance engine.
5. Set the reporting rhythm and, for teams of two or more, role definitions, delegation rules and performance standards.
6. For growth, retention, AI services or margins, apply [AI revenue and the seven-figure model](references/ai-revenue-and-seven-figure-model.md), the [growth roadmap](references/agency-growth-roadmap.md) and [economics and governance](references/agency-economics-and-governance.md); for partner delivery, use [white-label and partner delivery](references/white-label-and-partner-delivery.md).
7. Check every tax threshold, platform specification and benchmark against a register claim ID or a stated check; correct any unsupported figure and rerun the quality and anti-slop gates before handing the draft to the owner for sign-off.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Agency operating manual (onboarding, retainers, approvals, invoicing, QC, reporting, team) | Agency owner and delivery team | Every procedure names an owner, a deadline and a check; tiers carry UGX ranges and inclusions. |
| Growth and retention plan (Five Ones, CRR target, org structure, AI upsell where relevant) | Agency owner | CRR targets labelled engine policy; Nelson's figures cited as his experience. |
| Draft partner terms for white-label or sub-contracted work | Agency owner, then legal counsel | Pricing, NDA, brief standard, payment terms and exit present; marked draft for sign-off. |
| Assumption and gap register | Agency owner | Each assumed money figure, unverified rate and unassessed check has an owner or next action. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Figure and claim register | Table in the manual | Each tax figure, platform spec and benchmark carries a register ID (for example AD-08, PL-05) or a stated check. |
| Quality Criteria checklist result | Completed checklist | All applicable criteria in the procedures reference ticked or marked `not assessed`. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Signing contracts, sending invoices and committing to a partner need the agency owner's written approval.

## Degraded Mode

Without the owner's team size, client count and retainer range, return the narrowest qualified result and mark the affected checks `not assessed`. The onboarding checklist, approval protocol, QC checklist and reporting rhythm can still be delivered as standard templates.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Work repeatedly misses review or deadline gates | Change capacity, ownership or scope before adding clients. | Retainer growth that breaks delivery. |
| Delivery runs through a white-label or sub-contracting partner, or ownership, attribution or client access is ambiguous | Resolve it in the partner agreement before work starts, using [white-label and partner delivery](references/white-label-and-partner-delivery.md). | Hidden accountability, unpaid work and client conflict. |
| No signed agreement or first payment (50% upfront for new clients) | Do not begin work. | Unpaid delivery and weak cash flow. |
| Client has not approved content by the stated deadline | Reschedule the items to the following week; bill revisions beyond two rounds at UGX 30,000 per post. | Publishing unapproved work and unpaid scope creep. |
| A tax threshold, VAT or withholding figure is requested | Route to `chwezi-accounting-doctrine` and current URA or KRA guidance; state no figure from memory. | Wrong tax advice after a Finance Act change. |
| A dormant contact list is proposed for database reactivation | Apply the compliance gate first: lawful basis, opt-out in every message, registration where required (PL-01, PL-02). | Unlawful messaging and platform bans. |
| A contract is drafted or renewed, or the agency buys media for a client | Apply [commercial governance and contracts](references/commercial-governance-and-contracts.md): CSFA 2025 and ANA 2023 as reference models, audit rights, written opt-in for any non-transparent or principal media, disclosed rebates, the AI schedule (registers `ISBA-IPA-CSFA-2025`, `ANA-MEDIA-CONTRACT-2023`). | Hidden margins, audit disputes and unlicensed AI use. |
| Someone runs a client ad account, or credentials go into a pitch | Check the [certification and competency register](references/certification-and-competency-register.md): current Google Ads (one-year validity) and Meta certifications, reminder 30 days before expiry (registers `GOOGLE-ADS-CERTIFICATIONS`, `META-CERTIFICATION`). | Lapsed or overstated credentials. |
| Monthly CRR falls below 90% | Run a retention review before new acquisition spend (engine policy). | Filling a leaking bucket. |

## Quality Standards

- The 30-day onboarding checklist has day-by-day tasks in four phases (Day 1–3, 4–7, 8–14, 15–30).
- Retainer tiers appear in a table with UGX ranges, inclusions and target client type for all four tiers; client-owned ad spend is shown as pass-through.
- The approval protocol states the 48-hour rule and the two-revision-rounds policy.
- An invoicing tool is justified by team size and the nine mandatory invoice fields are listed.
- The tax note routes every figure to the finance engine instead of quoting thresholds.
- The nine-item QC checklist is a tickable list, and the reporting rhythm covers all four report types with frequency, owner and format.
- No tax threshold, platform specification or benchmark appears without a register claim ID or a stated check; the full criteria list is in the procedures reference.

## Anti-Patterns

- Starting work on a verbal yes. Fix: signed agreement and first payment received before Day 1 tasks begin.
- Collecting approvals image by image on WhatsApp. Fix: one Google Doc or Notion page per batch with caption, platform, date and image brief.
- Quoting VAT or income-tax thresholds from memory. Fix: route to the finance engine and the current revenue-authority guidance.
- Delegating to "the team" in a WhatsApp group. Fix: one owner, a due date and an expected output in the project management tool.
- Presenting Nelson's retention figures or illustrative UGX scenarios as benchmarks. Fix: cite them as his experience or label them illustrative.
- Messaging a client's dormant database because it is "our data". Fix: pass the compliance gate and WhatsApp template and opt-in rules first.
- Accepting white-label work without written terms. Fix: agree pricing, NDA, brief standard, payment terms and exit before starting.

## References

- [Agency operating procedures](references/agency-operating-procedures.md): read when running intake, onboarding, retainers, contracts, tools, invoicing, tax, QC, reporting or team set-up.
- [AI revenue and the seven-figure model](references/ai-revenue-and-seven-figure-model.md): read when pitching AI services, applying the Five Ones, retention rituals, the CRR formula or org structure.
- [Agency growth roadmap](references/agency-growth-roadmap.md): read when planning growth stages, niche, programmes, pricing, hiring and retention rituals.
- [Agency economics and governance](references/agency-economics-and-governance.md): read when setting margins, client concentration limits, team structure, creative reviews, meetings and asset management.
- [White-label and partner delivery](references/white-label-and-partner-delivery.md): read when evaluating, pricing, contracting, briefing or exiting a white-label or sub-contracting partnership with another agency.
- [Commercial governance and contracts](references/commercial-governance-and-contracts.md): read when drafting agency–client agreements, audit and transparency terms, principal-media disclosure or AI terms, and when explaining which UK/US frameworks are reference models for East Africa.
- [Certification and competency register](references/certification-and-competency-register.md): read when tracking Google Ads, Meta and IPA credentials, planning effectiveness training or mapping staff to the CIM 2024 competencies.
- [`01-client-brief`](../../pipeline/01-client-brief/SKILL.md): read when capturing client context at Day 1–3 of onboarding.
- [`meta-reporting`](../../meta-analytics-ops/meta-reporting/SKILL.md): read when producing monthly and quarterly reports.
- [`meta-roi-framework`](../../meta-analytics-ops/meta-roi-framework/SKILL.md): read when calculating return on retainer for quarterly and annual reviews.
- [`playbook-social-media-policy`](../playbook-social-media-policy/SKILL.md): read when setting internal content governance for QC.
- [Client retainer management](../playbook-client-retainer-management/SKILL.md): read when handling one client's scope, check-ins and value-first renewal.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting client-facing copy or the manual itself.
- [East African English standard](../../language/east-african-english/SKILL.md): read when proofreading content in QC.
<!-- dual-compat-end -->

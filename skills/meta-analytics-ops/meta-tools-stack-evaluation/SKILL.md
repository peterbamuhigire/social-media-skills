---
name: meta-tools-stack-evaluation
description: Use when a client asks which marketing or AI tools to keep, cut or buy (scheduling, design, analytics, email, CRM, AI writers), scored for fit, overlap, East African payment access, data governance and cost; produces the stack recommendation, AI vendor scorecards and trial briefs; not for AI maturity scoring (use `ai-readiness-diagnostic`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Meta Tools Stack Evaluation

Produces a structured, client-specific martech tools recommendation calibrated to Uganda/East Africa budgets, infrastructure and team capacity, applying the free-tier-first principle and Uganda DPA 2019 compliance throughout.

<!-- dual-compat-start -->
## Use When

- The client pays for overlapping tools such as Hootsuite, Canva Pro, Mailchimp or several AI writers and wants to know which to keep, cut or replace, and the total monthly subscription cost.
- A small team needs a recommended stack for a zero, Starter or Growth budget, free tiers first.
- The AI tools in use (ChatGPT, Jasper, Canva's AI features) need auditing for fit, whether they can be paid for from Uganda or Kenya with a local card, cost, and whether customer data is safe with them.
- A shortlist of AI vendors must be scored on an eight-factor scorecard, with a 30-day trial brief for each one worth testing.
- Migration priorities are needed before switching platforms so no data or workflow is lost.

## Do Not Use When

- `ai-readiness-diagnostic` for scoring how ready the team, data and processes are for AI.
- `ai-use-case-mapping` for deciding which marketing tasks AI should do.
- `meta-budget-planner` for dividing the whole marketing budget across channels.
- Stop before signing up, entering payment details or granting a tool access to client accounts; recommend only.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Current tools in use, each with monthly cost and how regularly it is used | Client; invoices or card statements | Yes | Stop the audit and removal list; start from the zero-budget stack and mark the current stack `not assessed`. |
| Primary pain points (for example "we miss posting schedules", "we cannot track leads", "design takes too long") | Client team | Yes | Stop; no tool is recommended without a named pain point. |
| Monthly budget for tools in UGX or USD | Client owner | Yes | Default to the zero-budget stack (UGX 0). |
| Team size and technical capacity (independent learners or simple tools only) | Client | Yes | Assume simple, intuitive tools and cap new tools at one per quarter. |
| Whether each tool stores customer personal data, and its privacy policy and DPA status | Vendor documents; client | For CRM and email tools | Flag the tool as not recommendable until a Data Processing Agreement is confirmed. |
| Client name, industry and country/city | Client brief | Yes | Default to East Africa/Uganda. |

The seven intake questions are in [core tools and budget stacks](references/core-tools-and-budget-stacks.md) § Required Input; do not proceed until all seven are collected.

## Workflow

1. Collect the intake; stop and route to `ai-readiness-diagnostic`, `ai-use-case-mapping` or `meta-budget-planner` when the request is AI readiness, AI task selection or whole-budget allocation.
2. Audit the current stack: cost per tool and whether it is used regularly, partially or not at all.
3. Map each pain point to a tool category (scheduling, design, analytics, email, CRM, project management) using the core tables, free tier first.
4. Run the five-question test on every candidate and every current tool; add the AI tool audit or the vendor scorecard when AI tools are in scope.
5. Select the zero, Starter or Growth stack as the default and adjust it to the pain points, stating costs in UGX with USD equivalents.
6. Build the implementation roadmap (no more than 2 new tools per quarter, 2–4 hours training each) and the DPA note.
7. Check the document against the quality standards; correct any tool without a pain point, mobile check or DPA status and rerun the cost totals before release.

Principles, tool tables, stacks and the document layout are in [core tools and budget stacks](references/core-tools-and-budget-stacks.md).

## Budget stacks and the five-question test

| Stack | Monthly budget | Adds | Total |
|---|---|---|---|
| Zero | Free tools only | Meta Business Suite, Canva, CapCut, Meta Insights + GA4, Mailerlite or MailChimp, Google Sheets CRM, Trello | UGX 0 |
| Starter | UGX 50,000–150,000 (~$13–40) | Canva Pro (~UGX 50,000), Buffer paid (~UGX 22,000) | ~UGX 72,000/month |
| Growth | UGX 150,000–400,000 (~$40–105) | Mailerlite paid (~UGX 34,000), HubSpot Starter (~UGX 56,000), Publer (~UGX 45,000) | ~UGX 207,000/month |

Five-question test: (1) solves a specific, named problem today; (2) free tier to test first; (3) the team will actually use it; (4) works on a smartphone as well as a laptop; (5) if it takes customer personal data, a DPA-compliant data processing agreement is in place. If question 1, 3 or 5 is No, do not recommend the tool and document the reason.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Tools evaluation document: current stack audit, recommended stack, tools to remove, implementation roadmap, total monthly cost, DPA note | Client owner and marketing lead | All six sections in order; every recommended tool maps to a named pain point. |
| Five-question test as a named section | Client team for future tool decisions | Applied to the client's specific tool enquiries, with reasons for each No. |
| AI tool audit or AI vendor scorecards with 30-day experiment briefs | Client owner | Built with the AI references; EA payment, UGX cost and DPA checks shown. |
| Migration priorities | Client lead | Data and workflows to move are listed before any platform switch. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Stack cost register | Table: tool, tier, monthly cost in UGX and USD, usage status, source date | Totals recompute; USD prices are dated or labelled for verification. |
| DPA and data-flow check | Table: tool, customer data stored, privacy policy reviewed, DPA status | Every tool storing customer data has a DPA status; unconfirmed ones are flagged. |
| Mobile and payment check | Pass/fail per tool on mobile use and local card payment | Desktop-only tools are rejected or flagged. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Signing up, entering payment details or granting a tool access to client accounts is outside this skill; recommend only.

## Degraded Mode

Without the current tool list, costs and named pain points, return the narrowest qualified result and mark the affected checks `not assessed`. The zero-budget stack, the five-question test and a DPA checklist can still be delivered as a starting point.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A tool fails question 1, 3 or 5 of the five-question test | Do not recommend it; document the reason; list current tools that fail under Tools to Remove. | Paying for tools nobody uses or that expose customer data. |
| A new client, or a team not yet using free tools consistently | Start with the zero-budget stack; upgrade only after one quarter of consistent use. | Over-tooled, under-skilled teams. |
| A tool is desktop-only or degrades badly on mobile data | Reject it or flag it. | Tools the team cannot use from a smartphone. |
| A tool stores customer personal data (CRM, email) | Confirm a Data Processing Agreement under the Uganda Data Protection and Privacy Act 2019 before recommending it. | Unlawful processing of customer data. |
| The roadmap would add more than 1–2 new tools in a quarter | Phase them across quarters with 2–4 hours training per tool. | Tools abandoned before the team learns them. |
| The client needs an AI tool audit or AI stack by function (content, SEO, social, email, automation, analytics, paid ads, influencer) | Apply the five-question AI test, category tables and budget profiles A–C in [ai-tool-fit-access-cost-governance](references/ai-tool-fit-access-cost-governance.md). | AI tools recommended on novelty, or without EA payment, UGX cost or DPA checks. |
| The client has a shortlist of up to four named AI tools for one marketing problem | Score each on the eight-factor /40 scorecard and write 30-day experiment briefs per [ai-vendor-due-diligence](references/ai-vendor-due-diligence.md). | Buying an AI tool before a measured experiment shows value. |
| The requested outcome belongs to `meta-budget-planner` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Quality Standards

- All six tool categories (scheduling, design, analytics, email, CRM, project management) are covered with a reference table and at least one recommendation per category.
- Three budget stacks are presented with costs stated in UGX and USD equivalents.
- The five-question evaluation framework is present and applied to the client's specific tool enquiries.
- Mobile accessibility is stated as a hard requirement and applied to reject or flag any desktop-only tools.
- Uganda DPA 2019 is cited and applied to all tools that process customer personal data.
- The free-tier-first principle is stated explicitly and the zero-budget stack is always the starting point before upgrades.
- The training time budget (2–4 hours per tool, maximum 1–2 new tools per quarter) is included in the implementation roadmap.
- Every recommended tool is mapped to a named client pain point from the intake; no hypothetical recommendations.

## Anti-Patterns

- Recommending a sophisticated tool for a hypothetical need. Fix: map every tool to a pain point the client has today.
- Recommending Hootsuite ($99/month) or Sprout Social ($249/month) to an EA SME. Fix: use Meta Business Suite, Buffer or Looker Studio unless the client is an agency at that scale.
- Uploading customer data to a CRM or email platform before the privacy review. Fix: confirm the DPA first; keep Google Sheets CRM internal.
- Introducing several tools at once. Fix: no more than 1–2 new tools per quarter with training time budgeted.
- Treating USD list prices as fixed. Fix: date each price and verify it before stating it to the client.
- Switching platforms before listing what must move. Fix: set migration priorities so no data or workflow is lost.
- Absorbing `meta-budget-planner` into this workflow. Fix: route the neighbouring output and hand over verified inputs.

## References

- [Core tools and budget stacks](references/core-tools-and-budget-stacks.md): read when running the intake, looking up tool tables, choosing a budget stack, applying the five-question test or laying out the evaluation document.
- [ai-tool-fit-access-cost-governance](references/ai-tool-fit-access-cost-governance.md): read when auditing AI marketing tools or recommending an AI stack by function and budget profile.
- [ai-vendor-due-diligence](references/ai-vendor-due-diligence.md): read when scoring a named shortlist of AI vendors and writing 30-day experiment briefs.
- [`meta-budget-planner`](../meta-budget-planner/SKILL.md): read when calculating total martech spend as part of a broader marketing budget.
- [AI-assisted production workflow](../../playbooks/playbook-content-production/references/ai-assisted-production-workflow.md) in `playbook-content-production`: read when AI writing or content generation tools are part of the recommended stack.
- [`meta-testing-framework`](../meta-testing-framework/SKILL.md): read when the client wants to A/B test tools before committing to a paid tier.
- [`playbook-agency-operations`](../../playbooks/playbook-agency-operations/SKILL.md): read when building a stack for an agency managing multiple clients rather than a single brand.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the document; [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

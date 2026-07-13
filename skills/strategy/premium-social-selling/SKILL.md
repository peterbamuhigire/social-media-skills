---
name: premium-social-selling
description: Use when the main deliverable concerns high-value social selling, executive outreach, nurture, authority, and conversion; use playbook-social-selling when that neighbouring workflow owns the primary decision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Premium Social Selling

<!-- dual-compat-start -->
## Use When

- Use this skill for high-value social selling, executive outreach, nurture, authority, and conversion.
- Use it when the requested deliverable needs the domain decisions and acceptance checks below.

## Do Not Use When

- Use `playbook-social-selling` when that neighbouring workflow owns the main decision or deliverable.
- Do not proceed when required evidence, approval, or safety review is absent; return the missing-input path instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, market, and intended decision | Client or approved brief | yes | Ask for it or state a narrow working assumption |
| Existing channel, content, commercial, or performance evidence relevant to high-value social selling, executive outreach, nurture, authority, and conversion | Client systems, supplied files, or verified research | conditional | Mark the check unassessed and avoid performance claims |
| Approval, policy, budget, access, or risk constraints | Accountable client owner | conditional | Stop before publishing, spending, collecting data, or making regulated claims |

## Workflow

1. Confirm the decision, consumer, market, and evidence boundary; distinguish the request from `playbook-social-selling`.
2. Inspect supplied artefacts and record missing or unverified inputs before drafting.
3. Apply the domain framework in this skill and use the decision rule below at each branch.
4. Stop for approval before publishing, spending, contacting people, changing live systems, or making regulated claims.
5. Review the deliverable against the quality and anti-slop gates; if a check fails, correct it and rerun the affected check.
6. Hand off the artefacts, assumptions, evidence, and unresolved risks to the named consumer.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| High-value social selling, executive outreach, nurture, authority, and conversion deliverable | Client decision-maker or delivery team | Names the chosen route, owners, sequence, assumptions, and measurable acceptance checks |
| Decision and risk record | Reviewer or implementer | Links each recommendation to supplied evidence or labels it as an assumption |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Input and assumption register | Table or annotated brief | Missing and unverified items are visible, not treated as passed |
| Release check | Completed quality checklist | All blocking findings are fixed or the deliverable is explicitly withheld |

## Capability and Permission Boundaries

Read and search are the minimum capabilities. Analysis and planning remain read-only. Edit only files placed in scope; publishing, outreach, spend, personal-data processing, production changes, and certification claims require explicit authority and evidence of success.

## Degraded Mode

If files, tools, network, current evidence, rendering, or authorised access are unavailable, return the narrowest useful qualified deliverable. Mark each unavailable check `not assessed`; never convert it into a pass or invent market facts.

## Decision Rules

| Choice condition | Action | Failure or risk avoided |
|---|---|---|
| The buyer is senior, affluent, enterprise, or high-ticket | Use proof-led, selective outreach and a longer trust path | Volume tactics damage premium positioning |
| Evidence is contradictory or materially incomplete | Pause the affected recommendation and request the accountable source | Confident advice built on an unresolved premise |
| Authority is limited to analysis or planning | Deliver a read-only plan and approval checklist | Unauthorised publication, spend, outreach, or data use |

## Quality Standards

- Keep Uganda/East Africa, British English, EAT, UGX, and WhatsApp-first assumptions explicit where they apply.
- Tie recommendations to observed evidence, a named assumption, or a verification action.
- Give the next operator enough detail to execute without guessing ownership, sequence, or acceptance.
- Apply `ai-marketing/anti-ai-slop` during drafting and block release on an F from `ai-marketing/ai-slop-audit`.

## Anti-Patterns

- Inventing a client metric, audience fact, price, partner, or platform rule. Fix: verify it or label the decision provisional.
- Treating a missing tool, source, render, or approval as a passed check. Fix: mark it `not assessed` and narrow the output.
- Producing channel tactics before defining the decision and consumer. Fix: state the required outcome and handoff first.
- Copying a global template without adapting Uganda/East Africa access, language, payment, or trust conditions. Fix: record which local assumptions apply.
- Recommending publication, outreach, spend, data collection, or a regulated claim without authority. Fix: stop at an approval-ready draft.
- Reporting activity as success without an acceptance condition. Fix: name the observable result and evidence source.

## References

- [AGENTS.md](../../../AGENTS.md)
<!-- dual-compat-end -->

## Use When

- A social or digital strategy must sell premium products, high-ticket services, agency offers, executive advisory, enterprise software, luxury/lifestyle products, or affluent-market experiences.
- The client needs LinkedIn/social authority, lead magnets, email nurture, outbound contact campaigns, or sales follow-up for high-value prospects.
- The goal is fewer better leads, higher trust, stronger positioning, and premium conversion rather than broad low-quality reach.

## Workflow

1. Define the premium audience: buyer role, status context, pain/risk, platform behaviour, proof expectations, and decision path.
2. Build authority positioning: expertise, point of view, proof, case studies, founder story, contrarian insight, and category clarity.
3. Design lead capture: premium lead magnet, diagnostic, private briefing, consultation, benchmark, audit, calculator, invitation, or executive roundtable.
4. Design nurture: email/social sequence that educates, proves, handles risk, and invites a concrete next step.
5. Design outreach: named-account/contact campaign, referral path, executive assistant/gatekeeper handling, personalised reason to meet, and follow-up cadence.
6. Align sales: qualification, discovery, objection handling, proposal handoff, CRM stages, and response-time SLA.
7. Apply `premium-commercial-writing` to the authority content, lead magnet promise, outreach language, and offer framing.
8. Run the premium social selling gate before publishing the strategy.

## Quality Bar

- Content attracts the right buyer and repels low-fit buyers.
- Social proof is specific, not decorative.
- The CTA matches buyer temperature: follow, download, reply, book diagnostic, attend briefing, request proposal, or start pilot.
- Outreach is researched and relevant, not spam.
- Premium brands do not over-promote, over-discount, or sound desperate.

## Outputs

- Premium social selling strategy.
- LinkedIn/content authority plan.
- Lead magnet and nurture sequence architecture.
- Executive outreach and follow-up plan.
- Sales-marketing alignment notes.

## References

- `references/premium-social-selling-gate.md` - detailed quality gate for high-ticket social/digital selling.
- `../premium-commercial-writing/SKILL.md` - cross-cutting writing layer for premium proof, value framing, price integrity, search authority, and high-trust conversion copy.

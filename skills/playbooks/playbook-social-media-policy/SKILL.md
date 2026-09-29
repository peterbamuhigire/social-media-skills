---
name: playbook-social-media-policy
description: 'Use when an organisation needs rules for how staff and agencies use social media: conduct, confidential information, disclosure, approvals and consequences, plus a RACI, certification, escalation levels and account access; produces the staff policy and governance model; not for rules on AI-made content (use `policy-ai-content-ethics`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Social Media Policy

Drafts the staff-facing social media policy (conduct, confidentiality, disclosure, approvals, consequences and acknowledgement) and, where needed, the governance behind it, as a starting framework for the client's legal counsel to review.

<!-- dual-compat-start -->
## Use When
- Staff post about work on personal accounts; clear dos and don'ts, prohibited content and disciplinary consequences are needed.
- Decide who may speak for the company, how customer enquiries on personal channels are handled and what employees must disclose.
- Set an approval process for employee-generated content and an annual policy review with staff acknowledgement.
- Build governance: a RACI for who posts and approves, staff certification before access, escalation levels, a command centre and agency password controls.

## Do Not Use When
- `policy-ai-content-ethics` for AI disclosure, AI copyright ownership and cultural bias checks.
- `playbook-crisis-communications` for an incident already under way.
- `playbook-social-selling` for encouraging staff to share company posts.
- Stop short of legal advice; the client's counsel must review the policy against employment contracts before it is issued.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client company name and country/city | Client | Yes | Default the jurisdiction to Uganda/East Africa; stop if the company name is unknown. |
| Designated social media approver (name and job title) | Client leadership | Yes | Leave the approval section as a marked gap; do not issue the policy. |
| HR contact name for violations and discipline | Client HR | Yes | Hold the consequences section as a draft for HR to complete. |
| Official customer contact channel (WhatsApp number or email) | Client | Yes | Mark the enquiry-handling script incomplete; do not invent a number. |
| Policy effective date and existing employment contracts or HR policy | Client HR or counsel | Yes | Mark consequences as a guide only, pending alignment with contracts. |
| Account ownership, agency access and escalation roles | Client operations | For governance | Deliver the staff policy only and list the governance gaps. |

## Workflow

1. Collect the required inputs; stop if the company name, approver or HR contact is missing.
2. Place the consultant's legal note before the policy body and confirm the jurisdiction's current law position before relying on it.
3. Draft the policy from the [staff policy template](references/staff-policy-template.md): purpose and scope, encouraged behaviours, prohibited activities, customer enquiries via personal channels, disclosure, approval process, consequences, review and acknowledgement.
4. Replace every placeholder with the client's actual names and contact details and tailor the disclosure examples to the client's business type.
5. Where the organisation needs RACI, certification, escalation levels, a command centre or agency controls, build them with [governance roles, access and approvals](references/governance-roles-access-and-approvals.md).
6. Route clauses that depend on law, employment terms or a collective agreement to qualified review.
7. Check the draft against the quality standards and the anti-slop gate; correct any failed item and rerun the check before hand-off to counsel.

## Legal standing of the template

This document is a starting framework based on established professional practice. It does not constitute legal advice. Advise the client to have this policy reviewed by their legal counsel and aligned with their existing employment contracts before issuing it to staff. In Uganda, align with the Computer Misuse Act 2011 as it stands after the Constitutional Court ruling of 17 March 2026: the Computer Misuse (Amendment) Act 2022 is void, several provisions of the principal Act and criminal libel were struck, and the remainder of the principal Act remains in force (register UG-CMA-2022-VOID-2026; verify the exact section list against the judgment on ULII before relying on it). Across East Africa, align with any applicable sector-specific regulations.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Staff social media policy document | Client HR, legal counsel, then all staff | Sections 1–8 complete with the client's names; legal note before the body; no visible placeholders. |
| Employee acknowledgement form | Client HR | Standalone, signable section with name, job title, signature and date. |
| Governance model (reporting line, RACI, certification, escalation, SMCC, agency controls) | Client leadership | Every high-risk account and approval step has an accountable owner. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Law and register check | Note citing UG-CMA-2022-VOID-2026 and the disclosure registers KE-01, UG-01, TZ-01 with check dates | Current position confirmed from the source or marked `not assessed`; never stated as legal advice. |
| Counsel review record | Dated sign-off or open-item list | The policy is not issued to staff until counsel has reviewed it against employment contracts. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Issuing the policy to staff, changing account access or passwords and starting disciplinary action are client HR and counsel decisions.

## Degraded Mode

Without counsel review and the client's employment contracts, return the narrowest qualified result and mark the affected checks `not assessed`. A complete draft policy with the legal note, marked as not yet issuable, can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A clause depends on law, employment terms or collective agreement | Route it for qualified review before adoption | Presenting operational guidance as settled law |
| No one owns a high-risk account or approval step, or the organisation needs RACI, escalation, certification or agency controls | Stop rollout, assign an accountable role and apply [governance roles, access and approvals](references/governance-roles-access-and-approvals.md) | Orphaned access and decisions |
| The Ugandan legal basis for conduct rules is cited | Cite the Computer Misuse Act 2011 as it stands after 17 March 2026 and verify the section list on ULII | Relying on a voided amendment or struck provision |
| An employee post references the company | Require disclosure of the employment relationship; check the jurisdiction register before stating any statute | Hidden endorsement and misleading-representation risk |
| A customer contacts staff on a personal account | Acknowledge, direct to the official channel, do not resolve personally, notify the manager | Personal accounts turning into unofficial service desks |
| A post uses company branding or unreleased news | Route to the designated approver, with a reply within 24 hours (48 hours on a Friday or public holiday) | Unapproved announcements |
| A violation occurs | Classify as minor, moderate or serious and involve the HR contact in all formal proceedings | Disproportionate or contract-inconsistent discipline |

## Quality Standards

- Every section uses the client's actual company name, approver name and contact details; no visible placeholder text in the delivered version.
- Prohibited activities are specific and unambiguous: each item names a concrete action or content type, not a vague principle.
- The customer-enquiry section gives word-for-word example language employees can use, not only a description.
- The disclosure section includes worked examples relevant to the client's business type.
- The consequences table clearly separates minor, moderate and serious violations with proportionate responses.
- The consultant's legal disclaimer is present and positioned before the policy body.
- The employee acknowledgement is a standalone, signable section.
- British English throughout; no American spellings in the delivered document.

## Anti-Patterns

- Issuing the template as legal advice. Fix: keep the legal note and have counsel review it against employment contracts before issue.
- Vague prohibitions such as "be sensible online". Fix: list the concrete content types, as in the confidential-information list.
- Restricting employees' lawful personal opinions. Fix: limit the policy to how the company is represented and what company information may be shared.
- Letting staff move a customer or their data into a private channel. Fix: use the official route, request only the minimum information and document who owns the handoff.
- Allowing fake reviews, customer impersonation or anonymous promotional accounts. Fix: prohibit them outright as a serious violation.
- Fixing consequences without HR. Fix: treat the severity table as a guide aligned to the client's disciplinary procedure.

## References

- [Staff policy template](references/staff-policy-template.md): read when collecting the policy inputs and drafting the policy document, scripts, consequences table and acknowledgement.
- [Governance roles, access and approvals](references/governance-roles-access-and-approvals.md): read when the client needs the governance behind the policy: reporting line, RACI, certification, escalation levels, SMCC, agency SLAs, after-action reviews or a social media business plan.
- [Influencer term sheet and disclosure register](../../pipeline/08-influencer-marketing-strategy/references/influencer-term-sheet-and-disclosure.md): read when checking the KE-01, UG-01 and TZ-01 disclosure register entries.
- [`policy-ai-content-ethics`](../../policies/policy-ai-content-ethics/SKILL.md): read when the rules concern AI-made content.
- [`playbook-crisis-communications`](../playbook-crisis-communications/SKILL.md): read when an incident is already under way.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read before any legal or regulatory claim leaves the draft.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting the policy wording.
- [East African English standard](../../language/east-african-english/SKILL.md): read when setting tone and spelling for staff-facing text.
<!-- dual-compat-end -->

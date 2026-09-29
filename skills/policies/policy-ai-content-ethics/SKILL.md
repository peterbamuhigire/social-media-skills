---
name: policy-ai-content-ethics
description: 'Use when an organisation needs rules for AI-made posts, images and ads: disclosure, SynthID watermarks, copyright ownership, bias checks on AI images of East Africans, EU AI Act notes and sector limits; produces the AI content policy, bias audit sign-off and IP record; not for staff social media conduct (use `playbook-social-media-policy`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI Content Ethics Policy

Produces a client's AI Content Policy, the consultant's per-piece checklist, the cultural bias audit sign-off and the AI IP record, so that a named human stands between every AI output and publication.

<!-- dual-compat-start -->
## Use When
- The team uses ChatGPT, Claude, Midjourney or Canva AI for client work and needs a written policy on what is allowed, disclosed and approved.
- Decide how AI-assisted posts and ads are labelled, watermarked with SynthID or similar, and recorded for provenance.
- Audit AI-generated images, personas or copy for Western cultural bias and misrepresentation of East Africans before delivery, with a qualified reviewer signing off.
- Work out who owns AI-assisted deliverables, whether they can be registered for copyright and what the contract should say.
- Set tighter AI rules for health, finance, NGO or donor, and political or public-sector clients, and note EU AI Act duties for cross-border work.

## Do Not Use When
- `playbook-social-media-policy` for staff conduct on social media and posting governance.
- `playbook-content-production` for the day-to-day AI drafting workflow.
- `anti-ai-slop` for humanising an AI-assisted draft.
- Stop short of a binding legal opinion on copyright or regulation; refer the stated issue to qualified counsel.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client business name, industry and primary goal for the policy (donor requirement, brand protection, formalising practice, audience enquiry) | Accountable sponsor or approved brief | Yes | Stop and request sponsor direction; do not generate a policy for an unnamed client. |
| Country and city; audience type (B2B professionals, general consumers, public sector, NGO/donor) | Client | Yes | Default to Uganda/Kampala; use general-consumer disclosure wording and flag it for review. |
| Client's AI awareness (Yes / No / Partial) and publishing voice (own name, persona, brand voice or anonymous channel) | Client | Yes | Record awareness as unconfirmed and omit persona clauses until the client confirms them. |
| Existing brand guidelines, code of conduct, donor compliance framework or prior ethics policy | HR, legal, communications or governance owner | Conditional | Record the gap and avoid claims of alignment. |
| Regulatory environment: UDPPA 2019, Kenya ODPC, donor rules (USAID, EU, UN), CMA/BoU, Ministry of Health, NITA-U / Electoral Commission | Client; current official source or qualified adviser | Yes | Draft general commercial clauses only; mark legal conclusions `not assessed` and require review. |
| AI tools in use and the named reviewer who signs off | Client and agency | Yes | List the tools as `[Tool]` placeholders; the policy cannot be signed until a reviewer is named. |

The full intake wording is in [policy intake and template](references/policy-intake-and-template.md#required-inputs-intake-questions).

## Workflow

1. Ask every intake question before generating output; stop if the client, goal or decision owner is missing, and route staff-conduct questions to `playbook-social-media-policy`.
2. Write the three-paragraph "why it matters" framing (production risk, audience trust in the EA context, protection for all parties) and the five-principles table, adapted to the sector and audience.
3. Generate the policy from the [template](references/policy-intake-and-template.md#section-2--ai-content-ethics-policy-template); fill every placeholder and omit, rather than leave blank, any clause whose regulatory option was not selected. Name an owner for each internal operating rule.
4. Add the clauses the decision rules trigger (attribution, IP, watermarking, training-data bias, EU AI Act, additional ethical requirements) from [policy clauses and checklists](references/policy-clauses-and-checklists.md), and the sector subsections from [sector guidance](references/sector-specific-ai-guidance.md).
5. For AI content depicting people or communities, run the signed [cultural bias audit](references/cultural-bias-audit-protocol.md); for ownership, registration or licensing questions, apply the [AI IP and copyright policy](references/ai-ip-and-copyright-policy.md) and its legal-referral triggers.
6. Verify every legal and regulatory claim against the governing source; where a claim cannot be verified, qualify it or refer it to counsel and stop short of a binding legal opinion.
7. Check the draft against the quality standards and the consultant checklist; correct any failing clause and rerun the check before hand-off for client signature.

## The five ethical principles

Apply throughout the policy; cite Ltifi (2025) and Johnsen (2024) on first use.

| Principle | Definition | Practical application |
|---|---|---|
| **Transparency** | Disclose AI use honestly to clients and audiences | State which tools are used; label substantially AI-generated content |
| **Fairness** | Monitor AI outputs for bias and discriminatory framing | Review outputs for stereotyping; audit targeting logic quarterly |
| **Nonmaleficence** | Do no harm — do not use AI to deceive, manipulate, or demean | Prohibit fake testimonials, deepfakes, and psychological targeting |
| **Accountability** | Humans remain responsible for AI output at all times | Named reviewer signs off every published piece |
| **Privacy** | Protect personal data from AI tools and cloud systems | No PII entered into any AI prompt under any circumstances |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Client AI Content Policy (purpose, tools, human review, accuracy, brand voice, disclosure, prohibited uses, data and privacy, compliance and review, signature block) | Client owner; agency team | No unfilled placeholders; every triggered clause is present; legal claims are cited or marked for counsel. |
| Consultant's internal AI ethics checklist | Agency reviewer, per piece of content | Run per piece, not per campaign; includes data-leakage and jailbreak items. |
| Cultural bias audit sign-off | Client approver | Signed by a reviewer with direct cultural knowledge of the community depicted. |
| AI IP and provenance record | Client owner; IP solicitor if referred | Human contribution and watermarking status are documented per deliverable. |
| Assumption and gap register | Approver | Every missing source, unassessed check and required approval has an owner or next action. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Legal and regulatory source record | Table: claim, governing source, date checked, status | Each law, article and register reference traces to a source or is marked `not assessed`. |
| Completed per-piece checklist | Checklist with reviewer name and date | Every item ticked or its failure recorded; human approval precedes publication. |
| Watermark and provenance log | Project-file entry per asset | Names which assets were AI-generated at source and confirms watermarking before editing or delivery. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. This skill drafts policy text and records; it does not give a binding legal opinion on copyright or regulation.

## Degraded Mode

Without the client's regulatory environment or a current legal source, return the narrowest qualified result and mark the affected checks `not assessed`. The five-principles framing, the policy template with general commercial clauses and the per-piece checklist can still be delivered, with legal clauses flagged for counsel.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| AI-generated content depicts people, communities or cultural practices | Run the signed pre-delivery cultural bias audit in `references/cultural-bias-audit-protocol.md`; the reviewer must have direct cultural knowledge of the community. | Western-default, stereotyped or conflated representation. |
| Client asks who owns AI-assisted work, wants to register/licence it, or needs a standalone IP policy | Apply `references/ai-ip-and-copyright-policy.md`, including its legal-referral triggers. | False ownership claim or unsupported legal assurance. |
| Content is substantially AI-generated with minimal human editing, or a virtual persona represents the brand | Label it with specific attribution ("AI-generated [specific element], art-directed and revised by [human team]"); disclose a persona in every post. | Vague "Made with AI" labels and undisclosed AI identity. |
| Thought leadership, opinion, personal brand or donor narrative content, or an attributed quote | Apply a Proof of Human signal and get the named individual's approval of the text. | Misrepresented human authorship. |
| Client distributes to EU audiences, receives EU donor funding with content rules, or runs EU-facing channels | Add the EU AI Act Article 50 note from [AI transparency and provenance](references/ai-transparency-and-provenance.md#7-eu-ai-act-article-50-eu-facing-work-only) (applies from 2 Aug 2026, register `EU-AI-ACT-ART50-FAQ`; primary text `NOT_ASSESSED`) and refer to a solicitor familiar with the Act. | Citing draft article numbers as settled law. |
| An AI-assisted asset is about to be published or trafficked | Record the disclosure decision with the risk-based table in [AI transparency and provenance](references/ai-transparency-and-provenance.md#3-risk-based-disclosure-decision-table) (IAB v2 thresholds, register `IAB-AI-DISCLOSURE-V2-2026`), label in the creative unless the platform is confirmed to render the label, and log C2PA and watermark status. | Blanket "Made with AI" labels, or a photorealistic synthetic person published unlabelled. |
| Client is in health, finance, legal, NGO/donor or political/public-sector work | Include every applicable sector subsection and require qualified-professional review of the output. | Regulated content published on AI output alone. |
| AI personalisation or targeting is planned | Require a demographic fairness audit before deployment, a documented data-minimisation rationale, no protected characteristics as primary targeting variables, and quarterly bias and drift reviews; flag each national data-protection regime. | Discriminatory targeting and cross-border non-compliance. |
| A rule depends on law, contract or platform terms, or an exception could expose people, rights or confidential data | Verify and cite the governing source; escalate before approval or publication. | Unsupported compliance claim or irreversible harm. |

## Quality Standards

- The policy template is complete: every bracketed field is filled with client-specific information from the intake.
- The five ethical principles appear as a table cited to Ltifi (2025) and Johnsen (2024).
- Prohibited uses name fake testimonials, deepfakes, bot engagement, fabricated beneficiary stories, filter-bubble risk and copyright/ownership uncertainty.
- The Disclosure clause carries the Proof of Human signal and the virtual-influencer disclosure requirement.
- Every AI-assisted asset has a recorded disclosure decision (threshold met or not, label applied or not) and marketer accountability is stated per the ICC Code 2024 (register `PREMIUM-ICC-2026`).
- The data and privacy clause bars both PII and confidential business information from cloud AI tools, names the Uganda Data Protection and Privacy Act 2019 and cites the Samsung incident (Venkatesan and Lecinski, 2026).
- Human review is stated in both the policy and the per-piece checklist; AI output is never published without human approval.
- Sector guidance covers at least health and finance with specific, actionable instructions, plus every other sector relevant to the client.
- The document is in British English throughout; the full criteria list is in [policy clauses and checklists](references/policy-clauses-and-checklists.md#quality-criteria).

## Anti-Patterns

- Publishing AI output without a named human reviewer. Fix: require sign-off per piece through the consultant checklist.
- Labelling content "Made with AI" and nothing more. Fix: state which element the AI made and which human art-directed and revised it.
- Pasting customer data, PII or strategy documents into a cloud AI tool. Fix: treat AI chat interfaces as public-facing; keep such data out of every prompt.
- Claiming copyright in AI output with minimal human input. Fix: document human contribution per deliverable and refer registration or licensing to an IP solicitor.
- Approving AI imagery of East Africans without a culturally qualified reviewer. Fix: run the cultural bias audit with a reviewer who knows the community depicted.
- Trusting AI for vernacular copy or Uganda-specific facts. Fix: require fluent native-speaker review and verify prices, bodies and programmes against current primary sources.
- Stating volatile platform or legal details from memory. Fix: verify the current official source or omit the claim.

## References

- [Policy intake and template](references/policy-intake-and-template.md): read when running the intake, writing the rationale or generating the client policy document.
- [Policy clauses and checklists](references/policy-clauses-and-checklists.md): read when adding attribution, IP, watermarking, bias-risk, EU AI Act or additional ethical clauses, running the per-piece checklist, applying East Africa considerations or checking the full quality criteria and citations.
- [Cultural bias audit protocol](references/cultural-bias-audit-protocol.md): read when AI content depicting people or communities needs a signed pre-delivery bias audit.
- [AI IP and copyright policy](references/ai-ip-and-copyright-policy.md): read when a client needs AI IP ownership, copyright threshold, disclosure wording, provenance records or IP-solicitor referral.
- [AI transparency and provenance](references/ai-transparency-and-provenance.md): read when deciding whether and how to label AI content (IAB v2 risk-based table), recording C2PA or IPTC provenance, checking Meta and TikTok AI labels, applying EU AI Act Article 50, or aligning the policy with ISO/IEC 42001 and NIST AI 600-1.
- [Sector-specific AI guidance](references/sector-specific-ai-guidance.md): read when the client is in health, finance, NGO/donor or political/public-sector work.
- [AI-assisted production workflow](../../playbooks/playbook-content-production/references/ai-assisted-production-workflow.md): read when setting up or auditing the client's AI-assisted production process.
- [`playbook-social-media-policy`](../../playbooks/playbook-social-media-policy/SKILL.md): read when the AI policy sits within or alongside the broader social media policy.
- [`04-brand-voice-intake`](../../pipeline/04-brand-voice-intake/SKILL.md): read when capturing the brand voice AI tools must be briefed against.
- [Legal/market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read before release; verify time-sensitive claims before use.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when checking AI-assisted copy before delivery.
- [East African English standard](../../language/east-african-english/SKILL.md): read when writing the policy text.
<!-- dual-compat-end -->

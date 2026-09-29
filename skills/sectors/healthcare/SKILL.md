---
name: healthcare
description: Use when a hospital, clinic, pharmacy, health NGO or insurer in East Africa needs social content, patient trust, misinformation replies or complaint handling; produces the health-sector social plan, patient-safe content rules and response protocol; not for hotels, restaurants or spa resorts (use `hospitality-hotel-restaurant`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Healthcare Sector Social Media

Plans social media for East African healthcare organisations and individual medical professionals, where misinformation about medicines, vaccines and treatment can cause direct patient harm. Trust, patient privacy and clinician sign-off come before reach.

<!-- dual-compat-start -->
## Use When

- A hospital, clinic, pharmacy, diagnostic lab or health NGO wants a social media plan patients will trust.
- Health posts must avoid unverified clinical claims, patient photos or records, and follow consent and privacy rules.
- False health rumours, miracle-cure claims or vaccine myths are spreading and need a calm, sourced reply plan.
- Complaints, trolls or a patient-safety incident on social need a response and escalation protocol.
- Doctors, nurses and staff need rules for what they may post about work on their own accounts.

## Do Not Use When

- `hospitality-hotel-restaurant` for hotels, restaurants, venues and spa or wellness resorts.
- `policy-ai-content-ethics` for the organisation's AI content ethics policy.
- `playbook-crisis-communications` for running a declared organisation-wide crisis.
- Stop before publishing any clinical claim, patient story or image without clinician sign-off and documented consent.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client type (hospital, clinic, NGO, pharmaceutical, public health department, or individual medical professional), name and specialty | Client | Yes | Ask; platform priorities differ for organisations and individuals. |
| Country/city | Client | Yes | Default to Uganda. |
| Primary goal (patient education, reputation, advocacy, crisis response, staff communications, professional brand, clinical knowledge-sharing) and target audiences | Client brief | Yes | Ask; do not set the complexity level or stakeholder map without it. |
| Current social presence: active platforms and approximate follower counts | Client; page exports | Conditional | Plan from zero and mark baseline `not assessed`; no performance claims. |
| Key compliance concern and existing social media policy with its key provisions | Client compliance or legal owner | Yes | Draft the 4-component policy framework as a proposal for review. |
| Clinician reviewer and consent records for any patient content | Client clinical governance | Yes, before release | Hold every clinical claim, patient story or image as an unpublishable draft. |

## Workflow

1. Ask the eight intake questions in the [strategy method](references/health-sector-strategy-method.md#required-input); distinguish the request from `policy-ai-content-ethics` and `playbook-crisis-communications`.
2. Set the complexity level (1–4) with Parsons' 4-Level Complexity Model and scale the strategy depth to it.
3. Map the stakeholders from the 11-stakeholder taxonomy with concern, channel and tone for each; apply the TTR standard to board, regulator and emergency communications.
4. Apply Rogers' five network strategies (Access, Engage, Customise, Connect, Collaborate), rank the platforms for the client type, and set the 60/30/10 Education/Community/Institutional content mix with the curation standards.
5. Before any patient content, apply the four de-identification principles and obtain written consent; draft the 4-component social media policy and professional boundary rules from the [compliance, complaints and crisis protocol](references/health-compliance-complaints-crisis.md).
6. Set the 4-step complaint protocol, the troll-type responses for the client's likely risks and the crisis structure (3–6 hour window, three prerequisites, holding statement).
7. Stop for qualified clinical, legal or data-protection review before publishing, spending, contacting people or making any clinical claim.
8. Review against the Quality Standards and the anti-slop gates; if a check fails, correct it and rerun the affected check, then hand over the plan, assumptions and unresolved risks.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Health-sector social plan (complexity level, stakeholder map, network strategies, platform ranking, 60/30/10 mix) | Communications lead and clinical governance | Every section tied to the client type and goal; no unverified clinical claim. |
| Patient-safe content rules (curation standards, 7 red flags, de-identification tests, consent rule) | Content team | Every patient item passes all four de-identification tests and has written consent on file. |
| Social media policy framework and professional boundary rules | Management and all staff | Covers all 4 components: purpose, approved platforms and accounts, staff personal use, crisis protocol. |
| Complaint, troll and crisis response protocol | Patient relations and designated spokesperson | 4-step complaint protocol, troll-type responses and holding statement template present. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Clinical sign-off and consent register | Table: item, clinician reviewer, consent record, date | No clinical claim or patient content released without both. |
| Curation check record for third-party content | Checklist against the 5 criteria and 7 red flags | Each shared item passes all five criteria. |
| Input and assumption register | Table or annotated brief | Missing and unverified items are visible, not treated as passed. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Patient data is handled under the Uganda Data Protection and Privacy Act 2019 (or the named market's law), and no diagnosis, treatment recommendation or prescription is ever given through social media.

## Degraded Mode

Without clinician review and documented patient consent, return the narrowest qualified result and mark the affected checks `not assessed`. The stakeholder map, platform plan, policy framework and complaint and crisis protocols can still be delivered, with clinical and patient content held as drafts.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Clinical or reputational risk is present | Require qualified clinical, legal, or data-protection review before release. | Unsafe health claims or unlawful patient-data use. |
| A patient story, photo, video, testimonial or case is proposed | Apply all four de-identification tests and obtain explicit written consent; if uncertain, do not share. | Re-identification from age, gender, location and condition. |
| A patient asks for advice on WhatsApp or in comments | Direct to an appointment: "For personalised advice, please book a consultation at [number/location]". | Diagnosis or prescription through social media. |
| A complaint appears publicly | Acknowledge within 24 hours, take it offline, escalate, and express care without a public apology. | Litigation exposure and a public argument. |
| A troll posts | Classify by the six troll types and respond as the table directs; wait 12–24 hours before replying to any troll. | Replies written in anger and unwinnable debates. |
| A crisis becomes known | Issue an initial holding statement within 3–6 hours through the single designated spokesperson. | Silence read as guilt or incompetence. |
| Third-party health content is proposed for sharing | Share only if it meets all 5 curation criteria and shows none of the 7 red flags. | Amplifying misinformation. |
| Evidence is contradictory or materially incomplete | Pause the affected recommendation and request the accountable source. | Confident advice built on an unresolved premise. |

## Quality Standards

- Identifies the client's complexity level (1–4) and adjusts strategy depth accordingly.
- Maps all relevant stakeholder groups from the 11-stakeholder taxonomy, with channel and tone specified for each.
- Applies all five Rogers network strategies (Access, Engage, Customise, Connect, Collaborate) with at least one specific EA-contextualised tactic per strategy.
- Recommends platform priorities explicitly ranked for the client type (organisation vs individual medical professional).
- Produces a content mix recommendation with 60/30/10 Education/Community/Institutional rationale.
- Addresses patient de-identification using all four principles before recommending any patient content.
- Includes a social media policy framework covering all 4 components.
- Specifies a 4-step complaint protocol and names the troll type responses for the client's most likely risks, and provides a crisis structure with holding statement template, 3-prerequisite checklist and Virginia Tech Principle rationale.

Keep Uganda/East Africa, British English, EAT, UGX and WhatsApp-first assumptions explicit where they apply; apply `ai-marketing/anti-ai-slop` during drafting and block release on an F from `ai-marketing/ai-slop-audit`.

## Anti-Patterns

- Apologising publicly on social media. Fix: express care and willingness to resolve; a public apology implies admitted fault and may be used in litigation.
- Deleting negative comments during a crisis. Fix: leave them; deletion inflames public anger and is widely noted.
- A mainly promotional feed. Fix: hold the 60/30/10 Education/Community/Institutional mix; promotion violates the trust patients need.
- Sharing scene photographs or reposting unverified third-party crisis content. Fix: post only official, verified updates through the designated spokesperson.
- Clinicians befriending or following patients on personal accounts. Fix: apply the professional boundary rules and require affiliation disclosure.
- Debating anti-vaccine communities comment by comment. Fix: post one evidence-based response and stop.
- Copying a global template without adapting Uganda/East Africa access, language, payment or trust conditions. Fix: record which local assumptions apply.

## References

- [Health-sector strategy method](references/health-sector-strategy-method.md): read when asking the intake questions, setting the complexity level, mapping stakeholders, applying the network strategies, ranking platforms, setting the content mix and curation standards, or citing sources.
- [Health compliance, complaints and crisis protocol](references/health-compliance-complaints-crisis.md): read when de-identifying patient content, drafting the policy or boundary rules, handling complaints and trolls, or preparing crisis communication.
- [Institutional health communication and infodemic response](references/institutional-health-communication-and-infodemic-response.md): read when planning participatory, evidence-led health communication and cyber-aware correction.
- [`playbook-crisis-communications`](../../playbooks/playbook-crisis-communications/SKILL.md): read when an organisation-wide crisis is declared.
- [`policy-ai-content-ethics`](../../policies/policy-ai-content-ethics/SKILL.md): read when the organisation needs its AI content ethics policy.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read before releasing any health, privacy or regulatory claim.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting posts and replies.
- [AGENTS.md](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

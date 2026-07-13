# Legal, privacy and market release gate

Use this gate for paid media, WhatsApp outreach, influencer work, AI-assisted content, UGC, competitions, public-sector communications, or any deliverable containing current market claims. It is an operational screening tool, not legal advice or certification.

## Required release record

| Field | Required evidence | Stop condition |
|---|---|---|
| Market and audience location | Named countries and any material regional targeting | Geography unknown or mixed without jurisdiction review |
| Accountable controller/advertiser | Named client owner and agency role | No accountable owner |
| Current sources | Source IDs, opened URLs, access dates and relevant sections from the [register](../source-registers/README.md) | Source overdue, unavailable or not applicable |
| Claim substantiation | Claim-to-evidence row covering copy, visual implication and landing page | Material claim has no admissible evidence |
| Personal data | Purpose, lawful basis, notice, fields, retention, access and deletion owner | Sensitive or unnecessary data; basis/notice unresolved |
| Rights and permissions | Licence/release for music, footage, creator, testimonial, likeness, logo and UGC | Ownership or permitted use is unproved |
| Platform policy | Named policy/category check on release date | Prohibited category or unresolved restriction |
| Approval | Legal/compliance/brand/platform approval where triggered | Required reviewer has not approved |

## Channel and practice checks

### Paid media

- Compare the ad, targeting, lead form and destination against the current platform policy and local law.
- Record targeting exclusions and confirm they do not discriminate unlawfully or infer sensitive traits.
- Match every price, outcome, scarcity, comparison and testimonial claim to evidence that covers the exact wording.
- Verify licences, age gates and approvals for regulated categories. If uncertain, do not launch.
- Keep a release snapshot: final creative, copy, URL, audience, budget authority, approver and timestamp.

### WhatsApp

- Retain the number source, opt-in wording, timestamp, scope and channel permission for each recipient cohort.
- Contact only recipients who supplied their number and opted in to the subsequent messages.
- Make the sender, purpose and opt-out method clear; process on- and off-platform opt-outs promptly.
- Use approved templates and the applicable service window where the Business Platform requires them.
- Screen regulated verticals and government/political use against the current WhatsApp policy before drafting.

### Influencer and creator work

- Record the commercial relationship and use the platform disclosure mechanism plus unambiguous copy visible with the endorsement.
- Contract the content scope, approval boundary, usage term, territory, edit rights, takedown process and measurement access.
- Substantiate creator claims; experience statements must be genuine and must not imply unsupported typical results.
- Verify audience suitability, including minors and regulated products; check current prohibited-industry rules.
- Preserve the posted asset, disclosure and approval evidence.

### AI-assisted content

- Do not upload confidential, personal or client-controlled source material to an unapproved service.
- Record the tool, model/service date, human reviewer, source assets and material transformations.
- Verify facts, rights, likenesses, cultural claims and synthetic-media disclosures; AI output is not evidence.
- Withhold impersonation, deceptive synthetic media, fabricated testimonials or invented performance proof.
- Apply the repository anti-slop and cultural-bias gates before release.

### UGC and testimonials

- Capture permission from the identifiable rights-holder; a public post is not blanket permission to reuse.
- Record permitted channels, territory, duration, edits, attribution, paid amplification and withdrawal route.
- Remove third-party personal information not covered by the permission.
- Verify that the testimonial is attributable, accurate and not edited into a broader claim.
- Takedown or dispute requests pause further use until resolved.

## Decision outcomes

| Outcome | Meaning | Action |
|---|---|---|
| Pass | All applicable checks have current evidence and named approval | Release only within the recorded scope |
| Conditional | Non-material item has a named owner and pre-release deadline | Hold release until the condition is evidenced; then rerun |
| Not assessed | Source, capability, artefact or reviewer was unavailable | Withhold the affected element and state what is needed |
| Fail | A prohibition, unsupported claim, missing permission or unresolved high-risk issue remains | Do not release; revise or obtain specialist decision |

## Market refresh protocol

At discovery and immediately before release, run `python -X utf8 scripts/check_source_freshness.py`. For each numeric market statement, record the source period and denominator. Replace unsupported channel folklore—such as universal platform dominance, fixed audience percentages or static payment fees—with client evidence or a qualified, dated source. A different market replaces Uganda/East Africa defaults; it is not layered onto them.

## Escalation triggers

Qualified legal or regulatory review is mandatory for political advertising, children, health claims, financial products, gambling, alcohol, tobacco, competitions with material prizes, biometric or sensitive data, cross-border transfers, unresolved copyright/likeness disputes, regulator complaints, or a proposed interpretation carrying material exposure. The reviewer’s decision and scope are evidence; “legal checked” without them is not.

Parent routes: [paid social](../../skills/playbooks/playbook-paid-social-advertising/SKILL.md), [WhatsApp](../../skills/platforms/platform-whatsapp/SKILL.md), [influencer strategy](../../skills/pipeline/08-influencer-marketing-strategy/SKILL.md), [UGC strategy](../../skills/playbooks/playbook-ugc-strategy/SKILL.md), [analytics privacy](../../skills/meta-analytics-ops/meta-analytics-privacy/SKILL.md), and [AI content ethics](../../skills/policies/policy-ai-content-ethics/SKILL.md).

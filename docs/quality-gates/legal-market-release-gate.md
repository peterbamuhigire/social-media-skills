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

Parent routes: [paid social](../../skills/playbooks/playbook-paid-social-advertising/SKILL.md), [WhatsApp](../../skills/platforms/platform-whatsapp/SKILL.md), [influencer strategy](../../skills/pipeline/08-influencer-marketing-strategy/SKILL.md), [UGC strategy](../../skills/pipeline/08-influencer-marketing-strategy/references/ugc-creator-and-customer-content.md), [analytics privacy and consent](../../skills/meta-analytics-ops/measurement-tracking-plan/SKILL.md), and [AI content ethics](../../skills/policies/policy-ai-content-ethics/SKILL.md).

## Advertising, direct-response and outreach checks (2026-09-23)

Run the [direct-marketing ethics filter](../../skills/content-writing/references/direct-marketing-ethics-filter.md) on every ad, offer, sales page, outreach sequence and influencer brief. Use only dated register claims:

| Check | Register record | Rule to apply |
|---|---|---|
| Special ad category | `META-SPECIAL-AD-CATEGORIES-2026` | Declare housing, employment, financial or political/social-issue ads; targeting limits apply in the US, Canada and Europe; no political ads in the EU since Oct 2025 |
| Political and social-issue ads | `META-SIEP-AD-LIBRARY-2026` | Authorisation and "Paid for by" disclaimer; UG/KE authorisation rules not assessed — escalate |
| Influencer disclosure | `FTC-ENDORSEMENTS-REVIEWS-2026`, `UK-ASA-CMA-INFLUENCER-2026`, `UG-KE-INFLUENCER-DISCLOSURE-2026` | Clear, upfront disclosure everywhere as best practice; no fake reviews or fake indicators of influence; UG/KE checks (UCC, CA, CAK, BCLB) stay open |
| Direct marketing (Uganda) | `UG-DPPA-2019`, `UG-DPPR-2021` | Consent to collect; honour written direct-marketing objections within 14 days; register with the PDPO; do not claim the Act requires marketing opt-in |
| Direct marketing (Kenya) | `KE-DP-GENERAL-2021` | Consent plus a free, simple opt-out; objections are absolute; sender identity shown; direct-marketing businesses register with the ODPC |
| EU/UK-facing measurement | `GOOGLE-CONSENT-MODE-GA4-2026` | Consent mode v2 signals via a CMP for EEA/UK/CH traffic |
| Ad-invoice tax | `UG-DIGITAL-TAX-ADS-2026` | Route VAT/DST treatment to `chwezi-accounting-doctrine`; never state it as settled |
| Consumer data cost (Uganda, 2026-09-29) | `UG-DATA-EXCISE` | The social media (OTT) tax ended on 1 Jul 2021 and was replaced by a 12% excise duty on internet data (medical and education data excepted), listed as current in a secondary tax summary reviewed 12 Jan 2026 (partial; URA and Act text not read). Never tell a client the OTT tax applies; when data cost shapes a creative or channel choice, cite the excise as partial and route tax treatment to `chwezi-accounting-doctrine` |
| Online publisher authorisation (Uganda, 2026-09-29) | `UG-UCC-ONLINE-PUBLISHERS` | UCC authorises online data communication services (blogs, online TV and radio, online newspapers, IPTV, video on demand). Whether a client's channel or creator needs authorisation, and current enforcement, are `NOT_ASSESSED`: escalate before launching a branded online TV, radio or news channel |
| Uganda cyber law (2026-09-29) | `UG-CMA-2022-VOID-2026`, `UG-CMA-SECTIONS-STRUCK-2026`, `UG-CMA-AG-DIRECTIVE-2026`, `UG-CMA-S25-2023` | Never cite the Computer Misuse (Amendment) Act 2022 (including s.26B) as law: it was declared void on 17 Mar 2026. The principal Act (2011) remains in force except the provisions reported struck (ss.11, 23, 26-29 of the 2023 revised edition; and s.25 in the numbering before the 2023 revision, struck 11 Jan 2023); criminal libel (Penal Code ss.162-163) was also struck. Verify the section list against the judgment on ULII before client use; appeal or re-enactment `NOT_ASSESSED` |
| Platform access (Uganda) | `UG-FACEBOOK-ACCESS-2026`, `UG-INTERNET-SHUTDOWN-2026` | Facebook status unstable: verify access at the campaign date and never assert it as blocked or open. Election periods and national events need the [shutdown contingency](../../skills/playbooks/playbook-crisis-communications/references/internet-shutdown-contingency.md) |
| Gambling with creators (Kenya) | `KE-BCLB-GAMBLING-ADS-2025` | No celebrities, influencers or content creators in gambling adverts; BCLB approval and KFCB classification before distribution (secondary report; directive text `NOT_ASSESSED`, escalate) |
| Bulk SMS (Kenya) | `KE-CA-POLITICAL-BULK-SMS-2017`, `KE-DP-GENERAL-2021` | The CA guideline covers political bulk and premium-rate messages only (express opt-in, working opt-out, sender named, 08:00-17:00 sending). For commercial bulk SMS apply the Data Protection Act consent, sender-identity and opt-out rules; KICA consumer-protection text `NOT_ASSESSED` |
| Advertising code (Kenya) | `KE-ASBK-CODE-2003`, `KE-INFLUENCER-LAW-2026` | ASBK Code of Advertising Practice (April 2003 edition): adverts clearly recognisable, testimonials genuine; confirm with ASBK that no later edition applies |
| Data-controller registration (Tanzania, Rwanda) | `TZ-PDPA-REGISTRATION-2026`, `RW-DPP-REGISTRATION-2026` | Tanzania: no collection or processing without PDPC registration (certificate 5 years; secondary). Rwanda: register with the NCSA Data Protection and Privacy Office before processing (Law 058/2021 art. 29). Online media services in Tanzania need a TCRA licence (`TZ-ONLINE-CONTENT-2020`) |

Parent route for advertising: [advertising strategy and budget](../../skills/advertising/advertising-strategy-and-budget/SKILL.md).

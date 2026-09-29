# Consent, Retention and Sharing Review

Merged from skills/meta-analytics-ops/meta-analytics-privacy on 2026-09-29 at 8eacccb; preservation map: [meta-analytics-privacy.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/meta-analytics-privacy.md)

Source works named by the original skill: Raaz (c.2023) *Web Analytics Blueprint*; Hanlon, A. and Tuten, T. (eds) (2022) *The SAGE Handbook of Digital Marketing*, SAGE.

## When to use this reference

Use it for the privacy half of a tracking plan: which data-protection frameworks apply, how the cookie banner must behave, how GA4 is configured for privacy, the data-minimisation register, WhatsApp contact data, deletion requests, and when to stop and refer the client to a lawyer. The output is an **analytics privacy review and remediation register**: every finding traces to an input, names an owner or next action, and marks assumptions and unassessed checks.

This is implementation guidance only. Legal advice, a data protection impact assessment (DPIA) or a privacy policy draft go to a qualified data-protection lawyer in the client's jurisdiction.

## Inputs

Ask for these before producing the review:

| # | Input | Why it matters |
|---|---|---|
| 1 | Client business name | Report header and register owner |
| 2 | Industry | Sensitive-data triggers (health, finance, biometrics) |
| 3 | Country / city (default Uganda / East Africa) | Primary framework |
| 4 | Primary goal (for example DPPA compliance, GA4 privacy settings, cookie consent set-up) | Scope of the review |
| 5 | Website platform (WordPress, Wix, Squarespace, custom) | How the consent banner is implemented |
| 6 | Audience geography (Uganda only; Uganda + Kenya; Uganda + international including the EU) | Which frameworks apply |
| 7 | GA4 access level (Admin needed to change privacy settings) | Whether configuration can be checked or only recommended |
| 8 | Data currently collected: every tracking pixel, analytics tool and third-party tag on the site | Starting inventory for minimisation |

Also needed: the data-flow inventory, consent records and the applicable jurisdiction (client, approved systems or dated platform exports), plus the purpose, audience and approval boundary. If the data-flow inventory is missing, stop that decision or issue a clearly bounded partial result.

## Why analytics privacy matters in East Africa

Uganda's Data Protection and Privacy Act 2019 (DPPA) and Kenya's Data Protection Act 2019 (DPA) both require **informed consent** before collecting personal data, and analytics data linked to an individual is personal data. Non-compliance brings financial penalties and reputational damage. Clients with international audiences (e-commerce, NGOs, professional services exporting to EU markets) may also fall under the GDPR (EU, 2018) and the CCPA (California). Treat consent as required where cookies or identifiers collect personal data, and confirm the position for each market with counsel. Register: UG-DPPA-2019, UG-PDPO-ORG, KE-DP-GENERAL-2021, KE-ODPC-DIRECT-MARKETING-2026.

## Decision rules

| Condition | Action | Risk avoided |
|---|---|---|
| Audience geography not yet confirmed | Identify the applicable frameworks first; give no implementation guidance before that | Configuring for the wrong law |
| Website accepts payments or enquiries from EU residents (the GDPR applicability test) | The GDPR applies; escalate to a data-protection lawyer before proceeding | Operating without a lawful EU consent mechanism |
| Any escalation trigger below applies | Pause implementation and refer to a lawyer | Overreaching into legal advice |
| Data inventory, consent records and jurisdiction are current and attributable | Produce the full review and remediation register citing the evidence | Decisions on stale or unrelated evidence |
| A material input is missing or contradictory | Stop that decision, ask, or issue a labelled partial result | Invented precision |
| The client handles Ugandan residents' data through foreign platforms (Google, Meta) | Record the legal basis, safeguards and justification for the transfer and keep the records for inspection (register UG-PDPO-OFFSHORE-2025, partial) | Undocumented cross-border transfers |

## Regulatory framework summary

| Framework | Applies when | Key requirement |
|---|---|---|
| Uganda DPPA 2019 | Client operates in Uganda or processes data of Ugandan residents | Informed consent before collection; right of access and deletion; registration with the PDPO (UG-PDPO-ORG) |
| Kenya DPA 2019 | Client operates in Kenya or processes data of Kenyan residents | Consent; data minimisation; right to erasure |
| GDPR (EU) | Client offers goods or services to EU residents or monitors EU users' behaviour | Explicit opt-in consent; right to be forgotten; a Data Protection Officer where core activities involve large-scale systematic monitoring or special-category data, or the controller is a public authority (verify) |
| CCPA (California) | Original skill: 50,000+ California consumers a year, or 25 %+ of revenue from California data. Thresholds changed under the CPRA; verify current values before stating (no register record) | Right to opt out of data sale; disclosure of collection practices |

The CCPA thresholds are carried from the original skill and have not been re-verified against current California law (the CPRA amendments changed several thresholds); verify before stating (no register record). Tanzania (TZ-PDPA, TZ-PDPA-REGISTRATION-2026) and Rwanda (RW-DPP-2021, RW-DPP-REGISTRATION-2026) are in the register for clients serving those markets.

## Cookie consent implementation

Every site that collects analytics data needs a consent banner that:

1. **appears before any tracking cookie is set**, not after the page has loaded with cookies already active;
2. **explains what is collected and why**, in plain language, not legal boilerplate;
3. **offers a genuine opt-out**: a real "Reject all" button, not a dark pattern that buries it;
4. **remembers the choice** for at least 12 months;
5. **separates cookie categories**, at minimum Necessary (no consent needed), Analytics (consent needed) and Marketing (consent needed).

Tools named in the original skill for EA clients (prices and plans: verify before stating, no register record):

- **CookieYes**: free tier; works with WordPress, Wix and custom sites; keeps a consent log.
- **Usercentrics**: stronger for GDPR work; paid.
- **Custom implementation**: acceptable where the client has a developer and all five requirements above are met.

If the client also sells Google ad inventory on its own site (AdSense, Ad Manager, AdMob) to EEA, UK or Swiss visitors, the CMP must be Google-certified and integrated with the IAB TCF (register GOOGLE-CMP-TCF-2026). For wiring the banner into Consent Mode v2 see [consent-mode-and-cmp.md](consent-mode-and-cmp.md).

**Dark patterns to avoid:** pre-ticked "Accept" boxes; a "Reject" option hidden in small text; "Accept all" in one click while "Manage preferences" takes three. The GDPR prohibits them; the original skill added that they are increasingly scrutinised under the DPPA (no register record; verify before stating).

## GA4 privacy configuration

Do these steps in order; all need **Admin** access in GA4.

1. **Data retention** (Admin → Data Settings → Data Retention). Set user-level and key-event data to **14 months**, the longest option on a standard property (the other option is 2 months). Retention affects explorations and funnel reports only; aggregated standard reports are unaffected, and Large or XL properties are cut to 2 months automatically (register GA4-DATA-RETENTION-2026). Choose 2 months where the client has no need for long explorations.
2. **Google signals** (Admin → Data Settings → Data Collection). Keep it **off** unless the client has a documented need for cross-device reporting. It links analytics data to signed-in Google accounts, which is personal-data linkage that needs explicit consent. Menu path: verify at use (no register record).
3. **IP addresses.** The original skill told consultants to switch on "Redact visitor IP addresses". Correction (register GA4-IP-2026, read 2026-09-29): **GA4 does not log or store IP addresses, so no IP-masking step is needed.** Record the step as "not applicable in GA4" in the review, and check instead that no personal data (emails, phone numbers) is sent in URLs or event parameters.
4. **Consent mode.** Configure the tag so it starts in a consent-pending (denied) state and collects full analytics only after the visitor grants consent through the banner. This needs the CMP connected to the Google tag, usually through Google Tag Manager. Detailed design: [consent-mode-and-cmp.md](consent-mode-and-cmp.md).
5. **Data deletion requests** (Admin → Data Deletion). Write down how the client answers a right-to-erasure request. Under the DPPA the client must be able to delete an individual's data within a reasonable time; in GA4 use the deletion tool for the relevant user identifier.

## Data minimisation principle

Collect only what the stated analytics purpose needs. Before adding any pixel, custom dimension or third-party tag, record:

1. **What it collects**: every data point captured;
2. **Why it is needed**: the analytics or business purpose;
3. **How long it is kept**: the retention period before deletion or anonymisation;
4. **Who has access**: internal and external parties.

This record is an ethical and a legal requirement under the DPPA 2019. A simple data register (a Google Sheet is enough for most EA clients) works. Add the cross-border columns: destination country, platform, legal basis and safeguard.

**Audit prompt:** review every active tag in Google Tag Manager; remove any tag unused in the past 90 days or whose purpose cannot be stated clearly.

## WhatsApp and social media data governance

WhatsApp Business gives no personal analytics about individual users, but the client's own records (broadcast lists, contact databases, chat histories) are **personal data** under the DPPA 2019. Advise the client to:

1. **Document the data:** a record of every WhatsApp contact with name, number, source, consent basis and date added;
2. **Honour opt-outs within 48 hours:** remove anyone who asks to leave a broadcast list at once and confirm the removal. This is a house standard, stricter than the statute: under DPPA s.26 the data subject may require in writing that direct marketing stop, and the controller responds within 14 days (register UG-DPPA-S26-DIRECT-MARKETING-2026; not legal advice);
3. **Not share contact data with third parties** without documented consent from each contact;
4. **Store exports securely:** contact lists exported to spreadsheets go in access-controlled files (for example Google Drive with restricted sharing), never in unsecured email attachments.

**Social platform note:** Facebook, Instagram and TikTok dashboards show page administrators aggregate data only, not individuals' personal data, so outside the EEA/UK native platform analytics need no extra consent; for EU audiences Page Insights involves joint controllership, so confirm with counsel. **Installing the Meta Pixel on a website is personal-data collection and needs cookie consent.** The same applies to the TikTok Pixel, LinkedIn Insight Tag and Google Ads tags.

## International framework escalation (stop and refer)

Pause implementation and refer the client to a qualified data-protection lawyer if any of these apply:

- the site serves EU residents and has no GDPR-compliant consent mechanism;
- the client collects or stores health, financial or biometric data of any kind;
- the client is a public institution or processes data for government bodies;
- the client has had a data breach in the past 12 months;
- the client operates in several East African jurisdictions with different frameworks.

## Remediation register (output template)

| # | Finding | Evidence (source, date) | Framework | Risk | Remediation | Owner | Due | Status (open / done / not assessed) |
|---|---|---|---|---|---|---|---|---|

## Release checklist

- [ ] Applicable frameworks (DPPA, DPA, GDPR, CCPA, plus TZ/RW where relevant) identified from audience geography before any guidance.
- [ ] GA4 configuration covers retention, Google signals, the IP position (not applicable in GA4), consent mode and deletion requests, in that order.
- [ ] Cookie banner meets all five requirements: before cookies, plain language, genuine opt-out, remembered choice, categories.
- [ ] Data minimisation is a documentation requirement (register with cross-border columns), not only a settings checklist.
- [ ] WhatsApp contact data is treated as personal data under the DPPA 2019.
- [ ] Legal-referral triggers are stated; the review gives no legal advice.
- [ ] Every blocked check is marked `not assessed` with the evidence needed to resume; missing access is never a pass.
- [ ] British English; imperative voice in instructions.

## Anti-patterns (carried from the source)

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark a provisional comparator.
- Producing the review without a data-flow inventory. Fix: stop the affected decision or issue a bounded partial output.
- Treating missing access or data as a passed check. Fix: record `not assessed`, its risk and the recovery input.
- Changing live GA4, GTM or CMP settings during a review. Fix: obtain separate explicit authority and keep action evidence.

## Worked example (from the source, adapted)

Given a verified data-flow inventory, the review lists each tag with its purpose, retention and access, the consent-state behaviour, and the remediation owner, with source dates and named assumptions. If the inventory cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

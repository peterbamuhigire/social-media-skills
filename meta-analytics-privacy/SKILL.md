---
name: meta-analytics-privacy
description: >
  Privacy-by-design analytics setup for clients operating under Uganda's Data
  Protection and Privacy Act 2019, Kenya's Data Protection Act 2019, and
  international frameworks (GDPR, CCPA). Covers cookie consent implementation,
  GA4 privacy configuration, data minimisation, and WhatsApp data governance.
  Invoke when setting up GA4 for a new client, configuring cookie consent
  banners, advising on analytics data governance, or when a client asks about
  data protection compliance for their digital channels. Does not replace legal
  counsel — flags compliance requirements and provides implementation guidance.
---

# Analytics Privacy and Data Governance

**Sources:** Raaz (c.2023) *Web Analytics Blueprint*; Hanlon and Tuten (2022) *The SAGE Handbook of Digital Marketing*

---

## Required Inputs

Ask for the following before generating any deliverable:

1. **Client business name**
2. **Industry**
3. **Country / city** (defaults to Uganda / East Africa)
4. **Primary goal** (e.g. achieve DPPA compliance, configure GA4 privacy settings, set up cookie consent)
5. **Website platform** (WordPress, Wix, Squarespace, custom-built — affects consent banner implementation)
6. **Audience geography** (Uganda only; Uganda + Kenya; Uganda + international including EU — determines which frameworks apply)
7. **GA4 access level** (Admin required for privacy configuration changes)
8. **Data currently collected** (list all tracking pixels, analytics tools, and third-party tags active on the website)

---

## Why Analytics Privacy Matters in EA

Uganda's Data Protection and Privacy Act 2019 (DPPA) and Kenya's Data Protection Act 2019 (DPA) both require **informed consent** before collecting personal data — including analytics data linked to individual users. Non-compliance carries financial penalties and significant reputational risk.

For clients with international audiences (e-commerce, NGOs, professional services exporting to EU markets), GDPR (EU, 2018) and CCPA (California, USA) may additionally apply.

**This skill provides implementation guidance only.** For specific legal advice, data protection impact assessments, or drafting of a privacy policy, refer the client to a qualified data protection lawyer in their jurisdiction.

---

## Regulatory Framework Summary

| Framework | Applies when | Key requirement |
|---|---|---|
| Uganda DPPA 2019 | Client operates in Uganda or processes data of Ugandan residents | Informed consent before data collection; right to access and deletion |
| Kenya DPA 2019 | Client operates in Kenya or processes data of Kenyan residents | Consent; data minimisation; right to erasure |
| GDPR (EU) | Client offers goods/services to EU residents OR monitors EU user behaviour | Explicit opt-in consent; right to be forgotten; Data Protection Officer for large-scale processing |
| CCPA (California) | Client has 50,000+ California consumers/year, or earns 25%+ revenue from California data | Right to opt-out of data sale; disclosure of data collection practices |

**GDPR applicability test:** Does the client's website accept payments or enquiries from EU residents? If yes, GDPR applies — escalate to a data protection lawyer before proceeding.

---

## Cookie Consent Implementation

All websites collecting analytics data must display a cookie consent banner that:

1. **Appears before any tracking cookies are set** — not after the page loads with cookies already active
2. **Explains what data is collected and why** — in plain language, not legal boilerplate
3. **Provides a genuine opt-out** — a real "Reject all" button, not a dark pattern that buries the opt-out
4. **Remembers the user's choice** — for a minimum of 12 months
5. **Distinguishes cookie categories** — at minimum: Necessary (no consent required) vs. Analytics (consent required) vs. Marketing (consent required)

**Recommended tools for EA clients:**
- **CookieYes** — free tier available; integrates with WordPress, Wix, and custom sites; generates a consent log
- **Usercentrics** — more robust for GDPR requirements; paid but affordable
- **Custom implementation** — acceptable if the client has a developer and the implementation meets all five requirements above

**Dark patterns to avoid:** Pre-ticked "Accept" boxes; hiding the "Reject" option in small text; making "Accept all" one click and "Manage preferences" three clicks. Dark patterns are explicitly prohibited under GDPR and are increasingly scrutinised under DPPA.

---

## GA4 Privacy Configuration

Complete these steps in order. All require **Admin access** in GA4.

**Step 1 — Data Retention**
Admin → Data Settings → Data Retention
Set to **14 months maximum**. This reduces the volume of personal data retained and is the minimum recommended setting for DPPA/GDPR alignment.

**Step 2 — Google Signals**
Admin → Data Settings → Data Collection → Google Signals
**Disable Google Signals** unless the client has a specific, documented need for cross-device tracking. Google Signals links analytics data to Google Account profiles — this is personal data linkage that requires explicit consent.

**Step 3 — IP Anonymisation**
Admin → Data Streams → [select stream] → Configure tag settings → Show all → Redact visitor IP addresses
Enable this setting. It masks the user's location to city level only — the user's precise IP address is not stored. This is recommended for all clients regardless of regulatory framework.

**Step 4 — Consent Mode Configuration**
Configure GA4 consent mode so the tag fires in "consent pending" state by default and only collects full analytics data after the user grants consent via the cookie banner. This requires integration between the consent management platform (CookieYes or equivalent) and the GA4 tag via Google Tag Manager.

**Step 5 — Data Deletion Requests**
Admin → Data Deletion
Document the process for responding to a user's right-to-erasure request. Under DPPA 2019, the client must be able to delete an individual user's data within a reasonable timeframe. In GA4, use the Data Deletion tool to remove data associated with a specific user identifier.

---

## Data Minimisation Principle

Collect only the data necessary for the stated analytics purpose. Before adding any tracking pixel, custom dimension, or third-party tag to a client's website, document:

1. **What data this collects** — list every data point captured
2. **Why it is needed** — the specific analytics or business purpose it serves
3. **How long it will be retained** — the retention period before deletion or anonymisation
4. **Who has access** — which internal and external parties can view this data

This documentation is both an ethical and legal requirement under DPPA 2019. Maintain it in a simple data register (a Google Sheet is sufficient for most EA clients).

**Audit prompt:** Review all active tags in Google Tag Manager. Remove any tag that has not been used in the past 90 days or whose purpose cannot be clearly stated.

---

## WhatsApp and Social Media Data Governance

WhatsApp Business does not provide personal analytics data about individual users. However, client-side records — broadcast lists, contact databases, conversation histories — constitute **personal data** under DPPA 2019.

Advise clients to:

1. **Document the data:** Maintain a record of all WhatsApp contacts — name, number, source of contact, consent basis, date added
2. **Honour opt-out requests within 48 hours:** If a contact asks to be removed from a broadcast list, remove them immediately and confirm removal
3. **Do not share contact data with third parties** without documented consent from each individual contact
4. **Store contact data securely:** WhatsApp contact lists exported to spreadsheets must be stored in access-controlled files (Google Drive with restricted sharing), not in unsecured email attachments

**Social media data note:** Facebook, Instagram, and TikTok analytics dashboards provide aggregate data only — they do not expose individual user personal data to page administrators. No additional consent is required for using native platform analytics. However, installing the Meta Pixel on a website does constitute personal data collection and requires cookie consent.

---

## International Framework Escalation

If any of the following conditions apply, pause implementation and refer the client to a qualified data protection lawyer before proceeding:

- The client's website serves EU residents and currently has no GDPR-compliant consent mechanism
- The client collects and stores health, financial, or biometric data of any kind
- The client is a public institution or processes data on behalf of government bodies
- The client has experienced a data breach in the past 12 months
- The client operates in multiple East African jurisdictions with different regulatory frameworks

---

## Quality Criteria

Output meets the standard for this skill if:

- The applicable regulatory frameworks (DPPA, DPA, GDPR, CCPA) are identified based on the client's audience geography before any implementation guidance is given
- All five GA4 privacy configuration steps are included and sequenced correctly
- Cookie consent implementation meets the five requirements: pre-load, plain language, genuine opt-out, remembered choice, and category distinction
- The data minimisation principle is applied — a documentation requirement is included, not just a configuration checklist
- WhatsApp contact data is addressed as personal data subject to DPPA 2019
- Legal referral triggers are clearly stated — the skill does not overreach into legal advice
- Language is British English throughout; imperative in all instructional sections

# Consent Mode v2 and CMP

New reference for `measurement-tracking-plan` (Social Kaizen S04-T01, benchmark rows SL06-C4, SL09-C5, SL15-C3, SL15-C4, SL14-C4; 29 September 2026). Platform facts were read live on 29 September 2026 and cite register IDs. This is implementation guidance, not legal advice.

## When to use this reference

Use it to design how Google, Meta and other tags behave before and after a visitor's consent choice: the consent parameters, default states per region, basic or advanced mode, the consent management platform (CMP), and what the client can still measure when consent is refused.

## Facts to work from

| Fact | Register |
|---|---|
| Consent Mode v2 has four parameters: `ad_storage` (advertising cookies), `analytics_storage` (analytics cookies), `ad_user_data` (sending user data to Google for advertising) and `ad_personalization` (personalised advertising). | GOOGLE-CONSENT-MODE-PARAMS-2026 |
| `ad_user_data` denied: using personal data for online advertising is disabled, including `user_id` cases. `ad_storage` denied: no new advertising cookies; Ads products truncate IP addresses at collection. `analytics_storage` denied: cookieless pings are sent and used for modelling. | GOOGLE-CONSENT-MODE-PARAMS-2026 |
| Google tag users receiving data from EEA end users must collect consent and pass consent signals to keep measurement, ad personalisation and remarketing. Certified CMPs update automatically; custom banners must implement Consent Mode v2. | GOOGLE-CONSENT-MODE-GA4-2026 (partial: March 2024 enforcement date) |
| Basic mode: Google tags do not load until the visitor interacts with the banner; nothing is sent before consent. Advanced mode: tags load with denied defaults and send consent state and cookieless measurements; modelling is advertiser-specific rather than general. | GOOGLE-CONSENT-MODE-DEV-2026 |
| GA4 behavioural modelling needs at least 1,000 events a day with `analytics_storage` denied for 7+ days and at least 1,000 daily users with it granted for 7 of the previous 28 days; tags must load before the dialog; reporting identity Blended. Eligibility is not guaranteed. | GA4-CONSENT-MODELLING-2026 |
| Publishers using AdSense, Ad Manager or AdMob need a Google-certified CMP integrated with the IAB TCF for EEA and UK traffic (from 16 Jan 2024) and Switzerland (from 31 Jul 2024). | GOOGLE-CMP-TCF-2026 |
| Uganda: informed consent before collecting personal data (DPPA 2019); organisations register with the PDPO; cross-border transfers need consent or an equivalent-protection destination, with records kept for inspection. | UG-DPPA-2019, UG-PDPO-ORG, UG-PDPO-OFFSHORE-2025 (partial) |
| Kenya, Tanzania, Rwanda: consent and registration duties apply under their own statutes. | KE-DP-GENERAL-2021, KE-ODPC-DIRECT-MARKETING-2026, TZ-PDPA, TZ-PDPA-REGISTRATION-2026, RW-DPP-2021, RW-DPP-REGISTRATION-2026 |

## Decision rules

| Condition | Action | Risk avoided |
|---|---|---|
| Any EEA, UK or Swiss traffic on pages with Google tags | Consent Mode v2 with all four parameters, driven by a CMP; region-specific defaults set to denied | Loss of remarketing, audiences and measurement for that traffic |
| East African audience only | Treat consent as required where cookies or identifiers collect personal data (Uganda DPPA 2019; Kenya DPA 2019, where consent is one lawful basis) and confirm the position with counsel; Consent Mode recommended so the same design scales if the client later sells to Europe | "Not Europe, so no consent" |
| Traffic volume is below the GA4 modelling thresholds | Choose basic or advanced on legal grounds only; tell the client modelled data is unlikely, so denied traffic is simply unmeasured in GA4 | Promising modelled numbers that will never appear |
| Legal counsel allows tags to load before consent with denied defaults | Advanced mode, for cookieless pings and advertiser-specific modelling | Losing all signal from refusers |
| Legal counsel requires no network call before consent | Basic mode; accept the measurement gap and plan panel or aggregate methods for it | Non-compliant pre-consent requests |
| The client's own site sells Google ad inventory to EEA/UK/CH visitors | Certified CMP with IAB TCF | Ads limited to non-personalised or limited serving |
| Personal data leaves East Africa (GA4, Google Ads, Meta, email tools) | Record destination, legal basis and safeguard in the minimisation register | Undocumented cross-border transfer |

## Procedure

1. **Establish the legal position per market** with the client's data-protection owner: which cookies need consent, whether any request may be sent before consent, registration status (PDPO, ODPC, PDPC, NCSA as applicable). Record gaps for counsel.
2. **Choose the CMP**: certified CMP where Google publisher products or EEA traffic are involved; otherwise any CMP (or custom banner) that meets the five banner requirements in [consent-retention-and-sharing-review.md](consent-retention-and-sharing-review.md) and can emit Consent Mode signals.
3. **Set defaults before any tag fires**: all four Google parameters denied for regulated regions; document the default for other regions and why.
4. **Map categories to parameters**: Analytics category → `analytics_storage`; Marketing category → `ad_storage`, `ad_user_data`, `ad_personalization`. Non-Google tags (Meta Pixel, TikTok Pixel, LinkedIn Insight Tag) fire only when the Marketing category is granted, through GTM consent checks.
5. **Choose basic or advanced mode** using the decision rules and record the reason.
6. **Server-side paths**: pass the consent state to the server container and to Conversions API or enhanced-conversions payloads; a server does not make consent unnecessary ([server-side reference](server-side-capi-and-enhanced-conversions.md)).
7. **Test**: for each consent state, confirm in GTM preview and the browser's storage panel which cookies are written and which requests leave; check Google Ads consent-mode diagnostics after launch. Log results in the QA log.
8. **Monitor**: consent rate by market monthly; if modelling was expected, re-check GA4 eligibility after 28 days.

## Activating first-party data under consent (benchmark SL14-C4)

Customer lists and CRM data used for advertising (Google Customer Match, Meta custom audiences, lookalikes, enhanced conversions, offline imports) need the same consent discipline as tags.

1. Confirm the list's collection notice covered advertising use, and record the consent basis and date per contact; exclude contacts without it and everyone who has opted out.
2. Check the platform's customer-data policy for the list type before upload (register GOOGLE-PERSONALISED-ADS for Google restricted targeting; verify Meta's custom-audience terms at use, no register record).
3. Normalise and hash identifiers as in [server-side-capi-and-enhanced-conversions.md](server-side-capi-and-enhanced-conversions.md); never upload raw lists by email attachment.
4. Record the upload in the minimisation register (destination, date, list size, legal basis, cross-border entry) and set a refresh or deletion date.
5. Stop if the client cannot show the consent basis; uploading needs explicit, action-specific client authority.

## Consent design output (template)

| Region | Default (ad_storage / analytics_storage / ad_user_data / ad_personalization) | Mode | CMP | Non-Google tags when Marketing denied | Server-side consent pass-through | Legal basis note | Owner |
|---|---|---|---|---|---|---|---|

## Anti-patterns

- Updating consent after tags have already fired. Fix: set defaults in the first script on the page, before GTM loads tags.
- Wiring only `ad_storage` and `analytics_storage` (v1). Fix: add `ad_user_data` and `ad_personalization`.
- Letting the Meta Pixel fire on page load while Google tags wait. Fix: put every marketing tag behind the same consent check.
- Presenting modelled conversions as observed. Fix: label them and state the eligibility status.
- A "Reject" button hidden behind "Settings". Fix: "Reject all" on the first layer with equal prominence.

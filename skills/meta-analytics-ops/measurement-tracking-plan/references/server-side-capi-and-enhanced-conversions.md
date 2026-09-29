# Server-Side Tagging, Conversions API and Enhanced Conversions

New reference for `measurement-tracking-plan` (Social Kaizen S04-T01, benchmark rows SL05-C2, SL06-C3, SL09-C5, SL10-C4, SL15-C2; 29 September 2026). Platform facts were read live on 29 September 2026 and cite register IDs.

## When to use this reference

Use it when a conversion is sent from a server as well as (or instead of) the browser, when hashed first-party data is used to match conversions, or when the client asks whether server-side GTM is worth it. It also covers consent-aware measurement of experiments run through a server container.

## Facts to work from

| Topic | Fact | Register |
|---|---|---|
| Server-side GTM | Moves tag instrumentation from the site to a server container on Google Cloud (Cloud Run, automatic provisioning) or other hosting. Fewer client-side tags; data handled in a customer-managed environment. | GOOGLE-SGTM-2026 |
| Server-side GTM cost and resilience | Default single-server deployment usually free within the free tier; upgraded deployments typically USD 30–50 per server per month plus traffic; at least 3 instances per container recommended for production. | GOOGLE-SGTM-2026 |
| First-party context | A custom subdomain lets the tagging server read and write HttpOnly cookies. | GOOGLE-SGTM-2026 |
| Meta deduplication | Match `event_id` (server) to `eventID` (Pixel) and `event_name` to `event`; deduplicated only if received within 48 hours; alternative `fbp` / `external_id` method works only for browser-first-then-server events. Meta recommends a redundant Pixel plus Conversions API setup. | META-CAPI-DEDUP-2026 |
| Meta payload | `event_time` up to 7 days before sending; `action_source` required (website, app, phone_call, chat, physical_store, system_generated, business_messaging, email, other); `event_source_url` required for website events. | META-CAPI-PARAMETERS-2026 |
| Meta hashing | SHA-256 after normalising: `em` (trim, lowercase), `ph` (digits only, country code, no leading zero), `fn`/`ln`, `db` (YYYYMMDD), `ge`, `ct`, `st`, `zp`, `country` (ISO alpha-2 lowercase). Never hash `client_ip_address`, `client_user_agent`, `fbc`, `fbp`, `ctwa_clid`. | META-CAPI-PARAMETERS-2026 |
| Google enhanced conversions | Hashed (SHA-256) email, phone, name and home address sent with conversions; normalise first (trim, lowercase, E.164 phone, remove periods in gmail/googlemail addresses). Two types: web, and leads (hashed form data matched to offline conversion imports). | GOOGLE-ENHANCED-CONVERSIONS-2026 |
| TikTok | Events API is TikTok's server route; Test Events and Diagnostics verify it. | PREMIUM-TT-PIXEL-2026 |

## Decision rules

| Condition | Action | Risk avoided |
|---|---|---|
| The client runs Meta ads and has a developer or a platform with a native integration | Pixel plus Conversions API (redundant setup) with a shared event ID | Lost browser signal; double counting |
| Only a Pixel is feasible now | Keep the Pixel, note the signal gap, schedule CAPI | Pretending the gap does not exist |
| Leads convert later by phone, WhatsApp or in a branch | Enhanced conversions for leads (Google) and CAPI with `action_source` = `phone_call`, `chat`, `business_messaging` or `physical_store` (Meta), within the 7-day event window for Meta | Bidding on form fills instead of revenue |
| Click-to-WhatsApp ads drive the sale | Capture `ctwa_clid` unhashed and send the order with `action_source` = `business_messaging` (verify the current Business Messaging setup at use) | Unattributed WhatsApp sales |
| The site has no developer and low volume | Use platform-native integrations (CMS plug-ins, Shopify or WooCommerce connectors) before server-side GTM | An unowned server |
| Server-side GTM is chosen | Custom first-party subdomain, 3+ instances in production, a named maintainer, monthly cost line | Silent outages and surprise bills |
| Consent is denied for advertising | Do not send identifiers or hashed data for that visitor; pass the consent state to the server | Using personal data without consent |
| An A/B or holdout test is measured through the server container | Tag variant and cohort in the data layer, respect consent state, record which traffic is unmeasured (denied) | Biased test reads from consent-skewed samples |

## Procedure

1. **Decide the route per event** (browser only, browser + server, server only, offline import) in the event map ([event-taxonomy-and-tracking-plan.md](event-taxonomy-and-tracking-plan.md)).
2. **Generate one event ID per action** in the data layer (order number or a UUID) and pass it to the Pixel `eventID` and the CAPI `event_id`; use `transaction_id` for Google purchases.
3. **Collect matching data lawfully**: email and phone only where the form collects them for the transaction, with consent recorded.
4. **Normalise then hash** on the server (or let the Google tag hash for enhanced conversions for web). Keep the never-hash fields raw.
5. **Send server events** with `event_time`, `action_source` and `event_source_url` (website events) for Meta; enhanced-conversion fields for Google.
6. **Verify**: Meta Test Events and event-match diagnostics; Google Ads conversion diagnostics; TikTok Test Events. Check that deduplicated counts match the order system within an agreed tolerance.
7. **Monitor weekly for the first month**, then monthly: deduplication rate, match quality indicators, discrepancy against CRM. Stop and fix if duplicates appear; rerun verification after every fix.

## Consent-aware experiment measurement (benchmark SL10-C4)

Use when an A/B test, holdout or geo test is read from GA4 or a server container rather than inside one ad platform's own lift tool. Design and statistics stay with `meta-testing-framework` and `advertising-attribution-and-measurement`; this procedure makes sure the measurement layer does not bias the read.

1. Assign the variant or cohort before any consent-dependent tag fires, and write it to the data layer (`experiment_id`, `variant`) so both browser and server events carry it.
2. Pass the consent state with every server event; send only what that state allows.
3. Report, per variant, the share of visitors whose analytics consent was denied. If the shares differ by more than the tolerance set in the test plan, stop and treat the read as biased.
4. Count the primary metric from the system of record (orders, CRM) where possible, so denied-consent visitors still count; use GA4 or platform figures as secondary.
5. Record in the test log which traffic was unmeasured and why; rerun the check after any CMP or container change during the test.

## Server-side cost line (template)

| Item | Assumption | Monthly cost | Source |
|---|---|---|---|
| Server instances | 3 instances, production | USD 30–50 per server (Google's typical figure) | GOOGLE-SGTM-2026 |
| Network traffic | Estimated requests × payload | Estimate; verify on the client's billing account | not assessed until live |
| Maintenance | Named owner, hours per month | Agency or client rate | client |

## Anti-patterns

- Sending purchases from both Pixel and CAPI with different IDs. Fix: one event ID generated once in the data layer.
- Hashing `fbp`, `fbc`, IP or user agent. Fix: send them raw as Meta requires.
- Hashing un-normalised phone numbers (for example `0772…` without the country code). Fix: normalise to digits with the country code (256 for Uganda, 254 for Kenya) before hashing.
- Sending CRM sales to Meta more than 7 days after the event. Fix: schedule daily or weekly uploads within the window.
- Selling server-side GTM as a way around consent. Fix: pass consent state to the server and respect it.
- Treating platform "matched" conversions as business results. Fix: reconcile against the CRM in `advertising-attribution-and-measurement`.

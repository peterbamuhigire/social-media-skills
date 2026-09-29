# Event Taxonomy and Tracking Plan

New reference for `measurement-tracking-plan` (Social Kaizen S04-T01, benchmark gap G04, 29 September 2026). Platform facts cite `docs/source-registers/source-register.json` IDs; anything without an ID is marked for verification at use.

## When to use this reference

Use it to write the event map, the data-layer specification and the QA log: the core of the tracking plan. It answers three questions for every business action: what is recorded, who owns it, and under which consent state it may be sent.

## Inputs

| Input | Provider | If absent |
|---|---|---|
| Value event (sale, qualified lead, booking, WhatsApp order) and the steps before it | Client lead | Stop; no event map without it |
| Site or app map with forms, checkout, WhatsApp click-to-chat buttons, phone links | Web owner | Map from a crawl or walkthrough; mark unverified pages |
| Current GTM container or tag inventory | Web or analytics owner | Plan target state only; current-state checks `not assessed` |
| CRM or order system fields (lead ID, order ID, status, value) | CRM owner | Plan a manual weekly export and flag the gap |
| Consent design | [consent-mode-and-cmp.md](consent-mode-and-cmp.md) | Mark every marketing tag "blocked until consent" |

## Decision rules

| Condition | Action | Risk avoided |
|---|---|---|
| An action does not feed a decision anyone will take | Do not track it; note it in the minimisation register | Data collected "in case" |
| Google publishes a recommended event name for the action (for example `generate_lead`, `purchase`, `sign_up`) | Use it rather than a custom name (verify the current recommended-events list at use; no register record) | Custom names that lose built-in reports |
| The action is the business outcome or its nearest observable proxy | Mark it a GA4 key event and the matching Google Ads or Meta conversion | Optimising for vanity steps |
| The action happens off-site (WhatsApp, phone, shop counter) | Record the on-site intent event (click-to-chat, call click) and plan an offline or CRM import for the outcome | Counting clicks as sales |
| The same action is also sent from a server | Create one ID in the data layer and pass it to browser and server events ([server-side reference](server-side-capi-and-enhanced-conversions.md)) | Double counting |
| An event parameter could carry personal data (email in a URL, phone in a form field name) | Remove or hash it before any tag reads it; never send raw personal data to GA4 | Personal data in analytics, which Google's policies prohibit (verify at use; no register record) |

## Procedure

1. **List business actions** from the value event backwards: outcome, qualifying steps, intent signals. Keep 5–15 events for an SME site; more needs a reason.
2. **Name each event** in lowercase snake_case (GA4 convention; verify at use, no register record), verb first, no spaces, no personal data. One name means one thing across GA4, Google Ads, Meta and TikTok mappings.
3. **Define parameters** per event: value and currency (UGX, KES, TZS, RWF, USD), item or service ID, lead type, form ID, WhatsApp button location, and the deduplication ID where the event is double-sent.
4. **Set key events**: normally one primary (the value event) and at most two secondary (qualified lead, booking). Everything else stays an ordinary event.
5. **Write the data-layer specification** for the developer: the `dataLayer.push` object per event, when it fires, and which fields are hashed server-side.
6. **Assign ownership**: the person who fixes the event when it breaks, and the person who signs off the numbers.
7. **Map consent**: for each event and destination, what is sent when analytics or ad consent is denied (see the consent reference).
8. **Write the QA log** (template below) and run it in GTM preview, GA4 DebugView and each platform's test tool before launch.
9. **Re-run QA** after any container publish, site release or CMP change; record the date.

## Event map template

| Business action | Event name | Trigger | Parameters | Key event? | Source (browser / server / CRM / WhatsApp) | Destinations (GA4, Google Ads, Meta, TikTok, LinkedIn) | Consent dependency | Dedup ID | Owner |
|---|---|---|---|---|---|---|---|---|---|
| Customer submits a quote form | `generate_lead` | Form success page or success event | `form_id`, `lead_type`, `value`, `currency`, `event_id` | Yes (primary for lead-gen) | Browser + server | GA4, Google Ads, Meta | analytics_storage for GA4; ad_storage / ad_user_data for ads | `event_id` from data layer | Web owner |
| Visitor taps "Chat on WhatsApp" | `whatsapp_click` | Click on wa.me link | `button_location`, `page_type` | No (intent signal) | Browser | GA4, Meta | analytics_storage | n/a | Web owner |
| Order confirmed in the CRM | `purchase` (offline import) | CRM status = paid | `transaction_id`, `value`, `currency` | Yes | CRM | Google Ads (enhanced conversions for leads or offline import), Meta CAPI | Consent captured at lead time | `transaction_id` | CRM owner |

## QA log template

| # | Event | Consent state tested (granted / denied / partial) | Tool | Expected result | Observed | Pass / fail / not assessed | Date | Tester |
|---|---|---|---|---|---|---|---|---|

Pass rule: every key event passes in the granted state; in the denied state no advertising cookie is written and only the behaviour allowed by the consent design is observed.

## GA4 settings that belong in the plan

- Engaged session = longer than 10 seconds, a key event, or 2+ page or screen views (register GA4-ENGAGED-SESSION-2026). Use engagement rate, not bounce rate, as the quality measure.
- Retention: 2 or 14 months on standard properties, affecting explorations and funnel reports only (register GA4-DATA-RETENTION-2026). Raw history beyond that needs the BigQuery export ([ga4-bigquery-export.md](ga4-bigquery-export.md)).
- GA4 does not log or store IP addresses (register GA4-IP-2026).
- Reporting identity must be Blended for consent-mode modelled data to appear (register GA4-CONSENT-MODELLING-2026).

## Release checklist

- [ ] Every event traces to a decision and an owner.
- [ ] Names are lowercase snake_case, consistent across destinations, free of personal data.
- [ ] Key events are limited to the value event and at most two qualifying steps.
- [ ] Every double-sent event carries one deduplication ID.
- [ ] Off-site outcomes have an import route or are marked `not assessed`.
- [ ] QA log run before launch, dated, and scheduled after each release.

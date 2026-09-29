---
name: measurement-tracking-plan
description: Use when a client needs a privacy-safe tracking plan before launch - event and key-event map, UTM convention, Consent Mode v2 and CMP, server-side tagging, Conversions API and enhanced conversions, GA4 BigQuery export; produces a tracking plan and QA log; not for attribution models or incrementality (use `advertising-attribution-and-measurement`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Measurement Tracking Plan

Decide what a client's website, app, WhatsApp and CRM touchpoints must record, under which consent state, through which route (browser tag, server container, platform API) and with which names, so that every later report, attribution read and experiment rests on signals the client is allowed to collect. The consumer is the client's web or analytics owner and the media team; the skill writes the plan and the QA evidence, it does not install tags.

<!-- dual-compat-start -->
## Use When
- A campaign or site is about to launch and nobody has written down which events, key events and parameters must fire, or who owns them.
- The client asks for Consent Mode v2, a cookie banner or consent management platform (CMP), or wants to know what happens to measurement when visitors refuse cookies.
- Conversions reported by Meta or Google look low or duplicated and the fix is signal quality: Conversions API with Pixel deduplication, enhanced conversions, server-side Google Tag Manager.
- The analyst wants raw GA4 events in BigQuery, or needs to know the export limits and cost before promising a dashboard.
- Standardise UTM naming, a campaign link register and WhatsApp dark-social tagging so every social link lands in GA4 under the right source, medium and campaign (formerly `meta-utm-tracking`).
- Review analytics privacy: cookie consent, GA4 retention and Google signals, data minimisation register, WhatsApp contact data, deletion requests and cross-border records under Uganda's DPPA 2019 or Kenya's DPA 2019 (formerly `meta-analytics-privacy`).

## Do Not Use When
- Choosing an attribution model, setting break-even ROAS or designing a holdout or geo test: use `advertising-attribution-and-measurement`.
- Building the monthly report or dashboard layout: use `meta-reporting`; defining the KPI dictionary itself: use `meta-social-metrics-framework`.
- Writing the landing-page build handoff (page, form and journey specification for developers): use `ad-to-site-journey-handoff`.
- Giving a legal opinion, drafting a privacy policy or a DPIA: stop and refer to qualified data-protection counsel; this skill states implementation positions only.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Business objective, value event and the actions that create revenue or leads | Approved brief or client lead | Yes | Stop; request it. No event map without a value event. |
| Current tag inventory (GTM container export, pixels, SDKs, CRM or WhatsApp labels) | Client web or analytics owner | Yes | Build the plan as "target state"; mark every current-state check `not assessed`. |
| Markets and audiences served, including any EEA, UK or Swiss visitors | Client lead | Yes | Assume the strictest market named anywhere in the brief and flag the assumption. |
| Consent position: banner or CMP in use, privacy notice, PDPO/ODPC registration status | Client data-protection owner | Conditional (yes when personal data or EEA/UK/CH traffic) | Plan consent-denied behaviour first; record the gap for counsel. |
| Platform accounts in scope (GA4 property type, Google Ads, Meta dataset, TikTok, LinkedIn) | Client-authorised accounts | Conditional | List as `not assessed`; do not state account-specific limits. |
| Campaign calendar and naming already in use | Content calendar or media plan | Conditional | Issue the UTM convention with placeholders and a migration note. |

## Workflow
1. Confirm the value event, the decisions the data must support and the markets served; route to `advertising-attribution-and-measurement` if the real question is credit or causality. Stop if no value event can be named.
2. Map events: for each business action write the event name, trigger, parameters, key-event flag, source (browser, server, CRM, WhatsApp) and owner, using [event taxonomy and tracking plan](references/event-taxonomy-and-tracking-plan.md).
3. Set the consent design before any tag choice: consent defaults per region, basic or advanced Consent Mode, CMP, and what each tag may do when consent is denied ([Consent Mode v2 and CMP](references/consent-mode-and-cmp.md)).
4. Choose the collection route per event: browser only, browser plus server (Conversions API, server-side GTM) with a deduplication key, or offline import (enhanced conversions for leads) ([server-side, CAPI and enhanced conversions](references/server-side-capi-and-enhanced-conversions.md)).
5. Fix the naming layer: UTM convention, campaign register and dark-social tagging ([UTM convention and campaign register](references/utm-convention-and-campaign-register.md)).
6. Plan storage and access: GA4 retention, BigQuery export type and its limits, who can see raw data, the data-minimisation register and cross-border records ([GA4 BigQuery export](references/ga4-bigquery-export.md); [consent, retention and sharing review](references/consent-retention-and-sharing-review.md)).
7. Write the QA plan: test cases per event and consent state, the tools used (GTM preview, GA4 DebugView, Meta Test Events, Google Ads diagnostics), expected result and pass rule.
8. Run the quality and anti-slop gates. If a blocking gap remains (no consent design for a regulated market, no deduplication key for a double-sent event), withhold the plan and correct it; rerun the QA checklist after every fix.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Tracking plan (event map, parameters, key events, owners, collection route) | Client web or analytics owner; media team | Every event has trigger, parameters, owner, consent dependency and route; every double-sent event names its deduplication key |
| Consent design | Client data-protection owner; developer | Defaults per region, mode (basic or advanced), CMP choice and denied-state behaviour stated per tag |
| UTM convention and campaign register | Everyone who publishes links | Approved source, medium and campaign values, lowercase-hyphen rules and a filled register template |
| QA log template and first QA run | Client analyst | Each event × consent state has a test, an expected result and a pass/fail/`not assessed` entry |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Source register extract | Table in the plan | Every platform limit or rule cites a register ID and date, or is marked `verify before stating` |
| Tag inventory diff | Table (current versus target) | Each tag: keep, change, remove or add, with the reason |
| Assumption and gap log | Table | Consent, legal and account assumptions named with an owner and the evidence that would close each |

## Capability and Permission Boundaries
Read and search only; analysis is read-only. Publishing, spend, live account changes, tag or container publishing, uploading customer data, changing consent settings and any personal-data processing need explicit, action-specific client authority. Legal conclusions route to qualified counsel.

## Degraded Mode
Without a tag inventory or account access, return the narrowest qualified result: a target-state plan, the consent design and a data request, with every current-state check marked `not assessed`. Never report a tag as firing, or a consent signal as passed, without a recorded test.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| EEA, UK or Swiss visitors reach pages carrying Google tags | Implement Consent Mode v2 (all four parameters) through a CMP; choose advanced mode when modelling is wanted and the legal position allows tags to load before consent (register GOOGLE-CONSENT-MODE-PARAMS-2026, GOOGLE-CONSENT-MODE-DEV-2026) | Lost audiences and remarketing, and non-compliant collection |
| Audience is Uganda, Kenya, Tanzania or Rwanda only | Treat consent as required where cookies or identifiers collect personal data (Uganda DPPA 2019; Kenya DPA 2019, where consent is one lawful basis) and confirm with counsel; Consent Mode is recommended, not a Google requirement, outside the EEA/UK/CH | Treating "not EEA" as "no consent needed" |
| The same conversion is sent by browser and server | Send one shared `event_id`/`eventID` and identical event name; Meta only deduplicates within 48 hours (register META-CAPI-DEDUP-2026) | Double-counted purchases and inflated ROAS |
| Leads close offline, on the phone or on WhatsApp | Capture a hashed email or phone at lead time and plan enhanced conversions for leads or a CRM offline import (register GOOGLE-ENHANCED-CONVERSIONS-2026) | Bidding systems optimising for form fills, not sales |
| Standard GA4 property expected to exceed 1M events a day | Filter the daily export or use streaming export (paid, no completeness guarantee) and say so in the plan (register GA4-BIGQUERY-EXPORT-2026) | Silent export failures and incomplete tables |
| Client proposes server-side GTM | Cost it (Cloud Run, at least 3 instances in production) and name who maintains it; server-side does not remove the need for consent (register GOOGLE-SGTM-2026) | An unowned server that fails quietly, or "server-side to avoid consent" |
| A link will be shared by WhatsApp or pasted into bios | Tag it with UTM values from the convention and shorten it; log it in the campaign register | Social traffic reported as "direct" |
| No lawful basis or registration evidence for personal data (PDPO, ODPC, PDPC) | Stop the personal-data parts of the plan; record the gap for the data-protection owner | Processing personal data without authority |

## Quality Standards
- One event map row per business action, with a named owner and a consent dependency.
- Consent behaviour is specified per tag and per consent state, not described in general terms.
- Every server-plus-browser event names its deduplication key; hashed fields and never-hashed fields follow the platform rules.
- Every platform limit (export caps, deduplication window, event age) cites a register ID and verification date.
- UTM values are lowercase and hyphenated and come from one approved table.
- The QA log exists before launch and is re-run after each container change.
- British English; no legal advice; "not assessed" used wherever evidence is missing.

## Anti-Patterns
- Firing marketing tags before the consent banner resolves on regulated traffic. Fix: set denied defaults before any tag loads and wire the CMP update.
- Sending Conversions API and Pixel events without a shared event ID. Fix: generate one ID per action in the data layer and pass it to both.
- Hashing the wrong fields (IP address, user agent, fbp, fbc) or hashing unnormalised values. Fix: follow the normalise-then-hash table in the server-side reference.
- Promising a BigQuery dashboard on a standard property with no volume check. Fix: estimate daily events first and choose daily, filtered or streaming export.
- Tracking every click "in case". Fix: keep only events tied to a decision and list each in the data-minimisation register.
- Letting each publisher invent UTM values. Fix: one approved values table and a campaign register checked monthly.
- Presenting modelled conversions as observed counts. Fix: label modelled figures and state the consent-mode eligibility status.

## References
- [Event taxonomy and tracking plan](references/event-taxonomy-and-tracking-plan.md) — read when writing the event map, data layer and QA log.
- [Consent Mode v2 and CMP](references/consent-mode-and-cmp.md) — read when designing consent defaults, choosing basic or advanced mode or a CMP.
- [Server-side tagging, Conversions API and enhanced conversions](references/server-side-capi-and-enhanced-conversions.md) — read when events are sent from a server, deduplicated or matched with hashed data.
- [GA4 BigQuery export](references/ga4-bigquery-export.md) — read when raw-event access, export limits or cost matter.
- [UTM convention and campaign register](references/utm-convention-and-campaign-register.md) — read when setting link naming, the link builder routine and WhatsApp dark-social tagging.
- [Consent, retention and sharing review](references/consent-retention-and-sharing-review.md) — read when reviewing cookie consent, GA4 privacy settings, data minimisation, WhatsApp contact data and legal-referral triggers.
- [Advertising attribution and measurement](../../advertising/advertising-attribution-and-measurement/SKILL.md) (models, economics, incrementality); [meta-reporting](../meta-reporting/SKILL.md); [meta-social-metrics-framework](../meta-social-metrics-framework/SKILL.md); [ad-to-site journey handoff](../../advertising/ad-to-site-journey-handoff/SKILL.md).
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md) during drafting; [AI slop audit](../../ai-marketing/ai-slop-audit/SKILL.md) at release.
- [Current-source register](../../../docs/source-registers/README.md); [legal, privacy and market release gate](../../../docs/quality-gates/legal-market-release-gate.md); [measurement proof pack](../../../docs/evidence-packs/measurement-proof-pack.md).
<!-- dual-compat-end -->

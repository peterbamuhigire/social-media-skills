# Measurement and ownership spec

When to read: when defining how a campaign journey is tagged, counted and owned before build and launch.

## 1. UTM table (per ad or ad group)

Follow the naming convention in `meta-utm-tracking`. Minimum columns:

| Ad ID | utm_source | utm_medium | utm_campaign | utm_content | utm_term (search) | Final URL | Short link (for WhatsApp/offline) |
|---|---|---|---|---|---|---|---|

Rules: lower case, no spaces, one agreed vocabulary; offline and WhatsApp-forwarded traffic uses short links, unique QR codes or keywords so it can be counted; dark-social caveats recorded.

## 2. Conversion events

| Event | Trigger | Where it fires | Primary or secondary | Value | Dedup rule |
|---|---|---|---|---|---|
| lead_submit | Successful form submission | Thank-you state | Primary | From budget model | Once per submission ID |
| whatsapp_click | Click on wa.me link | Page | Secondary | — | Once per session |
| call_click | Click on tel: link | Page | Secondary | — | Once per session |
| booking_confirmed | Booking system confirmation | Confirmation page or import | Primary | Booking value | Once per booking ID |
| qualified_lead (offline) | CRM stage change | Imported | Primary for bidding when volume allows | Agreed | CRM ID |

Platform event names differ by tool (for example Meta standard events such as Lead, Contact, Purchase); map the table to each platform's current event list on the day of build and record the date.

## 3. Consent and data protection

- EEA/UK/CH visitors with Google tags: CMP plus Consent Mode v2 signals (ad_storage, analytics_storage, ad_user_data, ad_personalization); advanced mode allows modelling, basic mode blocks tags until consent (CW-10, checked 2026-09-23).
- Uganda: collection requires consent under s.7; register with the PDPO where required; honour written direct-marketing objections within 14 days (PL-01). Do not describe the Act as requiring marketing opt-in.
- Kenya: consent plus a free, simple opt-out for direct marketing; objections are absolute; direct-marketing businesses register with the ODPC regardless of size (PL-02).
- Privacy notice discloses pixels, conversions APIs and retargeting.

## 4. Journey RACI

| Task | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Landing-page brief and copy | Agency strategist/copywriter | Agency account lead | Client marketing | Web team |
| Visual design | Designer (design-system-skills) | Agency creative lead | Client brand owner | Web team |
| Page build | Website team (website-skills) | Client web owner | Agency | Client marketing |
| Tags and events | Developer / tag owner | Client web owner | Agency analyst | Agency account lead |
| Consent tool | Developer | Client data-protection owner | Legal | Agency |
| QA (tracking, speed, accessibility, links) | Web team + agency analyst | Agency account lead | Client | Client approver |
| Go-live of traffic | Authorised media operator | Client approver | Agency | Web team |
| Monitoring and reporting | Agency analyst | Agency account lead | Web team | Client |

Adjust names per engagement; every row needs one accountable person and a date.

## 5. Go/no-go gate

- [ ] Message-match table complete and approved.
- [ ] Brand-slice audit passed (page, contact scripts, reviews, photos consistent with ad themes).
- [ ] Every conversion event tested; QA log dated.
- [ ] Consent handling confirmed for in-scope jurisdictions.
- [ ] Speed and accessibility results reported by the web team against the stated targets.
- [ ] Forms route to a monitored inbox or CRM; WhatsApp monitored with the promised response time.
- [ ] Mandatory disclosures and regulated-category text present.
- [ ] Client approval for traffic launch recorded.

Any unchecked blocking item withholds paid traffic.

## 6. Post-launch loop

Weekly for the first month, then monthly: funnel by level (suspect → lead → prospect → customer), cost per level by source, form drop-off points, response times, top objections heard by sales; hand a ranked fix list to the web team; re-run the gate after material page changes.

# Search build specification

When to read: when structuring a new Google Ads account, adding a campaign, or writing the build sheet an authorised operator will execute.

## 1. Intent map

| Intent layer | Example query shape | Campaign treatment |
|---|---|---|
| Brand | "[brand] [town]" | Separate brand campaign; protect; low budget share |
| Problem | "[symptom] fix", "why is my [thing]…" | Informational pages or lead magnets; judge on micro-conversions |
| Solution | "[service] in [town]", "[product] price" | Core money campaign; strongest landing pages |
| Comparison / competitor | "[competitor] alternative" | Only with legal and brand approval; no trademark misuse; comparison claims evidence-based |
| Local / urgent | "[service] near me", "open now" | Location and hours accurate; call and WhatsApp actions |
| Price / purchase | "[product] cost", "buy [product]" | Price on the landing page if commodity; offer terms clear |

## 2. Keyword research log

Record for every research session: tool, account locale and language, date, seed terms, filters, the exported list, and the decision per theme (use / test / exclude). Never invent or remember volumes. Where volumes are too low to show, use the test-first method (run a small budget on the theme and read real queries).

## 3. Structure template

```
Account
├── Brand — Search
│   └── Ad group: brand terms → home or brand page
├── [Service A] — Search (non-brand)
│   ├── Ad group: [service A] + [town]
│   └── Ad group: [service A] price / cost
├── [Service B] — Search (non-brand)
├── Performance Max (only when conversion signals and assets or feeds exist)
│   └── Asset group per product line or audience theme; search themes; brand exclusions
└── Demand Gen (visual demand generation / retargeting-style reach)
Shared: negative keyword list; conversion actions; audience lists (lawful basis recorded)
```

Match-type behaviour, keyword matching rules, bidding strategy minimums and learning periods change: record "checked on [date] against the Google Ads Help Centre" beside each choice.

## 4. Assets per ad group

- One responsive search ad per ad group to start (more only when testing a distinct message), written to the AD-05 limits; follow `ad-copy-and-hook-lab` format guidance.
- Sitelinks to real pages (pricing, booking, locations, proof), callouts (true, specific), structured snippets where relevant, call asset and location asset for local businesses; check current asset types on the day.
- Final URL with UTM parameters from `meta-utm-tracking`; one landing page per theme.

## 5. Conversion tracking brief

| Item | Specification |
|---|---|
| Primary conversion | e.g. qualified lead form submit, booked appointment, purchase — fires once per real action |
| Secondary conversions | calls over a set duration, WhatsApp click, key page view — tracked but not used for bidding unless agreed |
| Values | from the value per conversion agreed in the budget model |
| Offline conversions | CRM-qualified leads or sales imported where volume and consent allow |
| Consent | EEA/UK/CH users: CMP + Consent Mode v2 signals (ad_storage, analytics_storage, ad_user_data, ad_personalization); advanced mode enables modelling, basic mode blocks tags (CW-10, checked 2026-09-23) |
| Analytics | GA4 is Google's only analytics product (CW-10) |
| QA | Test each action; record screenshots and date; no launch until QA passes |

## 6. Budget and bidding plan

- Break-even CPA = gross profit per conversion (or lifetime contribution share agreed with finance).
- Start budget: enough to read the test within the planned window; spread thin budgets over fewer themes rather than many.
- Bidding: start with the approach whose data requirements the account can meet; move to automated conversion bidding only when the live help centre's current guidance is satisfied and tracking is clean.

## 7. Pre-launch checklist

- [ ] Conversion actions defined, valued and tested.
- [ ] Brand and non-brand separated; shared negatives applied.
- [ ] Each ad group has a matching landing page approved through the journey handoff.
- [ ] Ads pass the ethics filter and policy pre-check (health, finance, gambling, political and other restricted categories checked on the day).
- [ ] Budgets and end dates set in the build sheet; client written approval recorded.
- [ ] Reporting view and review cadence agreed.

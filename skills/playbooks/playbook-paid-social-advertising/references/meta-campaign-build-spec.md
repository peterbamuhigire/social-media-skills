# Meta campaign build spec

When to read: when writing the build sheet for Facebook, Instagram, Messenger or WhatsApp-destination campaigns. Platform facts are from the currentness register (checked 2026-09-23); anything not listed there is a check on the day.

## 1. Current platform facts (register)

| Topic | Fact | Register |
|---|---|---|
| Objectives | Awareness, Traffic, Engagement, Leads, App promotion, Sales | AD-01 |
| Advantage+ | A state of a normal campaign, on when Advantage+ audience, Advantage+ campaign budget and Advantage+ placements are all enabled; Advantage+ sales replaces Advantage+ shopping; Advantage+ app replaces the older app campaign; an Advantage+ leads campaign exists; legacy ASC/AAC creation blocked from Marketing API v25.0 | AD-02 |
| Special ad categories | Housing; Employment; Financial products and services (replaced "Credit", required since 14 Jan 2025); Social issues, elections or politics. Housing/employment/financial ads: ages 18–65+, all genders, minimum 15-mile/25-km radius, no postcode targeting, no lookalikes — for ads reaching the US, Canada and Europe. No social-issue, electoral or political ads in the EU since 6 Oct 2025 | AD-03 |
| Political/social-issue ads | Advertiser authorisation and a verified "Paid for by" disclaimer; kept in the Ad Library for 7 years; all active ads are searchable in the Ad Library | AD-04 |
| Feed image | Recommended 4:5, 1440×1800; supported 1.91:1 to 4:5 | AD-08 |
| Stories/Reels | 9:16, 1440×2560; keep ~14% top, ~35% bottom, ~6% each side free of text, logos and key elements | AD-08 |

Not assessed at T1 (check on the day): whether Uganda/Kenya-only campaigns must declare a special category (many advertisers are asked globally); country authorisation rules for political ads in UG/KE; exact v25/v26 dates; the reported 2026 Ads Manager UI merge; Meta's Uganda VAT page.

Do not teach "ASC" as a separate campaign type; do not use the retired "20% text in image" rule.

## 2. Structure

```
Campaign (objective; optional Advantage+ campaign budget)
└── Ad set (audience, placements, schedule, budget, optimisation event)
    └── Ad (creative, copy, CTA, destination, UTMs)
```

- One objective per campaign; separate prospecting from retargeting where pools are large enough to read.
- Two or three ads per ad set to start; one variable changes per test.
- Record for each field whether Advantage+ automation is on, and why.

## 3. Audiences

- Cold: location (city or district for Kampala-focused offers), age, interests or broad; lookalikes only from consented buyer lists and never for special-category ads where barred.
- Warm: video viewers, engagers, followers, messaging contacts.
- Retargeting: website visitors and abandoners via Pixel/Conversions API; lead-form openers.
- Exclusions: existing customers from acquisition ads; recent converters.
- Customer-list uploads: lawful basis and notice recorded (Uganda s.7 consent and s.26 objection right, PL-01; Kenya consent plus free simple opt-out, objections absolute, PL-02).

## 4. Tracking brief for the web developer

| Item | Specification |
|---|---|
| Base pixel | All pages, via tag manager where possible |
| Conversions API | Server-side events for reliability where the site supports it; check current setup options |
| Standard events | ViewContent (service/product page), Lead (successful enquiry submit), Contact (WhatsApp or phone click), Purchase (e-commerce) — confirm current event names on the day |
| Deduplication | Event IDs shared between browser and server events |
| Consent | CMP where required; EEA/UK/CH rules for Google tags are in CW-10; privacy notice discloses tracking |
| QA | Events Manager test tool; record dated screenshots; launch conversion campaigns only after QA passes |

## 5. Creative brief template (one per ad)

```
Client / campaign / ad set:
Objective and optimisation event:
Audience tier and awareness level:
Format and placement: [feed 4:5 | Stories/Reels 9:16 | carousel | video]  Spec source: AD-08 (2026-09-23) or help URL + date
Hook (first line / first seconds):
Primary text (short and long versions):
Headline / CTA button:
Proof element (consented):
Offer and terms (true deadline + reason):
Visual direction: [scene, product, person; safe zones respected; brand assets]
Captions: yes (sound-off)
Disclosure: [paid partnership label if creator/partner content]
Destination: [URL with UTMs | lead form | WhatsApp number + pre-filled message]
Approval owner and date:
```

Creative principles retained from Marshall (2024): contrast (look different from the feed), curiosity (an open loop), and genuine entertainment where the brand permits. Match copy to awareness: cold audiences get problem identification, warm get the solution, retargeting gets the specific offer or objection answer.

## 6. Pre-launch checklist

- [ ] Objective and optimisation event match the business goal.
- [ ] Special-category status declared or confirmed not applicable.
- [ ] Tracking QA passed; UTMs on every URL.
- [ ] Ads pass the ethics filter and current advertising-standards check.
- [ ] WhatsApp response staffing confirmed.
- [ ] Budget, dates and written approval recorded.

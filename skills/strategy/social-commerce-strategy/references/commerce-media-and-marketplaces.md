# Commerce media and marketplaces

Read when a client sells through, or advertises on, a retailer or marketplace (retail media, sponsored listings, Jumia, Jiji), when a commerce-media vendor reports sales results that need checking, when marketplace selling is weighed against social and WhatsApp commerce, or when a payment or mobile-money checkout set-up raises a licensing question. Parent skill: [social-commerce-strategy](../SKILL.md). Added in Social Kaizen S10 (29 Sep 2026).

Evidence status. Sources read live on 29 Sep 2026 unless marked. Marketplace fees, commissions and seller terms were **not** read and are `NOT_ASSESSED`; confirm them on the marketplace's own seller pages and date the check in the payment provider and fee register. The payments-law note is screening and escalation, not legal advice.

## 1. What retail-media measurement must show (IAB/MRC 2024)

The IAB/MRC *Retail Media Measurement Guidelines* (January 2024, register `IAB-MRC-RETAIL-MEDIA-2024`) set out what a retail media network's reporting should meet. Use them as the checklist when a client buys sponsored products, on-site display or off-site audiences from a retailer or marketplace:

| Area | What the guidelines expect | What to ask the network |
|---|---|---|
| Data quality | Documented collection and processing, de-duplication, quality checks and periodic internal and independent audits; known errors disclosed to users | Is the measurement audited or MRC-accredited? When was it last checked? |
| Impressions and viewability | Report impressions and viewable impressions under MRC standards (display: 50 % of pixels for one continuous second; video: 50 % for two seconds), with measured and viewable rates; distinguish on-site from off-site | Viewable and measured rates by placement, on-site and off-site separately |
| Invalid traffic | At least MRC general invalid traffic (GIVT) filtration, strongly encouraged sophisticated (SIVT) filtration; SIVT filtration required for outcome measurement; unknown IVT disclosed, not assumed valid | Which IVT filtration applies to the sales figures? |
| Attribution | Weighting of exposures supported by evidence and disclosed; attribution (look-back) windows empirically supported, consistent across similar objectives and **disclosed before the campaign**; day-level data so windows can be reconciled; SKU-level reporting and disclosure of "halo" products counted | The window used, set in writing before launch; SKU-level results; whether halo sales are included |
| Modelled and extrapolated sales | Transparency about modelling for unidentified buyers (cash, card and loyalty capture limits, privacy settings) and for sales at other retailers | How much of the reported sales is modelled rather than observed |
| Outcomes and viewability | Attribution based on non-viewable impressions may be reported only with a clear disclaimer beside compliant metrics | Compliant and non-compliant figures side by side |
| Incrementality | Chapter 4 covers randomised controlled trials, synthetic controls, matched-market tests and machine-learning models, with transparency about method and data limits | Has lift been measured with a control group, and how? |
| MMM inputs | At minimum a dataset for media-mix modelling (market, format, time, impressions, clicks, campaign, audience, device, cost) | Can we export it for our own model? |

East Africa: most local marketplaces and retailers do not offer audited retail-media reporting. Where a network cannot answer the table, treat its sales figures as vendor-reported attribution, label them "(Vendor)", and do not compare them with other channels as if they were incremental.

## 2. Commerce-media incrementality

Attributed sales are not incremental sales. The IAB and IAB Europe *Guidelines for Incremental Measurement in Commerce Media* (November 2025, register `IAB-INCREMENTAL-COMMERCE-MEDIA-2025`) group methods by causal strength: experiments (randomised controlled tests, holdouts or ghost ads, matched markets) are strongest; model-based counterfactuals (synthetic control, propensity models) are strong to moderate; media-mix models give the cross-channel view; and a credible counterfactual is the first requirement for any causal claim.

Planning rules:

1. Ask the network for a holdout or ghost-ad test before scaling spend; record its design, dates and control size.
2. Where the network offers no test, use a geo or time-based comparison the client can run itself (for example, switch sponsored listings off in one city or for alternate fortnights), measured on the client's own orders.
3. Report incremental return on ad spend separately from platform ROAS; route the method to [`advertising-attribution-and-measurement`](../../../advertising/advertising-attribution-and-measurement/SKILL.md).
4. Watch for contamination: buyers who see the same product on WhatsApp, TikTok or radio during the test.

## 3. Marketplaces in Uganda, Kenya and Tanzania

| Marketplace | Where it operates (checked 29 Sep 2026) | Model | Register |
|---|---|---|---|
| Jumia | Jumia Group's site says it is active in 8 countries: Egypt, Ghana, Ivory Coast, **Kenya**, Morocco, Nigeria, Senegal and **Uganda**. Tanzania and Rwanda are not in the list | Online retail marketplace with third-party sellers | `JUMIA-GROUP-MARKETS` |
| Jiji | jiji.ug is an active Uganda classifieds marketplace; its footer lists Jiji sites in Nigeria, **Kenya**, **Tanzania**, Ghana, Ethiopia and others. Jiji took over OLX's businesses in Ghana, Kenya, Tanzania and Uganda in April 2019 (OLX Group) | Classifieds: free listing as the base, with paid promotion tiers shown on listings (for example "VIP", "Diamond", "Enterprise" badges) | `JIJI-MARKETS`, `OLX-JIJI-2019` |

Rwanda: neither marketplace is confirmed there on these pages; marketplace options for Rwanda are `NOT_ASSESSED`.

Seller playbook (onboarding steps and fees `NOT_ASSESSED`; confirm on each marketplace's seller page):

1. **Choose by product and buyer.** Jumia suits packaged, shippable goods where buyers expect a retail checkout and delivery; Jiji suits used goods, vehicles, property, services and negotiable items where buyers call or chat and pay on meeting.
2. **Register as the business, not a person.** Prepare business registration, tax identification, a bank or mobile-money account for payouts and product images the client owns.
3. **List for search.** Titles with brand, model and key attribute; accurate stock; real photographs; prices in UGX, KES or TZS that match the social shop and WhatsApp catalogue.
4. **Record the economics before listing.** Commission, listing or promotion fees, delivery and return costs from the seller terms; check each product still passes the 3X rule and minimum-price rule in [pricing, conversion and differentiation](pricing-conversion-and-differentiation.md).
5. **Protect the buyer relationship lawfully.** Follow the marketplace's rules on moving buyers off-platform; invite repeat buyers to the WhatsApp list only through an opt-in that names the business (see [WhatsApp Platform pricing and templates](../../../platforms/platform-whatsapp/references/whatsapp-platform-pricing-and-templates.md) §6).
6. **Paid promotion.** Treat sponsored listings or Jiji promotion packages as retail media: set the test in §2 before scaling.
7. **Scam and trust controls.** On classifieds, use verified-seller features where offered, meet in safe public places or use tracked delivery, and never release goods before payment is confirmed on the provider's own record, not a screenshot alone.

## 4. Mobile-money checkout context

- **Scale.** GSMA's *State of the Industry Report on Mobile Money 2026*, as reported by Connecting Africa on 26 Mar 2026, puts sub-Saharan Africa's 2025 mobile-money transaction value at USD 1.4 trillion, with East Africa at USD 806 billion (register `GSMA-MOBILE-MONEY-2025`; **Secondary** — the GSMA report itself was not read).
- **M-Pesa (Kenya).** Safaricom's audited results for the year to 31 Mar 2026 report 40.99 million one-month active M-Pesa customers (+14.5 %), transaction value of KShs 41.68 trillion, and 3.1 million merchants (Pochi 2.1 million; Lipa na M-PESA 1.0 million) (register `SAFARICOM-FY2026-MPESA`). For Kenyan clients, a Lipa na M-PESA till or paybill is the default checkout; for Uganda, MTN MoMo and Airtel Money remain the primary methods set in the parent skill.
- Keep one payment confirmation rule across social shop, WhatsApp and marketplace orders: confirm receipt in the provider's merchant record before dispatch.

## 5. Payments-law screening note (Uganda)

Uganda's National Payment Systems Act 2020 requires payment service providers, electronic money issuers and payment system operators to be licensed by the Bank of Uganda; e-money issued by non-bank issuers must be matched by funds in a trust account; and the Act links to the Data Protection and Privacy Act 2019 (register `UG-NPS-ACT-2020`; **Secondary** summary published on kaa.co.ug, 8 Sep 2020; the Act's text was not read).

Screening use only:

- A client that only **accepts** payments through an established provider (for example MTN MoMo or Airtel Money merchant codes, or a payment gateway) relies on that provider's authorisation; confirm the provider's licence status on the Bank of Uganda's published list (`NOT_ASSESSED` here) and record it in the fee register.
- A client that proposes to **hold customer funds**, run a wallet, issue stored value (for example prepaid credit or a closed-loop wallet) or aggregate payments for other sellers may need a licence: stop and escalate to a Ugandan lawyer before any build or promotion. Kenya, Tanzania and Rwanda have their own payment laws, `NOT_ASSESSED` here.

## Sources

- `IAB-MRC-RETAIL-MEDIA-2024` — IAB/MRC, Retail Media Measurement Guidelines, January 2024 (PDF read live 29 Sep 2026).
- `IAB-INCREMENTAL-COMMERCE-MEDIA-2025` — IAB and IAB Europe, Guidelines for Incremental Measurement in Commerce Media, Nov 2025.
- `JUMIA-GROUP-MARKETS` — Jumia Group website (read live 29 Sep 2026).
- `JIJI-MARKETS` — jiji.ug (read live 29 Sep 2026); `OLX-JIJI-2019` — OLX Group, Jiji to welcome OLX users in Africa, 1 Apr 2019.
- `SAFARICOM-FY2026-MPESA` — Safaricom PLC, audited results for the year ended 31 Mar 2026 (PDF read live 29 Sep 2026).
- `GSMA-MOBILE-MONEY-2025` — Connecting Africa report of GSMA State of the Industry Report on Mobile Money 2026 (Secondary).
- `UG-NPS-ACT-2020` — KAA (kaa.co.ug), An overview of the National Payment Systems Act 2020 (Secondary).

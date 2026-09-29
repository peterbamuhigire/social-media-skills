# Shopping and product feeds

Read when a Google Ads plan includes Shopping ads, Performance Max with a product feed or free product listings, when a Merchant Center feed is being built or audited, or when the client asks whether Shopping can target Uganda, Kenya, Tanzania or Rwanda. Parent skill: [paid-search-advertising](../SKILL.md). Added in Social Kaizen S10 (29 Sep 2026).

Evidence status. Read live on 29 Sep 2026: Merchant Center Help, *Product data specification* (register `MERCHANT-CENTER-PRODUCT-DATA`) and *Supported languages and currencies* (register `MERCHANT-CENTER-COUNTRIES-2026`, partial: read through a summarising fetch, so recheck the table directly before promising a launch). The help pages call the product "Merchant Center"; no separate "Merchant Center Next" requirements were found. Feed rules change often; re-check before every build.

## 1. Required and conditional attributes (as the specification states on 29 Sep 2026)

| Attribute | Requirement | Key rule |
|---|---|---|
| `id` | Required | Unique per product, at most 50 characters; use the SKU where possible; keep it stable over time |
| `title` | Required | At most 150 characters; the product's name, matching the landing page |
| `description` | Required | At most 5,000 characters; describes the product accurately |
| `link` | Required | Landing page URL for the product (http or https) |
| `image_link` | Required | Main product image URL (the page cites a minimum size; recheck the pixel rule per category) |
| `availability` | Required | `in_stock`, `out_of_stock`, `preorder` or `backorder` |
| `availability_date` | Required if availability is `preorder` or `backorder` | Date the product becomes available |
| `price` | Required | Must match the landing page; number plus ISO currency code (for example `45000 UGX`); decimal point, not comma; include VAT outside the US and Canada |
| `brand` | Required for all new products except movies, books and musical recordings | The manufacturer's brand; not the store name unless the store makes the product |
| `gtin` | "Strongly recommended if available" | UPC, EAN, JAN, ISBN or ITF-14 as assigned by the manufacturer; no dashes or spaces |
| `mpn` | Required only if the product has no manufacturer-assigned GTIN | Manufacturer part number |
| `identifier_exists` | Submit when the product lacks a brand, GTIN or MPN (for example custom or handmade goods) | Set to `no` rather than inventing identifiers |
| `condition` | Required if the product is used or refurbished | `new`, `refurbished`, `used` |
| `age_group`, `gender`, `color`, `size`, `item_group_id` | Required for apparel (and variants) in named countries: Brazil, France, Germany, Japan, the UK and the US | Good practice elsewhere; East African targets are not in the required list |
| `google_product_category` | Optional, with category-specific rules (for example alcohol, gift cards, subscriptions) | Set it where the automatic category is wrong |

Attribute names and supported values are submitted in English, with underscores in multi-word names. Incorrect, inaccurate or missing product data leads to disapprovals and limits eligibility (register `MERCHANT-CENTER-PRODUCT-DATA`).

## 2. GTIN hygiene

- Use the GTIN printed on the packaging or supplied by the manufacturer; never buy loose barcodes or reuse one across different products or variants.
- Locally made products without manufacturer GTINs (common for Ugandan and Kenyan artisan, food and cosmetics brands) submit `brand`, `mpn` where one exists, or `identifier_exists = no`; do not fabricate numbers.
- Resellers of imported goods: take the GTIN from the manufacturer or distributor record, not from a marketplace listing.
- Keep one GTIN per variant (size, colour) and group variants with `item_group_id`.

## 3. Feed diagnostics routine

1. Build the feed from the client's single product source (shop platform, spreadsheet or catalogue export) so prices and stock match the website, social shop and WhatsApp catalogue.
2. After each upload, read Merchant Center's product and account diagnostics; fix account-level issues (website verification, policies, shipping and returns settings) before item-level issues.
3. Sort item issues by the number of products and revenue affected; price and availability mismatches first, then missing identifiers, then image and title quality.
4. Schedule the feed to refresh at least as often as prices or stock change; flash sales need a same-day update.
5. Record each diagnostic check with its date in the parent skill's research log; a feed change in the live account needs the client's authority and a named operator.

## 4. Can Shopping target East Africa?

- Merchant Center's *Supported languages and currencies* table lists **Uganda (UGX)**, **Kenya (KES)** and **Tanzania (TZS)** as supported target countries and currencies for Shopping ads and free listings. **Rwanda is not in the table**: treat Shopping in Rwanda as unavailable until the table changes (register `MERCHANT-CENTER-COUNTRIES-2026`, partial).
- None of the three East African countries carries the table's marker for the Shopping tab being shown to users there, so reach may come mainly through Search results, Performance Max and other surfaces rather than a Shopping tab. Actual impression volume is `NOT_ASSESSED`; run a small measured test before committing budget.
- Many East African shops lack a checkout on the landing page. Shopping and free listings need a landing page with the product, price and a way to buy; a WhatsApp order button can serve, but confirm it meets the landing-page and checkout policy at the time of build (`NOT_ASSESSED`).
- Where a feed is not feasible, run Search campaigns on product-intent queries and point them at product pages, per [campaign types and East Africa notes](campaign-types-and-east-africa.md).

## 5. Links to commerce media

Retail media, marketplace sponsored listings and their measurement standards sit in [commerce media and marketplaces](../../../strategy/social-commerce-strategy/references/commerce-media-and-marketplaces.md). Performance Max with a feed is still commerce media: ask for incrementality evidence as set out there before scaling.

## Sources

- `MERCHANT-CENTER-PRODUCT-DATA` — Merchant Center Help, Product data specification (read live 29 Sep 2026).
- `MERCHANT-CENTER-COUNTRIES-2026` — Merchant Center Help, Supported languages and currencies (read live 29 Sep 2026; partial).
- `IAB-INCREMENTAL-COMMERCE-MEDIA-2025` — cited through the linked commerce-media reference.

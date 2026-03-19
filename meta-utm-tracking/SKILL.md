---
name: meta-utm-tracking
description: Generates a complete UTM tracking system for a client — naming conventions, a campaign tracking spreadsheet template, and a guide to reading attribution reports in GA4. Invoke when a client needs to track social media traffic accurately, when the meta-roi-framework flags unattributed traffic, or when a client says they cannot tell which platform or post is driving website visits.
---

# meta-utm-tracking

## Purpose

Build a complete, usable UTM tracking system that a consultant sets up once and a client operates ongoing. Many East African SMEs have never heard of UTM parameters — explain the concept plainly, then deliver the system. Without UTM parameters on every social media link, the `meta-roi-framework` cannot accurately attribute traffic and conversions to specific campaigns or platforms.

---

## Required Input

Before generating any output, ask for:

- **Client name** — business name as it should appear in reports
- **Website URL** — the root domain (e.g., `www.akaciakampala.com`)
- **Platforms in scope** — which social platforms the client actively uses
- **Current monthly website visitors** — approximate figure if known; note "unknown" if not
- **GA4 installed?** — yes / no / unsure (if no or unsure, flag that GA4 installation must happen before UTM tracking has any value)
- **Campaign start date** — when the first UTM-tagged campaign launches

---

## Section 1 — What UTM Parameters Are

Generate three plain-English paragraphs:

**Paragraph 1 — What they are.** Explain that UTM parameters are invisible tags added to the end of a URL. They do not change what the visitor sees or where they land — they simply carry information about where that visitor came from. Google Analytics reads these tags the moment the page loads and records the source, medium, and campaign against that visit.

**Paragraph 2 — Why they matter.** Without UTM parameters, GA4 cannot reliably identify social media traffic. Most social platforms — particularly Facebook, Instagram, and WhatsApp — strip referrer data before sending the user to a website. GA4 then logs that visit as "direct" or "referral" with no campaign detail. The client's reporting dashboard shows a large "direct" traffic block that is actually a mix of social posts, WhatsApp shares, and email links — all invisible and unmeasurable.

**Paragraph 3 — What they look like.** Show a single complete example URL for the client's business. If no client context is provided yet, use this default East African example:

```
https://www.akaciakampala.com/sunday-brunch?utm_source=facebook&utm_medium=organic-post&utm_campaign=sunday-brunch-march-2026&utm_content=image-post-1
```

Explain that the `?` separates the page URL from the tracking tags, and each `&` separates one tag from the next. The visitor never sees this — they simply land on the brunch page.

---

## Section 2 — The 5 UTM Parameters

Generate this table, populated with the client's platforms where relevant:

| Parameter | What It Tracks | Required? | Example Value |
|---|---|---|---|
| `utm_source` | Which platform sent the visitor | Yes | `facebook` |
| `utm_medium` | The type of content or channel | Yes | `organic-post` |
| `utm_campaign` | The campaign name | Yes | `sunday-brunch-march-2026` |
| `utm_content` | The specific post or creative | Recommended | `carousel-v2` |
| `utm_term` | Keyword (paid search only) | Rarely needed for social | `kampala-restaurant` |

Note beneath the table: `utm_source`, `utm_medium`, and `utm_campaign` are the three parameters GA4 uses to build its standard acquisition reports. Always include all three. `utm_content` is essential when running multiple creatives in the same campaign — it identifies which specific post drove performance.

---

## Section 3 — Naming Convention Rules

State these rules as a numbered list. Apply them to every UTM parameter value without exception.

1. **Always use lowercase.** GA4 treats `Facebook` and `facebook` as two different sources. Mixed case creates duplicate rows in every report and corrupts historical data.
2. **Use hyphens, never spaces or underscores.** Spaces become `%20` in URLs, which breaks links on some platforms. Underscores are harder to read in GA4 reports. Hyphens are the standard.
3. **Be specific but not verbose.** Write `march-2026-brunch` not `sunday-brunch-promotion-for-the-month-of-march-in-the-year-two-thousand-and-twenty-six`. The campaign name must be recognisable at a glance in a GA4 dropdown list.
4. **Match campaign names to the content calendar.** The `utm_campaign` value must exactly match the campaign name used in the content calendar. This links analytics data directly to planned activity — no guesswork when reviewing performance.
5. **Match `utm_content` to the post ID or brief title from the content calendar.** If the content calendar calls a post "carousel-v2," the UTM tag reads `utm_content=carousel-v2`. Never invent new names at the point of posting.
6. **Set the naming convention once and never deviate.** One team member using `fb` while another uses `facebook` creates permanent data fragmentation. Document the approved values, share the reference table with every person who publishes links, and enforce it.

---

## Section 4 — Naming Convention Reference Table

Produce this reference table for the client. Add or remove rows based on the platforms in scope.

**Approved `utm_source` values**

| Platform | `utm_source` Value |
|---|---|
| Facebook | `facebook` |
| Instagram | `instagram` |
| LinkedIn | `linkedin` |
| TikTok | `tiktok` |
| YouTube | `youtube` |
| X / Twitter | `x-twitter` |
| WhatsApp | `whatsapp` |
| Email newsletter | `email` |
| Google (paid search) | `google` |

**Approved `utm_medium` values**

| Content Type | `utm_medium` Value |
|---|---|
| Standard feed post (organic) | `organic-post` |
| Story (Facebook or Instagram) | `story` |
| Instagram or Facebook Reel | `reel` |
| YouTube Short | `short` |
| WhatsApp broadcast | `broadcast` |
| Email newsletter | `newsletter` |
| Paid social post | `paid-post` |
| Bio link (Instagram or TikTok) | `bio-link` |
| Direct message link | `dm` |

**`utm_campaign` naming pattern**

| Campaign Type | Pattern | Example |
|---|---|---|
| Product launch | `product-launch-[month]-[year]` | `product-launch-march-2026` |
| Seasonal promotion | `seasonal-[season]-[year]` | `seasonal-easter-2026` |
| Brand awareness | `brand-awareness-q[n]-[year]` | `brand-awareness-q1-2026` |
| Event promotion | `event-[event-name]-[year]` | `event-kampala-marathon-2026` |
| Regular content series | `series-[name]-[year]` | `series-recipe-videos-2026` |

---

## Section 5 — UTM Link Builder

Instruct the client to use Google's free Campaign URL Builder at `ga-dev-tools.google.com/campaign-url-builder`. No login or paid subscription is required.

**Step-by-step instructions:**

1. **Enter the destination URL.** Paste the exact page URL the link should land on — the product page, menu page, or homepage. Do not use a shortened URL here; use the full destination address.
2. **Fill in `utm_source`.** Select the correct value from the approved reference table in Section 4.
3. **Fill in `utm_medium`.** Select the correct value from the approved reference table in Section 4.
4. **Fill in `utm_campaign`.** Type the campaign name exactly as it appears in the content calendar — lowercase, hyphens only.
5. **Fill in `utm_content`.** Type the post ID or brief title exactly as it appears in the content calendar. Do not skip this field.
6. **Copy the generated URL.** The builder displays the complete tagged URL. Copy it in full.
7. **Shorten the URL.** Paste the full UTM URL into `bit.ly` (free tier available) or `rb.gy`. Copy the shortened link. Use this shortened link in all captions, broadcast messages, and bio slots.

**Shortening guidance:**
- WhatsApp broadcasts and Instagram bio links: always shorten — long UTM strings look unprofessional and may discourage clicks.
- LinkedIn posts and email newsletters: shortening is optional because the full URL is not visible to the reader.
- Never change or rebuild the shortened link after posting — the UTM data must remain consistent for the duration of the campaign.

---

## Section 6 — Campaign Tracking Spreadsheet Template

Build this template in Google Sheets or Microsoft Excel. Create one sheet per month. The template captures every UTM link created, so the team can find and reuse links and the consultant can audit naming consistency.

**Columns:**

| Date Created | Campaign Name | Platform | Content Type | Destination URL | Short UTM URL | Notes |
|---|---|---|---|---|---|---|

**Three example rows for a Kampala business:**

| Date Created | Campaign Name | Platform | Content Type | Destination URL | Short UTM URL | Notes |
|---|---|---|---|---|---|---|
| 2026-03-10 | sunday-brunch-march-2026 | WhatsApp | broadcast | `https://www.akaciakampala.com/sunday-brunch` | `https://bit.ly/akacia-brunch-wa` | Sent to 340-person broadcast list; resend Thursday if bookings below target |
| 2026-03-12 | sunday-brunch-march-2026 | Instagram | reel | `https://www.akaciakampala.com/sunday-brunch` | `https://bit.ly/akacia-brunch-ig` | Reel hook variant A; compare to hook-b performance after 48 hours |
| 2026-03-14 | sunday-brunch-march-2026 | Facebook | organic-post | `https://www.akaciakampala.com/sunday-brunch` | `https://bit.ly/akacia-brunch-fb` | Image carousel; posted in Kampala Foodies group and on page |

Notes on the template:
- Use a unique shortened URL for each platform, even if the destination and campaign are identical. This preserves per-platform attribution in GA4.
- The `Notes` column is for operational observations — send times, audience segments, A/B variants, or flags for follow-up. Keep it brief.
- Archive each month's sheet rather than deleting it. Historical UTM logs are essential for year-on-year campaign comparisons.

---

## Section 7 — Reading Attribution in GA4

Instruct the client on how to find UTM data in Google Analytics 4. Note: these instructions reflect the GA4 interface, not Universal Analytics. If the client's account still shows "Universal Analytics," flag that they must migrate before proceeding.

**Finding source and medium data:**

1. Log in to Google Analytics at `analytics.google.com`.
2. Select the correct property from the account selector.
3. In the left-hand navigation, go to **Reports → Acquisition → Traffic Acquisition**.
4. The default dimension is **Session source / medium** — this shows which UTM sources drove sessions to the website. Look for entries such as `facebook / organic-post` and `whatsapp / broadcast`.

**Finding campaign data:**

1. In the same **Traffic Acquisition** report, click the primary dimension dropdown (currently showing "Session source / medium").
2. Change it to **Session campaign**.
3. Each row now shows a campaign name from `utm_campaign`. Rows labelled `(not set)` are visits that arrived without UTM tags.

**Key metrics to read:**

| Metric | What It Means |
|---|---|
| Sessions | Total visits from that source or campaign |
| Engaged sessions | Sessions lasting more than 10 seconds, with a conversion event, or with 2+ page views — a better quality signal than raw sessions |
| Engagement rate | Engaged sessions ÷ total sessions — use this to compare platform quality, not just volume |
| Conversions | Goal completions (form fills, bookings, purchases) — requires conversion events to be configured in GA4 |
| Revenue | Total e-commerce revenue attributed (only if e-commerce tracking is set up) |

**Monthly reporting routine:**

1. Open the Traffic Acquisition report on the first working day of each month.
2. Set the date range to the previous calendar month.
3. Screenshot the top five sources/mediums by engaged sessions (not raw sessions).
4. Note which social platform delivered the highest engagement rate — this is the platform producing the most qualified traffic, regardless of volume.
5. Cross-reference findings against the campaign tracking spreadsheet to identify which specific posts drove the strongest results.
6. Carry these findings into the monthly social media performance report and use them to inform the following month's content priorities.

---

## Section 8 — WhatsApp and Dark Social

Include this note in every UTM system delivered to an East African client. It is specific to the EA market context.

**What dark social is.** When someone copies a link from a website and shares it in a WhatsApp chat, the person who clicks that link arrives at the website with no referrer information. GA4 logs the visit as "direct" traffic. In Uganda and across East Africa, WhatsApp is the primary channel through which content spreads informally — links are copied from posts, forwarded between groups, and shared in family and business chats. A significant portion of what appears as "direct" traffic in GA4 is actually WhatsApp-driven dark social.

**Why it matters.** A client who sees 40% direct traffic may assume those visitors typed the URL manually or came from a bookmark. In reality, many of those visits came from social sharing that UTM tags never captured. This inflates the apparent value of direct traffic and understates the true contribution of social media.

**What to do about it:**

1. Always place UTM-tagged, shortened links in every WhatsApp broadcast. Tag the broadcast separately with `utm_medium=broadcast` so it is distinguishable from other WhatsApp traffic.
2. When creating posts on Facebook and Instagram that will be shared widely, include the UTM-tagged link in the caption or as a story link — not the bare URL.
3. Ask the client to use the UTM-tagged link (the shortened bit.ly version) when they personally share content in WhatsApp groups. Brief every team member who shares links informally.
4. Accept that dark social cannot be fully eliminated. The goal is to reduce unattributed traffic progressively — from a typical 40–60% "direct" share toward 20% or below — by making UTM-tagged links the default in all outbound communications.

Note the baseline "direct" percentage at campaign start. Report the reduction in unattributed traffic as a metric in the monthly report — it demonstrates the value of the UTM system itself.

---

## Quality Criteria

- Naming convention rules are specific enough that a non-technical client can follow them without errors — no ambiguity about which separator to use, which case to apply, or how to name a campaign
- All UTM parameter examples use real East African business contexts — no generic `mywebsite.com` or placeholder URLs in any deliverable
- The spreadsheet template is complete enough to copy directly into Google Sheets without redesign — columns are labelled, example rows are filled, and operational guidance is included
- GA4 navigation instructions match the actual GA4 interface — no references to Universal Analytics views, goals, or bounce rate (replaced by engagement rate in GA4)
- The WhatsApp and dark social note is specific to the EA market — it references the role of WhatsApp in Uganda, the informal sharing behaviour, and a realistic target for reducing unattributed traffic
- All tools referenced are free and require no paid subscription — Google Campaign URL Builder, bit.ly free tier, GA4 free tier
- The skill produces a complete, usable UTM system — naming convention, link builder workflow, tracking spreadsheet, and GA4 reading guide — not a conceptual overview
- British English throughout — "analyse," "recognise," "organise," "colour," "behaviour" — no American spellings

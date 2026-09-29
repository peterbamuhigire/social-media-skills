# UTM Convention and Campaign Register

Merged from skills/meta-analytics-ops/meta-utm-tracking on 2026-09-29 at 8eacccb; preservation map: [meta-utm-tracking.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/meta-utm-tracking.md)

## When to use this reference

Use it to build a UTM tracking system that a consultant sets up once and the client runs from then on: the naming convention, the approved values table, the link-builder routine, the campaign register, the GA4 reading routine and the WhatsApp dark-social note. Many East African SMEs have never heard of UTM parameters, so explain the idea plainly and then deliver the system. Without UTM tags on every social link, ROI work in [meta-roi-framework](../../meta-roi-framework/SKILL.md) cannot attribute traffic and conversions to campaigns or platforms.

Output: **UTM convention, campaign register and QA checklist**. Every recommendation traces to an input and names an owner or next action; assumptions and unassessed checks are marked.

## Inputs

| Input | Note |
|---|---|
| Client name | As it should appear in reports |
| Website URL | Root domain (for example `www.akaciakampala.com`) |
| Platforms in scope | The social platforms the client actively uses |
| Current monthly website visitors | Approximate; write "unknown" if not known |
| GA4 installed? | yes / no / unsure. If no or unsure, flag that GA4 must be installed first, or UTM tags have no value |
| Campaign start date | When the first tagged campaign launches |
| Channel taxonomy, campaign names, destination URLs, analytics access | Client, approved systems or dated exports; if absent, stop the affected decision or mark the field unknown |

## Section 1: what UTM parameters are (three plain-English paragraphs for the client)

1. **What they are.** UTM parameters are tags added to the end of a URL. They do not change what the visitor sees or where they land; they carry information about where the visitor came from. GA4 reads them when the page loads and records source, medium and campaign against the visit.
2. **Why they matter.** Without them GA4 cannot reliably identify social traffic. Most social platforms, particularly Facebook, Instagram and WhatsApp, strip referrer data before sending the user to a website, so GA4 logs the visit as "direct" or "referral" with no campaign detail. The client's dashboard then shows a large "direct" block that is really a mix of social posts, WhatsApp shares and email links, all unmeasured.
3. **What they look like.** Show one complete example URL for the client's business. Default East African example when no client context exists yet:

```
https://www.akaciakampala.com/sunday-brunch?utm_source=facebook&utm_medium=organic-post&utm_campaign=sunday-brunch-march-2026&utm_content=image-post-1
```

The `?` separates the page URL from the tags and each `&` separates one tag from the next. The visitor simply lands on the brunch page.

## Section 2: the parameters

| Parameter | What it tracks | Required? | Example value |
|---|---|---|---|
| `utm_source` | Which platform sent the visitor | Yes | `facebook` |
| `utm_medium` | The type of content or channel | Yes | `organic-post` |
| `utm_campaign` | The campaign name | Yes | `sunday-brunch-march-2026` |
| `utm_content` | The specific post or creative | Recommended | `carousel-v2` |
| `utm_term` | Keyword (paid search only) | Rarely needed for social | `kampala-restaurant` |
| `utm_id` | Campaign ID (matches the campaign register row) | Recommended by Google | `c2026-014` |
| `utm_source_platform` | The buying or organic platform that directed the traffic | Recommended by Google | `meta-ads` |

`utm_source`, `utm_medium` and `utm_campaign` build GA4's standard acquisition reports; always include all three. `utm_content` is essential when several creatives run in one campaign, because it identifies the post that performed. The original skill listed five parameters; GA4 now supports nine, including `utm_creative_format` and `utm_marketing_tactic`, which GA4 does not yet report, and Google strongly recommends adding `utm_id` and `utm_source_platform` (register GA4-UTM-PARAMETERS-2026, read 2026-09-29). Missing parameters show as `(not set)`.

## Section 3: naming convention rules (apply to every value, no exceptions)

1. **Always lowercase.** GA4 treats `Facebook` and `facebook` as two sources; mixed case creates duplicate rows and corrupts history.
2. **Hyphens, never spaces or underscores.** Spaces become `%20` and break links on some platforms; underscores are harder to read in reports.
3. **Specific but short.** `march-2026-brunch`, not a sentence. The name must be recognisable at a glance in a GA4 drop-down.
4. **Campaign names match the content calendar exactly.** This ties analytics to planned activity with no guesswork.
5. **`utm_content` matches the post ID or brief title in the content calendar.** If the calendar says "carousel-v2", the tag is `utm_content=carousel-v2`. Never invent names at the moment of posting.
6. **Set the convention once and never deviate.** One person using `fb` and another `facebook` fragments the data permanently. Document the approved values, share the table with everyone who publishes links, and enforce it.

## Section 4: approved values (add or remove rows for the platforms in scope)

**`utm_source`**

| Platform | Value |
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

**`utm_medium`**

| Content type | Value |
|---|---|
| Standard feed post (organic) | `organic-post` |
| Story (Facebook or Instagram) | `story` |
| Instagram or Facebook Reel | `reel` |
| YouTube Short | `short` |
| WhatsApp broadcast | `broadcast` |
| Email newsletter | `newsletter` |
| Paid social post | `paid-post` |
| Bio link (Instagram or TikTok) | `bio-link` |
| Direct-message link | `dm` |

Check the medium values against GA4's default channel grouping before launch: custom mediums such as `organic-post` or `broadcast` may fall into "Unassigned" unless a custom channel group maps them (verify at use; no register record). Record the mapping in the tracking plan.

**`utm_campaign` patterns**

| Campaign type | Pattern | Example |
|---|---|---|
| Product launch | `product-launch-[month]-[year]` | `product-launch-march-2026` |
| Seasonal promotion | `seasonal-[season]-[year]` | `seasonal-easter-2026` |
| Brand awareness | `brand-awareness-q[n]-[year]` | `brand-awareness-q1-2026` |
| Event promotion | `event-[event-name]-[year]` | `event-kampala-marathon-2026` |
| Regular content series | `series-[name]-[year]` | `series-recipe-videos-2026` |

## Section 5: link-builder routine

Use Google's free Campaign URL Builder at `ga-dev-tools.google.com/campaign-url-builder` (no login or subscription).

1. Enter the exact destination URL (product page, menu page or home page), never a shortened URL.
2. Fill `utm_source` from the approved table.
3. Fill `utm_medium` from the approved table.
4. Fill `utm_campaign` exactly as in the content calendar: lowercase, hyphens only.
5. Fill `utm_content` with the post ID or brief title from the calendar; do not skip it.
6. Copy the full generated URL.
7. Shorten it (for example bit.ly free tier or rb.gy) and use the short link in captions, broadcasts and bio slots.

Shortening rules:

- WhatsApp broadcasts and Instagram bio links: always shorten; long UTM strings look unprofessional and may deter clicks.
- LinkedIn posts and email newsletters: optional, because the reader does not see the full URL.
- Never change or rebuild a short link after posting; the UTM data must stay consistent for the whole campaign.

## Section 6: campaign register (spreadsheet template)

Build it in Google Sheets or Excel, one sheet per month. It records every UTM link, so the team can find and reuse links and the consultant can audit naming.

| Date created | Campaign name | Platform | Content type | Destination URL | Short UTM URL | Notes |
|---|---|---|---|---|---|---|
| 2026-03-10 | sunday-brunch-march-2026 | WhatsApp | broadcast | `https://www.akaciakampala.com/sunday-brunch` | `https://bit.ly/akacia-brunch-wa` | Sent to 340-person broadcast list; resend Thursday if bookings below target |
| 2026-03-12 | sunday-brunch-march-2026 | Instagram | reel | `https://www.akaciakampala.com/sunday-brunch` | `https://bit.ly/akacia-brunch-ig` | Reel hook variant A; compare with hook B after 48 hours |
| 2026-03-14 | sunday-brunch-march-2026 | Facebook | organic-post | `https://www.akaciakampala.com/sunday-brunch` | `https://bit.ly/akacia-brunch-fb` | Image carousel; posted in Kampala Foodies group and on the page |

Rules:

- Use a unique short URL per platform even when destination and campaign are identical; this keeps per-platform attribution in GA4.
- Keep the Notes column brief and operational: send times, segments, A/B variants, follow-up flags.
- Archive each month's sheet; never delete it. Historical logs are needed for year-on-year comparisons.
- Add a `utm_id` column when the campaign ID parameter is used.

## Section 7: reading attribution in GA4

These steps describe GA4. Universal Analytics has been shut down, so if a client still refers to "UA" views, treat the old data as archive only and work in GA4 (menu paths: verify at use; no register record).

**Source and medium:**

1. Log in at `analytics.google.com` and select the property.
2. Go to **Reports → Acquisition → Traffic acquisition**.
3. The default dimension is **Session source / medium**; look for rows such as `facebook / organic-post` and `whatsapp / broadcast`.

**Campaigns:**

1. In the same report, change the primary dimension to **Session campaign**.
2. Each row shows a `utm_campaign` value; `(not set)` rows arrived without UTM tags.

**Metrics:**

| Metric | Meaning |
|---|---|
| Sessions | Visits from that source or campaign |
| Engaged sessions | Sessions lasting more than 10 seconds, with a key event, or with 2+ page or screen views (register GA4-ENGAGED-SESSION-2026); a better quality signal than raw sessions |
| Engagement rate | Engaged sessions ÷ sessions; compare platform quality, not only volume |
| Key events (formerly "conversions" in GA4) | Completions such as form fills, bookings, purchases; the events must be marked as key events |
| Revenue | E-commerce revenue attributed, only if e-commerce tracking is set up |

**Monthly routine:**

1. Open Traffic acquisition on the first working day of the month.
2. Set the range to the previous calendar month.
3. Capture the top five source/medium rows by engaged sessions, not raw sessions.
4. Note the platform with the highest engagement rate: it sends the most qualified traffic, whatever the volume.
5. Cross-check against the campaign register to find the posts that drove the best results.
6. Carry the findings into the monthly report ([meta-reporting](../../meta-reporting/SKILL.md)) and next month's content priorities.

## Section 8: WhatsApp and dark social (include in every EA delivery)

**What dark social is.** When someone copies a link and shares it in a WhatsApp chat, the person who clicks arrives with no referrer, and GA4 logs "direct". In Uganda and across East Africa, WhatsApp is the main route by which content spreads informally: links are copied from posts and forwarded between family and business groups (register WHATSAPP-USAGE-EA-2026). A large part of "direct" traffic is WhatsApp-driven dark social.

**Why it matters.** A client seeing 40 % direct traffic may assume people typed the URL or used a bookmark; in reality much of it came from social sharing that no tag captured. Direct traffic looks more valuable than it is and social looks less valuable.

**What to do:**

1. Put a UTM-tagged short link in every WhatsApp broadcast, with `utm_medium=broadcast` so it is distinct from other WhatsApp traffic.
2. On Facebook and Instagram posts likely to be shared widely, use the tagged link in the caption or story link, never the bare URL.
3. Ask the client and every team member who shares links informally to use the tagged short link.
4. Accept that dark social cannot be removed entirely. Aim to reduce the "direct" share progressively, from a typical 40–60 % towards 20 % or below, by making tagged links the default (the original skill's planning range; verify against the client's own baseline, no register record).

Record the "direct" percentage at campaign start and report its fall monthly; it shows the value of the UTM system itself.

## Decision rules

| Condition | Action | Risk avoided |
|---|---|---|
| GA4 is not installed or its status is unknown | Install and verify GA4 first; UTM work waits | Tags nobody can read |
| Several creatives share one campaign | Require `utm_content` from the calendar ID | Unable to tell which post performed |
| A link goes into WhatsApp or a bio | Tag and shorten it; log it in the register | Dark-social loss |
| Channel taxonomy, names, URLs and access are current and attributable | Produce the full convention, register and QA checklist | Stale or unrelated evidence |
| A material input is missing or contradictory | Stop that decision or issue a labelled partial | Invented precision |

## QA checklist

- [ ] Rules are clear enough for a non-technical client: separator, case and naming pattern leave no ambiguity.
- [ ] Every example uses a real East African business context; no `mywebsite.com` placeholders.
- [ ] The register template can be pasted straight into Google Sheets: labelled columns, filled example rows, operating notes.
- [ ] GA4 instructions describe GA4 only: no Universal Analytics views, goals or bounce rate as the headline metric.
- [ ] The WhatsApp dark-social note refers to WhatsApp's role in Uganda, informal sharing and a realistic reduction target.
- [ ] All tools named are free: Campaign URL Builder, bit.ly free tier, GA4 standard.
- [ ] The system is complete: convention, builder routine, register and GA4 reading guide, not a concept note.
- [ ] Medium values are mapped to a channel group (default or custom) and the mapping is recorded.
- [ ] British English throughout (analyse, recognise, organise, colour, behaviour).

## Anti-patterns (carried from the source)

- Using an undated benchmark as the client's result. Fix: use account evidence or label it a provisional comparator.
- Producing the convention without a channel taxonomy. Fix: stop the affected decision or issue a bounded partial.
- Treating missing access as a passed check. Fix: record `not assessed`, its risk and the recovery input.
- Publishing or editing live accounts while planning. Fix: obtain separate explicit authority and keep action evidence.

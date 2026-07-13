---
name: hashtag-strategy
description: Use when Hashtag Strategy is needed to produce a decision-ready strategy for social-media or digital-marketing work; use `caption-writer` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Hashtag Strategy

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **decision-ready strategy** and the supplied brief falls within hashtag strategy.

## Do Not Use When
- Use `caption-writer` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Content brief, channel, audience, message, format and call to action | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Issue a qualified finding and identify the evidence needed. |

## Capability and Permission Boundaries
Default to read-only: inspect supplied material and report findings. Editing, publishing, contacting people, spending, or changing live systems requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified decision-ready strategy; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Channel, format and audience commitment level are known | Choose the hook, structure and call to action native to that context. | Copy that could be pasted unchanged onto any channel or brand. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact decision-ready strategy, consumer, market, channel and approval boundary; route to `caption-writer` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete decision-ready strategy; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Decision-ready strategy | Requester, client reviewer or delivery team | The decision-ready strategy addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
| Decision and gap note | Approver or next workflow | Names the chosen route, evidence used, unresolved inputs and any action requiring authority. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Finding-to-source register and unassessed-check list | Inline table, checklist or linked source note | Every material claim, decision and unavailable check is traceable. |

## Quality Standards
- Preserve the domain guidance and East African market context below; replace it only when the requester names another market.
- Use British English unless the target language or market requires otherwise, and verify names, figures, quotations and platform rules before use.
- Make the key choice visible, cover failure and edge cases, and keep the result ready for its named consumer.
- Run the repository's `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested decision-ready strategy, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [caption-writer](../caption-writer/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

## How to Use This Skill
Collect the Required Input below. Generate a complete hashtag strategy document in one output. Include all seven sections. Use the client's industry, location, and audience to select and justify every hashtag — do not generate generic lists. For Uganda/East Africa clients, prioritise the EA-specific tags listed in each section where relevant.

## Required Input
Ask for the following before generating the strategy:

- **Client name** — trading name of the business
- **Industry** — sector (e.g. fashion retail, professional services, food and beverage, health, NGO)
- **Country / city** — default Uganda/East Africa; specify city (e.g. Kampala, Nairobi, Dar es Salaam)
- **Primary goal** — what the client wants to achieve through social media (awareness / community / sales / partnerships)
- **Primary platform** — the platform where hashtag strategy matters most (Instagram and TikTok typically; less critical on Facebook and LinkedIn)
- **Target audience description** — who the client is trying to reach (demographics, interests, location)
- **Brand name** — exact spelling, as it will appear in the branded hashtag
- **Any existing branded hashtags** — hashtags the client has already used or promoted to their audience
- **Active platforms** — all platforms the client posts on (determines the usage guide)

## Output: Complete Hashtag Strategy Document
Generate the cover section and all seven sections in full. For each hashtag: explain when to use it, which platform it performs best on, and what type of content it suits. Justify selections — do not list without explanation.

### Cover
**[Client Name] — Hashtag Strategy**
Prepared for: [Client Name]
Industry: [Industry]
Primary market: [City / Country]
Date: [Date]

### Section 1: Branded Hashtags
Branded hashtags are unique to [Client Name]. They build a searchable content library, encourage user-generated content (UGC), and make it easy for customers to find and contribute to the brand community. Use at least the primary branded hashtag on every post across all platforms.

**1. Primary branded hashtag**
`#[BrandName]`
Use on: every post, every platform
Purpose: creates a complete, searchable archive of all brand content. Promotes it in the bio on every platform.
Promotion: include in the profile bio, print it on receipts, packaging, or physical signage, and invite customers to use it when they share photos.

**2. Campaign hashtag format**
`#[BrandName][CampaignName]` — create fresh per campaign (e.g. `#[BrandName]Launch2025`, `#[BrandName]Ramadan`)
Use on: all posts related to that specific campaign; prompt customers to use it to enter competitions or share experiences
Purpose: keeps campaign content separate and trackable; builds a UGC gallery for each campaign
Note: retire campaign hashtags once the campaign ends — do not continue using them as evergreen tags

**3. Community hashtag**
`#[BrandCommunityName]` — a hashtag for customers, fans, and advocates to use (e.g. `#KawaHeroes` for a coffee brand, `#NakibuukaFamily` for a restaurant)
Use on: community posts, UGC reposts, customer appreciation content
Purpose: builds identity and belonging around the brand; encourages organic tagging by loyal customers
Promotion: feature it on product packaging, in Stories, and when resharing customer content

**4. Product or service hashtag**
`#[BrandName][ProductOrService]` — a tag for a specific product line or service (e.g. `#[BrandName]ColdPress`, `#[BrandName]Tailoring`)
Use on: product-specific posts only — not on general brand content
Purpose: allows customers interested in a specific product to find relevant posts without sorting through unrelated content

**5. Value or mission hashtag**
A hashtag that reflects what the brand stands for — not what it sells.
Examples: `#MadeWithCare` / `#BuildingUganda` / `#HomegrownQuality` / `#SupportLocal[City]`
Use on: behind-the-scenes, values-led, and community posts
Purpose: attracts an audience that shares the brand's values — these tend to be the most loyal customers

Generate all 5 branded hashtags for [Client Name] based on the brand name and industry provided in the Required Input. If the client already uses existing branded hashtags, incorporate those and note which category they fall into.

### Section 2: Niche Hashtags (10)
Niche hashtags have between 1,000 and 100,000 posts. They are highly relevant to a specific topic, product, or location, and face lower competition than broad tags — meaning the content stays visible for longer and reaches a genuinely interested audience.

Generate 10 niche hashtags based on the client's industry and location. For each, provide:

| Hashtag | Platform | Estimated reach | Best content type |
|---|---|---|---|
| [hashtag] | [platform] | [1K–100K] | [image / video / carousel] |

**EA-specific niche hashtags to consider (select those relevant to the client's industry):**

| Tag | Industry fit |
|---|---|
| #KampalaFashion | Fashion, retail, beauty |
| #UgandaFood | Food and beverage, agriculture |
| #NairobiBusiness | B2B, professional services (Kenya) |
| #KampalaEats | Restaurants, food delivery, catering |
| #UgandaTech | Technology, software, fintech |
| #EastAfricaHealth | Health, wellness, medical |
| #MadeInKenya | Products, retail (Kenya) |
| #DarEsSalaamBusiness | B2B, professional services (Tanzania) |
| #UgandaNGO | NGOs, social enterprises, development sector |
| #KampalaEvents | Events, entertainment, hospitality |
| #UgandaWeddings | Events, floristry, catering, fashion |
| #UgandaFarming | Agriculture, agri-tech, rural business |

For the final strategy, select the most relevant 10, supplement with industry-specific global niche tags (e.g. `#NaturalHairUganda` for a beauty brand), and present as the table above.

### Section 3: Community Hashtags (10)
Community hashtags connect the brand to broader audience groups — people who identify with a community, movement, or shared interest beyond the immediate product category. They have between 100,000 and 500,000 posts and drive discovery by new audiences.

Generate 10 community hashtags relevant to the client's audience. Present in the same table format as Section 2.

**EA-specific community hashtags to include where relevant:**

| Tag | Community |
|---|---|
| #EastAfricaBusiness | EA business community broadly |
| #AfricanEntrepreneur | Entrepreneurs across Africa |
| #MadeInAfrica | African-made products and brands |
| #AfricanWomenInBusiness | Women entrepreneurs, female-led brands |
| #AfricaRising | Pan-African growth and development narrative |
| #BlackOwnedBusiness | Black-owned enterprises (resonates with diaspora audiences) |
| #SocialEnterprise | NGOs, social businesses, impact organisations |
| #StartupAfrica | Tech, innovation, and startup ecosystem |
| #SMEAfrica | Small and medium businesses |
| #AfricanCreatives | Creative industry professionals |

Select those relevant to [Client Name]'s audience and supplement with global community tags specific to the industry (e.g. `#WomenInTech`, `#SustainableFashion`, `#PlantBased` as relevant).

### Section 4: Awareness / Trending Hashtags (5)
These are broad tags with 500,000+ posts. They maximise reach but offer low targeting precision — the content competes with an enormous volume of posts. Use sparingly: 1–2 per post maximum, combined with niche tags.

**Select 5 from the categories below, relevant to the client:**

*Industry-wide tags (choose 1–2):*
`#Marketing` / `#SocialMedia` / `#SmallBusiness` / `#Entrepreneurship` / `#Business` / `#Branding` / `#ContentCreator` / `#DigitalMarketing`

*Location tags (include at least 1):*
`#Uganda` / `#Kampala` / `#EastAfrica` / `#Africa` / `#Kenya` / `#Nairobi` / `#Tanzania`

*Global observance tags (include relevant ones when applicable):*
Use global days that align with content: `#InternationalWomensDay` / `#WorldEnvironmentDay` / `#SmallBusinessSaturday` — only when the post directly relates to the occasion. Do not tag global days on unrelated content.

Present the final 5 selected tags with a note on when to use each.

### Section 5: Platform-Specific Usage Guide
Apply this guide every time a post is scheduled. Mixing hashtag sets incorrectly across platforms reduces performance.

| Platform | Recommended count | Placement | Sets to combine |
|---|---|---|---|
| Instagram | 5–10 | End of caption or first comment | 1 branded + 2–3 niche + 2–3 community + 1 awareness |
| Facebook | 1–3 | In the caption | 1 branded + 1 niche only — Facebook hashtags add limited value |
| LinkedIn | 3–5 | End of post | 1 branded + 2–3 niche or community; industry-relevant only |
| TikTok | 3–5 | In caption — naturally or at end | 1 niche + 1 trending/broad + 1 branded |
| X / Twitter | 1–2 | Woven naturally into the tweet text | Branded or 1 trending; never stacked at the end |
| WhatsApp | None | Not applicable | Hashtags do not function on WhatsApp |

**How to Build a Post-Specific Hashtag Set**

For each post, start with the standard set below and swap out 2–3 tags for ones specific to the topic:

*Instagram standard set for [Client Name]:*
`#[PrimaryBranded]` `#[NicheTag1]` `#[NicheTag2]` `#[CommunityTag1]` `#[CommunityTag2]` `#[LocationTag]` `#[AwarenessTag]`

Generate this standard set in the output, using the hashtags selected in Sections 1–4.

### Section 6: Hashtags to Avoid
**Engagement bait tags**
`#follow4follow` `#likeforlike` `#f4f` `#l4l` `#followback` — these attract bot accounts and inactive profiles, not genuine customers. They inflate follower counts with no commercial value.

**Overused generic tags (invisible in the feed)**
`#love` `#instagood` `#photooftheday` `#beautiful` `#happy` — with hundreds of millions of posts, new content disappears within seconds. No audience uses these tags to find content they want.

**Potentially restricted or shadow-banned tags**
Instagram periodically restricts tags associated with spam or inappropriate content. To check whether a tag is restricted: search the tag on Instagram. If the **Top Posts** section does not appear — only **Recent** — the tag may be restricted. Remove it from the strategy immediately.

Tags to check before using (Instagram commonly restricts variants of): `#desk` `#beautyblogger` `#easter` — restrictions change frequently. Check any unfamiliar tag before use.

**Competitor brand names**
Do not use competitor brand names as hashtags. It is ineffective for discovery and looks unprofessional. Use for monitoring only (search the tag to see competitor content — do not post with it).

**Misleading or irrelevant tags**
Never tag content with a hashtag that does not relate to the post. Instagram's algorithm penalises irrelevant hashtagging. It also damages trust if audiences click a tag and find unrelated content.

### Section 7: Hashtag Performance Tracking
Review hashtag performance monthly. Retire underperformers. Test replacements.

**How to Check if Hashtags Are Working (Instagram)**

1. Open a post → tap **View Insights**
2. Scroll to **Impressions** → look for the **From Hashtags** figure
3. A high "from hashtags" figure means hashtags are driving new audience discovery — these are working
4. A zero or near-zero "from hashtags" figure means the hashtags are not generating discovery

**Monthly Tracking Process**

At the end of each month, review the 10 most recent posts:
- Note which posts had the highest "from hashtags" impressions
- Identify any hashtags that consistently appear in high-performing posts
- Remove any hashtag from the standard set that has not contributed to discovery in 4+ consecutive posts
- Research 2–3 replacement niche tags using Instagram's search suggestion feature (search a hashtag → tap **Related** to see what Instagram recommends)

**Quarterly Refresh**

Every 3 months: run a full review of the entire hashtag strategy. Check all niche tags for restriction, refresh community tags to reflect any shifts in the audience or content mix, and update the standard set for each platform.

**Reporting**

Include a "Hashtag Performance" row in the monthly social media report (from meta-reporting). Note the average impressions from hashtags per post and flag any tags that generated significantly above or below average discovery.

## Human Authenticity Gate
All hashtag strategy documents produced using this skill must be reviewed by a human consultant familiar with the client's audience before delivery. AI-generated hashtag selections must meet the Golden Rule: every set must be as precisely targeted and culturally informed as if selected by a skilled human digital strategist with deep knowledge of East African social media. Generic, untargeted, or culturally misaligned hashtag sets are not acceptable regardless of how efficiently they were produced.

## Quality Criteria
- [ ] All 5 branded hashtags are generated specifically for this client — not generic placeholders
- [ ] 10 niche hashtags are relevant to the client's actual industry and city — not a generic list
- [ ] 10 community hashtags reflect the client's target audience, not just broad EA tags
- [ ] Platform usage table is populated with the correct hashtag counts and combinations for each active platform
- [ ] Hashtags to avoid section is specific — not a generic warning
- [ ] Standard post hashtag set is generated and ready to copy for each primary platform
- [ ] British English throughout
- [ ] Every hashtag set respects platform-specific count limits — no overloading

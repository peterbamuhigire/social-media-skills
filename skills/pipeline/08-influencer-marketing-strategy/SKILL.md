---
name: 08-influencer-marketing-strategy
description: Generates a complete influencer marketing strategy for clients who want to use creators and influencers to extend their reach, build trust, or drive sales. Applies Uganda/East Africa ecosystem context throughout — including tier definitions, engagement benchmarks, outreach norms, and barter-versus-fee guidance. Invoke when a client has identified influencer marketing as a growth channel, or when 06-digital-marketing-strategy has flagged influencer as a priority channel requiring a dedicated sub-strategy.
---
# Influencer Marketing Strategy Generator

Produce a complete influencer marketing strategy document. Apply Uganda/East Africa ecosystem context throughout — tier definitions, engagement benchmarks, and outreach norms must reflect local market realities, not global averages. Apply British English throughout. Default to Uganda/East Africa context unless the client specifies otherwise.

This skill covers strategy and execution guidance only. It does not produce legal contracts. Refer the client to a lawyer for formal influencer agreements.

---

<!-- dual-compat:start -->
## Use when
- Generates a complete influencer marketing strategy for clients who want to use creators and influencers to extend their reach, build trust, or drive sales. Applies Uganda/East Africa ecosystem context throughout — including tier definitions, engagement benchmarks, outreach norms, and barter-versus-fee guidance. Invoke when a client has identified influencer marketing as a growth channel, or when 06-digital-marketing-strategy has flagged influencer as a priority channel requiring a dedicated sub-strategy.
- Use this skill when it is the closest match to the requested deliverable or workflow.

## Do not use when
- Do not use this skill for graphic design, video production, software development, or legal advice beyond the repository's stated scope.
- Do not use it when another skill in this repository is clearly more specific to the requested deliverable.

## Workflow
1. Collect the required inputs or source material before drafting, unless this skill explicitly generates the intake itself.
2. Follow the section order and decision rules in this `SKILL.md`; do not skip mandatory steps or required fields.
3. Review the draft against the quality criteria, then deliver the final output in markdown unless the skill specifies another format.

## Anti-Patterns
- Do not invent client facts, performance data, budgets, or approvals that were not provided or clearly inferred from evidence.
- Do not skip required inputs, mandatory sections, or quality checks just to make the output shorter.
- Do not drift into out-of-scope work such as code implementation, design production, or unsupported legal conclusions.

## Outputs
- A structured onboarding, strategy, or planning document in markdown, ready to hand off to the next skill in the workflow.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Ask for all of the following before generating the strategy document:

- **Client name** — trading name
- **Industry and sub-sector** — e.g. "FMCG — personal care", "hospitality — restaurant chain"
- **Country/city** — defaults to Kampala, Uganda if not specified
- **Target audience** — reference personas from 03-audience-personas if available; otherwise describe: age range, gender split, location, key interests
- **Campaign objective** — brand awareness / product trial / event promotion / sales / community growth / all: state primary objective
- **Budget for influencer marketing** — monthly or per-campaign; specify currency (default UGX); distinguish between barter value and cash fees
- **Platforms in scope** — select from: Instagram, TikTok, YouTube, Facebook, X/Twitter, WhatsApp

---

## Document Structure

Generate all seven sections in order. Use markdown headings. Do not omit any section.

### 1. Influencer Tier Definitions

Apply EA-specific context for all tier definitions. Global benchmarks do not apply directly — EA audiences have different trust dynamics and platform usage patterns.

**Nano-influencers (1,000–10,000 followers)**
EA characteristics:
- High trust: audiences often know the influencer personally or through a shared community (school, church, neighbourhood, profession)
- High engagement: typical engagement rate 5–10%; audiences interact as though talking to a friend
- Low or no cost: product barter, free experience, or small cash fee is the norm
- Best for: hyperlocal campaigns, community-specific products, word-of-mouth amplification in a specific city or town, new brand awareness among a tight demographic
- Platforms: Instagram, TikTok, Facebook personal pages, WhatsApp group admins (500+ engaged members in a specific community — treat these as nano-influencers even without a formal profile)
- Key risk: limited content quality; may require more creative direction

**Micro-influencers (10,000–100,000 followers)**
EA characteristics:
- Best balance of reach and engagement for most EA campaigns: typical engagement rate 3–6%
- Known face in their niche (beauty, food, parenting, fitness, business/professional, faith)
- Moderate cost: combination of product barter and cash fee; rates vary widely — negotiate based on deliverables and content reuse rights
- Best for: brand awareness in a specific niche, product launches, testimonial-style content, sustained always-on partnerships
- Platforms: Instagram (primary for lifestyle), TikTok (fast-growing for entertainment and tutorial content), YouTube (for tutorial reviews and unboxing, especially tech and beauty)
- Key risk: audience overlap between similar-niche micro-influencers — vet carefully to avoid redundancy

**Macro-influencers (100,000+ followers)**
EA characteristics:
- High reach but lower engagement: typical engagement rate 1–3% (follower-to-engagement ratio dilutes at scale)
- Includes local celebrities, national TV personalities, prominent YouTubers, and cross-border EA creators
- Significant cost: cash fees required; product barter alone is rarely sufficient
- Best for: brand launches targeting broad awareness, national campaigns, major product launches requiring reach over engagement depth
- Key consideration: macro influencer content can feel less authentic in markets where personal trust drives purchase decisions — weigh reach against credibility for your category
- Platforms: Instagram, YouTube, TikTok (newer macro cohort), Facebook (for older demographics)

**WhatsApp community admins (special category)**
In Uganda and broader EA, WhatsApp group admins with 500+ engaged members (e.g. alumni groups, professional networks, faith communities, neighbourhood groups, mama groups) function as micro-influencers with extremely high trust and direct access. Engage them as nano/micro equivalents. Content takes the form of personal endorsements or forwarded messages rather than produced content.

---

### 2. Identifying the Right Influencers

**Audience match criteria:**
Before reaching out to any influencer, verify:
- Their audience demographics match the target persona (ask for a screenshot of audience insights — Instagram and TikTok provide this in creator accounts)
- Their audience is primarily Uganda/EA-based (or the relevant geography for this campaign)
- Their content niche is relevant to the product or service category
- Their audience size is realistic for the tier claimed — follower counts can be inflated

**Engagement rate benchmarks:**

| Tier | Followers | Expected Engagement Rate | Red Flag Threshold |
|---|---|---|---|
| Nano | 1K–10K | 5–10% | Below 3% |
| Micro | 10K–100K | 3–6% | Below 2% |
| Macro | 100K+ | 1–3% | Below 0.5% |

Calculate engagement rate manually: (Total likes + comments on last 10 posts) ÷ (Followers × 10) × 100. Do not rely on self-reported figures.

**Content quality assessment:**
- Consistency: do they post regularly (at least weekly)? Gaps longer than 3 weeks suggest unreliability.
- Quality: is the content well-produced? For nano/micro, basic phone video is acceptable; for macro, expect professional or near-professional production.
- Authenticity: do captions sound genuine, or are they clearly template-written? Engaged audiences respond to real voice.
- Comments quality: are comments genuine interactions or generic emoji reactions? Purchased engagement produces shallow comments ("Nice!", fire emojis with no substance).

**Platform fit:**
- Match the influencer's primary platform to where the target audience spends time
- Do not engage a primarily TikTok creator for a campaign targeting Facebook-dominant audiences
- YouTube creators are best for long-form product reviews, tutorials, and unboxing — plan lead time accordingly (video production cycles are longer)

**Brand safety check:**
- Review the influencer's last 90 days of content: any controversial topics, political statements, or sensitive brand associations?
- Check comment sections: is there evidence of harassment, divisive debates, or inflammatory responses from the influencer?
- Is there any history of failed paid partnerships (not disclosing ads, fake reviews, public complaints from brands)?
- If in doubt, do not proceed. A poor partnership is harder to undo than a missed opportunity.

**Where to find influencers in Uganda/EA:**
- Manual search on Instagram: search relevant hashtags (#KampalaFood, #UgandanBeauty, #UgandaBusiness) and review who is posting consistently with genuine engagement
- Manual search on TikTok: search for content in the relevant category; check for Ugandan or EA creators by location tag or language cues
- Facebook groups and communities: identify group admins in relevant communities (parenting groups, professional groups, regional interest groups)
- Ask existing customers: your customers may follow — or be — influencers in their own networks
- No formal EA creator directory currently exists at scale — manual discovery is the primary method

---

### 3. Outreach Approach

**The first message:**
Keep the first outreach message short, personal, and specific. Never send a generic campaign brief as the first contact. Structure:
1. One sentence showing you know their content — reference a specific post or series
2. One sentence on what the brand does and who it serves
3. One clear proposition: what you want to explore and what you are offering
4. A simple ask: are they open to a conversation?

Template (adapt to fit the influencer and brand):

> "Hi [Name], I've been following your [content type, e.g. 'home cooking videos'] and especially enjoyed [specific post]. I work with [Brand Name], a [brief description, e.g. 'Kampala-based food brand']. We'd love to explore a potential partnership — we're offering [product barter / fee / experience]. Would you be open to a quick conversation?"

Keep the tone warm and peer-to-peer. Avoid corporate language. Use WhatsApp DM or Instagram DM — email is rarely effective for influencer outreach in EA.

**What to offer by tier:**

| Tier | Typical Offer |
|---|---|
| Nano | Product barter; free experience; gift hamper; no cash fee expected |
| Micro | Product barter + cash fee (negotiate; typical range UGX 100K–500K per deliverable) |
| Macro | Cash fee (negotiate); product provided in addition |
| WhatsApp admins | Product sample or small cash fee; reciprocal promotion in your channels |

Agree the deliverables, timeline, and any usage rights expectations before sending product or payment. Even for barter deals, confirm expectations in writing (WhatsApp message is acceptable for nano-level; formal brief for micro and above).

**Following up:**
If no response after 5 days, send one follow-up message. Keep it brief — one sentence. If still no response, move on. Do not persist beyond two contact attempts.

---

### 4. Campaign Brief Template for Influencers

Use this template for all micro and macro influencer engagements. Adapt for nano — a simplified WhatsApp message is sufficient for nano-level barter deals.

---

**[Client/Brand Name] — Influencer Campaign Brief**

**Campaign name:** [Short working title]
**Brand overview:** [2–3 sentences: what the brand does, who it serves, what makes it different]
**Campaign objective:** [Single sentence — what this campaign must achieve]
**Key message:** [The one thing the audience must remember after seeing this content]
**Target audience:** [Brief description — age, location, interests]
**Campaign dates:** [Start date — End date, day-month-year format]

**Content deliverables:**

| Deliverable | Platform | Format | Quantity | Due Date |
|---|---|---|---|---|
| [e.g. Instagram Reel] | Instagram | [Specs: 9:16, 30–60 seconds] | [e.g. 1] | [Date] |
| [e.g. Instagram Story] | Instagram | [Specs: 9:16, static or video] | [e.g. 3 frames] | [Date] |
| [e.g. TikTok video] | TikTok | [Specs: 9:16, 30–90 seconds] | [e.g. 1] | [Date] |

**Do's:**
- [e.g. Show the product in use in a natural, everyday setting]
- [e.g. Use the campaign hashtag: #[Hashtag]]
- [e.g. Tag @[BrandHandle] in the caption and in the video]
- [e.g. Include the brand's unique discount code: [CODE]]

**Don'ts:**
- [e.g. Do not compare our product to competitors by name]
- [e.g. Do not mention price — we will handle pricing communication separately]
- [e.g. Do not use a filter that significantly alters the product's appearance]

**Disclosure:** Clearly disclose this as a paid partnership or gifted collaboration. On Instagram, use the Paid Partnership label. On TikTok, use the Branded Content toggle. In captions, include #Ad or #Gifted. This is international best practice; local enforcement is limited but disclosure protects the influencer's credibility and the brand's reputation.

**Usage rights:** By accepting this partnership, you grant [Brand Name] the right to repurpose your content on our owned social media channels for a period of [6 months / 12 months] from the date of publication. We will always credit your handle when repurposing. [Note: for formal usage rights transfer, refer to a lawyer to draft appropriate contract language.]

**Reporting requirements:** Please share native analytics screenshots (reach, impressions, engagement) within 7 days of posting. If a unique link or discount code was provided, share click or redemption data.

**Questions:** Contact [Name] via [WhatsApp / Instagram DM / Email] at [Contact Details].

---

### 5. Content Usage Rights Guidance

This guidance is not legal advice. Refer the client to a lawyer for formal contracts.

**What to ask for:**
When commissioning influencer content, ask explicitly for the right to repurpose the content on the brand's owned channels (Instagram, Facebook, website, email). This should be agreed before posting, not after.

**Standard timeframes:**
- 6 months: standard for most nano/micro partnerships; sufficient for most campaign cycles
- 12 months: appropriate for hero content (launch videos, brand testimonials) or evergreen content you intend to use across multiple campaigns

**How to request it:**
Include usage rights language in the written brief (see Section 4 template). For nano-level barter deals, a WhatsApp message confirming the terms is acceptable. For micro and above, request written acceptance of the brief.

**What you cannot do without explicit permission:**
- Edit or alter the influencer's content in ways that change the meaning or message
- Use the content in paid advertising (boosted posts or paid ads) without a separate usage rights agreement — this typically involves an additional fee
- Repurpose content beyond the agreed timeframe

**When to involve a lawyer:**
- Any macro-level partnership with cash fees above UGX 1 million
- Any agreement that involves paid advertising usage rights
- Any multi-month retainer arrangement
- Any exclusivity clause (preventing the influencer from working with competitors)

---

### 6. Performance Metrics

Track the following metrics for every influencer campaign. Set targets before the campaign starts.

| Metric | What It Measures | How to Track |
|---|---|---|
| Reach | Number of unique accounts that saw the content | Native analytics screenshot from influencer |
| Impressions | Total number of times content was seen (including repeat views) | Native analytics screenshot |
| Engagement rate | Quality of audience interaction (likes + comments + saves ÷ reach) | Calculate manually |
| Link clicks | Number of clicks to the brand's link | UTM-tagged link in bio or Linktree |
| Discount code redemptions | Direct sales attributed to the influencer | Track unique code in point-of-sale or e-commerce |
| Story swipe-ups / link stickers | Direct traffic from Stories | Native analytics |
| New followers gained | Follower growth on brand channels during campaign period | Manual count: before and after |
| Attributed enquiries | DMs or enquiries mentioning the influencer or campaign | Manual count |

**Attribution tools:**
- UTM links: create a unique UTM-tagged link for each influencer (use Google Campaign URL Builder). Track via Google Analytics.
- Discount codes: assign each influencer a unique code (e.g. SARAH15, JAMES20). Track redemptions in your sales records or e-commerce platform.
- Direct ask: include "How did you hear about us?" in your sales or enquiry process. Some of the best attribution in EA is still manual.

---

### 7. Red Flags to Avoid

**Bought followers:**
Compare follower count to engagement rate. An account with 50,000 followers and 50 likes per post (0.1% engagement) has bought followers. Walk away. Cross-check with a free tool such as HypeAuditor or modash.io if budget allows; otherwise calculate manually using the benchmarks in Section 2.

**Misaligned audience:**
An influencer with 80,000 followers based primarily in Nigeria is not the right partner for a Kampala-only campaign. Always ask for audience location data before committing.

**Brand safety risks:**
Avoid influencers who post content that is consistently inflammatory, divisive, or associated with controversial positions — even if their niche is relevant. The brand association risk is real, and disengagement mid-campaign is costly.

**History of controversial brand partnerships:**
Search the influencer's name + the word "review" or "ad" to identify any past partnerships that generated public complaints. One incident can be contextual; a pattern is a warning sign.

**No-shows and late delivery:**
For first-time partnerships, ask for proof of past campaign delivery (screenshots of previous brand posts). Establish a clear deadline in the brief and include a catch-up clause: if content is not posted within 48 hours of the agreed date, the brand reserves the right to reclaim product or withhold payment.

**Over-claiming results:**
Be cautious of influencers who guarantee specific sales numbers or reach figures before a campaign. Legitimate influencers share what their typical metrics look like; they do not promise outcomes they cannot control.

---

## The Creator Economy — Structural Principles (Hund, 2023; Falls, 2021; Hennessy, 2018)

### Why Influencer Marketing Works When It Works

Influencer marketing derives its effectiveness from parasocial trust — the one-sided relationship that audiences build with creators they follow consistently. Audiences trust recommendations from a creator they watch daily more than they trust a brand advertisement, because the creator has earned that trust through consistent, authentic presence over time. The moment influencer content appears manufactured or out-of-character for that creator, the parasocial trust breaks — and brand association produces negative rather than positive effects.

**The authenticity imperative (Falls, 2021):** The single most important criterion when selecting an influencer is not reach or engagement rate — it is authentic fit. A creator who genuinely uses a product produces content that audiences recognise as real. A creator promoting a product they have never touched produces content audiences also recognise — and dismiss. Authentic fit requires that the brand seek creators who are already in the natural habitat of the product or service category.

**Resonance over reach (Hennessy, 2018):** The influencer industry undervalued resonance for most of its early history, obsessing over follower counts. Resonance — the emotional connection and behavioural influence an influencer has with their audience — is the actual commercial variable. A micro-influencer with 15,000 deeply engaged followers in a specific niche will consistently outperform a macro-influencer with 500,000 disengaged followers on product trial and purchase metrics.

**The three-tier selection model (Hennessy, 2018):**

| Consideration | Primary question |
|---|---|
| **Reach** | Does this creator's audience include enough members of our target persona to justify the investment? |
| **Resonance** | Do followers take action on this creator's recommendations — not just like and scroll? |
| **Relevance** | Is the creator's content category a natural home for our product or service? |

All three must meet threshold before proceeding. An influencer with high Reach and Relevance but low Resonance (poor audience action rate) is a wasted investment.

### The Influencer Industry Structure (Hund, 2023)

The influencer industry is now professionalised at the macro level and semi-professional at the micro level. Understand the business structure before negotiating:

- **Creator's perspective:** Influencers are running media businesses. Their content is their IP, their audience is their asset, and their sponsorship income is tied directly to the value they deliver to that audience. Brands that ask for excessive creative control, unusually short deadlines, or content that does not fit the creator's established voice will receive poor results — because the creator's audience will not respond to content that breaks from their established voice.

- **Long-term partnerships outperform one-post deals:** A creator who mentions a brand once is an advertisement. A creator who integrates a brand naturally across four weeks of content becomes an endorsement. Audiences build brand familiarity through repeated, contextually appropriate exposure — not a single sponsored post. Wherever budget allows, structure campaigns as a minimum of 3–4 touchpoints across 4–6 weeks.

- **Content usage rights negotiation:** Influencer-created content typically belongs to the creator. Usage rights for branded channels, paid advertising, and extended time periods must be negotiated and paid for separately from the post fee. In Uganda/EA, this is often not formalised — state rights expectations clearly in the written brief before content is produced, not after.

### Winfluence — The Influence Continuum (Falls, 2021)

Falls proposes the Influence Continuum: at one end, transient influencers (celebrities with broad but shallow reach); at the other end, relevant influencers (niche experts with narrow but deep impact). For most EA marketing objectives, content on the Relevant end of the continuum — micro and nano creators who are genuine authorities in their category — produces better commercial outcomes than celebrity association.

**The five influence mechanisms (Falls, 2021):**
1. **Authority** — expertise that makes followers trust the recommendation
2. **Acumen** — business and product knowledge that makes endorsements credible
3. **Access** — the creator's exclusive position (behind-the-scenes, first to know, personal experience)
4. **Agility** — responsiveness to trends and timely relevance
5. **Audience Match** — the degree to which the creator's audience mirrors the target persona

Evaluate every potential partner against all five. An influencer who scores high on only one or two mechanisms is a weak investment.

---

## Quality Criteria

- Tier definitions apply EA-specific engagement benchmarks — not global averages
- Audience match criteria include a clear instruction to verify audience location before committing
- Engagement rate calculation method is specified and can be performed manually without paid tools
- Outreach message template sounds personal and human — not corporate
- Campaign brief template is complete and fill-in-the-blanks ready for immediate use
- Usage rights guidance explicitly notes it is not legal advice and specifies when to involve a lawyer
- Performance metrics include at least two trackable attribution methods (UTM links and discount codes)
- Red flags section addresses bought followers with a concrete detection method
- WhatsApp group admins are explicitly identified as a nano-influencer category relevant to the EA context
- British English spelling throughout; monetary values in UGX where referenced

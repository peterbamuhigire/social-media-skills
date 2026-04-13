---
name: meta-social-listening
description: Sets up and operates a systematic social listening programme for a client — covering keyword taxonomy, tool setup across four free or low-cost platforms, a repeatable listening cadence, intelligence extraction protocol, and a log template. Also maps how listening findings feed back into content, strategy, community management, and crisis response across the skill suite. Invoke this skill when onboarding a new client to establish their listening baseline, when a client wants to understand what is being said about them online, when a competitor gap analysis requires ongoing monitoring, or when the first signs of a reputational issue need to be caught early.
---
# Social Listening Programme

<!-- dual-compat:start -->
## Use when
- Sets up and operates a systematic social listening programme for a client — covering keyword taxonomy, tool setup across four free or low-cost platforms, a repeatable listening cadence, intelligence extraction protocol, and a log template. Also maps how listening findings feed back into content, strategy, community management, and crisis response across the skill suite. Invoke this skill when onboarding a new client to establish their listening baseline, when a client wants to understand what is being said about them online, when a competitor gap analysis requires ongoing monitoring, or when the first signs of a reputational issue need to be caught early.
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
- A structured audit, report, model, or analytical framework in markdown, with decisions and recommendations tied to evidence.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Collect the following before generating the listening programme:

- **Client name** and trading name (if different)
- **Industry** and sub-sector (e.g., hospitality > restaurant; retail > clothing)
- **Country / city** (default: Uganda / Kampala)
- **Primary goal** (e.g., catch complaints early, track competitor activity, surface content ideas)
- **Brand name** — exact spelling plus all known misspellings and abbreviations
- **Founder or spokesperson name** (if public-facing — leave blank if the brand is not personality-led)
- **3–5 competitor names** — include their social media handles if known
- **Primary product or service category keywords** — what customers call the product, not industry jargon
- **Primary platforms to monitor** (default: Facebook, Instagram, TikTok, X/Twitter, Google Business Profile)
- **Local language variants** of brand or product names in Luganda, Swahili, or Sheng (if applicable)
- **Current monitoring setup** — what, if anything, is already in place

---

## What Social Listening Is (and Is Not)

Social listening is the practice of monitoring online conversations about your brand, your competitors, and your industry in order to surface intelligence you would otherwise miss. It means searching systematically for mentions of your business name, your products, your key people, and your sector — across social media platforms, news sites, blogs, forums, and review sites — and then interpreting what you find to inform decisions. Listening is active and analytical: it asks "what does this tell us?" rather than simply recording that it happened.

Social listening is not the same as social media reporting. Reporting is quantitative — it measures reach, engagement rate, follower growth, and return on investment using platform analytics. Listening is qualitative: it reads the *content* of what people say, not just how many people said it. A business can have excellent reporting numbers and still be completely unaware that a forum thread is circulating a complaint about their customer service. Listening catches what the metrics miss. Do not conflate the two; they serve different purposes and require different skills.

For clients in Uganda and East Africa, listening carries a particular strategic weight. The majority of customer feedback in this market travels through WhatsApp — a private, end-to-end encrypted channel that cannot be monitored externally. What reaches public platforms — Facebook comments, Google reviews, X/Twitter posts — is therefore a fraction of the total conversation. That fraction is nonetheless a meaningful proxy: if five customers complain publicly on Facebook, it is reasonable to infer that many more have shared the same frustration privately. Listening catches the visible signal and uses it to understand the invisible majority. The EA consultant who monitors consistently will always know more about their client's reputation than one who relies on the client to report problems themselves.

---

## 1. Keyword Taxonomy

Build the client's keyword list across five categories before setting up any tool. A complete taxonomy ensures no critical mentions are missed and avoids wasting time monitoring irrelevant noise.

### Category 1 — Brand Terms (Must Monitor)

| Keyword type | Example | Client's version |
|---|---|---|
| Exact business name | "Kampala Fresh Bakery" | |
| Common misspelling 1 | "Kampala Fresh Bakary" | |
| Common misspelling 2 | "Kla Fresh Bakery" | |
| Product / service name | "sourdough bread Kampala" | |
| Founder name (if public) | "Sarah Nakato bakery" | |
| Brand hashtag | #KampalaFreshBakery | |

### Category 2 — Competitor Terms

| Keyword type | Example | Client's version |
|---|---|---|
| Competitor 1 brand name | "City Breads Uganda" | |
| Competitor 2 brand name | "Kampala Cakes" | |
| Competitor 3 brand name | "Bake House UG" | |
| Competitor product name | "City Breads croissant" | |
| Comparison search | "vs City Breads" | |

### Category 3 — Industry Terms

| Keyword type | Example | Client's version |
|---|---|---|
| Customer-language category term | "fresh bread Kampala" | |
| Common customer question | "where to buy sourdough Kampala" | |
| Industry hashtag | #KampalaBakery | |
| Discovery phrase | "best bakery in Kampala" | |

### Category 4 — Sentiment Triggers

| Sentiment | Example search string | Client's version |
|---|---|---|
| Negative | "[Brand] complaint" | |
| Negative | "[Brand] bad / scam / disappointed / problem" | |
| Positive | "[Brand] recommend / excellent / love / happy" | |
| Positive | "[Brand] best" | |

### Category 5 — Location Terms (EA-Specific)

| Keyword type | Example | Client's version |
|---|---|---|
| Brand + city | "[Brand] Kampala" | |
| Brand + country | "[Brand] Uganda" | |
| Brand + region | "[Brand] East Africa" | |
| Industry + city (discovery) | "bakery Kampala" | |
| Local language brand variant | "omugati" (bread in Luganda) | |

Work through this table with the client at onboarding. A complete taxonomy takes 20–30 minutes to build and saves hours of wasted monitoring time.

---

## 2. Tool Setup (Free and Low-Cost)

Set up all four tools below. Each covers a different source type; together they provide sufficient coverage for an EA small-to-medium business without paid subscription costs.

### Google Alerts (Free)

Google Alerts monitors news sites, blogs, and the open web — not social media. It is the best free tool for catching press coverage, blog mentions, and forum posts.

**Setup steps:**
1. Go to alerts.google.com (sign in with a Google account)
2. In the search box, type the first keyword (e.g., the exact brand name in quotation marks: "Kampala Fresh Bakery")
3. Click "Show options"
4. Set **How often** to "At most once a day"
5. Set **Sources** to "Automatic"
6. Set **Language** to "Any language" (to catch Luganda or Swahili mentions)
7. Set **Region** to "Any region" unless the client is hyperlocal — in that case set to Uganda
8. Set **How many** to "All results"
9. Enter the client's email address in **Deliver to** — use a dedicated agency Gmail address, not your personal one
10. Click "Create Alert"
11. Repeat for: competitor brand names (one alert per competitor), founder name, top 2 industry keywords
12. Total alerts to create: brand name + misspelling + founder name + 3 competitor names + 2 industry terms = 8–9 alerts

**Limitation:** Google Alerts does not index Facebook, Instagram, TikTok, or WhatsApp. It is a supplement to platform monitoring, not a replacement.

---

### Native Platform Search (Free)

Conduct manual searches on each platform weekly. This is the most reliable way to find social mentions; it requires no tool, no account upgrade, and no budget.

**Facebook:**
- Log into a personal or agency Facebook account
- Click the search bar and type the brand name → select "Posts" tab
- Repeat for top competitor names and top industry terms
- Scan the last 7 days of results for mentions, complaints, reviews, and discussions
- Check the client's Facebook Page comments and reviews directly

**Instagram:**
- Search the brand name hashtag (e.g., #KampalaFreshBakery) — tap "Recent" to see the latest posts
- Search the brand name as a text term — check tagged posts and mentions
- Save the top 5 monitoring hashtags in Instagram Collections for quick weekly access
- Check competitor handles weekly for content themes and engagement signals

**TikTok:**
- Open TikTok, tap the search icon, type the brand name
- Sort by "Latest" to see recent content — not "Top" (which shows historical viral content)
- Repeat for competitor names and top industry keywords
- Note any user-generated content mentioning the client

**X / Twitter:**
- Go to x.com/search-advanced (no account needed for basic search; log in for full results)
- Enter the brand name in "All of these words"; set "From this date" to 7 days ago
- Run the same search for competitor names
- Save these as bookmarked searches if using a logged-in account
- Check daily — X is the fastest-moving platform for reputation signals in Uganda's opinion-leader community

**LinkedIn:**
- Search the brand name → click the "Content" filter to see posts mentioning the brand
- Repeat for competitor names
- Particularly relevant for B2B clients or businesses in the formal sector

---

### Brand24 or Mention (Freemium)

Use Brand24 (brand24.com) or Mention (mention.com) for automated mention tracking. Both offer free tiers adequate for small clients starting out.

**Brand24 free tier:** monitors up to 3 keywords; shows a limited number of recent mentions. Set up: brand name, primary competitor name, primary industry keyword.

**Mention free tier:** 250 mentions per month. Set up the same 3 keywords.

**Setup steps (Brand24 example):**
1. Create a free account at brand24.com
2. Click "New project"
3. Enter the client business name as the project name
4. Add keyword 1: exact brand name (with quotation marks for exact match)
5. Add keyword 2: primary competitor name
6. Add keyword 3: primary industry keyword
7. Set language filter to "All languages" to capture Luganda and Swahili mentions
8. Connect the dashboard email notifications to the client or agency email
9. Review the dashboard weekly

**Budget note:** Paid tiers for Brand24 start at approximately $49 per month (approximately UGX 180,000). Flag this to the client. For most small EA clients, the free tier combined with native platform search is sufficient until monthly social media revenue warrants the upgrade.

---

### Google Business Profile Reviews (Free)

GBP reviews are one of the highest-intent feedback sources available — customers who leave a review have had a direct experience with the business.

**Setup steps:**
1. Log into the client's Google Business Profile at business.google.com
2. Go to Settings → Notifications → enable email notifications for "New reviews"
3. Check GBP weekly: note the current star rating, read all new reviews, and look for recurring themes
4. Check 3–5 competitor GBP profiles weekly: search the competitor name in Google Maps and read their recent reviews for intelligence on their customer experience weaknesses

---

## 3. Listening Cadence

Build listening into the weekly workflow. Unscheduled monitoring does not happen consistently.

### Daily (5 minutes)

- X/Twitter Advanced Search: brand name + top competitor name — scan for new mentions from the past 24 hours
- Google Alerts email: scan for news, blog, and web coverage — flag anything relevant to the client

### Weekly (20 minutes)

- Facebook native search: brand + competitor + top industry term (10 minutes)
- Instagram hashtag and text search: brand + competitor (3 minutes)
- TikTok search: brand + top industry keyword (3 minutes)
- LinkedIn content search: brand + competitor (2 minutes)
- Brand24 / Mention dashboard: review flagged mentions, check sentiment trend (2 minutes)
- GBP reviews: read all new reviews; check 2–3 competitor GBP profiles (3 minutes)
- Log all findings in the Listening Log (Section 5)

### Monthly (45 minutes)

- Full competitor social media review: feeds, follower counts, engagement estimates — use the output to update `meta-competitor-analysis`
- Sentiment summary: count positive, neutral, and negative mentions this month versus last month — note any trend change
- Theme extraction: identify the 3–5 topics that appeared most frequently in mentions this month
- Share-of-voice estimate: count brand mentions versus total mentions of all monitored brands in the same category — express as a percentage
- Complete the monthly debrief (Section 4) and share with the client

---

## 4. Intelligence Extraction Protocol

Raw mentions have no value until they are interpreted. Apply these five questions to listening data every week.

**The 5 Weekly Listening Questions:**

1. **What are customers praising about us this week?**
Surface these in the log as "amplify" opportunities. Praised experiences become content: a customer complimenting the bakery's sourdough is a prompt for a Reel about the sourdough-making process. Share the finding with the content calendar (see `11-content-calendar`).

2. **What complaints or frustrations appeared?**
Log each complaint with its platform, sentiment rating, and whether it was resolved. Recurring complaints (the same theme appearing three or more times across separate posts) indicate a service or product issue — escalate to the client's operations team, not just the social media manager.

3. **What are people saying about our competitors?**
Competitor complaints are positioning opportunities. If three customers in one week complain that a competitor's delivery is slow, and the client offers faster delivery, that is a campaign angle. Feed findings into `09-campaign-strategy`.

4. **What questions are people asking about our category?**
Unanswered category questions are content gaps. A cluster of "where can I find sourdough bread in Kampala?" searches means no one is answering that question well. The client who answers it first wins the discovery. Feed findings into `11-content-calendar` as FAQ content.

5. **Are there any emerging topics in our industry we should comment on?**
New regulations, food safety news, industry trends, local events — topics gaining traction in listening are thought leadership opportunities. Feed findings into `10-content-pillars` if a theme is recurring.

**Weekly debrief format:** Complete the five questions above in writing. Takes 15 minutes. Share the written debrief with the client once per month, collated as a monthly listening summary. This makes the intelligence visible and justifies the monitoring time investment.

---

## 5. Listening Log Template

Maintain this log as a Google Sheet. Create one tab per month. Share view access with the client.

| Date | Platform | Mention type | Sentiment | Summary (1 sentence) | Action taken | Priority |
|---|---|---|---|---|---|---|
| DD/MM/YYYY | Facebook / Instagram / GBP / TikTok / X / Other | Brand / Competitor / Industry | Positive / Neutral / Negative | | | High / Medium / Low |

**Column guidance:**
- **Mention type:** Brand = about the client; Competitor = about a named competitor; Industry = about the category with no specific brand named
- **Sentiment:** Positive = favourable; Neutral = factual or ambiguous; Negative = complaint, criticism, or warning
- **Action taken:** "Replied via DM", "Escalated to client", "Added to content ideas", "No action required", "Flagged for crisis monitoring"
- **Priority:** High = requires a response or escalation within 24 hours; Medium = note and monitor; Low = logged for context

**Example rows (Kampala business — bakery):**

| Date | Platform | Mention type | Sentiment | Summary | Action taken | Priority |
|---|---|---|---|---|---|---|
| 15/03/2026 | Facebook | Brand | Negative | Customer posted that their birthday cake order arrived 2 hours late with no apology from staff | Replied publicly; escalated to client; issued DM apology with voucher | High |
| 17/03/2026 | Google Business Profile | Competitor | Negative | 3 reviews this week on City Breads profile complaining about dry cake texture | Added "freshness guarantee" angle to next month's content brief | Medium |
| 18/03/2026 | TikTok | Industry | Positive | Creator with 12K followers posted taste-test video of Kampala bakeries; client not featured | Identified creator; flagged to client for potential collaboration | Medium |

---

## 6. Converting Listening Into Strategy

Listening is the intelligence layer that makes every other skill in this suite more effective. Use the findings actively — do not let them sit in a log.

**→ Content calendar (`11-content-calendar`):**
Themes and questions surfaced in listening become content ideas for the following month. Add listening-derived ideas to the content brief at the monthly planning session.

**→ Content pillars (`10-content-pillars`):**
If the same theme appears in listening for three or more consecutive months, review whether it warrants its own content pillar or an adjustment to an existing one. Listening validates whether the current pillar structure reflects what the audience actually cares about.

**→ Campaign strategy (`09-campaign-strategy`):**
Competitor weaknesses identified in listening become campaign angles. A documented pattern of competitor complaints is evidence for a positioning campaign — "We do what [competitor] gets wrong."

**→ Community management (`playbook-community-management`):**
Unresolved complaints found in listening that were not responded to on the platform become community management priorities. Check the log at the start of each community management session.

**→ Crisis communications (`playbook-crisis-communications`):**
Listening is the early warning system for reputational risk. A sudden increase in negative brand mentions — particularly if the same topic appears across multiple platforms in the same 48-hour window — is a Level 1 crisis trigger. Escalate immediately using the crisis classification in `playbook-crisis-communications`.

**→ Product and service feedback (client operations):**
Listening intelligence about product frustrations, delivery problems, and service failures has operational value beyond social media. Share a monthly summary of product-related complaints with the client's operations lead. Social listening is a low-cost substitute for formal customer research in markets where research budgets are limited.

---

## 7. EA-Specific Considerations

**Multilingual monitoring:**
Ugandan customers regularly mix English and Luganda in social media posts — this is called Luganda-English code-switching and is normal in urban Kampala. Standard keyword monitoring will miss Luganda-language mentions entirely unless you build them in. Work with the client at onboarding to identify the top 5 product and service names as customers actually say them in conversation. Examples: "omugati" (bread), "emmere" (food), "ssente" (money/payment), "omusawo" (doctor). Add these as separate keywords in Brand24 and in platform searches. Apply the same principle for Swahili in the Kenyan or Tanzanian market and Sheng for urban Nairobi audiences.

**WhatsApp is unmonitorable — acknowledge this explicitly:**
WhatsApp is the primary channel for customer feedback in Uganda, and it is end-to-end encrypted. No external tool can monitor it. Do not imply otherwise. What can be done: brief the client's customer-facing staff to flag recurring WhatsApp complaints themes monthly. Create a simple staff feedback form (a shared Google Sheet or WhatsApp Group poll) asking: "What are the top 3 complaints or questions you received via WhatsApp this month?" Incorporate the responses into the monthly listening debrief.

**Facebook Groups:**
A significant proportion of EA community and industry conversation happens in private or semi-private Facebook Groups rather than on public pages. Identify 3–5 relevant groups at onboarding — local industry groups, neighbourhood community groups, city-specific consumer groups (e.g., "Kampala Foodies", "Kampala Business Network"). Join them using an agency or client account and monitor manually each week. Note that Facebook Group content does not appear in external tool searches.

**Informal and tabloid media monitoring:**
In Uganda, informal online news outlets such as Sqoop (sqoop.co.ug), Nile Post (nilepost.co.ug), and Chimp Reports (chimpreports.com) can amplify negative stories quickly and are read widely. Add their RSS feeds to Google Alerts or Feedly (free) so that coverage appears in the daily digest. Do not rely solely on mainstream media monitoring.

---

## Quality Criteria

Output meets the standard if it:

- The keyword taxonomy template is fully completed with the client's actual terms across all five categories — not left as a blank template for the client to fill in themselves
- All four tools have step-by-step setup instructions with numbered steps, not just tool names and descriptions
- The listening cadence specifies exact tasks, time estimates, and frequencies — daily, weekly, and monthly tasks are each listed separately and are individually actionable
- The five listening questions are specific enough that a consultant with access to public social media data can answer each one within 15 minutes
- The listening log template is complete with column guidance and example rows, and is explicitly described as a Google Sheet so the client can implement it immediately
- EA-specific considerations address multilingual monitoring with concrete examples in Luganda, the WhatsApp limitation with a named practical workaround, and Facebook Groups with a named monitoring method
- The strategy integration section explicitly connects this skill to at least five other skills in the suite by slug name
- British English throughout — no American spellings anywhere in the deliverable

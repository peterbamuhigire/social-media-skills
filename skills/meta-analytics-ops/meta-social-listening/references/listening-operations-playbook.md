# Listening Operations Playbook

Merged from skills/playbooks/playbook-sentiment-listening on 2026-09-29 at 8eacccb; preservation map: [playbook-sentiment-listening.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/playbook-sentiment-listening.md)

## When to use this reference

Read this reference when the client needs listening run as a repeatable operation with AI sentiment scoring on top: a tool stack matched to budget, a keyword set that includes crisis triggers, weekly NSS reporting, a real-time dashboard specification, a sentiment-to-decision table, and a Monday / Wednesday / Friday / monthly routine with named owners. Typical goals are brand health monitoring, competitor tracking, crisis prevention and content inspiration.

The parent [SKILL.md](../SKILL.md) is the foundation (keyword taxonomy, free tool setup, cadence, listening log). This reference adds AI sentiment scoring, NSS reporting and the decision framework on top of it; use them together, not as alternatives. For the full monthly scoring method (manual classification, NSS bands for EA service businesses, share of voice, theme extraction, monthly report) use [sentiment-and-share-of-voice-method.md](sentiment-and-share-of-voice-method.md).

## Why listening needs sentiment

Social listening monitors what people say about a brand, a competitor, an industry or a topic across social platforms, forums, news sites and review pages. Sentiment analysis extends it by applying Natural Language Processing (NLP) to classify each item as Positive, Neutral, Negative or Mixed and to extract emotion categories (joy, anger, fear, surprise, disgust).

The two are distinct but inseparable: listening without sentiment gives a volume count with no meaning; sentiment without listening has nothing to process. Together they answer three questions raw platform analytics cannot: what do people actually feel about this brand, is that feeling improving or deteriorating, and what is driving the change?

At meaningful market presence the mention volume is too large for manual review, so AI is the primary mechanism: it processes thousands of mentions per hour, clusters them by theme and flags trends before they become crises. Manual review checks what AI surfaces. (In mixed-language East African datasets, manual review of local-language content remains mandatory; see the decision rules.)

Johnsen (2024) holds that sentiment data has no value unless it drives a decision. Make the intelligence → decision → action loop explicit at the outset: every sentiment report ends with a named action, a named owner and a deadline. Data that produces no action wastes consultant time and client budget.

## Inputs

| Input | What to capture |
|---|---|
| Client business name and industry | For example "Kampala Fresh Bakery — food and beverage" |
| Country / city | Defaults to Uganda / Kampala if not specified |
| Primary goal (select one) | Brand health monitoring / competitor tracking / crisis prevention / content inspiration |
| Budget for tools (select one) | Free / USD 30–100 per month / enterprise (USD 300+) |
| Languages to monitor (one or more) | English only / English + Luganda / English + Swahili / all three |
| Competitors to track | Up to three brand names with social handles if known |
| Crisis sensitivity (select one) | High (any negative spike triggers an alert) / medium (3 negative mentions on the same topic within 6 hours) / low (weekly review only) |
| Current workflow, assets and performance evidence | Conditional; if absent, label the baseline unassessed and use a minimum viable routine |
| Roles, budget, timing and approval limits | Required for execution; if absent, produce a draft only — do not schedule, spend or publish |

## Decision rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Automated sentiment conflicts with language or cultural context | Sample by hand and relabel before reporting | False conclusions from weak classification |
| A tool needs payment infrastructure unavailable in Uganda (for example US-only card processing without international support) | Do not recommend it | A stack the client cannot pay for |
| Fewer than 500 monthly brand mentions, small EA business | Starter (free) configuration plus the weekly routine | Paying for capacity that is not needed |
| NSS reported | Always pair it with total mention volume for the period and a note on the theme driving the score | Misreading a low-volume week (−10 on few mentions is not −10 on many) |
| SOV requested for a single week | Mark it N/A; calculate SOV monthly only | Conclusions from a sample too small to mean anything |
| Client story appears on an informal Ugandan news outlet (Sqoop, Nile Post, Chimp Reports) | Treat as a Level 2 crisis minimum; activate [playbook-crisis-communications](../../../playbooks/playbook-crisis-communications/SKILL.md) | Local amplification that outruns the brand's own reach |
| Action would publish, spend, contact people or change production state | Require explicit approval first | Unauthorised external impact |

## Procedure

### 1. Select tools by budget

Tool reference (source-recorded capability, access and approximate cost; verify current plans and prices before stating, no register record):

| Tool | Type | Sentiment capability | EA access | Cost (approx.) |
|---|---|---|---|---|
| Google Alerts | Web monitoring | None | Yes | Free |
| Meta Business Suite | Facebook/Instagram comments | Basic (positive/negative flag) | Yes | Free |
| Talkwalker Alerts | Social monitoring | Basic | Yes | Free tier |
| Mention | Brand monitoring + social | Basic sentiment scoring | Yes | USD 29+/month |
| MonkeyLearn | NLP API, custom sentiment models | Yes — trainable | Yes | USD 0–299/month |
| Hootsuite Insights | Social listening + sentiment | Yes — AI-powered | Yes | USD 99+/month |
| Brandwatch | Enterprise listening | Yes — advanced NLP | Yes | Enterprise pricing |
| Africa's Talking + custom NLP | SMS and WhatsApp text analysis | Via API integration | Yes (EA-native) | Pay-per-use |

Configurations:

- **Starter (free):** Google Alerts (web and news) + Meta Business Suite (Facebook and Instagram) + Talkwalker Alerts (social web) + manual weekly platform search. Sufficient for a small EA business with fewer than 500 monthly brand mentions. Pair with the weekly routine in step 6.
- **Growth (USD 30–100 per month):** add Mention or MonkeyLearn to the starter stack. Use Zapier (free tier) to pipe Mention alerts into a shared Slack channel or Google Sheet for team visibility. MonkeyLearn's API allows custom sentiment training, useful for Ugandan English, Luganda-English code-switching and local complaint vocabulary.
- **Scale (enterprise):** Brandwatch or Hootsuite Insights as the primary platform. These aggregate sentiment across the major social platforms, report share of voice against named competitors and export dashboards fit for client presentation. Budget separately for the subscription and for consultant time to configure and maintain keyword sets.
- **Africa's Talking (growth or scale tier):** for clients with high SMS or WhatsApp Business API volumes, Africa's Talking (africastalking.com) is an EA-native API that can pipe message data into a custom NLP sentiment model via MonkeyLearn or a similar service. Document the integration in the client's tools stack ([meta-tools-stack-evaluation](../../meta-tools-stack-evaluation/SKILL.md)) and cost it explicitly before recommending it.

### 2. Build the keyword set, including crisis triggers

Build the taxonomy before configuring any tool, with the client at onboarding (20–30 minutes; it prevents weeks of missed intelligence).

- **Brand, competitor and industry terms** — use the Category 1–3 tables in the parent SKILL.md § 1 Keyword Taxonomy. This playbook adds an abbreviation-style misspelling ("KFB Kampala") to the brand list and names the brand hashtag as the primary brand hashtag. Monitor competitor sentiment alongside brand sentiment: a competitor negative spike is an intelligence signal, not background noise (see step 5).
- **Crisis triggers** — add this category for every client:

| Trigger type | Example keywords | Client's version |
|---|---|---|
| General complaint language | "fraud", "scam", "stolen", "disappointed", "terrible", "avoid" | |
| Service failure language | "no response", "ignored", "kept waiting", "not delivered" | |
| Mobile Money complaint language | "MoMo failed", "Airtel Money stuck", "transaction pending", "refund not received" | |
| EA-specific escalation signals | "report", "expose", "warning ugandans", "consumer protection" | |
| Product or safety complaint | "food poisoning", "expired", "broken", "fake" | |

EA-specific keyword rules:

- Add Luganda equivalents of key brand and product terms; urban Kampala customers code-switch between English and Luganda in the same post. Terms to consider: "emmere" (food/meal), "ssente" (money), "omusawo" (doctor/health), "omugati" (bread). A complaint such as "that place is really bad — banakola!" will not be caught by an English-only set. Build Luganda and Swahili variants for all brand and crisis-trigger terms, verified by a Luganda-speaking staff member or the client — never by machine translation.
- Add Swahili equivalents if the client operates in or targets Kenya, Tanzania or Rwanda (for example "pesa" for money, "chakula" for food).
- Include Mobile Money complaint vocabulary for any client whose customers pay via MTN Mobile Money, Airtel Money or similar; payment complaints travel fast on Facebook and X/Twitter in Uganda and are often high priority.
- For delivery or logistics clients add boda-boda and delivery complaint language: "delivery late", "boda disappeared", "rider no show", "wrong address delivered".
- Add the informal news domains (Sqoop, sqoop.co.ug; Nile Post, nilepost.co.ug; Chimp Reports, chimpreports.com) to Google Alerts; they can amplify a negative story within hours to audiences far larger than the brand's own following.

### 3. Score and report weekly

Apply NSS to every weekly and monthly report:

```
NSS = (Positive mentions − Negative mentions) ÷ Total mentions × 100
```

Example: 80 positive, 15 negative, 5 neutral = (80 − 15) ÷ 100 × 100 = **NSS +65**.

Weekly operating bands (Johnsen, 2024). These differ from the monthly EA service-business bands in [sentiment-and-share-of-voice-method.md](sentiment-and-share-of-voice-method.md); name the band set used in each report.

| NSS range | Interpretation | Required action |
|---|---|---|
| Above +40 | Healthy — brand sentiment is strong | Maintain; surface positive themes for content |
| +20 to +40 | Attention required — monitor closely | Investigate negative themes; review community management |
| Below +20 | Crisis territory — immediate review required | Activate crisis review; brief the client within 24 hours |
| Negative (below 0) | Active reputational threat | Escalate to playbook-crisis-communications immediately |

Share of voice: SOV = client mentions ÷ total category mentions (client + all monitored competitors) × 100. Example: client 120, competitor A 90, competitor B 60; total 270; SOV = 120 ÷ 270 × 100 = **44.4%**. Calculate monthly to track whether the client is gaining or losing prominence; never from a single week.

### 4. Specify the real-time dashboard

Specify these elements in priority order at growth or scale tier. At starter tier, replicate the structure by hand in a Google Sheet or Looker Studio (free).

| Priority | Element | Specification |
|---|---|---|
| 1 | NSS trend | Line chart over rolling 7-day and 30-day windows, both visible at once; green above +40, amber +20 to +40, red below +20 |
| 2 | Mention volume by platform | Bar or stacked area chart split by Facebook, Instagram, X/Twitter, TikTok, Google Business Profile, news/web, other; updated daily; shows which platform drives volume changes |
| 3 | Top negative themes (auto-clustered) | Ranked top 5 negative topic clusters this week; Brandwatch and MonkeyLearn generate these; at starter tier group all negative mentions by subject by hand |
| 4 | Crisis alert indicator | Visible status flag (green/red) at the client's sensitivity: high = 2 negative mentions on the same topic within 4 hours; medium (default) = 3 within 6 hours; low = weekly NSS below +20 |
| 5 | SOV vs competitors | Pie or grouped bar chart against up to two named competitors; updated monthly; shown as this month vs last month |
| 6 | Top positive themes | Ranked top 3 positive clusters; feed the content calendar ([11-content-calendar](../../../pipeline/11-content-calendar/SKILL.md)); a theme present for three or more consecutive weeks warrants a content pillar review ([10-content-pillars](../../../pipeline/10-content-pillars/SKILL.md)) |

### 5. Translate sentiment into decisions every week

Sentiment data has no value until it drives a decision (Johnsen, 2024). Apply this table weekly.

| Sentiment signal | Threshold for action | Required action |
|---|---|---|
| Spike in negative mentions about a product or service | NSS drops 10+ points in one week | Identify the top negative theme; draft a client brief; activate playbook-crisis-communications if the theme is public-facing and spreading |
| Positive theme emerging organically | Same theme in 5+ positive mentions in one week | Develop content around it within 48 hours; add to 11-content-calendar immediately |
| Competitor negative spike | Competitor NSS drops 15+ points in one week | Review the competitor's negative themes; develop positioning content on the client's strength in that area; feed [09-campaign-strategy](../../../pipeline/09-campaign-strategy/SKILL.md) |
| NSS falls below +20 | Single observation sufficient | Review the past 7 days of published content and community-management responses; establish whether the client's own posts or replies are generating negative reactions |
| Recurring complaint topic | Same theme in 3+ separate mentions across 2+ weeks | Escalate to the client's operations or product team with a written brief; do not treat a recurring operational complaint as a social media problem |
| Positive UGC identified | Any organic customer content meeting quality and brand standards | Request permission to reshare; use the UGC curation and republishing workflow in [08-influencer-marketing-strategy](../../../pipeline/08-influencer-marketing-strategy/references/ugc-creator-and-customer-content.md#5-curation-and-republishing-workflow) |
| NSS below 0 (net negative) | Single observation sufficient | Treat as an active reputational threat; brief the client immediately; escalate to playbook-crisis-communications without delay |

Customise the action column for the client's industry: a food and beverage client treats "food poisoning" differently from a logistics client seeing "delivery fraud". At onboarding, name the two or three negative topics most damaging to this business and set the crisis alert threshold accordingly.

### 6. Run the weekly listening routine

Fix listening into a weekly schedule — unscheduled monitoring does not happen consistently — and assign a named person to each task.

| When | Time | Tasks |
|---|---|---|
| Monday — weekend review | 15 min | Pull all mentions from Friday 5pm to Monday 9am; note weekend volume spikes; update the dashboard NSS; flag crisis alert items to the client before 10am. Weekends in Uganda are high-activity periods for consumer social media — do not skip this review |
| Wednesday — mid-week NSS check | 10 min | Check the rolling 7-day NSS; if it has dropped 5+ points since Monday, identify the driving theme; review new negative mentions and confirm earlier community-management replies were given; flag emerging negative clusters to the client |
| Friday — weekly summary | 20 min | Produce the one-page weekly summary (template below); compare NSS with last week; name the top 3 themes; confirm the alert item and recommended action; share with the client or at the weekly team meeting; file a copy in the client's monthly reporting folder for [meta-reporting](../../meta-reporting/SKILL.md) |
| Monthly close (end of each calendar month) | 45 min | Calculate the month's SOV; chart NSS by week; extract the top 5 positive and top 5 negative themes; escalate operationally any complaint topic seen across three or more weeks; share the monthly summary with the client and file it in meta-reporting for quarterly review |

### 7. Cover the channels no tool reaches

- **WhatsApp cannot be monitored.** It is the dominant communication channel in Uganda (verify at use; see register WHATSAPP-USAGE-EA-2026) and end-to-end encrypted; no external tool can monitor it, and the client must not be told otherwise. Brief all customer-facing staff to note recurring WhatsApp complaint themes monthly and report them to the social media manager. Use a simple monthly staff input form (Google Sheet or WhatsApp Group poll) asking: "What were the top 3 complaints or questions you received via WhatsApp this month?" Put the answers in the monthly sentiment summary as "WhatsApp intelligence (staff-reported)". Separately, identify 3–5 relevant public or semi-public WhatsApp groups (local industry, neighbourhood consumer, city community groups) and assign a team member to review them weekly.
- **Facebook Groups carry much of the brand conversation.** A material share of EA consumer and community discussion happens in private or semi-public groups, not on public pages, and does not appear in automated tool searches. Identify 3–5 relevant groups at onboarding (local industry, neighbourhood, city consumer groups such as "Kampala Foodies" or "Kampala Business Network") and assign a named team member to review them weekly.

## Template — weekly summary (one page or screen)

- **Total mentions this week:** [number] (vs [number] last week — [up/down X%])
- **Net Sentiment Score:** [+/− number] (vs [number] last week)
- **Share of Voice:** [%] (vs last month: [%]) — monthly only; mark N/A in weekly reports
- **Top 3 themes this week:** [theme 1] / [theme 2] / [theme 3]
- **Alert item:** [one specific issue needing attention, or "None this week"]
- **Recommended action:** [named action, named owner, deadline]

Its purpose is to make the intelligence visible and actionable, not to document every mention.

## Deliverable and evidence

| Output | Consumer | Acceptance condition |
|---|---|---|
| Listening operations playbook | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
| Assumption and gap register | Approver or next workflow | Every missing source, unassessed check and required approval has an owner or next action |
| Release-gate result | Completed checklist | No blocking policy, factual, permission or anti-slop finding remains |

Write in British English with the East African usage rules in [east-african-english](../../../language/east-african-english/SKILL.md). A worked example must use a labelled scenario, not fabricated client evidence.

## Checklist

- [ ] Tools match the stated budget and are confirmed accessible in EA — none that are unavailable or need payment infrastructure absent in Uganda.
- [ ] All four keyword categories (brand, competitor, industry, crisis triggers) are populated with the client's actual terms, not left blank.
- [ ] NSS is applied correctly with all three thresholds (+40, +20, 0) and a named required action for each.
- [ ] The dashboard names metrics, thresholds and chart types, not a vague list of things to track.
- [ ] The sentiment-to-action table is customised to the client's industry with at least two industry-specific signals.
- [ ] EA context is explicit: Luganda and/or Swahili variants built in; the WhatsApp limitation named with a practical workaround; Facebook Group monitoring assigned to a named person.
- [ ] The weekly routine is a named schedule (Monday / Wednesday / Friday / monthly) with time estimates and task descriptions.
- [ ] Every report template ends with a named action, owner and deadline (Johnsen's intelligence → decision → action principle).
- [ ] No action item is delivered without owner, timing and acceptance; items lacking them are returned as unresolved gaps.

## Sources

- Johnsen, M. (2024) *AI in Digital Marketing*. Mercury Learning and Information.
- Ltifi, M. (ed.) (2025) *Advances in Digital Marketing in the Era of AI*. CRC Press.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson.
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. John Wiley and Sons.

---
name: meta-ai-tools-audit
description: Produces a structured evaluation of AI marketing tools for a specific client, mapped by function (content creation, SEO, social media management, email marketing, automation, analytics, paid advertising, influencer marketing) with East African market accessibility, cost, and capability ratings. Outputs a recommended AI tool stack calibrated to the client's budget profile in UGX. Invoke when a client asks which AI tools to adopt, wants to assess their current AI tool usage, needs to build an AI-powered martech stack, or is evaluating AI capabilities against their marketing goals.
---

# Meta AI Tools Audit

## Purpose

Produce a structured, client-specific evaluation of AI marketing tools calibrated to Uganda/East Africa budgets, payment infrastructure, and team capacity. Map every tool by function, assess EA accessibility explicitly, and deliver a recommended stack for the client's budget profile. Based on Johnsen, M. (2024) *AI in Digital Marketing* and Upadhyay, M. A. (2024) *Generative AI for Marketing*.

---

## Required Input

Ask for all of the following before generating any output:

1. **Client business name, industry, and country/city** — e.g., "Nile Organics, food retail, Kampala"
2. **Primary marketing goal** — e.g., increase brand awareness, generate leads, grow email list, improve content output
3. **Monthly tools budget range (UGX)** — Starter: under UGX 500,000 / Growth: UGX 500,000–2,000,000 / Scale: above UGX 2,000,000
4. **Current tools already in use** — list every tool, free or paid, currently in the workflow
5. **Team technical comfort level** — None (no prior software experience) / Basic (email and social apps) / Intermediate (uses multiple SaaS tools) / Advanced (API-comfortable, automation-literate)
6. **Primary channels** — Facebook, Instagram, WhatsApp, email, website/SEO, TikTok, LinkedIn, YouTube

Do not generate any output until all six inputs are collected.

---

## Section 1 — AI Tool Evaluation Framework

Before recommending any tool, apply this five-question test. If any critical question is answered No, do not recommend the tool.

1. **Does it address a specific, named marketing problem the client has today?** — Do not recommend AI tools on novelty grounds alone.
2. **Is it accessible with EA payment methods?** — USD credit/debit card (Visa/Mastercard issued in EA), Mobile Money (MTN, Airtel), or free tier. Tools requiring USD PayPal or US billing address only are inaccessible for most EA clients.
3. **Is there a free or low-cost entry point the team can test?** — Prioritise tools with free tiers before recommending paid subscriptions.
4. **Will the team realistically use it?** — Match AI capability complexity to the stated technical comfort level. Advanced automation tools assigned to non-technical teams will go unused.
5. **Does it process customer personal data?** — If yes, a Data Processing Agreement (DPA) is required under the Uganda Data Protection and Privacy Act 2019 before recommending.

Apply this framework as a named section in every deliverable so clients can use it independently.

---

## Section 2 — Tool Evaluation Tables by Function

Produce one table per category. Use the ratings below consistently.

**EA Recommendation ratings:**
- **Recommended** — accessible, affordable, strong EA fit
- **Conditional** — accessible but USD-priced; viable only if budget confirmed
- **Defer** — enterprise pricing, inaccessible payment, or low EA market penetration

---

### Category 1 — Content Creation

| Tool | AI Capability | EA Accessibility | Pricing Tier | EA Recommendation |
|---|---|---|---|---|
| ChatGPT (OpenAI) | Writing, brainstorming, first drafts, repurposing; GPT-4o via web | Free tier via web; paid via USD card | Free / ~USD 20/month | Recommended |
| Claude (Anthropic) | Long-form writing, strategy documents, nuanced analysis, structured outputs | Free tier via web; paid via USD card | Free / ~USD 20/month | Recommended |
| Gemini (Google) | Integrated with Google Workspace; writing, summarising, Docs/Slides assistance | Free via Google account; Workspace paid plans | Free / USD 12/month | Recommended |
| Jasper | Marketing-specific templates, brand voice, campaign copy | USD card required; no free tier | USD 49/month+ | Defer — high cost for EA budgets |
| Copy.ai | Short-form copy, social captions, ad copy; workflow automation | Free tier (limited); paid via USD card | Free / USD 36/month | Conditional |
| Canva AI / Magic Write | Design-integrated AI copy, image generation, presentation drafts | Free tier on Canva; Canva Pro via USD card or mobile payment on some EA platforms | Free / USD 15/month | Recommended — free tier sufficient for most EA clients |

**EA note:** ChatGPT and Claude are the most widely used AI writing tools in Uganda and East Africa. Jasper's USD 49/month entry point is prohibitive for most EA SME budgets; use Copy.ai starter or Claude free tier instead.

---

### Category 2 — SEO and Content Optimisation

| Tool | AI Capability | EA Accessibility | Pricing Tier | EA Recommendation |
|---|---|---|---|---|
| Surfer SEO | Content brief generation, SERP analysis, real-time content scoring | USD card required | USD 89/month+ | Defer — cost exceeds EA SEO ROI for most SMEs |
| SEMrush AI features | AI-assisted keyword clustering, competitive gap analysis, content ideas | USD card required; limited free tier | Free (limited) / USD 120/month | Conditional — only for clients with active SEO programmes |
| Ahrefs AI | Backlink analysis, keyword research, AI content gap tools | USD card required | USD 99/month+ | Defer — enterprise cost |
| RankMath (WordPress) | On-page SEO scoring, AI title/meta suggestions, schema markup | Free WordPress plugin; Pro via USD card | Free / USD 59/year | Recommended — primary free SEO option for EA clients on WordPress |

**EA note:** RankMath is the recommended default for EA clients with WordPress websites. Surfer SEO and SEMrush are USD-priced and appropriate only when a client has a dedicated SEO budget and an active content programme generating measurable organic traffic.

---

### Category 3 — Social Media Management

| Tool | AI Capability | EA Accessibility | Pricing Tier | EA Recommendation |
|---|---|---|---|---|
| FeedHive | AI content suggestions, post recycling, performance prediction scores | USD card; free tier available | Free / USD 19/month | Recommended — best value for EA budgets |
| Buffer | AI assistant for caption writing and post ideas; scheduling | USD card; free tier (3 channels) | Free / USD 6/month | Recommended |
| Hootsuite | AI content assistant, sentiment analysis, bulk scheduling | USD card; no affordable tier | USD 99/month+ | Defer — enterprise only |
| Later | AI caption writer, visual content planning, link-in-bio analytics | USD card; limited free tier | Free / USD 18/month | Conditional — best for Instagram-heavy clients |
| Metricool | Analytics, scheduling, AI hashtag suggestions, affordable paid tier | USD card; free tier available | Free / USD 18/month | Recommended — strong analytics at low cost |

**EA note:** FeedHive and Metricool offer the strongest value for EA budgets. Hootsuite is an enterprise product; recommend only to agencies managing 10+ client accounts with confirmed budget.

---

### Category 4 — Email Marketing

| Tool | AI Capability | EA Accessibility | Pricing Tier | EA Recommendation |
|---|---|---|---|---|
| Mailchimp | AI subject line optimiser, send-time optimisation, content suggestions | USD card; free tier (up to 500 contacts) | Free / USD 13/month | Recommended — free tier viable starting point |
| Brevo (formerly Sendinblue) | AI send-time optimisation, segmentation, SMS + email automation | USD card; generous free tier (300 emails/day) | Free / USD 25/month | Recommended — best free tier for high-volume senders |
| ActiveCampaign | Advanced AI segmentation, predictive sending, lead scoring | USD card; no free tier | USD 15/month+ | Conditional — justified for clients with 1,000+ contact lists and active automation needs |
| ConvertKit | Simple automation, AI subject line suggestions, creator-focused | USD card; free tier (up to 1,000 subscribers) | Free / USD 9/month | Conditional — best for content creators and solo consultants |

**EA note:** Brevo and Mailchimp free tiers are the recommended starting points. USD card payment is required for all platforms — confirm the client has a USD-capable Visa or Mastercard before recommending any paid tier.

---

### Category 5 — Marketing Automation

| Tool | AI Capability | EA Accessibility | Pricing Tier | EA Recommendation |
|---|---|---|---|---|
| Zapier | Connects 6,000+ apps; AI-assisted workflow builder; no-code automation | USD card; free tier (5 single-step Zaps) | Free / USD 19.99/month | Recommended — free tier for simple connections |
| Make (formerly Integromat) | Visual automation builder; more complex multi-step flows than Zapier | USD card; free tier (1,000 operations/month) | Free / USD 9/month | Recommended — better value than Zapier for complex workflows |
| Africa's Talking | SMS, WhatsApp, USSD, voice automation; EA-native API platform | Local EA payment; pay-per-use; UGX billing available | Pay-per-use (~UGX 30–60/SMS) | Recommended — primary EA automation tool; the only platform on this list with local payment and EA infrastructure |
| ManyChat | Facebook, Instagram, WhatsApp chatbot automation; AI reply suggestions | USD card; free tier (up to 1,000 contacts) | Free / USD 15/month | Recommended — strong WhatsApp/Instagram chatbot option |

**EA note:** Africa's Talking is the primary EA-native automation tool and must be included in any EA marketing automation recommendation. It supports UGX billing, bulk SMS, WhatsApp Business API, and USSD — capabilities no other tool on this list replicates for the EA market. See `playbook-ai-automation-workflow/SKILL.md` for building automation sequences using these tools.

---

### Category 6 — Analytics and Insights

| Tool | AI Capability | EA Accessibility | Pricing Tier | EA Recommendation |
|---|---|---|---|---|
| Google Analytics 4 | AI anomaly detection, predictive metrics, automated insights | Free — requires Google account | Free | Recommended — essential; zero cost |
| Meta Business Suite Insights | AI-powered content performance summaries, audience insights | Free — requires Meta Business account | Free | Recommended — essential for all Facebook/Instagram clients |
| Brandwatch | Social listening, AI sentiment analysis, trend detection | USD card; enterprise sales process | USD 1,000+/month | Defer — large brands only; not viable for EA SMEs |
| MonkeyLearn | NLP text analysis, sentiment classification, API-based | USD card; free tier available | Free / USD 299/month | Conditional — useful for clients with high-volume text data to analyse |
| Sprout Social | AI social analytics, sentiment analysis, competitive benchmarking | USD card; no free tier | USD 249/month+ | Defer — enterprise; rarely justified for EA budgets |

**EA note:** GA4 and Meta Business Suite Insights are free, essential, and must be in every client's stack regardless of budget. Brandwatch and Sprout Social are enterprise products appropriate only for large corporate or NGO clients with confirmed analytics budgets.

---

### Category 7 — Paid Advertising

| Tool | AI Capability | EA Accessibility | Pricing Tier | EA Recommendation |
|---|---|---|---|---|
| Meta Advantage+ | AI-automated targeting, creative optimisation, budget allocation | Accessible via Meta Business account; UGX and USD card payment | Ad spend only; no platform fee | Recommended — accessible with UGX card payment |
| Google Performance Max | AI-optimised cross-platform ads across Search, Display, YouTube, Gmail | Accessible via Google Ads account; USD card | Ad spend only; no platform fee | Recommended — accessible with EA USD card |
| TikTok Smart+ | Automated TikTok campaign management; AI creative and targeting | Accessible via TikTok Business account; USD card | Ad spend only; no platform fee | Recommended — accessible for EA clients targeting under-35 urban audiences |

**EA note:** All three platforms are accessible via Meta, Google, and TikTok business accounts using a Ugandan or EA Visa/Mastercard. Minimum ad spend thresholds apply — confirm with the client before recommending. Note that this skill covers tool selection only; paid ad campaign strategy and creative testing are out of scope (refer to `playbook-paid-social-advertising/SKILL.md`).

---

### Category 8 — Influencer Marketing

| Tool | AI Capability | EA Accessibility | Pricing Tier | EA Recommendation |
|---|---|---|---|---|
| Modash | AI influencer discovery, audience analytics, performance tracking | USD card; free trial available | USD 99/month+ | Conditional — justified only for clients running structured influencer programmes |
| HypeAuditor | Audience authenticity scoring, fraud detection, AI competitor benchmarking | USD card; limited free tier | Free (limited) / USD 99/month+ | Conditional — use free tier to vet influencers before paid campaigns |
| Upfluence | End-to-end influencer management, AI-matched discovery, campaign tracking | USD card; enterprise pricing | Enterprise — custom | Defer — not viable for EA budgets |

**EA note:** All three tools are USD-priced and designed for markets with large influencer databases. EA influencer databases are sparse in these platforms. For most EA clients, manual influencer discovery (Instagram search, TikTok discovery, personal network) combined with HypeAuditor's free tier for audience vetting is more practical and cost-effective than a paid subscription. See `08-influencer-marketing-strategy/SKILL.md` for manual EA influencer sourcing frameworks.

---

## Section 3 — Recommended Stacks by Budget Profile

### Budget Profile A — Starter (under UGX 500,000/month on tools)

Free tools only. Apply as the default starting point for all new clients.

| Function | Tool | Monthly Cost |
|---|---|---|
| Content creation | ChatGPT (free), Claude (free), Canva AI (free) | UGX 0 |
| SEO | RankMath (free WordPress plugin) | UGX 0 |
| Social media management | FeedHive (free), Meta Business Suite | UGX 0 |
| Email marketing | Mailchimp (free, up to 500 contacts) or Brevo (free, 300 emails/day) | UGX 0 |
| Automation | Zapier (free, 5 Zaps), Africa's Talking (pay-per-use) | UGX 30–60/SMS |
| Analytics | GA4, Meta Business Suite Insights | UGX 0 |
| Paid advertising | Meta Advantage+ (ad spend only) | Ad spend only |
| Influencer | HypeAuditor (free tier), manual discovery | UGX 0 |

**Total monthly platform cost: UGX 0 + ad spend + Africa's Talking usage**

Do not introduce paid tools until the client has used this stack consistently for at least one quarter and has identified a specific limitation.

---

### Budget Profile B — Growth (UGX 500,000–2,000,000/month on tools)

Build on Profile A. Add these paid upgrades when free tier limitations are confirmed.

| Addition | Tool | Approx. Monthly Cost (UGX) |
|---|---|---|
| Social scheduling upgrade | FeedHive Pro | ~UGX 70,000 |
| Email marketing upgrade | Brevo paid (up to 20,000 emails/month) | ~UGX 95,000 |
| Social analytics | Metricool (starter paid) | ~UGX 70,000 |
| Automation upgrade | Make Starter (10,000 operations/month) | ~UGX 35,000 |
| Text/NLP analysis | MonkeyLearn (free tier first; API as needed) | Free / usage-based |
| AI content tool | Copy.ai Starter or Claude Pro | ~UGX 75,000 |

**Approximate total: UGX 345,000–500,000/month + Profile A tools + ad spend**

---

### Budget Profile C — Scale (above UGX 2,000,000/month on tools)

Build on Profile B. Add these tools when the client has a dedicated marketing team and active programmes across all channels.

| Addition | Tool | Approx. Monthly Cost (UGX) |
|---|---|---|
| Enterprise social management | Hootsuite or Sprout Social | ~UGX 370,000–950,000 |
| SEO platform | SEMrush (Pro) or Ahrefs (Lite) | ~UGX 450,000–380,000 |
| Email automation | ActiveCampaign (Starter) | ~UGX 56,000 |
| Influencer vetting | HypeAuditor (paid) | ~UGX 380,000 |
| Social listening | Brandwatch (for large brands only) | USD 1,000+/month — confirm budget before recommending |

**Note:** Prices stated in UGX are approximate USD-to-UGX conversions at prevailing rates. Reconfirm at time of proposal. All USD-priced tools require a Ugandan or EA Visa/Mastercard with international payments enabled.

---

## Section 4 — Output Structure

Produce the deliverable in the following order:

1. **Current Stack Audit** — list every tool the client currently uses, its function, cost, and whether it is actively used / partially used / unused
2. **AI Tools Evaluation Tables** — one table per category (all eight categories; no gaps)
3. **Recommended Stack** — match to the client's budget profile (A, B, or C); state all costs in UGX
4. **Tools to Remove** — any current tools that fail the five-question framework, with brief rationale
5. **Implementation Roadmap** — introduce no more than 2 new tools per quarter; include estimated onboarding time per tool (2–4 hours)
6. **DPA Note** — flag every tool in the recommended stack that processes customer personal data; note that a Data Processing Agreement is required under the Uganda Data Protection and Privacy Act 2019
7. **Next Steps** — 3 specific, named actions the client should take in the next 30 days

---

## Quality Criteria

- All 8 tool categories are assessed with a reference table — no gaps in the evaluation
- EA accessibility is rated explicitly for every tool, not assumed; payment method viability is stated
- Budget profiles reflect real UGX costs, not USD assumptions carried over without conversion
- Recommended stack is specific to the client's stated budget profile, channels, and technical comfort level — not a generic list
- At least 3 free or freemium options are included in every budget profile
- Africa's Talking is included as the primary EA-native automation tool in every recommendation
- Output is a reference the client can act on immediately — no vague "explore options" or "consider using" language
- The five-question evaluation framework is applied to every tool, not just listed as a principle

---

## Related Skills

- `playbook-ai-automation-workflow/SKILL.md` — use for building automation sequences with the tools recommended here
- `ai-use-case-mapping/SKILL.md` — use before this audit to determine which marketing functions to prioritise for AI adoption
- `meta-tools-stack-evaluation/SKILL.md` — use when the client needs a broader martech stack evaluation beyond AI-specific tools
- `08-influencer-marketing-strategy/SKILL.md` — use for manual EA influencer sourcing when paid influencer tools are deferred
- `playbook-paid-social-advertising/SKILL.md` — use for paid advertising strategy; this skill covers tool selection only

---

## References

- Johnsen, M. (2024) *AI in Digital Marketing*. Mercury Learning — AI tool capability classifications and marketing automation frameworks
- Upadhyay, M. A. (2024) *Generative AI for Marketing*. Packt — generative AI application across content, SEO, analytics, and personalisation
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice* — RACE framework for tool selection against marketing objectives
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book* — ROI framework for tool investment decisions: (TLV − COCA) ÷ COCA
- Uganda Data Protection and Privacy Act 2019 — applies to all tools processing customer personal data

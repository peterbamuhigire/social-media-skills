# AI Tool Fit, Access, Cost and Governance

Merged from skills/meta-analytics-ops/meta-ai-tools-audit on 2026-09-29 at 7c60138; preservation map: [meta-ai-tools-audit.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/meta-ai-tools-audit.md)

## When to use this reference

Use it when the stack evaluation must cover AI marketing tools: auditing the AI tools a client already uses, or recommending an AI tool stack by function, calibrated to Uganda and East African budgets, payment infrastructure and team capacity. It maps every tool by function, rates EA accessibility explicitly and delivers a recommended stack for the client's budget profile. It draws on Johnsen (2024) and Upadhyay (2024).

- Client already has a shortlist of named AI tools for one problem and needs a scored go/no-go: use [ai-vendor-due-diligence.md](ai-vendor-due-diligence.md).
- Marketing functions to prioritise for AI adoption are not yet decided: run [`ai-use-case-mapping`](../../../ai-marketing/ai-use-case-mapping/SKILL.md) first.
- Non-AI martech (scheduling, design, CRM, project management): use the core tables in the parent `SKILL.md`.

## Inputs (all six required before any output)

1. **Client business name, industry and country/city**: for example "Nile Organics, food retail, Kampala".
2. **Primary marketing goal**: brand awareness, lead generation, email list growth, content output, and so on.
3. **Monthly tools budget range (UGX)**: Starter under UGX 500,000 / Growth UGX 500,000–2,000,000 / Scale above UGX 2,000,000.
4. **Current tools already in use**: every tool, free or paid, in the workflow.
5. **Team technical comfort level**: None (no prior software experience) / Basic (email and social apps) / Intermediate (uses several SaaS tools) / Advanced (API-comfortable, automation-literate).
6. **Primary channels**: Facebook, Instagram, WhatsApp, email, website/SEO, TikTok, LinkedIn, YouTube.

Do not generate any output until all six are collected.

## Decision rules: the five-question AI tool test

Apply to every tool before recommending it. If any critical question is answered No, do not recommend the tool. Include the test as a named section in every deliverable so the client can reuse it.

| # | Question | Pass condition |
|---|---|---|
| 1 | Does it address a specific, named marketing problem the client has today? | Never recommend an AI tool on novelty alone. |
| 2 | Is it accessible with EA payment methods? | USD credit/debit card (Visa/Mastercard issued in EA), Mobile Money (MTN, Airtel), or a free tier. Tools that accept only USD PayPal or a US billing address are inaccessible for most EA clients. |
| 3 | Is there a free or low-cost entry point the team can test? | Prioritise free tiers before paid subscriptions. |
| 4 | Will the team realistically use it? | Complexity matches the stated technical comfort level; advanced automation handed to non-technical teams goes unused. |
| 5 | Does it process customer personal data? | If yes, a Data Processing Agreement (DPA) is required under the Uganda Data Protection and Privacy Act 2019 before recommending. |

EA recommendation ratings used in every table:

- **Recommended**: accessible, affordable, strong EA fit.
- **Conditional**: accessible but USD-priced; viable only if budget is confirmed.
- **Defer**: enterprise pricing, inaccessible payment, or low EA market penetration.

## Tool evaluation tables by function

Produce one table per category in the deliverable; all eight categories, no gaps. Prices are undated figures carried from the source skill; reconfirm before any proposal.

### 1. Content creation

| Tool | AI capability | EA accessibility | Pricing tier | EA recommendation |
|---|---|---|---|---|
| ChatGPT (OpenAI) | Writing, brainstorming, first drafts, repurposing; GPT-4o via web | Free tier via web; paid via USD card | Free / ~USD 20/month | Recommended |
| Claude (Anthropic) | Long-form writing, strategy documents, nuanced analysis, structured outputs | Free tier via web; paid via USD card | Free / ~USD 20/month | Recommended |
| Gemini (Google) | Integrated with Google Workspace; writing, summarising, Docs/Slides assistance | Free via Google account; Workspace paid plans | Free / USD 12/month | Recommended |
| Jasper | Marketing templates, brand voice, campaign copy | USD card required; no free tier | USD 49/month+ | Defer: high cost for EA budgets |
| Copy.ai | Short-form copy, social captions, ad copy; workflow automation | Free tier (limited); paid via USD card | Free / USD 36/month | Conditional |
| Canva AI / Magic Write | Design-integrated AI copy, image generation, presentation drafts | Free tier; Canva Pro via USD card or mobile payment on some EA platforms | Free / USD 15/month | Recommended: free tier sufficient for most EA clients |

ChatGPT and Claude are the most widely used AI writing tools in Uganda and East Africa. Jasper's USD 49/month entry point is prohibitive for most EA SME budgets; use Copy.ai starter or the Claude free tier instead.

### 2. SEO and content optimisation

| Tool | AI capability | EA accessibility | Pricing tier | EA recommendation |
|---|---|---|---|---|
| Surfer SEO | Content briefs, SERP analysis, real-time content scoring | USD card required | USD 89/month+ | Defer: cost exceeds EA SEO ROI for most SMEs |
| SEMrush AI features | Keyword clustering, competitive gap analysis, content ideas | USD card; limited free tier | Free (limited) / USD 120/month | Conditional: only for clients with active SEO programmes |
| Ahrefs AI | Backlink analysis, keyword research, AI content-gap tools | USD card required | USD 99/month+ | Defer: enterprise cost |
| RankMath (WordPress) | On-page SEO scoring, AI title/meta suggestions, schema markup | Free WordPress plugin; Pro via USD card | Free / USD 59/year | Recommended: primary free SEO option for EA clients on WordPress |

RankMath is the default for EA clients on WordPress. Surfer SEO and SEMrush suit only clients with a dedicated SEO budget and an active content programme producing measurable organic traffic.

### 3. Social media management

| Tool | AI capability | EA accessibility | Pricing tier | EA recommendation |
|---|---|---|---|---|
| FeedHive | AI content suggestions, post recycling, performance prediction scores | USD card; free tier | Free / USD 19/month | Recommended: best value for EA budgets |
| Buffer | AI caption and post-idea assistant; scheduling | USD card; free tier (3 channels) | Free / USD 6/month | Recommended |
| Hootsuite | AI content assistant, sentiment analysis, bulk scheduling | USD card; no affordable tier | USD 99/month+ | Defer: enterprise only |
| Later | AI caption writer, visual planning, link-in-bio analytics | USD card; limited free tier | Free / USD 18/month | Conditional: best for Instagram-heavy clients |
| Metricool | Analytics, scheduling, AI hashtag suggestions | USD card; free tier | Free / USD 18/month | Recommended: strong analytics at low cost |

FeedHive and Metricool give the strongest value for EA budgets. Recommend Hootsuite only to agencies managing 10+ client accounts with confirmed budget.

### 4. Email marketing

| Tool | AI capability | EA accessibility | Pricing tier | EA recommendation |
|---|---|---|---|---|
| Mailchimp | AI subject-line optimiser, send-time optimisation, content suggestions | USD card; free tier (up to 500 contacts) | Free / USD 13/month | Recommended: viable free starting point |
| Brevo (formerly Sendinblue) | AI send-time optimisation, segmentation, SMS + email automation | USD card; free tier (300 emails/day) | Free / USD 25/month | Recommended: best free tier for high-volume senders |
| ActiveCampaign | Advanced AI segmentation, predictive sending, lead scoring | USD card; no free tier | USD 15/month+ | Conditional: for lists of 1,000+ contacts with active automation needs |
| ConvertKit | Simple automation, AI subject-line suggestions, creator-focused | USD card; free tier (up to 1,000 subscribers) | Free / USD 9/month | Conditional: content creators and solo consultants |

Brevo and Mailchimp free tiers are the starting points. Every paid tier needs a USD-capable Visa or Mastercard; confirm the client has one first.

### 5. Marketing automation

| Tool | AI capability | EA accessibility | Pricing tier | EA recommendation |
|---|---|---|---|---|
| Zapier | Connects 6,000+ apps; AI-assisted workflow builder; no-code | USD card; free tier (5 single-step Zaps) | Free / USD 19.99/month | Recommended: free tier for simple connections |
| Make (formerly Integromat) | Visual builder; more complex multi-step flows than Zapier | USD card; free tier (1,000 operations/month) | Free / USD 9/month | Recommended: better value than Zapier for complex workflows |
| Africa's Talking | SMS, WhatsApp, USSD and voice automation; EA-native API platform | Local EA payment; pay-per-use; UGX billing available | Pay-per-use (~UGX 30–60/SMS) | Recommended: primary EA automation tool; the only one here with local payment and EA infrastructure |
| ManyChat | Facebook, Instagram, WhatsApp chatbots; AI reply suggestions | USD card; free tier (up to 1,000 contacts) | Free / USD 15/month | Recommended: strong WhatsApp/Instagram chatbot option |

Africa's Talking must be included in every EA marketing automation recommendation. It supports UGX billing, bulk SMS, WhatsApp Business API and USSD, which no other tool listed replicates for the EA market. Build sequences with [`playbook-marketing-automation`](../../../playbooks/playbook-marketing-automation/SKILL.md).

### 6. Analytics and insights

| Tool | AI capability | EA accessibility | Pricing tier | EA recommendation |
|---|---|---|---|---|
| Google Analytics 4 | AI anomaly detection, predictive metrics, automated insights | Free; Google account | Free | Recommended: essential; zero cost |
| Meta Business Suite Insights | AI content performance summaries, audience insights | Free; Meta Business account | Free | Recommended: essential for all Facebook/Instagram clients |
| Brandwatch | Social listening, AI sentiment analysis, trend detection | USD card; enterprise sales process | USD 1,000+/month | Defer: large brands only; not viable for EA SMEs |
| MonkeyLearn | NLP text analysis, sentiment classification, API-based | USD card; free tier | Free / USD 299/month | Conditional: clients with high-volume text data |
| Sprout Social | AI social analytics, sentiment, competitive benchmarking | USD card; no free tier | USD 249/month+ | Defer: enterprise; rarely justified for EA budgets |

GA4 and Meta Business Suite Insights belong in every client's stack regardless of budget. Brandwatch and Sprout Social suit only large corporate or NGO clients with confirmed analytics budgets.

### 7. Paid advertising

| Tool | AI capability | EA accessibility | Pricing tier | EA recommendation |
|---|---|---|---|---|
| Meta Advantage+ | AI-automated targeting, creative optimisation, budget allocation | Meta Business account; UGX and USD card payment | Ad spend only; no platform fee | Recommended: accessible with UGX card payment |
| Google Performance Max | AI-optimised ads across Search, Display, YouTube, Gmail | Google Ads account; USD card | Ad spend only; no platform fee | Recommended: accessible with EA USD card |
| TikTok Smart+ | Automated TikTok campaign management; AI creative and targeting | TikTok Business account; USD card | Ad spend only; no platform fee | Recommended: for EA clients targeting under-35 urban audiences |

All three are accessible with a Ugandan or EA Visa/Mastercard. Minimum ad-spend thresholds apply; confirm with the client. This reference covers tool selection only; campaign strategy and creative testing belong to [`playbook-paid-social-advertising`](../../../playbooks/playbook-paid-social-advertising/SKILL.md).

### 8. Influencer marketing

| Tool | AI capability | EA accessibility | Pricing tier | EA recommendation |
|---|---|---|---|---|
| Modash | AI influencer discovery, audience analytics, performance tracking | USD card; free trial | USD 99/month+ | Conditional: only for structured influencer programmes |
| HypeAuditor | Audience authenticity scoring, fraud detection, competitor benchmarking | USD card; limited free tier | Free (limited) / USD 99/month+ | Conditional: use the free tier to vet influencers before paid campaigns |
| Upfluence | End-to-end influencer management, AI-matched discovery, tracking | USD card; enterprise pricing | Enterprise, custom | Defer: not viable for EA budgets |

All three are USD-priced and built for markets with large influencer databases; EA coverage in them is sparse. For most EA clients, manual discovery (Instagram search, TikTok discovery, personal network) plus HypeAuditor's free tier for vetting is more practical. Manual EA sourcing frameworks: [`08-influencer-marketing-strategy`](../../../pipeline/08-influencer-marketing-strategy/SKILL.md).

## Recommended AI stacks by budget profile

Approximate UGX figures are undated USD conversions carried from the source skill; reconfirm at proposal time. Every USD-priced tool needs a Ugandan or EA Visa/Mastercard with international payments enabled.

### Profile A: Starter (under UGX 500,000/month on tools)

Free tools only; the default starting point for every new client.

| Function | Tool | Monthly cost |
|---|---|---|
| Content creation | ChatGPT (free), Claude (free), Canva AI (free) | UGX 0 |
| SEO | RankMath (free WordPress plugin) | UGX 0 |
| Social media management | FeedHive (free), Meta Business Suite | UGX 0 |
| Email marketing | Mailchimp (free, up to 500 contacts) or Brevo (free, 300 emails/day) | UGX 0 |
| Automation | Zapier (free, 5 Zaps), Africa's Talking (pay-per-use) | UGX 30–60/SMS |
| Analytics | GA4, Meta Business Suite Insights | UGX 0 |
| Paid advertising | Meta Advantage+ | Ad spend only |
| Influencer | HypeAuditor (free tier), manual discovery | UGX 0 |

Total monthly platform cost: UGX 0 + ad spend + Africa's Talking usage. Introduce no paid tool until the client has used this stack consistently for at least one quarter and has named a specific limitation.

### Profile B: Growth (UGX 500,000–2,000,000/month on tools)

Build on Profile A; add paid upgrades only when free-tier limits are confirmed.

| Addition | Tool | Approx. monthly cost |
|---|---|---|
| Social scheduling upgrade | FeedHive Pro | ~UGX 70,000 |
| Email marketing upgrade | Brevo paid (up to 20,000 emails/month) | ~UGX 95,000 |
| Social analytics | Metricool (starter paid) | ~UGX 70,000 |
| Automation upgrade | Make Starter (10,000 operations/month) | ~UGX 35,000 |
| Text/NLP analysis | MonkeyLearn (free tier first; API as needed) | Free / usage-based |
| AI content tool | Copy.ai Starter or Claude Pro | ~UGX 75,000 |

Approximate total: UGX 345,000–500,000/month + Profile A tools + ad spend.

### Profile C: Scale (above UGX 2,000,000/month on tools)

Build on Profile B when the client has a dedicated marketing team and active programmes across all channels.

| Addition | Tool | Approx. monthly cost |
|---|---|---|
| Enterprise social management | Hootsuite or Sprout Social | ~UGX 370,000–950,000 |
| SEO platform | SEMrush (Pro) ~UGX 450,000 or Ahrefs (Lite) ~UGX 380,000 (source listed the range as "450,000–380,000") | ~UGX 380,000–450,000 |
| Email automation | ActiveCampaign (Starter) | ~UGX 56,000 |
| Influencer vetting | HypeAuditor (paid) | ~UGX 380,000 |
| Social listening | Brandwatch (large brands only) | USD 1,000+/month; confirm budget before recommending |

## Deliverable structure (in this order)

1. **Current stack audit**: every tool in use, its function, cost, and status (actively used / partially used / unused).
2. **AI tools evaluation tables**: one per category, all eight categories, no gaps.
3. **Recommended stack**: matched to budget profile A, B or C; all costs in UGX.
4. **Tools to remove**: current tools failing the five-question test, with brief rationale.
5. **Implementation roadmap**: no more than two new tools per quarter, with estimated onboarding time per tool (2–4 hours).
6. **DPA note**: every recommended tool that processes customer personal data, noting that a Data Processing Agreement is required under the Uganda Data Protection and Privacy Act 2019.
7. **Next steps**: three specific, named actions for the next 30 days.

## Acceptance checklist

- [ ] All eight categories assessed with a reference table; no gaps.
- [ ] EA accessibility rated explicitly for every tool, with payment-method viability stated, never assumed.
- [ ] Budget profiles use real UGX costs, not unconverted USD figures.
- [ ] Recommended stack is specific to the client's budget profile, channels and technical comfort level, not a generic list.
- [ ] At least three free or freemium options in every budget profile.
- [ ] Africa's Talking included as the primary EA-native automation tool in every recommendation.
- [ ] Output is actionable immediately; no vague "explore options" or "consider using" language.
- [ ] The five-question test applied to every tool, not just listed as a principle.

## Related skills

- [`playbook-marketing-automation`](../../../playbooks/playbook-marketing-automation/SKILL.md): building automation sequences with the recommended tools.
- [`ai-use-case-mapping`](../../../ai-marketing/ai-use-case-mapping/SKILL.md): before this audit, to prioritise marketing functions for AI adoption.
- [`08-influencer-marketing-strategy`](../../../pipeline/08-influencer-marketing-strategy/SKILL.md): manual EA influencer sourcing when paid influencer tools are deferred.
- [`playbook-paid-social-advertising`](../../../playbooks/playbook-paid-social-advertising/SKILL.md): paid advertising strategy; this reference covers tool selection only.
- [`anti-ai-slop`](../../../ai-marketing/anti-ai-slop/SKILL.md) during production and [`ai-slop-audit`](../../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## Sources

- Johnsen, M. (2024) *AI in Digital Marketing*. Mercury Learning. AI tool capability classifications and marketing automation frameworks.
- Upadhyay, M. A. (2024) *Generative AI for Marketing*. Packt. Generative AI across content, SEO, analytics and personalisation.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson. RACE framework for tool selection against marketing objectives.
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley. ROI framework for tool investment decisions: (TLV − COCA) ÷ COCA.
- Uganda Data Protection and Privacy Act 2019: applies to every tool processing customer personal data.

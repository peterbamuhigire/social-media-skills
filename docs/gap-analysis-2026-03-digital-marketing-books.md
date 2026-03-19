# Gap Analysis — Digital Marketing Books (March 2026)

**Date:** 2026-03-19
**Books analysed:** 11
**Method:** Parallel thematic extraction across 4 groups; cross-referenced against 3 prior gap analyses and the 120+ skill suite

---

## Books Analysed

| # | Title | Author | Year | Group |
|---|---|---|---|---|
| 1 | *Digital Marketing: Foundations and Strategy* (5th ed.) | Zahay, Labrecque, Reavey & Roberts | 2024 | G1 — Foundations |
| 2 | *Digital Marketing* | Wind & Mahajan | 2001 | G1 — Foundations |
| 3 | *The SAGE Handbook of Digital Marketing* | Hanlon & Tuten (Eds.) | 2022 | G1 — Foundations |
| 4 | *Advances in Digital Marketing in the Era of Artificial Intelligence* | Ltifi (Ed.) | 2024 | G2 — AI |
| 5 | *AI in Digital Marketing* | Johnsen | 2024 | G2 — AI |
| 6 | *Web Analytics Blueprint* | Raaz | c.2023 | G3 — Analytics |
| 7 | *High-Velocity Digital Marketing* | Kahan | 2022 | G3 — Analytics |
| 8 | *Get Scrappy* | Westergaard | 2016 | G4 — Tactical |
| 9 | *Digital Marketing in 2023: A Quickstart Guide* | Pidsley | 2023 | G4 — Tactical |
| 10 | *The Digital Marketing Handbook* | Bly | 2018 | G4 — Tactical |
| 11 | *Ethical Marketing and Consumer Trust in Digital and Sustainable Markets* | Rageh (Ed.) | 2026 | G4 — Tactical |

---

## The Golden Rule Audit

The agency's foundational quality standard states that every output must look, feel, and sound as if it was produced by the most skilled human creatives. The `ai-content-humaniser` skill is the enforcement layer. The following content-generating skills currently contain no explicit human authenticity gate, no mention of voice craft, no cultural nuance test, and no equivalent of the "Proof of Human" standard. These are strengthening priorities regardless of book-specific recommendations.

- **`caption-writer`** — generates client-facing copy with no quality gate, no uncanny valley check, no EA cultural register test
- **`blog-writer`** — generates long-form text; no human voice checklist, no AI signature detection step
- **`email-copywriter`** — generates high-stakes conversion copy; no brand voice calibration step, no tone-register check per email type
- **`content-writing`** — general content standards skill but does not specify a humanisation editing pass
- **`content-whitepaper-ebook`** — B2B long-form deliverables; no quality gate to detect mechanical uniformity (the primary detectable AI signature per Johnsen)
- **`content-ideas`** — AI-assisted ideation that may generate ideas indistinguishable from generic AI output
- **`hashtag-strategy`** — low copy risk but no cultural relevance check for EA markets
- **`playbook-ai-content-workflow`** — by definition the most important: existing version lacks an explicit uncanny valley calibration section (to be addressed under existing skill strengthening below)

All of the above should, at minimum, include a cross-reference to `ai-content-humaniser` and a note that all AI-assisted copy must pass the human authenticity gate before client delivery.

---

## New Skills to Create

Priority definitions:
- **HIGH** = fills a major service delivery gap; clients will ask for this; builds directly on book frameworks
- **MEDIUM** = meaningful extension; builds on existing skills; not urgent
- **LOW** = valuable but niche or with market caveats for East Africa

### HIGH Priority

| Slug | Purpose | Source |
|---|---|---|
| `playbook-lead-magnet-system` | Design, placement, and optimisation of lead magnets for building owned email and WhatsApp subscriber lists. Covers Bly's specificity formula (promise a specific outcome, high perceived value, instant delivery, unique expertise), six lead magnet formats (report, checklist, video, quiz, tool, webinar), placement sequence (hero → sidebar → post-content → exit intent), double opt-in setup, and list hygiene. For EA: WhatsApp opt-in mechanics as a direct substitute for email lead capture. | Bly (2018) |
| `playbook-email-funnel` | Full email marketing operations — distinct from `email-copywriter` which covers copy only. Covers the 90/90 rule (90% of buyers buy within 90 days of joining a list), six email KPIs (bounce rate, opt-out rate, open rate, CTR, conversion rate, gross revenue), the content-to-sales ratio (minimum 50% pure content emails), CTA placement rules (minimum twice per email), subject line A/B testing, mobile email design rules (14px body, 22px headlines, single-column, 44px CTA buttons), and giveaway list-building tactics. | Bly (2018) |
| `playbook-marketing-automation` | Design of automated lead nurturing sequences triggered by actions — form submission, content download, WhatsApp opt-in, webinar attendance. Covers trigger event mapping, sequence architecture (trigger → welcome → nurture → conversion offer), message timing, personalisation tokens, and conversion offer design. Addresses the EA-specific reality that WhatsApp Business replaces email drip sequences for many clients. Distinct from `playbook-ai-automation-workflow` (which covers AI tool automation) and `email-copywriter` (which covers copy only). | Pidsley (2023); Zahay et al. (2024); Hanlon & Tuten (2022) |
| `playbook-whatsapp-business` | WhatsApp Business setup, chatbot conversation flows, broadcast lists, catalogue configuration, away messages, greeting messages, quick replies, and customer service protocols — specific to the WhatsApp-dominant EA market. Major commercial gap: WhatsApp is the #1 platform by penetration in Uganda/EA (90%+ smartphone users) but no skill currently covers how to use WhatsApp Business as a structured marketing and sales channel beyond the basic `platform-whatsapp` overview. | Pidsley (2023) |
| `meta-revenue-planning` | Bottom-up, data-driven marketing plan: reverse-engineering a revenue target through funnel CVRs to quarterly inquiry, lead, and opportunity volumes per channel. Covers: reading historical CVR data, calculating the inquiry-to-lead, lead-to-opportunity, and opportunity-to-deal ratios, assigning targets by channel (marketing vs. sales vs. partner/channel), and building a performance dashboard that tracks actuals vs. plan. Kahan's framework is the backbone — this is "the connective tissue between strategy, content, and ROI" that currently has no home in the suite. | Kahan (2022) |
| `framework-digital-transparency` | Operational framework for building perceived digital transparency across channels. Covers Rageh's three-dimensional transparency model (Clarity: clear information about products, prices, policies; Openness: interactive feedback channels and permission-based data; Objectivity: displaying negative alongside positive reviews). Implementation tactics per channel (website, social, email, WhatsApp). Empirical chain: transparency → trust (β=0.730) → commitment (β=0.525) → online engagement (β=0.413). Especially relevant in EA where first-time digital commerce buyers have higher distrust than mature markets. Positions the consultancy as a trust architect. | Rageh (Ed.) (2026) |
| `meta-lead-scoring` | Design and calibration of a lead-scoring model for B2B and B2C clients. Covers explicit criteria (job title, company size, industry, revenue) and implicit behaviour weighting (content downloads, website visits, webinar attendance, form completions, email opens). Score threshold setting, calibration loop with sales team input, and iteration process based on CVR data. Includes BANT qualification framework (Budget, Authority, Need, Time frame) for the Evaluate stage. Directly applicable to EA B2B consultancy clients managing CRM and sales pipelines. | Kahan (2022); Zahay et al. (2024) |

### MEDIUM Priority

| Slug | Purpose | Source |
|---|---|---|
| `meta-cohort-analysis` | How to build time-based and behaviour-based user cohorts in GA4; track retention, lifetime value, and conversion rate by cohort over time; identify which acquisition channels produce the most durable customers (high LTV) versus single-transaction buyers. Presents cohort data to clients in a format that demonstrates campaign durability, not just campaign reach. Particularly relevant for EA clients in subscription, FMCG, and repeat-purchase categories. | Raaz (c.2023) |
| `meta-dashboard-design` | Standards for client-facing dashboard design: chart type selection by data type (line charts for trends, bar for comparisons, pie for proportions, heatmaps for user behaviour); mobile-responsive design (critical in EA where clients access dashboards on smartphones); storytelling structure (insight → context → recommendation, not raw metric tables); tool selection (Google Looker Studio recommended — free, Google-integrated, mobile-accessible within EA bandwidth constraints); and accessibility guidelines. | Raaz (c.2023) |
| `meta-sales-marketing-alignment` | Shared KPI ownership framework for marketing and sales teams: defines which metrics marketing owns (visitor-to-lead CVR, leads generated, cost per lead, MQL volume, marketing-sourced pipeline, CAC, marketing ROI), which sales owns (total revenue, pipeline coverage, closing ratio, average sales cycle, average revenue per account), and which both own (CLV). Establishes CRM as the single source of truth, SLAs for lead follow-up speed (Kahan: leads go cold within 24 hours), and monthly joint review meeting structure. Addresses attribution disputes with data, not politics. | Kahan (2022) |
| `strategy-experiential-marketing` | Experiential marketing as a strategic discipline for product launches, events, activations, and pop-ups. Covers the SAGE Handbook's ExM framework (Schmitt 1999): four distinguishing features of experiential marketing vs. traditional, the Experience Economy (Pine & Gilmore) premium-pricing rationale, the ExM Scorecard for design and evaluation, and digital/hybrid ExM (virtual events, AR trials, interactive storytelling). Applies to EA clients running product launches, brand activations, trade shows, and community events — contexts where social media alone cannot generate the emotional brand connection that ExM creates. | Hanlon & Tuten (2022) |
| `strategy-ewom-reviews` | Systematic management of electronic word-of-mouth as a strategic marketing asset. Distinct from `playbook-reputation-management` (which focuses on damage control) — this skill is about designing, stimulating, and amplifying positive eWOM. Covers the SAGE Handbook's GST framework (Give, Seek, Transmit eWOM behaviours), activation tactics (making review requests at peak satisfaction moments, identifying eWOM transmitters who differ from top reviewers), and the objectivity principle: displaying negative alongside positive reviews increases trust more than curating only positives. | Hanlon & Tuten (2022) |
| `strategy-multigenerational-digital` | Strategy for clients with multigenerational audiences. Covers Rageh's Generational Digital Trust Spectrum: Generation Z (authenticity-first, algorithmic transparency, 73% expect brands to take positions on social issues), Millennials (control over data, co-creation preference), Generation X (security, reliability, traditional authority markers), Baby Boomers (institutional credibility, personal service, conventional business ethics). Channel allocation, messaging calibration, and influencer type selection by generational cohort. Growing need in EA as the middle class diversifies across age bands. | Rageh (Ed.) (2026) |
| `meta-analytics-privacy` | Privacy-by-design analytics setup for clients: cookie consent banners and frameworks (appropriate for Uganda's Data Protection and Privacy Act 2019, Kenya's Data Protection Act 2019), GA4 data retention settings, IP anonymisation, data minimisation rationale documentation, and consent-based tracking configurations. For EA clients with international e-commerce audiences, addresses GDPR and CCPA implications. Covers the regulatory landscape concisely without replacing legal counsel. | Raaz (c.2023); Hanlon & Tuten (2022) |
| `meta-social-proof-system` | Systematic collection, organisation, and deployment of social proof across digital touchpoints. Covers Bly's six-source taxonomy (customers/testimonials, experts/endorsements, celebrities/influencers, crowds/large-numbers, friends/peer recommendations, certifications/third-party validation). Testimonial collection scripts, case study formats, review generation mechanics, placement strategy (landing pages, email, proposals, sales pages), and the key rule: volume of proof from multiple sources outperforms a single strong testimonial. | Bly (2018) |
| `ai-influencer-strategy` | AI-powered influencer marketing: using AI tools to identify and vet influencers, detect fraudulent engagement patterns (irregular follower growth, purchased likes via pattern analysis), and choose between human and virtual/CGI influencers. Covers Ltifi's Parasocial Interaction Scale for Virtual Influencers (admiration, identification, uncanny valley rejection, sarcasm), the strategic trade-off between virtual influencers (full message control, no scandal risk) and human influencers (authenticity signals, parasocial trust). Includes the audit matrix: brand risk tolerance vs. control requirements. Note: this skill addresses AI-assisted strategy and vetting, not influencer contracts or payments (out of scope per CLAUDE.md). | Ltifi (Ed.) (2024) |
| `playbook-question-engine` | Systematic process for mining customer questions — from frontline staff, social listening, search data, FAQ logs, and sales call notes — and converting them into a content pipeline of blog posts, social posts, video scripts, and FAQs. Based on Westergaard's interpretation of Marcus Sheridan's River Pools case study: answering what customers are already asking dominates search and builds trust without ad spend. High relevance for EA businesses where customer education is the primary trust-building mechanism. | Westergaard (2016) |

### LOW Priority

| Slug | Purpose | Source |
|---|---|---|
| `strategy-demand-generation` | B2B demand generation as a distinct discipline. Covers Zahay's seven-step B2B demand generation process: Content Creation → Lead Generation → Prospect Identification → Lead Nurturing → Lead Scoring/Qualification → MQL → Sales Handover. The statistic that 85% of B2B purchase decisions are made before a buyer contacts a salesperson underpins the strategic logic. Relevant for formal-sector B2B clients in Uganda/EA (banks, NGOs, telecoms, professional services). Lower priority because `meta-lead-scoring` and `meta-revenue-planning` cover the most actionable sub-components. | Zahay et al. (2024) |
| `strategy-scenario-planning` | Scenario planning as a strategic tool for digital marketing under high uncertainty. Covers Wind & Mahajan / Clemons & Bradley's four-step process: surface key uncertainties, rank by strategic importance, combine extremes into concrete scenarios, build plausible narrative stories. Particularly relevant in East African markets where platform adoption, regulatory environments (data protection frameworks, mobile money regulation), and competitive dynamics are rapidly shifting. Lower priority because most EA clients need execution tools more urgently than strategic planning methodologies. | Wind & Mahajan (2001) |
| `meta-abm-framework` | Account-Based Marketing measurement framework for consultancies working with large B2B clients targeting specific named accounts. Covers Kahan's ABM requirements: intent data from IP-address tracking for account selection, persona-based tailored messaging, strict sales-marketing alignment, and long-horizon metrics (account engagement score, pipeline coverage per targeted account, deals closed vs. accounts targeted over a 6+ month window). Lower priority because ABM is largely limited to enterprise clients; most EA clients are SMEs. | Kahan (2022) |

---

## Existing Skills to Strengthen

### 1. `ai-content-humaniser` — HIGHEST PRIORITY

This is the enforcement layer for the Golden Rule. Both G2 books identify specific additions that directly protect the quality standard.

- **Add an Uncanny Valley Calibration Checklist** (source: Ltifi, Ch.13, pp.208–216): A named section with a checklist to detect whether AI output falls in the uncanny zone — too structurally perfect, lacks idiosyncrasy, no natural hesitation or colloquialism, suspiciously balanced phrasing throughout. Instruct editors to deliberately introduce controlled imperfection markers: a conversational aside, a rhetorical question, an Africa-specific cultural reference, a sentence fragment used for emphasis. The goal is to push content convincingly past the uncanny threshold, not merely past a grammar check.
- **Add the "AI as Creative Partner, not Creator" opening principle** (source: Johnsen, Ch.9, pp.163–165): Reinforce as the foundational editorial philosophy — AI drafts are raw material, never finished work. This mirrors the Golden Rule exactly and gives editors the conceptual authority to rewrite freely rather than polish lightly.
- **Add a Consistency Red Flag check** (source: Johnsen, Ch.9, p.162): AI achieves mechanical consistency but loses the natural micro-variation that signals human authorship. Add to the Human Voice Checklist: "Does this content have the natural variation in sentence length, register, and vocabulary that characterises human writing, or does it have AI's telltale mechanical uniformity?"
- **Add Micro-Moment Tone-Matching guidance** (source: Ltifi, Ch.1, pp.16–17): AI copy used at pivotal customer journey moments (cart abandonment, post-browse pause, comparison-shopping moment) must match the emotional register of that moment — urgency without pressure, reassurance without sycophancy. Generic AI output fails at these moments because it cannot detect emotional context. Human editors must impose the correct register.
- **Add a Sentiment-Register Alignment step** (source: Ltifi, Ch.1, p.15; Ch.8, pp.141–143): When editing AI drafts, run a quick sentiment check: does the tone of the copy match the sentiment data about the audience at this moment? If social listening shows audience anxiety or frustration, check the AI draft for inappropriate positivity or enthusiasm before delivery.
- **Add a Scalability Quality Gate** (source: Johnsen, Ch.9, p.162): When content is produced at AI-generated scale, quality review becomes the bottleneck. Add guidance on volume limits: assign word-count or post-count ceilings to what a single editor can review per session without quality degradation. Quality gates must scale with volume.
- **Add Translation and Localisation Quality Flag** (source: Johnsen, Ch.9, p.162): For translated AI content (including Luganda, Swahili, or Amharic adaptations in EA markets), verify cultural idiom accuracy, not just linguistic accuracy. A linguistically correct translation may contain examples or idioms that are foreign to the target culture.

### 2. `06-digital-marketing-strategy`

- **Add P.O.S.T. Methodology as a pre-strategy checklist** (source: Zahay et al., 2024, Ch.9, pp.230–233): People (understand the audience and their social media behaviours first) → Objectives (set business-aligned goals) → Strategy (develop the approach) → Technology (only then select platforms). This prevents platform-first thinking.
- **Add the 5Cs Social Media Motivation Framework** (source: Zahay et al., 2024, Ch.9, pp.233–239): Consume, Control, Connect, Compete, Create — use to diagnose what the target audience is primarily doing on each platform, which determines appropriate content strategy per channel.
- **Add the Digital Marketing Lifecycle section** (source: Zahay et al., 2024, Ch.1, pp.5–7): Frame all digital channel decisions against the four lifecycle stages — Acquisition, Conversion, Retention, Value Growth — and specify which tools serve which stage. Prevents clients treating all channels as acquisition tools.
- **Add the Scrappy Budget Prioritisation framework** (source: Westergaard, 2016): For EA SME clients with constrained budgets, add Westergaard's Brains Before Budget decision logic — rank channel investments by strategic leverage (which channel most efficiently achieves the defined objective?) not by budget availability. Include the Digital Compass methodology: tie every channel choice to a specific business destination.
- **Add the Hub-and-Spoke vs Central Site architecture decision** (source: Bly, 2018): Before writing a digital strategy, the choice between one authoritative central domain vs. multiple niche microsites has major implications for SEO, content investment, and conversion architecture. Add as a decision point in the strategy process.
- **Add the 90/90 Rule as a nurture design principle** (source: Bly, 2018): 90% of online subscribers who purchase do so within 90 days of joining a list. Digital strategy should specify front-loaded nurture intensity in the first 90 days of any new subscriber relationship, not a flat ongoing cadence.
- **Add Transparency as a Strategic Channel Choice** (source: Rageh, 2026): Strategy should include explicit transparency practices per digital channel — what data is collected, how it is used, and how the brand communicates this. Increasingly important as African data protection frameworks develop (Uganda DPPA 2019, Kenya DPA 2019).
- **Add platform review cadence** (source: Pidsley, 2023): Include a standing note that platform channel mix must be reviewed annually — platforms continue to emerge and decline, and the EA market adoption curve differs from global trends.

### 3. `meta-roi-framework`

- **Add the CAC Cap Rule** (source: Kahan, 2022, p.133): Customer Acquisition Cost must not exceed 25% of average Customer Lifetime Value. Provide this as a concrete budget governance ceiling for presentations to clients and boards. Formula: CAC ≤ (CLV × 0.25).
- **Add Bottom-Up Revenue Modelling** (source: Kahan, 2022): Supplement the top-down (TLV − COCA) ÷ COCA formula with a bottom-up model that works backward from a revenue target through CVR rates to required inquiry volume, making ROI projections more defensible in client budget negotiations.
- **Add Pipeline Stage Weighting for quarterly forecasting** (source: Kahan, 2022): Five-stage pipeline model — Open Opportunity (10%), Active Project (30%), Shortlist (60%), Forecast (85%), Close Win (100%) — as a standard forecasting tool alongside the core ROI formula.
- **Add Deal Velocity as an ROI component** (source: Kahan, 2022): Faster conversion reduces the time-cost of capital and increases revenue per quarter at the same spend. Express velocity in days (inquiry-to-lead velocity, lead-to-opportunity velocity, opportunity-to-deal velocity, end-to-end deal velocity) and incorporate into ROI narrative for clients.
- **Add CLV Modelling by acquisition cohort** (source: Raaz, c.2023; Zahay et al., 2024): Replace single-average CLV with cohort-based LTV calculation, giving a more accurate ROI result per channel and campaign. Note Zahay's benchmark: average repeat customer spends 67% more in months 31–36 than in months 1–6 — use as justification for retention investment.
- **Add Predictive Churn Modelling as an ROI input** (source: Raaz, c.2023): Flag customers with high churn probability before they leave; calculate the saved revenue as a measurable ROI component in the framework.

### 4. `meta-reporting`

- **Add Data Storytelling Structure** (source: Raaz, c.2023): Mandate that every report section follows the insight → context → recommendation structure, not raw metric tables. This makes reports more persuasive for clients and less dependent on the client's own data literacy.
- **Add Dashboard Design Standards** (source: Raaz, c.2023): Specify which chart type to use for which metric — trends: line chart; comparisons: bar chart; proportions: pie or donut; user behaviour: heatmap. Apply to all client-facing reporting.
- **Add a Real-Time Monitoring Tier** (source: Raaz, c.2023): Add a "live dashboard" layer above the weekly reporting cadence for clients who need same-day campaign performance visibility. Specify which metrics justify real-time vs. weekly vs. monthly reporting.
- **Add Mobile-Responsive Report Design** (source: Raaz, c.2023): All client dashboards must be viewable and usable on a smartphone — critical in Uganda/EA where clients access reports primarily on mobile. Google Looker Studio recommended for EA: free, Google-integrated, mobile-accessible.
- **Add Funnel CVR Benchmarks Table** (source: Kahan, 2022): Add benchmark CVRs at each funnel stage as a reference for monthly and quarterly reports: visitor-to-lead >5%, inquiry-to-lead ~3%, lead-to-opportunity ~25%, opportunity-to-deal ~40%. This allows clients to immediately see whether their funnel is poor, acceptable, or excellent at each stage.
- **Add Revenue-Sourced Attribution by First Touch** (source: Kahan, 2022): Add a "revenue sourced by channel (first-touch)" table to quarterly reports, distinguishing marketing-sourced from sales-sourced and channel-sourced revenue. Prevents sales from absorbing credit for marketing-generated opportunities.
- **Add a Data Quality Audit Cadence** (source: Raaz, c.2023): Build a monthly data integrity check (spam filters, bot exclusions, tracking validation, sampling rate review) into the reporting workflow as a standing quality gate.
- **Add Lead Quality Distribution Report** (source: Kahan, 2022): Add a "lead score distribution" chart to monthly reports — what percentage of leads came in at high, medium, and low scores — as a leading indicator of campaign quality, not just campaign volume.

### 5. `framework-community-trust`

- **Add Three-Dimensional Transparency Model** (source: Rageh, 2026, Ch.6): Significant addition to the "Know" and "Trust" stages of the Like-Know-Trust framework. Clarity (clear, complete, easy-to-understand information), Openness (interactive feedback channels, permission-based data collection), and Objectivity (presenting negative information alongside positive) are the three operationalised dimensions of what trust-building actually looks like at the platform level.
- **Add Commitment as the Terminal Engagement Driver** (source: Rageh, 2026, Ch.6, β=0.413): The empirical finding that commitment — not trust or satisfaction alone — is the strongest driver of online engagement (β=0.413 vs. trust β=0.730 path to commitment) should shift the framework's goal from trust acquisition to commitment-building. Add this as the final stage beyond "Trust."
- **Add Four Types of Social Influencers grid** (source: Westergaard, 2016): Connected Catalysts (broad reach, low action probability), Passionate Publishers (medium reach, high content output), Everyday Advocates (narrow reach, high action probability), Altruistic Activators (narrow reach, maximum loyalty). Most community strategies over-invest in Catalysts and under-invest in Activators — the Fan Elevation System corrects this.
- **Add Generational Trust Differences** (source: Rageh, 2026, Ch.2): Community trust strategies must be calibrated by generational audience, not applied uniformly. Gen Z demands brand activism (73% expect position-taking on social issues); Boomers require institutional credibility markers. Add as an audience segmentation lens within the framework.

### 6. `policy-ai-content-ethics`

- **Add Algorithmic Bias in Personalisation Systems** (source: Ltifi, 2024, Ch.2 and Ch.4): AI personalisation algorithms can inadvertently reinforce stereotypes — showing certain product types only to certain demographic segments, creating discriminatory feedback loops. Add a requirement to audit any AI personalisation tool for demographic fairness before deployment.
- **Add Explicit Non-Discrimination Clause** (source: Ltifi, 2024, Ch.1 and Ch.4): AI-generated advertising targeting must not use protected characteristics (gender, ethnicity, religion, age) as primary targeting variables in ways that constitute discrimination. Cite GDPR Article 22 and Uganda's DPPA 2019.
- **Add Explainability Obligation** (source: Johnsen, Ch.28, pp.515–517): When AI drives a significant strategic recommendation to a client, the agency has an obligation to explain the AI's reasoning in plain terms — not just present the output. This applies especially to audience targeting decisions, content strategy pivots, and budget allocation recommendations.
- **Add Continuous Monitoring as an Ethical Obligation** (source: Johnsen, Ch.28, p.517): Ethical AI deployment is not a one-time review. Add a requirement for quarterly bias audits and model drift reviews as standard practice.
- **Add East African Regulatory Alignment note** (source: Johnsen, Ch.28, p.518): For clients operating across multiple EA countries, AI regulations differ — Uganda DPPA 2019, Kenya DPA 2019, Tanzania's Electronic and Postal Communications Act vary in scope and enforcement. Add a flag to check national regulatory context before deploying AI personalisation systems.
- **Add Data Minimisation Principle** (source: Ltifi, 2024, Ch.2, p.34): AI personalisation systems should collect only the minimum data necessary for the task. Require clients to document their data minimisation rationale before implementing any AI personalisation.

### 7. `owned-media-strategy`

- **Add Lead Magnet System as an Owned Asset** (source: Bly, 2018): Expand the skill to cover how email and WhatsApp subscriber lists are built from social media traffic — the mechanisms of lead magnets, opt-in pages, giveaways, and list swaps between non-competing complementary businesses. This converts the strategy from theory (own your audience) to practice (here is how to build your list from zero).
- **Add Double Opt-In and List Hygiene protocols** (source: Bly, 2018): Add mandatory double opt-in requirement, with hard bounce removal and re-engagement campaign protocols before removing inactives. List hygiene is the operational maintenance of the owned asset.

### 8. `07-email-marketing-strategy`

- **Add the 90/90 Rule as a sequencing principle** (source: Bly, 2018): The first 90 days of a new subscriber relationship must be front-loaded with high-frequency, high-value nurture content — this is when the buying window is open. Email strategy must reflect this urgency, not assume a flat ongoing cadence.
- **Add Content-to-Sales Ratio as a list health standard** (source: Bly, 2018): Mandate minimum 50% pure content emails in any email programme. If more than half of sends are promotional, opt-out rates rise and list health deteriorates.
- **Add Send Time Optimisation as a named deliverable** (source: Johnsen, 2024, Ch.1 and Ch.17): AI-driven per-subscriber optimal send time (not a single blast time for the whole list) produces measurable uplift in open and conversion rates. Name this as a distinct deliverable within email marketing strategy.
- **Add Six Email KPIs** (source: Bly, 2018): Bounce rate (target under 1%), opt-out rate (target under 0.1% per send), open rate (typically 10–15%), CTR (1–5%), conversion rate, gross revenues. Add the CTR × conversion rate multiplier insight: optimising both together produces compounding revenue gains.

### 9. `03-audience-personas`

- **Add Technology Acceptance Model (TAM) as a research framework** (source: Hanlon & Tuten, 2022, Ch.7, pp.100–116): TAM's two adoption variables — Perceived Usefulness and Perceived Ease of Use — are highly applicable in EA where technology adoption barriers (digital literacy, connectivity cost, trust in digital transactions) are significant. Use TAM to diagnose which digital services and platforms a persona is likely to adopt and why, rather than assuming adoption based on demographics alone.
- **Add Generational Digital Trust Spectrum** (source: Rageh, 2026, Ch.2): Where personas span multiple generations (common for EA clients targeting urban professionals and older family decision-makers simultaneously), add a generational trust calibration layer to each persona — what does this cohort need to see to trust a brand digitally?

### 10. `biz-dev-proposal` and `biz-dev-credentials`

- **Add Kahan's Marketing Agency Scorecard dimensions** (source: Kahan, 2022): Kahan's 26-point scorecard evaluates agencies across six dimensions: digital demand generation expertise, knowledge of client's business, campaign planning for all audiences, campaign planning for all prospect touchpoints, provable revenue contribution, and agency integrity. Adapt this as a self-assessment that the consultancy uses to demonstrate its HVDM capability in proposals and credentials — essentially, "here is how we score ourselves, and here is the evidence."
- **Add Social Proof Taxonomy to credentials structure** (source: Bly, 2018): Proposals should incorporate all six social proof sources — client testimonials with photos, expert endorsements, crowd proof (number of clients served), peer recommendations, and certifications. Multiple sources of proof outperform a single strong testimonial.
- **Add the Free Diagnostic Offer** (source: Bly, 2018): Including a lead magnet in a proposal — free social media audit, free campaign diagnostic, free content gap analysis — reduces the commitment threshold and increases proposal conversion rate.

### 11. `meta-metrics-framework`

- **Add Velocity as a Fourth Measurement Dimension** (source: Kahan, 2022): Current skills measure volume (how many), rate (what percentage), and value (what revenue). Add velocity (how fast) as the fourth dimension, with these specific metrics: inquiry-to-lead velocity (days), lead-to-opportunity velocity (days), opportunity-to-deal velocity (days), and end-to-end deal velocity (days). Faster conversion at the same spend = higher revenue per quarter.
- **Add Funnel CVR Benchmarks and Diagnostic Decision Tree** (source: Kahan, 2022): Benchmark CVRs: visitor-to-lead >5%, inquiry-to-lead ~3%, lead-to-opportunity ~25%, opportunity-to-deal ~40%. Include a diagnostic decision tree: if inquiry-to-lead CVR is low → check content quality and audience targeting; if lead-to-opportunity CVR is low → check lead scoring threshold and sales response time SLA.

---

## Cross-Reference: Already Planned in Prior Gap Analyses

The following concepts appear in the new digital marketing extractions but were already proposed or built in prior gap analyses. They are confirmed priorities but should not be rebuilt — they should be tracked for build progress.

| Concept / Skill | Prior Gap Analysis | Status |
|---|---|---|
| `playbook-ai-content-workflow` | gap-analysis-2026-03.md (High priority); gap-analysis-2026-03-ai-books.md (AI-E batch) | Planned; `ai-content-humaniser` built |
| `social-commerce-strategy` | gap-analysis-2026-03.md (Medium priority) | Planned; cross-referenced with Hanlon & Tuten eWOM/community chapters — confirmed priority |
| `playbook-community-management` | gap-analysis-2026-03.md (existing skill to expand) | In existing suite; SAGE Handbook's 9-factor community model should be added to the skill |
| `meta-utm-tracking` | gap-analysis-2026-03.md (High priority) | Planned; Zahay UTM guidance (Ch.9, p.249) confirms this is a foundational gap |
| `playbook-sms-whatsapp-marketing` | gap-analysis-2026-03.md (High priority) | Planned; `playbook-whatsapp-business` proposed in this analysis is distinct (WhatsApp Business-specific) and should complement rather than duplicate |
| `playbook-chatbot-strategy` | gap-analysis-2026-03.md (High priority) | Planned; Pidsley confirms EA relevance of WhatsApp chatbot flows |
| Attribution modelling (multi-touch) | gap-analysis-2026-03.md (expand `meta-roi-framework`) | Partially confirmed; SAGE Handbook six attribution models should be added to `meta-roi-framework` when updated |
| Marketing automation architecture | gap-analysis-2026-03-ai-books.md (Tier 1 AI workflow skills) | Partially addressed by `playbook-ai-automation-workflow`; `playbook-marketing-automation` proposed here is the client-facing strategy companion, not a duplicate |
| `playbook-sentiment-listening` | gap-analysis-2026-03-ai-books.md (Tier 3) | Built; Johnsen's 5-stage sentiment pipeline should be reviewed against current skill for completeness |
| `owned-media-strategy` | gap-analysis-2026-03.md (Medium priority) | Planned; Bly's lead magnet and list-building mechanics are high-priority additions confirmed |
| `strategy-csr-purpose-communications` | gap-analysis-2026-03.md (Low priority) | Planned; Rageh's Green Trust Model confirms relevance, especially for NGO/INGO clients in EA |
| `training-content-repurposing` | gap-analysis-2026-03-new-books.md (G4 extraction reference) | Not yet in plan; Westergaard's four content creation hacks confirm this is worth building |

---

## Bibliography

Bly, R.W. (2018) *The Digital Marketing Handbook: A Step-by-Step Guide to Creating Websites That Sell*. AWAI.

Hanlon, A. and Tuten, T.L. (Eds.) (2022) *The SAGE Handbook of Digital Marketing*. London: SAGE Publications.

Johnsen, M. (2024) *AI in Digital Marketing*. Dulles, VA: Mercury Learning and Information.

Kahan, S.M. (2022) *High-Velocity Digital Marketing: Develop and Implement the Winning Strategy That Best Fits Your Business*. Berkeley, CA: Apress.

Ltifi, M. (Ed.) (2024) *Advances in Digital Marketing in the Era of Artificial Intelligence*. Boca Raton, FL: CRC Press / Taylor & Francis.

Pidsley, M. (2023) *Digital Marketing in 2023: A Quickstart Guide*. Self-published.

Raaz, S.A. (c.2023) *Web Analytics Blueprint*. [Publisher details not confirmed in extraction.]

Rageh, A. (Ed.) (2026) *Ethical Marketing and Consumer Trust in Digital and Sustainable Markets*. [Publisher details not confirmed in extraction.]

Westergaard, N. (2016) *Get Scrappy: Smarter Digital Marketing for Businesses Big and Small*. New York: AMACOM.

Wind, J. and Mahajan, V. (2001) *Digital Marketing: Global Strategies from the World's Leading Experts*. Hoboken, NJ: John Wiley & Sons.

Zahay, D., Labrecque, L., Reavey, B. and Roberts, M.L. (2024) *Digital Marketing: Foundations and Strategy* (5th ed.). Mason, OH: Cengage Learning.

---
name: meta-budget-planner
description: Produces a social media and digital marketing budget plan for a client, allocating available monthly budget across channels, content production, tools, and paid amplification. Calibrated for Uganda/East Africa SME budgets with UGX rate tables and tier templates. Invoke this skill when a client asks how to allocate a marketing budget, wants to know what they should be spending and where, or needs to justify digital marketing expenditure to a stakeholder.
---
# Meta Budget Planner

<!-- dual-compat:start -->
## Use when
- Produces a social media and digital marketing budget plan for a client, allocating available monthly budget across channels, content production, tools, and paid amplification. Calibrated for Uganda/East Africa SME budgets with UGX rate tables and tier templates. Invoke this skill when a client asks how to allocate a marketing budget, wants to know what they should be spending and where, or needs to justify digital marketing expenditure to a stakeholder.
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

Ask for the following before generating the budget plan:

1. **Client business name and industry** — e.g., "Nakawa Organics — retail food & beverage"
2. **Country/city** — default is Uganda/East Africa if not specified
3. **Total monthly digital marketing budget** — state in UGX or USD; ask for both if the client is unsure of the exchange rate
4. **Primary business objective for the next 6 months** — must be a single, SMART objective (e.g., "Increase online sales leads by 40% by September 2026")
5. **Current channels and current spend on each** — list every channel (Facebook, WhatsApp, Google, email, etc.) and what they are currently spending per month on each, including zero-spend channels they are active on
6. **Team size** — how many in-house staff handle social media and digital marketing, or is the account fully agency-managed?
7. **Budget constraints or non-negotiables** — e.g., "We must continue running Facebook Ads", "We cannot spend on influencers", "The WhatsApp Business API subscription is fixed at UGX 120,000/month"

---

## Section 1 — Budget Planning Principles

Apply these five principles before building the plan. State each principle explicitly in the output and show how it affects the client's allocation.

### Principle 1: Objective drives allocation

Every budget line must connect directly to the stated business objective. If a line item cannot be justified by the objective, remove it. A client whose objective is lead generation has no business spending on brand awareness influencer posts until leads are flowing. Allocate ruthlessly.

### Principle 2: Owned before paid

Invest in building owned assets — the email subscriber list, the WhatsApp opt-in list, the blog archive — before scaling paid media spend. Owned assets compound over time; paid reach stops the moment the budget stops. Following the POEM model (Paid/Owned/Earned), owned channels form the foundation. Allocate a minimum budget line for email/WhatsApp list building at every tier.

### Principle 3: Test before scaling

Run small paid experiments (UGX 50,000–200,000 per test) before committing to large ad spends on any single channel or creative format. Use the `meta-testing-framework` skill for structured test design. Never commit more than 30% of the paid budget to an untested channel in the first month.

### Principle 4: Content is the multiplier

Paid amplification of weak content wastes money. Allocate budget for content production first; then amplify the content that earns the strongest organic engagement. A UGX 1,000,000 ad spend behind a poor creative will underperform a UGX 300,000 ad spend behind a strong one.

### Principle 5: Measure returns

Apply the ROI formula to justify every channel allocation — **ROI = (TLV − COCA) ÷ COCA** — where TLV is Total Lifetime Value and COCA is Cost of Customer Acquisition (Bodnar and Cohen, 2012). An ROI above zero means the channel is profitable. An ROI of 2.0 means every UGX 1 spent generates UGX 3 back (original cost plus two times return). Cross-reference with `meta-roi-framework` for a full per-channel model.

---

## Section 2 — Budget Tier Templates

Match the client to the appropriate tier based on their stated monthly budget. Present the relevant tier table in full. If the client's budget falls between tiers, present the lower tier as the base and note what the higher tier adds.

All amounts are in UGX. USD approximations use an exchange rate of UGX 3,700 = USD 1 (2026 estimate — confirm the current rate with the client).

---

### Tier 1 — Starter (UGX 500,000 – 1,500,000/month | approx. USD 130–400)

Suitable for: sole traders, early-stage SMEs, businesses new to paid digital marketing.

| Category | Item | Monthly UGX | % |
|---|---|---|---|
| Content production | Copywriting + graphics (basic) | 300,000 | 25% |
| Paid social | Facebook/Instagram boost budget | 300,000 | 25% |
| Tools | Canva Pro or equivalent | 60,000 | 5% |
| Community management | Time cost (if agency) | 540,000 | 45% |
| **Total** | | **1,200,000** | **100%** |

**Notes for Tier 1:**
- At this budget level, focus all paid spend on one platform only — Facebook is the default for Uganda/EA given audience size.
- Community management is the largest line because response time and engagement quality are the primary growth lever at this scale.
- Do not add a second paid channel until organic content is producing consistent engagement and the Facebook boost is generating measurable results.

---

### Tier 2 — Growth (UGX 1,500,000 – 5,000,000/month | approx. USD 400–1,350)

Suitable for: established SMEs ready to invest in consistent content output and managed paid campaigns.

| Category | Item | Monthly UGX | % |
|---|---|---|---|
| Content production | Copywriting, graphics, 2 short videos | 700,000 | 20% |
| Paid social | Facebook/Instagram Ads (managed) | 1,000,000 | 29% |
| SEO / blog | 1 blog post per month | 200,000 | 6% |
| Email marketing | MailChimp subscription + copywriting | 150,000 | 4% |
| Tools | Canva Pro + scheduling tool | 120,000 | 3% |
| Community management | Time cost (agency) | 1,000,000 | 29% |
| Analytics + reporting | Monthly report preparation | 300,000 | 9% |
| **Total** | | **3,470,000** | **100%** |

**Notes for Tier 2:**
- Introduce email marketing at this tier — begin building the owned list before increasing ad spend further.
- The blog post supports SEO and provides content to repurpose across social channels (Hero/Hub/Hygiene model).
- Analytics line is non-negotiable: without a monthly report, reallocation decisions at the quarterly review have no evidence base.

---

### Tier 3 — Scale (UGX 5,000,000 – 15,000,000/month | approx. USD 1,350–4,000)

Suitable for: growth-stage businesses, funded startups, and organisations running multi-channel digital marketing programmes.

| Category | Item | Monthly UGX | % |
|---|---|---|---|
| Content production | Full content suite (copy, graphics, 4 videos) | 2,000,000 | 18% |
| Paid social — Facebook/Instagram | Managed campaigns | 3,000,000 | 27% |
| Google Ads | Search + display | 1,000,000 | 9% |
| Influencer / creator fees | 1–2 micro-influencer partnerships | 800,000 | 7% |
| Email + WhatsApp marketing | Tool subscription + production | 300,000 | 3% |
| SEO / blog | 2 posts per month + SEO audit | 500,000 | 5% |
| Tools | Full martech stack | 300,000 | 3% |
| Strategy + account management | Senior consultant time | 2,000,000 | 18% |
| Analytics + reporting | Monthly + quarterly reports | 500,000 | 5% |
| Contingency (testing) | A/B tests, new channel exploration | 600,000 | 5% |
| **Total** | | **11,000,000** | **100%** |

**Notes for Tier 3:**
- The contingency line (5%) is mandatory — it funds structured tests before any new channel is added to the permanent mix.
- Influencer fees at this level should target micro-influencers (5,000–50,000 followers) with high engagement rates in the client's sector. Refer influencer contracts to a legal professional — do not draft terms as part of this skill.
- Google Ads is appropriate only where the client has a functional website with conversion tracking enabled.

---

## Section 3 — Channel Allocation Decision Framework

Use this four-step framework to decide which channels receive paid budget. Apply it to every client regardless of tier.

**Step 1: List active channels.**
List every channel the client is currently active on — paid and organic. Include WhatsApp, Facebook, Instagram, TikTok, YouTube, LinkedIn, X/Twitter, email, and Google as applicable.

**Step 2: Assess each channel on three criteria.**
For each channel, identify:
- Current organic reach (average post reach or impressions per month)
- Cost per result from any previous paid activity (cost per lead, cost per click, cost per purchase)
- Fit with the primary objective (direct fit / indirect fit / no fit)

**Step 3: Rank channels using this priority logic.**
- **Highest priority:** channels where previous paid activity produced a cost per result below the client's acceptable acquisition threshold
- **Medium priority:** channels with strong organic reach where paid amplification would multiply results
- **Low priority:** channels with low organic reach and no prior evidence of paid return

**Step 4: Allocate paid budget by rank.**
Allocate a minimum of 70% of the total paid budget to the highest-priority channel. Include no more than three channels in the paid mix at one time. Spreading budget across four or more channels simultaneously makes measurement impossible and performance unreliable.

---

## Section 4 — Content Production Budget Guide

Apply these EA market rate ranges when advising on content production costs. All rates are in UGX as of 2026. Confirm current rates with local suppliers before presenting to the client.

| Item | Freelance / Junior Rate | Agency / Mid Rate | Notes |
|---|---|---|---|
| Social media caption (per post) | 10,000–20,000 | 25,000–50,000 | Per post, per platform |
| Static graphic design (per post) | 15,000–30,000 | 40,000–80,000 | Per image |
| Short video / Reel (15–60 sec) | 100,000–200,000 | 250,000–500,000 | Script + edit; no filming |
| Blog post (800–1,200 words) | 50,000–100,000 | 150,000–300,000 | Includes SEO optimisation |
| Monthly content package (20 posts + graphics) | 400,000–600,000 | 800,000–1,500,000 | Common retainer scope |
| Photography session (2 hours) | 100,000–200,000 | 300,000–600,000 | Product or lifestyle shoot |

**Guidance on content budget decisions:**
- For Tier 1 clients, recommend a monthly content package from a junior freelancer to keep costs within budget.
- For Tier 2 and above, recommend agency/mid-rate production for video — quality difference is significant and affects paid performance.
- Photography sessions should be planned quarterly, not monthly, to manage costs. Batch 8–12 weeks of visual assets in a single session.

---

## Section 5 — Budget Review Cadence

Build a review schedule into every budget plan. Recommend the client assigns a named person responsible for each review.

**Monthly review (every 4 weeks):**
- Compare actual spend against the planned budget line by line
- Review cost per result for each active paid channel
- Flag any channel that has spent more than 15% above plan — pause and investigate before continuing
- Check that content production deliverables have been received and approved

**Quarterly review (every 3 months):**
- Assess whether the SMART objective is on track
- Reallocate budget from underperforming channels to top performers — apply the channel allocation decision framework (Section 3) with three months of live data
- Review whether the current tier is still appropriate — upgrade if the business has grown; reduce if the budget has contracted
- Assess owned asset growth: email list size, WhatsApp opt-in list size, organic reach trends

**Annual review (every 12 months):**
- Full budget reset — start from the objective, not from the previous year's allocation
- Revisit the tier level based on 12-month business performance
- Add or remove channels based on full-year data only — do not make channel decisions on less than 90 days of data
- Benchmark rates against current EA market prices; update the content production guide accordingly

---

## Section 6 — ROI Tracking

Connect every budget line to a measurable return using the Bodnar and Cohen (2012) framework.

**Formula: ROI = (TLV − COCA) ÷ COCA**

- **TLV (Total Lifetime Value):** average revenue per customer × average customer lifespan in months/years
- **COCA (Cost of Customer Acquisition):** total digital marketing spend in the period ÷ number of new customers acquired in the same period

**How to apply this in the budget plan:**

1. Ask the client for their average order value or monthly revenue per client.
2. Ask how long a typical customer stays (repeat purchase rate or contract length).
3. Calculate TLV: e.g., a client spending UGX 150,000/month for an average of 8 months has a TLV of UGX 1,200,000.
4. Calculate COCA from the monthly budget: e.g., UGX 1,200,000/month in marketing ÷ 6 new customers = UGX 200,000 COCA.
5. Calculate ROI: (1,200,000 − 200,000) ÷ 200,000 = **5.0** — every UGX 1 spent returns UGX 6 (cost plus five times return).

**Interpretation benchmarks:**
- ROI < 0: the channel is losing money — pause and diagnose before continuing
- ROI 0–1.0: the channel is marginally profitable — optimise before scaling
- ROI 1.0–3.0: healthy return — maintain and test incremental scaling
- ROI > 3.0: strong return — consider increasing budget allocation to this channel

Cross-reference with `meta-roi-framework` for a full per-channel ROI model and attribution methodology.

---

## Quality Criteria

Good output from this skill meets all of the following standards:

- All three tier templates are present in the output, with UGX amounts and percentage allocations for every line item; the client's appropriate tier is identified and highlighted
- The channel allocation decision framework is applied step-by-step using the client's actual channels and stated objective — not presented as a generic template
- The content production rate table uses EA market rates in UGX and includes guidance on freelance versus agency rates appropriate to the client's tier
- The ROI formula (Bodnar and Cohen, 2012) is cited, defined, and applied with the client's own figures where available, or with worked examples where figures are unknown
- A monthly, quarterly, and annual review cadence is included with named responsibilities and specific triggers for reallocation
- The owned-before-paid principle is explicitly applied — the plan includes at least one owned-channel budget line (email, WhatsApp, or blog) at Tier 2 and above
- Every budget line maps to the client's stated objective — any line that cannot be justified is flagged for removal or deprioritisation

---

## References

Consult these linked skills when building or extending the budget plan:

- `meta-roi-framework/SKILL.md` — full per-channel ROI model and attribution methodology; read when the client needs a detailed return calculation per channel
- `meta-testing-framework/SKILL.md` — structured test design for paid experiments; read before designing any new paid channel test
- `09-campaign-strategy/SKILL.md` — campaign-level strategy and objective setting; read when the client's objective needs to be refined into campaign-level tactics
- `peso-integrated-strategy/SKILL.md` — PESO (Paid/Earned/Shared/Owned) channel integration; read when the client requires a fully integrated channel strategy before the budget plan is finalised

---

*Rates and platform data are calibrated for the Uganda/East Africa market as of 2026. Confirm current exchange rates, tool subscription costs, and freelance market rates before presenting any budget plan to a client.*

# Bottom-Up Revenue Plan

Merged from skills/meta-analytics-ops/meta-revenue-planning on 2026-09-29 at 8eacccb; preservation map: [meta-revenue-planning.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/meta-revenue-planning.md)

## When to use this reference

Read this reference when the client needs the budget tied to a revenue outcome rather than to activity: a bottom-up revenue plan that works back from a revenue target through funnel conversion rates to the inquiries, leads and opportunities each channel must deliver, a weighted pipeline model, a CAC ceiling and a monthly funnel review. Produce the revenue plan first when the budget ceiling is not yet agreed; the CAC ceiling it yields then caps the budget plan in the SKILL.md.

Why it matters: most marketing plans set activity goals ("post three times per week", "run one campaign per month", "attend two networking events per quarter"). Those plans cannot be judged for commercial performance because nothing connects them to revenue. The bottom-up model works backwards from the revenue target to the exact number of visitors, enquiries and leads the programme must generate each quarter. Judge every activity against that standard: does it contribute to the required lead volume? If not, deprioritise it.

## Inputs

Ask for the following before generating any output:

| Input | What to capture |
|---|---|
| Business name | Trading name of the client |
| Industry | Sector and niche |
| Country / city | Default Uganda/East Africa |
| Primary goal | Revenue target for the planning period; state whether quarterly or annual |
| Average deal or order value | Revenue per new client or transaction, in UGX or the local currency |
| Historical conversion data | Visitor-to-lead, lead-to-opportunity and opportunity-to-deal rates if available; if not, apply the Kahan (2022) benchmarks below and label them |
| Current channel mix | Channels that currently generate leads (social media, referrals, events, email, search) |
| Sales team capacity | How many sales conversations the team can handle per week |

Definitions used throughout:

- **Contact / inquiry**: anyone who has entered the top of the funnel: followed the brand on social media, visited the website, submitted a form or sent a first WhatsApp message.
- **Qualified lead**: a contact who has shown intent beyond the first enquiry: engaged with content, attended a webinar, replied to an email or requested information.
- **Opportunity**: a qualified sales conversation; a prospect who has confirmed interest and is actively considering a purchase.

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| The client has its own historical conversion rates | Use them; apply Kahan (2022) benchmarks only where no data exists, and flag in the plan which figures are actuals and which are benchmarks. | Unexplained figures; benchmarks passed off as client results. |
| The client's actual rates are below benchmark | Show the gap the model reveals (more inquiries needed, better conversion needed, or both) and present it to the client as an explicit choice. | A hidden assumption that inflates the plan. |
| The business sells several products at different price points | Calculate a blended average revenue per client, or run a separate calculation for each product line. | One average masking very different deal sizes. |
| The plan needs more budget than the CAC cap permits | Do not spend more. Improve conversion rates or reduce the scope of the target. | Buying revenue at a loss. |
| A funnel stage is consistently slower than its velocity target | Treat it as a process bottleneck at that stage and fix the process before increasing lead volume. | Pouring more leads into a blocked stage. |
| The monthly shortfall sits at the top of the funnel (inquiries) | Respond with marketing action. | Applying the wrong fix. |
| The monthly shortfall sits in the middle (lead-to-opportunity) | Respond with a sales process change. | Blaming marketing volume for a sales process gap. |

The Kahan (2022) benchmark rates, the CAC-to-CLV ratio, the pipeline weights and the velocity targets are practitioner guidance, not East Africa market data. Verify before stating (no register record); present them as provisional comparators until the client's own data replaces them.

## Procedure: the six-step bottom-up model (Kahan, 2022)

Work through the six steps in order. Do not skip a step; each calculation feeds the next.

1. **State the revenue target** in local currency for the planning period. Example: "We need to generate UGX 120,000,000 in new revenue from digital marketing in Q1 2026."
2. **Calculate new clients required**: revenue target ÷ average revenue per new client. Example: UGX 120,000,000 ÷ UGX 6,000,000 = **20 new clients**.
3. **Calculate opportunities required**: new clients ÷ opportunity-to-deal rate (benchmark ~40%). Example: 20 ÷ 0.40 = **50 opportunities**.
4. **Calculate qualified leads required**: opportunities ÷ lead-to-opportunity rate (benchmark ~25%). Example: 50 ÷ 0.25 = **200 qualified leads**.
5. **Calculate total inquiries required**: qualified leads ÷ inquiry-to-lead rate (benchmark ~3%). Example: 200 ÷ 0.03 = **6,667 inquiries or contacts per quarter**.
6. **Allocate inquiries by channel**: spread the required volume across the channels the programme will use. Base the split on historical performance; use estimated proportions where no data exists.

Example channel allocation:

| Channel | Allocation % | Inquiries required |
|---|---|---|
| Facebook organic + content | 30% | 2,000 |
| WhatsApp referral traffic | 25% | 1,667 |
| Email list | 20% | 1,333 |
| LinkedIn (B2B) | 15% | 1,000 |
| Events and referrals | 10% | 667 |
| **Total** | **100%** | **6,667** |

## Funnel conversion benchmarks (Kahan, 2022)

| Funnel stage | Benchmark rate |
|---|---|
| Visitor-to-lead (website) | Over 5% |
| Inquiry-to-lead | ~3% |
| Lead-to-opportunity | ~25% |
| Opportunity-to-deal | ~40% |

## Customer acquisition cost cap

Rule (Kahan, 2022): customer acquisition cost (CAC) must not exceed 25% of customer lifetime value (CLV): **CAC ≤ CLV × 0.25**. This is the budget governance ceiling.

1. Calculate CLV: average revenue per client × average number of transactions × average client lifespan in years.
2. Calculate the CAC ceiling: CLV × 0.25.
3. Calculate actual CAC: total quarterly marketing budget ÷ new clients needed.
4. Confirm actual CAC is below the ceiling before presenting the budget to the client or board.

This ceiling sits alongside the Bodnar and Cohen (2012) ROI check in the SKILL.md `Section 6 — ROI Tracking`: the cap limits what the plan may spend per client; the ROI formula judges each channel's return once it runs.

## Weighted pipeline

Forecast quarterly revenue from weighted pipeline values: multiply each deal's full value by its stage weight so the forecast reflects the probability of closure.

| Pipeline stage | Weight |
|---|---|
| Open Opportunity (first conversation had) | 10% |
| Active Project (proposal or quote sent) | 30% |
| Shortlist (client has confirmed they are comparing 2–3 options) | 60% |
| Forecast (verbal commitment received) | 85% |
| Closed Won | 100% |

Weighted pipeline value = sum of (each deal value × its stage weight). Present it next to the target every month. The gap between weighted pipeline and the quarterly target is the lead volume the marketing programme must fill.

## Deal velocity targets

Measure the number of days at each funnel stage. Faster conversion at the same spend yields more revenue per quarter without extra budget.

| Stage transition | Velocity target |
|---|---|
| Inquiry → qualified lead | Within 48 hours |
| Qualified lead → opportunity | Within 14 days |
| Opportunity → deal | Within 60 days |

## Monthly review

At the end of each month review actuals against plan at every funnel stage, not only at revenue.

| Metric | Target (monthly) | Actual | Variance |
|---|---|---|---|
| Total inquiries / new contacts | — | — | — |
| Qualified leads generated | — | — | — |
| Opportunities opened | — | — | — |
| Deals closed | — | — | — |
| Revenue from new clients | — | — | — |
| Weighted pipeline value | — | — | — |
| CAC actual vs. CAC ceiling | — | — | — |

## Output: revenue planning document

1. **Bottom-up calculation**: all six steps completed with client data or benchmarks, clearly labelled.
2. **Channel allocation table**: inquiry volume targets per channel per quarter.
3. **CAC analysis**: CLV calculation, CAC ceiling and budget governance recommendation.
4. **Weighted pipeline template**: a table the client can maintain monthly.
5. **Deal velocity targets**: specific timeframes per funnel stage.
6. **Monthly review table**: pre-populated with targets; actuals column left blank for the client to fill.

## Release checklist

- [ ] The revenue target is stated in UGX (or the client's local currency) before any other calculation, anchoring the plan to a commercial outcome.
- [ ] All four funnel conversion rates come from the client's own history or are explicitly attributed to Kahan (2022) benchmarks; no figure is unexplained.
- [ ] Inquiry volume is allocated by channel, not left as a total no channel owner is responsible for.
- [ ] The CAC cap is calculated and confirmed within the CLV × 0.25 ceiling before any budget recommendation.
- [ ] Stage weights produce a weighted pipeline value alongside the absolute target, so the plan separates what is targeted from what is probable.
- [ ] Deal velocity targets are set for each funnel stage: process targets as well as volume targets.
- [ ] The monthly review runs from day one, comparing actuals with plan at every funnel stage, not only the revenue line.

## Source

Kahan, R. (2022) *High-Velocity Digital Marketing: 7 Proven Strategies to Send Your Revenue Soaring Using Today's Best Digital Practices*. Amplify Publishing.

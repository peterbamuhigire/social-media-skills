---
name: meta-revenue-planning
description: >
  Builds a defensible, bottom-up marketing plan by reverse-engineering a revenue target
  through funnel conversion rates to the required inquiry, lead, and opportunity volumes
  per channel. Invoke when a client needs to connect digital marketing activity to a
  revenue target — replacing vague activity goals with a data-driven quarterly plan
  that is reviewable at every stage. Source: Kahan (2022) High-Velocity Digital
  Marketing.
---
# Revenue Planning Framework

<!-- dual-compat:start -->
## Use when
- Builds a defensible, bottom-up marketing plan by reverse-engineering a revenue target through funnel conversion rates to the required inquiry, lead, and opportunity volumes per channel. Invoke when a client needs to connect digital marketing activity to a revenue target — replacing vague activity goals with a data-driven quarterly plan that is reviewable at every stage. Source: Kahan (2022) High-Velocity Digital Marketing.
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

## Required Inputs

Ask for the following before generating any output:

1. **Business name** — trading name of the client
2. **Industry** — sector and niche
3. **Country / city** — default is Uganda/East Africa
4. **Primary goal** — revenue target for the planning period (specify: quarterly or annual)
5. **Average deal or order value** — revenue per new client or transaction in UGX (or local currency)
6. **Historical conversion data** — if available: visitor-to-lead rate, lead-to-opportunity rate, opportunity-to-deal rate; if not available, Kahan benchmarks are applied
7. **Current channel mix** — which channels currently generate leads (social media, referrals, events, email, search)
8. **Sales team capacity** — how many sales conversations the team can handle per week

---

## The Problem This Solves

Most marketing plans set activity goals: "post three times per week", "run one campaign per month", "attend two networking events per quarter." These plans cannot be evaluated for commercial performance because they are not connected to a revenue outcome.

Bottom-up revenue planning works backwards from a revenue target through conversion rates to determine exactly how many leads, enquiries, and visitors the marketing programme must generate per quarter. Every activity can then be evaluated against this standard: does it contribute to the required lead volume? If not, deprioritise it.

---

## The Bottom-Up Revenue Model (Kahan, 2022)

Work through the following six steps in sequence. Do not skip a step; each calculation feeds the next.

### Step 1: State the Revenue Target

Express the target in local currency for the planning period.

> "We need to generate UGX 120,000,000 in new revenue from digital marketing in Q1 2026."

### Step 2: Calculate New Clients Required

> Revenue target ÷ average revenue per new client = new clients needed

**Example:**
> UGX 120,000,000 ÷ UGX 6,000,000 = **20 new clients needed**

Where the business sells multiple products at different price points, calculate a blended average or run separate calculations for each product line.

### Step 3: Calculate Opportunities Required

> New clients needed ÷ opportunity-to-deal conversion rate = opportunities needed

**Kahan (2022) benchmark:** ~40% opportunity-to-deal conversion rate

**Example:**
> 20 ÷ 0.40 = **50 opportunities needed**

An "opportunity" is a qualified sales conversation — a prospect who has confirmed interest and is actively considering a purchase.

### Step 4: Calculate Qualified Leads Required

> Opportunities needed ÷ lead-to-opportunity conversion rate = qualified leads needed

**Kahan (2022) benchmark:** ~25% lead-to-opportunity conversion rate

**Example:**
> 50 ÷ 0.25 = **200 qualified leads needed**

A "qualified lead" is a contact who has shown intent beyond initial enquiry — they have engaged with content, attended a webinar, replied to an email, or requested information.

### Step 5: Calculate Total Inquiries Required

> Qualified leads needed ÷ inquiry-to-lead conversion rate = total inquiries needed

**Kahan (2022) benchmark:** ~3% inquiry-to-lead conversion rate

**Example:**
> 200 ÷ 0.03 = **6,667 total inquiries / contacts needed per quarter**

A "contact" at this stage is anyone who has entered the top of the funnel: followed the brand on social media, visited the website, submitted a form, or sent a first WhatsApp message.

### Step 6: Allocate Inquiries by Channel

Distribute the required inquiry volume across the channels the marketing programme will use. Base the allocation on historical performance data; use estimated proportions where no data is available.

**Example allocation:**

| Channel | Allocation % | Inquiries Required |
|---|---|---|
| Facebook organic + content | 30% | 2,000 |
| WhatsApp referral traffic | 25% | 1,667 |
| Email list | 20% | 1,333 |
| LinkedIn (B2B) | 15% | 1,000 |
| Events and referrals | 10% | 667 |
| **Total** | **100%** | **6,667** |

---

## Funnel Conversion Rate Benchmarks (Kahan, 2022)

Use client historical data where available. Apply Kahan benchmarks where no data exists. Flag clearly in the plan which figures are actuals and which are benchmarks.

| Funnel Stage | Benchmark Rate |
|---|---|
| Visitor-to-lead (website) | Over 5% |
| Inquiry-to-lead | ~3% |
| Lead-to-opportunity | ~25% |
| Opportunity-to-deal | ~40% |

Where a client's actual conversion rates are below benchmark, the bottom-up model will reveal the gap: either more inquiries are needed, or the conversion rate must be improved, or both. Present this as an explicit choice to the client — not a hidden assumption.

---

## Customer Acquisition Cost Cap

**CAC Cap Rule (Kahan, 2022):** Customer Acquisition Cost (CAC) must not exceed 25% of Customer Lifetime Value (CLV).

> CAC ≤ CLV × 0.25

**Application:**
1. Calculate CLV: average revenue per client × average number of transactions × average client lifespan in years
2. Calculate CAC ceiling: CLV × 0.25
3. Divide total quarterly marketing budget by new clients needed = actual CAC
4. Confirm actual CAC is below the ceiling before presenting the budget to the client or board

This is the budget governance ceiling. If the plan requires more budget than the CAC cap permits, the answer is not to spend more — it is to improve conversion rates or reduce the scope of the target.

---

## Pipeline Stage Weighting

Apply weighted pipeline values when forecasting quarterly revenue. Multiplying each pipeline item's full value by its stage weight produces a realistic forecast that accounts for the probability of closure.

| Pipeline Stage | Weight |
|---|---|
| Open Opportunity (first conversation had) | 10% |
| Active Project (proposal or quote sent) | 30% |
| Shortlist (client has confirmed they are comparing 2–3 options) | 60% |
| Forecast (verbal commitment received) | 85% |
| Closed Won | 100% |

**Weighted pipeline calculation:**
> Sum of (each deal value × its stage weight) = weighted pipeline value

Present weighted pipeline alongside the target each month. The gap between weighted pipeline and the quarterly target is the lead volume the marketing programme must fill.

---

## Deal Velocity Targets

Measure the number of days at each funnel stage. Faster conversion at the same spend equals more revenue per quarter without additional budget.

| Stage Transition | Velocity Target |
|---|---|
| Inquiry → qualified lead | Within 48 hours |
| Qualified lead → opportunity | Within 14 days |
| Opportunity → deal | Within 60 days |

Where a stage is consistently slower than the target, the bottleneck is in the process at that stage — not in the volume of leads. Fix the process before increasing lead volume.

---

## Monthly Review Protocol

Review the plan at the end of each month against actuals at every funnel stage — not only at revenue.

**Monthly review table:**

| Metric | Target (Monthly) | Actual | Variance |
|---|---|---|---|
| Total inquiries / new contacts | — | — | — |
| Qualified leads generated | — | — | — |
| Opportunities opened | — | — | — |
| Deals closed | — | — | — |
| Revenue from new clients | — | — | — |
| Weighted pipeline value | — | — | — |
| CAC actual vs. CAC ceiling | — | — | — |

A shortfall at the top of the funnel (inquiries) requires a marketing response. A shortfall in the middle (lead-to-opportunity) requires a sales process response. Knowing where the gap sits prevents the wrong solution being applied.

---

## Output: Revenue Planning Document

Generate the following for the client:

1. **Bottom-up calculation** — all six steps completed with client data or benchmarks; clearly labelled
2. **Channel allocation table** — inquiry volume targets per channel per quarter
3. **CAC analysis** — CLV calculation, CAC ceiling, and budget governance recommendation
4. **Weighted pipeline template** — a table the client can maintain monthly
5. **Deal velocity targets** — specific timeframes per funnel stage
6. **Monthly review table** — pre-populated with targets; actuals column left blank for the client to fill

---

## Quality Criteria

Output meets the standard when:

1. Revenue target is stated in UGX (or the client's local currency) before any other calculation begins — the plan is anchored to a specific commercial outcome
2. All four funnel conversion rates are sourced from the client's own historical data or explicitly attributed to Kahan (2022) benchmarks — no figures are unexplained
3. Inquiry volume target is allocated by channel — not left as an undifferentiated total that no single channel owner is responsible for delivering
4. CAC cap is calculated and confirmed as within the CLV × 0.25 ceiling before any budget recommendation is made
5. Pipeline stage weightings are applied to produce a weighted pipeline value alongside the absolute revenue target — the plan distinguishes between what is targeted and what is probable
6. Deal velocity targets are set for each funnel stage — the plan includes process targets, not only volume targets
7. Monthly review protocol is established from day one — actuals vs. plan at every funnel stage, not only at the revenue line

---

## Reference

Kahan, R. (2022) *High-Velocity Digital Marketing: 7 Proven Strategies to Send Your Revenue Soaring Using Today's Best Digital Practices*. Amplify Publishing.

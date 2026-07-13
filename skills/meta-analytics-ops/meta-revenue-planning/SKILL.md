---
name: meta-revenue-planning
description: "Use when building a bottom-up revenue plan from funnel stages, deal values and capacity. Produces revenue plan and weighted pipeline model; use `meta-roi-framework` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Revenue Planning Framework


<!-- dual-compat-start -->
## Use When

- Use this skill for building a bottom-up revenue plan from funnel stages, deal values and capacity.
- Confirm that `meta-roi-framework` is not the closer route before proceeding.

## Do Not Use When

- Use `meta-roi-framework` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Revenue target, historical conversion, deal value and sales-cycle data | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Revenue plan and weighted pipeline model | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified revenue plan and weighted pipeline model. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Revenue target, historical conversion, deal value and sales-cycle data is current and attributable | Produce the full revenue plan and weighted pipeline model and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `meta-roi-framework` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `meta-roi-framework` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the revenue plan and weighted pipeline model, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the revenue plan and weighted pipeline model without revenue target. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `meta-roi-framework` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified revenue target, the skill produces a revenue plan and weighted pipeline model with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`meta-roi-framework`](../meta-roi-framework/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

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

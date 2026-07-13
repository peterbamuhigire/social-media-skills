---
name: meta-social-media-roi-business-case
description: "Use when building an executive case for social investment, including risk, proof and measurement limits. Produces social-media investment business case; use `meta-roi-framework` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# meta-social-media-roi-business-case

## Purpose

Produce a professional business case document — or the structured inputs for a board presentation — that justifies social media investment to Ugandan and East African organisations whose leadership teams are not yet convinced of its value. Frame the argument in language C-suite executives understand: competitive risk, customer acquisition cost, financial return, and market position.

Most Ugandan clients at banks, NGOs, manufacturers, and large SMEs operate without a dedicated social media budget. This skill gives the consultant the frameworks, calculations, and language to change that.

**Primary reference:** Funk, T. (2013) *Advanced Social Media Marketing*. Apress. — cited for the "Risk of Ignoring" framework and fan/follower valuation methods.

**Supporting references:**
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*

---


<!-- dual-compat-start -->
## Use When

- Use this skill for building an executive case for social investment, including risk, proof and measurement limits.
- Confirm that `meta-roi-framework` is not the closer route before proceeding.

## Do Not Use When

- Use `meta-roi-framework` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Decision audience, proposed spend, business outcomes and verified baseline | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Social-media investment business case | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified social-media investment business case. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Decision audience, proposed spend, business outcomes and verified baseline is current and attributable | Produce the full social-media investment business case and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `meta-roi-framework` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `meta-roi-framework` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the social-media investment business case, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the social-media investment business case without decision audience. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `meta-roi-framework` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified decision audience, the skill produces a social-media investment business case with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`meta-roi-framework`](../meta-roi-framework/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Input

Ask the client or collect from the brief before generating any output:

1. **Client business name** — exact trading name
2. **Industry** — e.g. commercial banking, manufacturing, NGO, hospitality, FMCG
3. **Country/city** — defaults to Uganda/Kampala if not specified
4. **Primary goal** — e.g. increase sales, defend market share, grow brand awareness, attract donors
5. **Decision-maker audience** — who will read or receive this business case (board, CEO, finance committee, donor)
6. **Current social media presence** — none, minimal, or existing but unfunded
7. **Known competitor social activity** — any information on what direct competitors are doing on social media
8. **Approximate annual marketing spend** — to calibrate budget recommendations (if client declines to share, use industry-tier estimates)
9. **Previous social media attempts** — has the client tried and stopped before? If yes, what happened?

---

## When to Use This Skill

Use this skill in any of the following situations:

- A client's leadership team or board is sceptical of social media's business value
- A new proposal includes a social media retainer and is being challenged on ROI grounds
- The client has never allocated a dedicated social media budget
- An existing budget is up for renewal and the finance team requires justification
- A competitor has recently launched a strong social media presence and the client needs to respond
- A donor or parent organisation is asking for evidence of digital engagement as part of a grant renewal

---

## Section 1 — The "Risk of Ignoring" Framing (Funk, 2013)

Frame competitor social media activity as a direct business risk, not merely a missed opportunity. Decision-makers respond to threat framing more strongly than opportunity framing.

**The core argument:** Every month a competitor runs an active social media programme, they are building an audience the client does not have access to. That audience represents revenue at risk.

### Calculating the Risk of Ignoring

Use this formula to quantify the competitive threat:

```
Revenue at Risk = Competitor Audience Size × Estimated Conversion Rate × Average Order Value
```

**Steps:**
1. Record the competitor's follower count on their most active platform (publicly visible).
2. Apply a conservative conversion rate. Use 1–2% for B2C; 0.5–1% for B2B. Cite Funk (2013) as the basis for conservative estimates.
3. Multiply by the client's average order value or annual customer value.
4. Present this as an annual figure: multiply monthly estimate × 12.

**Example (Ugandan commercial bank):**
- Competitor Facebook page: 45,000 followers
- Estimated conversion rate: 1%
- Average new account value (first-year fees + average deposit product): UGX 480,000
- Revenue at Risk = 45,000 × 1% × UGX 480,000 = **UGX 216,000,000/year**

**Presentation guidance:** Present the calculation transparently. Show all assumptions. Invite the decision-maker to adjust the conversion rate. A conservative, honest calculation is more credible than an inflated one. The goal is to establish that the risk is real and quantifiable, not to produce an impressive number.

---

## Section 2 — Fan/Follower Valuation

Demonstrate that a social media following has a calculable financial value before any campaign spend.

### Method A — Impression Valuation (Advertising Equivalency)

Estimate the advertising value of organic reach from a social following.

```
Monthly Advertising Value = (Followers × Organic Reach Rate × Posts per Month) ÷ 1,000 × CPM
```

**EA-calibrated CPM benchmarks (Facebook, Uganda):**
- Low estimate: USD 0.30 / UGX 1,100
- Mid estimate: USD 0.55 / UGX 2,000
- High estimate: USD 0.80 / UGX 3,000

*Source: Meta Ads Manager observed rates, Uganda market, 2023–2024. Use mid estimate as default.*

**Assumptions to state explicitly:**
- Facebook organic reach rate for a page with consistent posting: 5–8% of followers per post
- Posting frequency: assume 12–16 posts per month (3–4 per week)

**Example:** A page with 10,000 followers, 6% reach per post, 14 posts/month, CPM UGX 2,000:
- Monthly impressions: 10,000 × 6% × 14 = 8,400
- Advertising value: (8,400 ÷ 1,000) × UGX 2,000 = **UGX 16,800/month** in organic media value

### Method B — Loyalty Premium Valuation

If social media followers convert at 2–3× the rate of non-followers (Funk, 2013), the follower base carries a loyalty premium.

**Steps:**
1. Establish the client's baseline conversion rate from general market (from CRM, sales data, or industry benchmark).
2. Apply a 2× multiplier for social followers (conservative; cite Funk, 2013).
3. Calculate the incremental revenue from the follower base at the higher conversion rate.
4. Present the difference as the loyalty premium.

State clearly that this is a modelled estimate, not a measured result — and recommend a formal Attitude & Usage study (Section 3) to validate it over time.

---

## Section 3 — Attitude & Usage (A&U) Study

An A&U study compares brand perception, purchase intent, and loyalty between social media followers and non-followers. It is the most rigorous method for demonstrating social media's effect on brand equity.

### Full A&U Study

A professional A&U study involves a research agency surveying a representative sample of followers and a matched sample of non-followers. Metrics measured: brand awareness (prompted and unprompted), purchase intent, Net Promoter Score, and brand attribute ratings. Commission this for clients with research budgets (UGX 15,000,000+ for a credible study in Uganda).

### Lightweight A&U (No Research Budget)

For clients without research budgets, conduct a simple version:

1. **Follower survey** — deploy a 5-question poll via Instagram Stories or a WhatsApp broadcast to existing followers. Ask: likelihood to purchase, brand rating (1–10), whether they have recommended the brand, and top brand associations.
2. **Non-follower benchmark** — compare follower responses against any available market data: previous brand health surveys, industry NPS benchmarks, or customer satisfaction scores from the client's CRM.
3. **Gap analysis** — present the difference between follower perceptions and general market perceptions as evidence of the social media programme's effect on brand equity.

**What to do with the findings:**
- Include in the business case as a "brand equity delta" metric
- Use as a baseline to track improvement after investment begins
- Present to the board as evidence that the audience already built has measurable value

---

## Section 4 — Net Promoter Score (NPS) Integration

NPS measures the proportion of customers who would actively recommend the brand. Social media accelerates word-of-mouth, which directly influences NPS.

**The connection to social media:**
- Active social media communities generate more brand advocates (Promoters)
- Responsive community management converts Passives to Promoters and prevents Detractors from escalating
- Every 1-point NPS improvement correlates with measurable revenue growth (Reichheld, 2003, cited via Chaffey, 2024)

### Deploying a Simple NPS Survey via WhatsApp

1. Send a WhatsApp broadcast to the client's customer contact list: *"On a scale of 0–10, how likely are you to recommend [Brand] to a friend or colleague?"*
2. Follow up with one open-ended question: *"What is the main reason for your score?"*
3. Calculate NPS: % Promoters (9–10) minus % Detractors (0–6).
4. Record baseline. Repeat quarterly.

### Presenting NPS as a Financial Outcome

Translate NPS improvement into financial language for the board:

- Estimate the client's average customer lifetime value (CLV).
- Apply the rule of thumb: a 5-point NPS improvement correlates with 1.5–3% revenue growth (Chaffey, 2024).
- Present the projected revenue impact of improving NPS from the current baseline.

State clearly that this is a directional estimate. Recommend tracking NPS alongside social media activity to build a proprietary correlation over 12–18 months.

---

## Section 5 — Budget Allocation Framework

### Rule of Thumb

Social media budget = 5–15% of total marketing spend (Chaffey, 2024). For clients with no existing marketing budget, present the three tiers below.

### Uganda/EA Budget Tiers

| Tier | Monthly Budget | Suitable For |
|---|---|---|
| Starter | UGX 500,000–1,000,000 | First-time social media investment; 1–2 platforms; content only |
| Growth | UGX 2,000,000–5,000,000 | Established brand; 2–3 platforms; content + paid amplification |
| Scale | UGX 10,000,000+ | Market leader or aggressive growth phase; full-platform programme |

*Note: These are consultant/agency fees plus content production. Paid media (boosted posts, ads) is a separate line item.*

### Budget Line Items

Include these in every budget proposal:

1. **Content production** — copywriting, photography direction, graphic design briefs
2. **Community management** — monitoring, responding, moderating across platforms
3. **Paid amplification** — boosted posts and targeted ads (keep separate from agency fees)
4. **Tools and software** — scheduling, analytics, social listening (e.g. Hootsuite, Buffer, Brandwatch)
5. **Reporting and strategy** — monthly performance reports and quarterly strategy reviews

### The 90/10 Core vs. Test-and-Learn Split

Allocate 90% of the budget to proven, core activities (content production and community management on the primary platform). Reserve 10% for testing new formats, platforms, or audience segments. Present this to sceptical finance teams as a disciplined, low-risk approach to budget management.

---

## Section 6 — Business Case Document Structure

Generate the business case in this exact structure:

**1. Executive Summary** (1 paragraph)
What is being proposed, how much it will cost, and what the expected return is. Written last; presented first.

**2. Current Situation and Competitive Risk**
- Client's current social media position (absent or minimal)
- Competitor activity mapped with follower counts and engagement estimates
- Revenue at Risk calculation (Section 1 formula)

**3. Proposed Investment**
- Recommended budget tier with rationale
- Platforms to be prioritised and why
- Agency/consultant scope of work in plain language

**4. Expected Outcomes**
- Month 3: follower growth target, content volume, share of voice estimate
- Month 6: community size, lead generation or enquiry volume, website referral traffic
- Month 12: brand awareness lift (from A&U or NPS data), sales influence estimate

**5. ROI Calculation**
Apply the TLV−COCA÷COCA formula from `meta-roi-framework`. Define TLV (Total Lifetime Value of a customer acquired via social) and COCA (Cost of Customer Acquisition through the social programme). Present two scenarios: conservative and realistic.

**6. Risk of Not Investing**
Restate the Revenue at Risk figure. Add reputational risk: if the brand is absent from social media when a crisis or negative conversation occurs, it cannot respond. Frame this as risk management.

**7. Recommended Starting Budget**
State the recommended tier, the monthly cost, and the 12-month total. Include a phased approach: start at Starter tier, review at month 3, scale to Growth tier if targets are met.

**8. Success Metrics and Review Cadence**
- Monthly: reach, impressions, follower growth, community response rate
- Quarterly: NPS, lead volume, A&U data point
- Annually: full ROI review using TLV−COCA÷COCA

---

## Section 7 — Presenting to the Board or C-Suite

### Language to Use

| Use this | Because |
|---|---|
| "Market share" | Finance and strategy language |
| "Competitive risk" | Triggers risk-management thinking |
| "Customer acquisition cost" | Connects to financial KPIs the board already tracks |
| "Lifetime value" | Frames social media as an investment, not a cost |
| "Share of voice" | Demonstrates market position vs. competitors |
| "Brand equity" | Recognised metric in marketing finance |

### Language to Avoid

| Avoid | Replace with |
|---|---|
| "Going viral" | "Achieving broad organic reach" |
| "Engagement" | "Customer interactions" or "community responses" |
| "Likes" | "Brand affinity signals" or omit entirely |
| "Content is king" | Present data; avoid clichés |
| "Everyone is on social media" | Present platform penetration data for Uganda specifically |

### Handling Objections

**"Our customers are not on social media."**
Respond with data. Facebook has approximately 3.2 million users in Uganda (Meta, 2024). WhatsApp penetration among smartphone users exceeds 90%. Ask: what is the client's target customer profile, and present platform demographics that match that profile. Offer to run a lightweight A&U poll on WhatsApp in the first 30 days to verify.

**"We tried it before and it didn't work."**
Ask what was tried, for how long, and how success was defined. In most cases: the previous attempt had no budget, no strategy, no dedicated resource, and no defined KPIs. Acknowledge the failure honestly. Present this business case as the difference between an unfunded experiment and a managed investment with defined outcomes and a review cadence. Commit to a 90-day review gate.

---

## Quality Criteria

Output from this skill meets the standard if:

1. **All financial calculations are transparent** — every figure shows its formula, assumptions, and data source; no black-box numbers
2. **The Revenue at Risk calculation is present and specific** — uses actual competitor follower data or a clearly stated proxy; states the conversion rate assumption explicitly
3. **Budget recommendations are calibrated to Uganda/EA** — figures are in UGX with USD equivalents; tiers are realistic for the Ugandan market
4. **Board language is used throughout** — competitive risk, customer acquisition cost, lifetime value; no social media jargon in the executive summary or recommendation sections
5. **Two ROI scenarios are presented** — conservative and realistic, using the TLV−COCA÷COCA formula and referencing `meta-roi-framework`
6. **Objection-handling language is included** — the business case anticipates and pre-empts the two most common objections (customers not on social media; previous failure)
7. **The document structure follows Section 6 exactly** — eight numbered sections in the correct order, suitable for direct submission to a board or finance committee
8. **British English throughout** — no American spellings; professional East African register consistent with `east-african-english` skill standards

---
name: meta-roi-framework
description: Calculates and presents the ROI of the client's social media and digital marketing investment using the Bodnar and Cohen (2012) formula: ROI = (TLV − COCA) ÷ COCA. Produces a step-by-step TLV calculation, COCA by channel, ratio benchmarks, attribution guidance, break-even analysis, a 12-month projection table, and consultant talking points for retainer justification. Invoke this skill when a client questions the value of the retainer, when preparing a proposal for a new client, or at a quarterly strategy review to demonstrate return on investment.
---

# ROI Framework

## Required Input

Before generating the ROI analysis, collect the following from the consultant:

- **Client name** and trading name (if different)
- **Industry** and sub-sector
- **Country / city** (default: Uganda / Kampala)
- **Primary goal** (e.g., grow customer base, increase revenue, justify retainer renewal)
- **Currency** (UGX or USD — use the client's primary operating currency throughout)
- **Average transaction value** (what the average customer spends per transaction)
- **Average number of transactions per year per customer** (how often a typical customer buys)
- **Average customer relationship length in years** (how long a typical customer remains a customer)
- **Monthly social media investment:**
  - Consultant / agency retainer fee
  - Content production costs (photography, video, copywriting if outsourced)
  - Paid ad spend (monthly average)
  - Total monthly investment
- **New customers acquired per month via digital channels** (estimated; ask the client to check CRM records or enquiry logs — even a rough estimate is useful)
- **Gross margin %** (revenue minus direct costs, expressed as a percentage of revenue)
- **Any available channel attribution data** (e.g., "20 enquiries last month came via WhatsApp, 5 via Facebook DM")

If the client cannot provide exact figures, ask for a reasonable estimate and document all assumptions in the output.

---

## Output Structure

Generate all seven sections below in order.

---

### 1. Total Lifetime Value (TLV) Calculation

Apply the formula from Bodnar and Cohen (2012):

**TLV = Average transaction value × Transactions per year × Customer relationship length (years)**

Walk through the calculation step by step:

| Input | Client value |
|---|---|
| Average transaction value | [Currency] [Amount] |
| Average transactions per year per customer | [Number] |
| Average customer relationship length | [Number] years |
| **Total Lifetime Value (TLV)** | **[Currency] [Amount]** |

**Worked example (Uganda context):**
A Kampala accounting firm charges UGX 1,200,000 per quarterly filing per client. The average client files 4 times per year and stays for 3 years.
TLV = UGX 1,200,000 × 4 × 3 = **UGX 14,400,000**

Produce the same worked example using the client's actual figures.

**Note:** If the client serves both high-value and low-value customer segments, calculate TLV separately for each segment. Use the segment most relevant to the digital acquisition strategy as the primary figure.

---

### 2. Cost of Customer Acquisition (COCA) by Channel

Apply the formula:

**COCA = Monthly social media spend ÷ New customers acquired per month via that channel**

| Channel | Monthly spend allocated | New customers/month | COCA |
|---|---|---|---|
| Facebook (organic + ads) | [Currency] [Amount] | [Number] | [Currency] [Amount] |
| Instagram (organic + ads) | [Currency] [Amount] | [Number] | [Currency] [Amount] |
| WhatsApp (broadcast + referral) | [Currency] [Amount] | [Number] | [Currency] [Amount] |
| LinkedIn (if applicable) | [Currency] [Amount] | [Number] | [Currency] [Amount] |
| TikTok (if applicable) | [Currency] [Amount] | [Number] | [Currency] [Amount] |
| **Total (all channels combined)** | [Currency] [Amount] | [Number] | **[Currency] [Amount]** |

**Where channel-level attribution is not available:**
Use total monthly investment ÷ total new customers from digital channels as the blended COCA. Note this as an estimate in the output and recommend the client implement enquiry source tracking (see Section 4).

**Where new customer numbers are unknown:**
Use enquiry volume as a proxy (COCA per enquiry) and apply the client's conversion rate to estimate COCA per customer. State all assumptions clearly.

---

### 3. COCA:TLV Ratio Interpretation

Calculate the ratio: **TLV ÷ COCA**

| Metric | Value |
|---|---|
| TLV | [Currency] [Amount] |
| COCA | [Currency] [Amount] |
| **TLV:COCA ratio** | **[X]:1** |

**Benchmark interpretation:**

| Ratio | Interpretation | Action |
|---|---|---|
| 10:1 or above | Excellent — significant return on acquisition spend | Increase investment in what is working; scale the best-performing channel |
| 5:1 to 9:1 | Healthy and sustainable | Maintain current approach; optimise underperforming channels |
| 3:1 to 4:1 | Borderline viable — monitor closely | Identify the highest-COCA channel and reduce spend there; focus on conversion rate improvement |
| Below 3:1 | Acquisition cost is too high relative to customer value | Either grow TLV (raise prices, add upsell, increase retention) or reduce COCA (better targeting, improved conversion funnel) |

State clearly where the client sits and what this means for the retainer decision.

**If TLV cannot be calculated (e.g., the client cannot estimate relationship length):**
Use a conservative single-transaction value as TLV and note this understates the true return. Recommend the client track customer retention data.

---

### 4. Attribution Methodology

For service businesses and B2B clients where direct digital attribution is difficult, implement the following tracking approach:

**Step 1 — Enquiry source logging**
Ask the client to record where every new enquiry comes from. Log the following for every new enquiry:

| Field | Options |
|---|---|
| Enquiry date | DD/MM/YYYY |
| Enquiry channel | WhatsApp / Facebook DM / Instagram DM / Phone call / Walk-in / Website form / Referral / Other |
| Referral source (if applicable) | Which social content, post, or profile triggered the referral |
| Converted to sale? | Yes / No / Pending |

Review this log monthly as part of the reporting cycle.

**Step 2 — UTM link tracking**
Place UTM-tagged links in all social media bios and any posts that direct traffic to the website. Use Google Analytics (free) to see which platform and which specific posts drive website visits and form submissions. UTM parameters: source, medium, campaign, content.

**Step 3 — Monthly enquiry source report**
Each month, count enquiries by source. This becomes the input for COCA calculation and shows directional channel performance.

**Important caveat:** Attribution is never perfect for social media. Social content influences purchasing decisions that are tracked to other channels (e.g., a customer sees an Instagram post, then calls the business directly). The goal of this methodology is directional understanding — not accounting-level precision.

---

### 5. Break-Even Analysis for Content Investment

Calculate how many new customers per month are needed to cover the social media investment:

**Break-even customers = Monthly investment ÷ (TLV × Gross margin %)**

| Input | Value |
|---|---|
| Monthly social media investment | [Currency] [Amount] |
| TLV | [Currency] [Amount] |
| Gross margin % | [%] |
| TLV × Gross margin | [Currency] [Amount] |
| **Break-even customers per month** | **[Number — round up]** |

**Worked example (Uganda context):**
A Kampala interior design firm invests UGX 3,500,000 per month in social media (retainer + production). TLV per client is UGX 12,000,000. Gross margin is 35%.

Break-even = UGX 3,500,000 ÷ (UGX 12,000,000 × 35%) = UGX 3,500,000 ÷ UGX 4,200,000 = **0.83 → 1 new client per month breaks even**

Produce the same calculation using the client's actual figures. Frame the result in plain language: "If social media brings in just [X] new customers per month, the investment pays for itself."

---

### 6. 12-Month ROI Projection Table

Build a monthly projection using a conservative new customer estimate (use the current monthly average, or the break-even number if current data is unavailable).

| Month | Projected new customers from social | COCA (est.) | TLV per customer | Monthly ROI | Cumulative ROI |
|---|---|---|---|---|---|
| Month 1 | | | | | |
| Month 2 | | | | | |
| Month 3 | | | | | |
| Month 4 | | | | | |
| Month 5 | | | | | |
| Month 6 | | | | | |
| Month 7 | | | | | |
| Month 8 | | | | | |
| Month 9 | | | | | |
| Month 10 | | | | | |
| Month 11 | | | | | |
| Month 12 | | | | | |
| **Total** | | | | | **[Cumulative ROI]** |

**Monthly ROI formula:** (TLV × customers acquired − Monthly investment) ÷ Monthly investment × 100

**Note:** These projections are estimates based on current trends. Revisit and update this table quarterly using actual customer acquisition data.

---

### 7. Talking Points for the Consultant

Use these points when presenting the ROI analysis to the client:

**Framing the retainer fee**
Do not present the retainer as a standalone cost. Present it relative to TLV: "Our monthly investment of [amount] needs to bring in [break-even number] new customers to pay for itself. Based on current enquiry volumes, we are [above / at / approaching] that threshold."

**The break-even argument**
"You do not need social media to bring in all your customers — only enough to justify the investment. At your TLV of [amount] and a gross margin of [%], you need [X] new customers per month from digital channels. We are currently tracking [Y] enquiries per month from social media."

**Comparison to traditional marketing**
If data allows, compare COCA via social media to the client's cost per referral via traditional marketing (events, print advertising, sales calls). Social media at scale often has a lower COCA than traditional methods — use this comparison if the numbers support it.

**When COCA is above the benchmark**
Do not deflect. Acknowledge it and recommend the specific action: "Our COCA is currently above the 5:1 benchmark. The most effective action is [grow TLV with a loyalty programme / improve our conversion rate from enquiry to sale / reduce ad spend on [underperforming channel] and reallocate to [higher-performing channel]]."

**Long-term framing**
Social media builds brand equity that is not captured in COCA. Organic reach, follower growth, and content library value compound over time. The ROI calculation covers direct acquisition — the full picture includes brand value that is harder to quantify but real.

---

## Quality Criteria

Output meets the standard if it:

- Uses the correct Bodnar and Cohen (2012) formula: ROI = (TLV − COCA) ÷ COCA
- All calculations are shown step by step with the client's actual figures — not only the final result
- COCA is calculated per channel where attribution data exists; blended COCA is used and labelled as an estimate where it does not
- Ratio interpretation names the specific action required at the client's ratio level — not generic advice
- Attribution methodology section gives the client a practical tracking system to implement, not a conceptual explanation
- Break-even calculation is expressed in plain language the client can use in a conversation
- 12-month projection table is populated with the client's figures and includes a clear caveat about projection assumptions
- Talking points are specific to the client's ratio and figures — not a generic script
- All currency figures use the client's specified currency (default UGX for Uganda)

---

## Framework Reference

Apply the **ROI formula** (Bodnar and Cohen, 2012): ROI = (TLV − COCA) ÷ COCA. Apply the **POEM model** when attributing spend across paid, owned, and earned channels.

*Bodnar, K. and Cohen, J. (2012) The B2B Social Media Book. Hoboken: Wiley.*
*Chaffey, D. (2024) Digital Marketing: Strategy, Implementation and Practice. 8th edn. Harlow: Pearson.*

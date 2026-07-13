---
name: meta-lead-scoring
description: "Use when designing and calibrating explicit, behavioural and decay rules with sales. Produces lead-scoring model and handover thresholds; use `meta-sales-marketing-alignment` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Lead Scoring Playbook


<!-- dual-compat-start -->
## Use When

- Use this skill for designing and calibrating explicit, behavioural and decay rules with sales.
- Confirm that `meta-sales-marketing-alignment` is not the closer route before proceeding.

## Do Not Use When

- Use `meta-sales-marketing-alignment` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Historical lead outcomes, crm fields and sales capacity | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Lead-scoring model and handover thresholds | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified lead-scoring model and handover thresholds. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Historical lead outcomes, crm fields and sales capacity is current and attributable | Produce the full lead-scoring model and handover thresholds and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `meta-sales-marketing-alignment` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `meta-sales-marketing-alignment` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the lead-scoring model and handover thresholds, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the lead-scoring model and handover thresholds without historical lead outcomes. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `meta-sales-marketing-alignment` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified historical lead outcomes, the skill produces a lead-scoring model and handover thresholds with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`meta-sales-marketing-alignment`](../meta-sales-marketing-alignment/SKILL.md) for the neighbouring contract.
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
4. **Primary goal** — what lead scoring must achieve (prioritise sales follow-up, demonstrate marketing ROI, reduce sales team time wasted on unqualified leads, improve conversion rate)
5. **Ideal customer profile** — describe the best customers in terms of company size, role, industry, location, and budget level (for B2B) or demographic and behaviour (for B2C)
6. **Sales team capacity** — how many qualified lead conversations the sales team can manage per week
7. **Current CRM or contact management tool** — what system stores lead data (spreadsheet, CRM, email platform)
8. **Available data** — what information is currently captured for each lead at the point of entry

---

## What Lead Scoring Is

Lead scoring is a numerical model that assigns point values to leads based on two dimensions:

- **Explicit attributes** — who the lead is (demographic and firmographic characteristics)
- **Implicit behaviours** — what the lead has done (signals of intent and engagement)

A lead whose total score crosses a defined threshold is forwarded to the sales team for immediate follow-up. A lead below the threshold re-enters the nurture sequence and accumulates score over time through further engagement. This ensures that the sales team's time is spent on the highest-probability buyers — not distributed equally across every contact regardless of intent.

---

## Explicit Scoring Criteria (Demographic / Firmographic)

These criteria describe the lead's fit with the ideal customer profile. A perfect explicit score indicates the lead looks like the best existing customers.

**B2B scoring model:**

| Criterion | Condition | Points |
|---|---|---|
| Job title / authority | Director, owner, or MD | 20 |
| | Manager or department head | 10 |
| | Executive or coordinator | 5 |
| | Unknown | 0 |
| Company size | Within target range | 20 |
| | Adjacent (slightly outside range) | 10 |
| | Outside target range | 0 |
| Industry | Primary target sector | 20 |
| | Secondary sector | 10 |
| | Out of scope | −10 |
| Budget indication | Confirmed budget aligned to pricing | 30 |
| | Estimated budget in range | 15 |
| | No indication | 0 |
| Location | Within service geography | 10 |
| | Outside service geography | −5 |

**B2C scoring model (adapt as required):**

| Criterion | Condition | Points |
|---|---|---|
| Age range | Primary target demographic | 15 |
| | Adjacent demographic | 5 |
| | Outside demographic | 0 |
| Income or spending level | High-value segment | 20 |
| | Mid-range segment | 10 |
| | Budget segment (if out of scope) | −5 |
| Location | Target city or region | 10 |
| | Outside target region | −5 |

Customise both models for the client's specific ideal customer profile. Do not apply the template without adapting the criteria to the client's actual product, pricing, and geography.

---

## Implicit Scoring Criteria (Behavioural)

These criteria measure what the lead has done. Behavioural signals are more powerful predictors of conversion than demographic fit alone — a contact who has visited the pricing page twice in one week is more likely to buy than a perfectly profiled lead who has never engaged with any content.

| Behaviour | Points | Rationale |
|---|---|---|
| Downloaded a lead magnet | 10 | Showed enough interest to exchange contact details |
| Attended a webinar or live event | 20 | High-intent action; invested time in the brand |
| Visited the pricing page (if trackable) | 25 | The single strongest behavioural signal available |
| Opened 3 or more emails in the nurture sequence | 15 | Consistent engagement with content |
| Clicked a link in an email | 10 | Moved beyond passive reading to active interest |
| Replied to an email or WhatsApp message | 20 | Initiated a two-way conversation |
| Visited the website 3 or more times in 7 days | 20 | Research behaviour indicates active consideration |
| Requested a consultation, quote, or call | 40 | Explicit buying signal — highest single behavioural score |
| Shared content or referred another contact | 15 | Advocacy behaviour; high engagement |
| Attended an in-person event or demo | 25 | Significant time and interest investment |

---

## Score Decay

Apply score decay to prevent stale leads retaining artificially high scores. A lead who was highly engaged six months ago but has not opened an email or visited the website since is not a hot prospect — they are a disengaged contact who should be in a re-engagement sequence, not on the sales team's priority list.

**Decay rule:** Deduct 10 points from the lead's score for every 30 days of inactivity.

| Inactivity Period | Score Deduction |
|---|---|
| 30 days | −10 points |
| 60 days | −20 points |
| 90 days | −30 points (trigger re-engagement sequence) |
| 120 days | −40 points (review for list removal) |

In practice, apply score decay as a monthly batch update. Most CRM tools and email platforms support automated score adjustment based on inactivity rules.

---

## Threshold Calibration with Sales

Do not set the scoring threshold in isolation. The threshold must be agreed with the sales team before the model goes live — and reviewed after 60 days of operation.

**Calibration process:**

1. Propose an initial threshold (recommended starting point: 60 points out of a maximum of approximately 175 points in a standard B2B model)
2. Run the model for 60 days without adjusting the threshold
3. At the 60-day review, ask the sales team:
   - Are the leads arriving above the threshold genuinely qualified?
   - Are there leads below the threshold that the sales team considers worth pursuing?
   - What is the conversion rate of threshold-crossing leads compared with the previous period?
4. Adjust the threshold up or down based on the answers
5. Repeat the review at 90 days and then quarterly

The scoring model is not a formula — it is a calibration conversation between marketing and sales, mediated by data. A model that marketing imposes on the sales team without their input will be ignored.

---

## BANT Qualification Layer

Apply BANT as a secondary qualification check for all leads that cross the scoring threshold. A lead with a high score that fails BANT should be returned to nurture, not forwarded to sales.

**BANT framework:**

| Dimension | Question | Signal |
|---|---|---|
| **Budget** | Has the lead indicated or implied a budget that aligns with the product pricing? | Confirmed = pass; absent = enquire before forwarding |
| **Authority** | Is this person a decision-maker or a recommender? | Decision-maker = pass; recommender = flag for multi-stakeholder approach |
| **Need** | Is there a stated or clearly implied business problem this product or service addresses? | Explicit need = pass; vague interest = return to nurture |
| **Timeframe** | Is there a defined decision date, a project deadline, or an urgency signal? | Defined timeframe = pass; open-ended = lower priority |

A lead that crosses the scoring threshold and passes all four BANT dimensions is a Marketing Qualified Lead (MQL) — ready for sales handover. Document the BANT assessment in the CRM record at the point of handover.

---

## East Africa Application

For most EA clients — particularly SMEs with limited CRM data — a simple scoring model with five to eight criteria is more effective than a complex one. Begin with the four highest-signal behaviours and add criteria as data quality improves.

**Recommended starter model for EA clients:**

| Criterion | Points |
|---|---|
| Attended a webinar or live event | 20 |
| Visited the pricing page | 25 |
| Replied to a WhatsApp message or email | 20 |
| Requested a consultation or quote | 40 |
| **Suggested threshold** | **40 points** |

At a threshold of 40 points, a single consultation request triggers immediate sales follow-up — as it should. Two or more moderate signals in combination also cross the threshold. Review and expand the model at the 60-day calibration.

---

## Output: Lead Scoring Design Document

Generate the following for the client:

1. **Explicit scoring table** — customised to the client's ideal customer profile; all criteria and point values documented
2. **Implicit scoring table** — behavioural criteria relevant to the client's channels and content types
3. **Score decay rule** — stated clearly with monthly deduction schedule
4. **Initial threshold recommendation** — with rationale
5. **60-day calibration protocol** — questions for the sales review meeting and adjustment methodology
6. **BANT qualification checklist** — to be completed by the sales team for every lead crossing the threshold
7. **CRM implementation notes** — how to configure scoring in the client's existing tool (or recommendation for a simple spreadsheet model if no CRM is in use)
8. **Monthly review report template** — lead score distribution, threshold crossings, MQL-to-deal conversion rate

---

## Quality Criteria

Output meets the standard when:

1. Scoring model is built collaboratively with the client's sales team — the threshold and criteria are agreed, not imposed by marketing alone
2. Both explicit (demographic or firmographic) and implicit (behavioural) criteria are included in the model — a model with only one dimension is incomplete
3. Score decay is applied — the model reduces scores for inactive leads on a monthly schedule; no lead retains a high score indefinitely without recent engagement
4. Initial threshold is set, formally reviewed at 60 days, and adjusted based on sales feedback — the model is treated as a living calibration, not a fixed formula
5. BANT framework is applied as a secondary check on all leads crossing the threshold before they are handed to the sales team
6. The scoring model is documented in a shared spreadsheet or CRM field accessible to both marketing and sales — neither team operates from a version the other cannot see
7. Lead score distribution is reviewed monthly as a leading indicator of campaign quality — a shift in score distribution signals a change in lead quality before conversion data is available

---

## References

Kahan, R. (2022) *High-Velocity Digital Marketing: 7 Proven Strategies to Send Your Revenue Soaring Using Today's Best Digital Practices*. Amplify Publishing.

Zahay, D. et al. (2024) *Digital Marketing Management: A Handbook for the Current (or Future) CEO*. 3rd edn. Business Expert Press.

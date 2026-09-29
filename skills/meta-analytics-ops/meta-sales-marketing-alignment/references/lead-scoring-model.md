# Lead Scoring Model

Merged from skills/meta-analytics-ops/meta-lead-scoring on 2026-09-29 at 8eacccb; preservation map: [meta-lead-scoring.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/meta-lead-scoring.md)

## When to use this reference

Read this reference when the client needs a full lead-scoring design document rather than the short starter model in the SKILL.md `Lead Scoring Foundation`: explicit (fit) and implicit (behaviour) scoring tables, score decay, a threshold calibrated with sales, a BANT check before handover and CRM set-up notes. The SKILL.md prerequisites still apply: the CRM must be adopted before scoring goes live, and the handover SLA governs what happens after a lead crosses the threshold.

Lead scoring is a numerical model that gives each lead points on two dimensions:

- **Explicit attributes**: who the lead is (demographic and firmographic fit with the ideal customer profile).
- **Implicit behaviours**: what the lead has done (signals of intent and engagement).

A lead whose total crosses the agreed threshold goes to sales for immediate follow-up. A lead below it re-enters the nurture sequence and builds score through further engagement. Sales time then goes to the highest-probability buyers instead of being spread evenly across every contact regardless of intent.

## Inputs

Ask for the following before generating any output:

| Input | What to capture |
|---|---|
| Business name | Trading name of the client |
| Industry | Sector and niche |
| Country / city | Default Uganda/East Africa |
| Primary goal | What scoring must achieve: prioritise sales follow-up, demonstrate marketing ROI, reduce sales time wasted on unqualified leads, or improve conversion rate |
| Ideal customer profile | Best customers by company size, role, industry, location and budget level (B2B), or by demographic and behaviour (B2C) |
| Sales team capacity | How many qualified lead conversations sales can manage per week |
| Current CRM or contact tool | Where lead data lives (spreadsheet, CRM, email platform) |
| Available data | What is captured for each lead at the point of entry |
| Historical lead outcomes (won/lost with source and CRM fields) | From the CRM owner; if absent, mark the threshold provisional and recalibrate at 60 days |

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| Building the model | Include both explicit and implicit criteria; a one-dimension model is incomplete. Customise every criterion to the client's product, pricing and geography. | Applying the template unchanged; fit-only or behaviour-only scores. |
| Explicit fit and behaviour disagree | Weight behaviour more heavily: a contact who viewed the pricing page twice in one week is likelier to buy than a perfectly profiled lead who has never engaged. | Chasing well-profiled but cold contacts. |
| A lead has been inactive | Deduct 10 points per 30 days of inactivity (schedule below). | Stale leads keeping artificially high scores. |
| Setting the threshold | Agree it with sales before go-live; never set it in isolation. | A model imposed by marketing that sales ignores. |
| A lead crosses the threshold but fails BANT | Return it to nurture; do not forward it to sales. | Handing sales high-score leads with no budget, authority, need or timeframe. |
| The client is an East Africa SME with thin CRM data | Start with 5–8 criteria, beginning with the four highest-signal behaviours (starter model below); add criteria as data quality improves. | A complex model the data cannot support. |
| No CRM is in use | Recommend a simple shared spreadsheet model in the CRM implementation notes (and see the SKILL.md `CRM as Single Source of Truth`). | Scoring that lives in one person's inbox. |

The point values, the 60-point and 40-point thresholds and the decay schedule are practitioner starting points, not measured East Africa benchmarks. Verify before stating (no register record); calibrate them with the client's own conversion data.

## Procedure

1. Build the **explicit scoring table** from the ideal customer profile (templates below).
2. Build the **implicit scoring table** from the behaviours the client's channels and content can actually track.
3. Set the **decay rule** and schedule it as a monthly batch update. Most CRM tools and email platforms support automated score adjustment from inactivity rules.
4. Propose an **initial threshold** with rationale and agree it with sales.
5. Run the model for 60 days without changing the threshold, then hold the **calibration review** (below).
6. Apply **BANT** to every lead that crosses the threshold, and document the BANT assessment in the CRM record at handover.
7. Review the **lead score distribution** monthly as a leading indicator of campaign quality: a shift in distribution signals a change in lead quality before conversion data arrives.

### Explicit scoring: B2B template

| Criterion | Condition | Points |
|---|---|---|
| Job title / authority | Director, owner or MD | 20 |
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

### Explicit scoring: B2C template (adapt as required)

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

A perfect explicit score means the lead looks like the client's best existing customers.

### Implicit (behavioural) scoring

| Behaviour | Points | Rationale |
|---|---|---|
| Downloaded a lead magnet | 10 | Interested enough to exchange contact details |
| Attended a webinar or live event | 20 | High-intent action; invested time in the brand |
| Visited the pricing page (if trackable) | 25 | The strongest single behavioural signal available |
| Opened 3 or more emails in the nurture sequence | 15 | Consistent engagement with content |
| Clicked a link in an email | 10 | Moved from passive reading to active interest |
| Replied to an email or WhatsApp message | 20 | Started a two-way conversation |
| Visited the website 3 or more times in 7 days | 20 | Research behaviour shows active consideration |
| Requested a consultation, quote or call | 40 | Explicit buying signal; highest single behavioural score |
| Shared content or referred another contact | 15 | Advocacy; high engagement |
| Attended an in-person event or demo | 25 | Significant investment of time and interest |

### Score decay

A lead who was highly engaged six months ago but has not opened an email or visited the site since is not a hot prospect. It is a disengaged contact that belongs in a re-engagement sequence, not on the sales priority list.

| Inactivity period | Score deduction |
|---|---|
| 30 days | −10 points |
| 60 days | −20 points |
| 90 days | −30 points (trigger re-engagement sequence) |
| 120 days | −40 points (review for list removal) |

### Threshold calibration with sales

1. Propose an initial threshold. Recommended starting point: 60 points out of a maximum of about 175 in a standard B2B model.
2. Run the model for 60 days without adjusting the threshold.
3. At the 60-day review ask sales: Are leads arriving above the threshold genuinely qualified? Are there leads below it that sales considers worth pursuing? What is the conversion rate of threshold-crossing leads compared with the previous period?
4. Move the threshold up or down based on the answers.
5. Repeat the review at 90 days, then quarterly.

The model is not a formula. It is a calibration conversation between marketing and sales, settled with data.

### BANT qualification layer

| Dimension | Question | Signal |
|---|---|---|
| **Budget** | Has the lead indicated or implied a budget that fits the product pricing? | Confirmed = pass; absent = enquire before forwarding |
| **Authority** | Is this person a decision-maker or a recommender? | Decision-maker = pass; recommender = flag for a multi-stakeholder approach |
| **Need** | Is there a stated or clearly implied business problem the product or service addresses? | Explicit need = pass; vague interest = return to nurture |
| **Timeframe** | Is there a defined decision date, project deadline or urgency signal? | Defined timeframe = pass; open-ended = lower priority |

A lead that crosses the threshold and passes all four dimensions is a Marketing Qualified Lead (MQL), ready for handover under the SKILL.md `Lead Handover SLA`.

### East Africa starter model

| Criterion | Points |
|---|---|
| Attended a webinar or live event | 20 |
| Visited the pricing page | 25 |
| Replied to a WhatsApp message or email | 20 |
| Requested a consultation or quote | 40 |
| **Suggested threshold** | **40 points** |

At 40 points a single consultation request triggers immediate sales follow-up, as it should, and two or more moderate signals together also cross the threshold. Review and expand the model at the 60-day calibration. The SKILL.md `Lead Scoring Foundation` adds WhatsApp-specific signals (question in reply to a broadcast, price-list request) that fit this starter model.

## Output: lead scoring design document

1. **Explicit scoring table**: customised to the client's ideal customer profile, with every criterion and point value documented.
2. **Implicit scoring table**: behaviours relevant to the client's channels and content types.
3. **Score decay rule**: stated clearly with the monthly deduction schedule.
4. **Initial threshold recommendation**: with rationale.
5. **60-day calibration protocol**: questions for the sales review meeting and the adjustment method.
6. **BANT qualification checklist**: completed by sales for every lead crossing the threshold.
7. **CRM implementation notes**: how to configure scoring in the client's existing tool, or a simple spreadsheet model if no CRM is in use.
8. **Monthly review report template**: lead score distribution, threshold crossings, MQL-to-deal conversion rate.

## Release checklist

- [ ] The model is built with the client's sales team; threshold and criteria are agreed, not imposed by marketing alone.
- [ ] Both explicit (demographic or firmographic) and implicit (behavioural) criteria are included.
- [ ] Score decay reduces inactive leads' scores on a monthly schedule; no lead keeps a high score indefinitely without recent engagement.
- [ ] The initial threshold is set, formally reviewed at 60 days and adjusted from sales feedback; the model is treated as a living calibration.
- [ ] BANT is applied to every lead crossing the threshold before handover to sales.
- [ ] The model sits in a shared spreadsheet or CRM field that both marketing and sales can see; neither team works from a version the other cannot see.
- [ ] Lead score distribution is reviewed monthly as a leading indicator of campaign quality.

## Sources

Kahan, R. (2022) *High-Velocity Digital Marketing: 7 Proven Strategies to Send Your Revenue Soaring Using Today's Best Digital Practices*. Amplify Publishing.

Zahay, D. et al. (2024) *Digital Marketing Management: A Handbook for the Current (or Future) CEO*. 3rd edn. Business Expert Press.

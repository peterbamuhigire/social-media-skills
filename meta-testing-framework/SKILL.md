---
name: meta-testing-framework
description: >
  Designs structured A/B tests and content experiments for social media campaigns and organic content.
  Calibrated for Uganda/East Africa markets with limited budgets (UGX 50,000–200,000 per test).
  Invoke this skill when a client wants to know what content, creative, copy, or audience approach
  performs best before committing their full budget or monthly content plan to it. Also invoke when
  a client is seeing inconsistent results and needs a systematic method to identify what is working.
---
# meta-testing-framework

A structured approach to experiment design, A/B testing, and result interpretation for social media
content and campaigns in Uganda and East Africa.

---

<!-- dual-compat:start -->
## Use when
- Designs structured A/B tests and content experiments for social media campaigns and organic content. Calibrated for Uganda/East Africa markets with limited budgets (UGX 50,000–200,000 per test). Invoke this skill when a client wants to know what content, creative, copy, or audience approach performs best before committing their full budget or monthly content plan to it. Also invoke when a client is seeing inconsistent results and needs a systematic method to identify what is working.
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

Ask for all of the following before generating any test design:

1. **Client business name and industry** — e.g., "Kampala Fresh, FMCG grocery delivery"
2. **Country and city** — default is Uganda; specify if Nairobi, Dar es Salaam, Kigali, etc.
3. **Primary goal** — what the client is ultimately trying to improve (sales, enquiries, followers, reach)
4. **Platform focus** — Facebook, TikTok, Instagram, LinkedIn, or a combination
5. **Current monthly ad budget (if any)** — in UGX or USD; state "organic only" if no paid budget
6. **What they want to test** — creative, copy/caption, audience segment, CTA, or posting time
7. **Access to platform analytics** — Meta Ads Manager, TikTok Ads Manager, native insights, or none
8. **Duration they can commit** — minimum 7 days; ask if they have any blackout dates

---

## Section 1 — Testing Principles

### One Variable at a Time

Change only one element per test. If two elements change simultaneously — for example, a new image
and a new caption — there is no way to know which change caused the difference in results.
This rule is non-negotiable. Enforce it with the client even when they push back.

**What breaks when multiple variables change:**
- Results become unattributable — the client learns nothing actionable
- Budget is wasted on data that cannot inform future decisions
- The test must be repeated, costing more time and money

**Example of a correctly isolated test:**
- Control: same image, caption A ("Order now — same-day delivery in Kampala")
- Variant: same image, caption B ("Delivered to your door in 3 hours — order before 2pm")
- Only the caption changes. All other variables — image, audience, budget, schedule — are identical.

### Statistical Significance

Require enough data before declaring a winner. The minimum thresholds are:

- **Paid tests:** 50 conversions per variant, or 1,000 impressions per variant, whichever comes first
- **Organic tests:** 200 organic reach per post, or 48 hours after publishing, whichever comes later

Meta Ads Manager displays a statistical confidence score in the A/B test results panel.
Require a minimum of **90% confidence** before acting on paid test results.

For organic posts on small accounts, statistical significance is rarely achievable.
Use **directional data** — if one format consistently outperforms another across three or more tests,
treat that as sufficient evidence to update the content plan.

### Practical Significance

Distinguish between statistical significance and practical significance.

A 2% improvement in click-through rate on a page with 500 monthly visitors produces 10 extra clicks.
If each click is worth UGX 500, that is UGX 5,000 per month. The cost of running and tracking the test
likely exceeds the gain. Apply this filter before recommending a test: ask whether a realistic positive
result would produce a meaningful improvement in the client's business.

Apply the ROI formula from Bodnar and Cohen (2012): **(TLV − COCA) ÷ COCA**. If the test cannot move
COCA (cost of customer acquisition) by a meaningful margin, deprioritise it.

### Test Duration

- **Minimum:** 7 days — shorter periods miss weekly audience behaviour cycles
- **Maximum:** 4 weeks — longer tests accumulate too many confounding variables (promotions, news events, algorithm updates)
- **Never stop a test early**, even if one variant appears to be winning. Early stopping inflates the
  apparent effect size and leads to false conclusions. This is the most common mistake in social media testing.

---

## Section 2 — What to Test (Priority Order)

Test elements in this order. Higher items produce larger improvements for the same effort.

1. **Headline / hook** — first line of caption or first 3 seconds of video. This is the single
   highest-leverage element. On Facebook and TikTok, users decide within 2–3 seconds whether to
   stop scrolling. Test a question-format hook against a statement hook, or a local cultural reference
   against a generic one. *Example: "Tired of waiting for delivery?" vs "Same-day delivery is here."*

2. **Visual format** — static image vs Reel vs carousel. In Uganda, Reels and short video
   consistently outperform static images for reach; however, static images often produce higher
   click-through for product offers. Test format before assuming video is always better.

3. **Call to action** — button text (if paid) or closing line (if organic). Test directive language
   against benefit-led language. *Example: "Shop now" vs "See today's prices".*

4. **Audience segment** — by age bracket, location (Kampala central vs greater Kampala vs upcountry),
   or declared interest. Keep the creative identical; only the audience definition changes.

5. **Posting time** — EAT morning window (7–9am, commute and pre-work) vs evening window (6–8pm,
   post-work). Note: WhatsApp and Facebook see a secondary peak at 12–1pm (lunch). Test within
   one timezone; cross-country tests require separate audience controls.

6. **Caption length** — short (under 50 words) vs long (over 150 words). Long captions can build
   authority for B2B and educational content; short captions typically perform better for
   product-led and entertainment content on TikTok and Instagram.

7. **Hashtag set** — branded only vs mixed (branded + category + niche) vs no hashtags.
   On Facebook, hashtags have minimal reach impact; on TikTok and Instagram, they contribute to
   discovery. Test in the relevant platform context.

---

## Section 3 — Test Design Templates

Use one of the three templates below. Fill every field before the test begins.

---

### Template A — A/B Creative Test (Paid)

```
Hypothesis:     "Changing [element] from [A] to [B] will increase [metric]
                 because [reason]."
                 Example: "Changing the caption hook from a question to a
                 benefit statement will increase link clicks because our
                 audience responds to direct value cues."

Control:        [Describe Ad A — creative, copy, format]
Variant:        [Describe Ad B — single changed element only]
Platform:       [Facebook / TikTok / Instagram]
Audience:       [Define precisely — keep identical for both variants]
Budget split:   50/50 (recommended) or 60/40 if budget is under UGX 100,000
Total budget:   UGX [amount] over [X] days
Duration:       [Start date] → [End date] — minimum 7 days
Primary metric: [Reach / Engagement rate / Link clicks / Cost per result]
Decision rule:  Declare the variant the winner if it outperforms the control
                by at least [10%] with a minimum of [1,000 impressions per
                variant] and [90%] confidence in Meta Ads Manager.
Next action:    [What changes in next month's plan if the variant wins]
```

---

### Template B — Organic Post Test

```
Hypothesis:     [Same format as Template A]

Post A:         [Description — format, hook, caption, CTA, hashtags]
Post B:         [Description — single element changed]
Schedule:       Post A on [date + time]. Post B exactly one week later at
                the same time on the same day of the week.
                Do not run both posts in the same week — audience overlap
                distorts results.
Measurement:    Screenshot metrics for both posts at exactly 48 hours
                after each goes live. Record reach, likes, comments, shares,
                saves, and profile visits.
Primary metric: Engagement rate = (likes + comments + shares) ÷ reach × 100
Decision rule:  Whichever post produces a higher engagement rate is
                directionally preferred. If the margin is under 5 percentage
                points, treat as inconclusive and run a second round.
Next action:    Carry the winning format into the following month's
                content calendar.
```

---

### Template C — Audience Segment Test (Paid)

```
Hypothesis:     "Audience segment [A] will produce a lower cost per result
                 than segment [B] for [creative X] because [reason]."

Creative:       [Identical for both — do not change any element]
Audience A:     [Define precisely: age, location, interests, behaviours]
Audience B:     [Define precisely: single dimension differs from Audience A]
Platform:       [Facebook / TikTok]
Budget split:   50/50
Total budget:   UGX [amount]
Duration:       [Start date] → [End date]
Primary metric: Cost per result (paid) — e.g., cost per link click, cost per
                lead form submission
Decision rule:  The segment with the lower cost per result at end of test
                period becomes the primary target audience for the next
                campaign cycle.
```

---

## Section 4 — Tracking Sheet

Create a Google Sheets document with the following columns. Record every test, including
inconclusive ones.

| Column | What to enter |
|---|---|
| **Test #** | Sequential number — T001, T002, T003 |
| **Hypothesis** | Full hypothesis statement as written in the template |
| **Element Tested** | Hook / Format / CTA / Audience / Time / Caption length / Hashtags |
| **Control** | Brief description of the A variant |
| **Variant** | Brief description of the B variant |
| **Platform** | Facebook / TikTok / Instagram / Organic |
| **Start Date** | DD/MM/YYYY |
| **End Date** | DD/MM/YYYY |
| **Metric** | The single primary metric used to judge the test |
| **Control Result** | Numeric result for A — e.g., 3.2% engagement rate |
| **Variant Result** | Numeric result for B |
| **Winner** | A / B / Inconclusive |
| **Confidence** | % confidence from platform (paid), or "Directional" (organic) |
| **Action** | What changed in the content plan or next campaign as a result |

Add a **Notes** column for anomalies: a post that went viral, a public holiday, a platform
outage, or a news event that may have distorted results.

---

## Section 5 — Reading Results

### Meta Ads Manager A/B Test Results

Navigate to: Ads Manager → Experiments → A/B Test. Meta reports:

- **Cost per result** for each variant
- **Statistical confidence** as a percentage
- **Winning variant** (only displayed when confidence exceeds 95% in Meta's default setting)

Require 90% confidence as the minimum threshold when managing the account manually.
Do not act on results before the scheduled end date, even if Meta displays a winning variant early.

### Organic Post Comparison

1. Set a reminder to screenshot each post's native insights at exactly 48 hours after publishing.
2. Record reach, impressions, likes, comments, shares, and saves in the tracking sheet.
3. Calculate engagement rate manually: (likes + comments + shares) ÷ reach × 100.
4. Do not compare posts published in different weeks if a public holiday or major event fell
   in between — flag those results as potentially distorted in the Notes column.

### Common Mistakes

- **Declaring a winner too early** — the most frequent error. Enforce the minimum duration and
  minimum sample size rules with every client.
- **Not controlling the audience** — for paid tests, ensure both variants target an identical
  audience definition. Even a single interest difference invalidates the comparison.
- **Ignoring seasonal variation** — a post published during a national holiday week will
  outperform or underperform for reasons unrelated to the content. Flag and discard these results.
- **Changing the creative mid-test** — once a test begins, nothing changes. If a client requests
  an edit, stop the test, record it as inconclusive, and restart.
- **Comparing across platforms** — a Facebook result does not transfer directly to TikTok.
  Run platform-specific tests.

---

## Section 6 — Building a Testing Calendar

### Monthly Cadence

Run a maximum of **1–2 tests per month**. Running more simultaneously creates audience overlap
(for paid) and cognitive overload in the tracking process. Prioritise tests with the highest
potential impact on the client's primary metric.

### Periods to Avoid in Uganda/East Africa

Do not start a test during the following periods — results will be distorted by abnormal
audience behaviour:

| Period | Approximate dates | Why to avoid |
|---|---|---|
| Ramadan | Varies (lunar calendar) | Significant shift in online activity hours and purchasing patterns |
| Christmas / New Year | 20 Dec – 5 Jan | Elevated emotional content consumption; distorts engagement benchmarks |
| Uganda Independence Day | 9 October | Spike in patriotic and political content suppresses other categories |
| School holidays (Uganda) | Jan, Apr, Aug, Dec | Audience composition shifts significantly for youth-skewed products |
| Election periods | As declared | Organic reach suppressed; political content dominates feeds |
| End of financial year | June (public sector) | B2B engagement drops sharply |

If a test is already running when one of these periods begins, note the dates in the tracking
sheet and weight results accordingly.

### Negative Results Are Data

Record every test result, including inconclusive tests. Over 6–12 months, the tracking log
becomes the most valuable strategic asset in the account. Patterns emerge: certain content formats
consistently underperform, certain audience segments produce lower costs, certain posting times
hold up across seasons. These patterns are not visible without a complete record.

---

## EA-Specific Considerations

### Budget Realities

Most clients in Uganda and East Africa cannot sustain the sample sizes required for statistical
significance in paid tests. The practical approach:

- **Micro-budget paid tests:** UGX 50,000–200,000 (approximately USD 13–53) per test.
  This is sufficient for directional data on Facebook and TikTok at Ugandan CPM rates.
- **Organic-first testing:** For clients with no paid budget, run organic post tests using
  Template B. Two posts per test, one week apart, measured at 48 hours. This costs nothing
  and produces actionable directional data within a fortnight.
- **Avoid testing below UGX 30,000** — the sample size will be too small to be directional.

### Platform Priority for Paid Testing in Uganda

1. **Facebook** — widest reach, lowest CPM for mass-market products; use for audience and
   format tests
2. **TikTok** — fast-growing, strong for 16–30 demographic; use for hook and creative format tests
3. **Instagram** — urban, 18–35; use for visual format and caption length tests for
   aspirational or lifestyle brands
4. LinkedIn paid testing is not recommended for most Ugandan clients — CPM is too high relative
   to the addressable professional audience size.

### Data Limitations on Small Accounts

Small accounts (under 5,000 followers or under UGX 500,000/month in ad spend) will rarely
achieve statistical significance. Apply the following adjustments:

- Use **directional data** and professional judgement rather than waiting for 90% confidence
- Run **three rounds** of the same test type before drawing conclusions (e.g., three hook tests)
- Document the pattern across rounds in the tracking sheet — three consistent directional
  results are more reliable than one statistically significant result from an underpowered test

### Mobile-First Testing

95%+ of East African users view social media content on mobile. Before publishing any test variant:

- Preview all creatives on a mobile screen (not desktop)
- Ensure caption text is legible without expanding — front-load key information in the first two lines
- Verify that any link or CTA button is thumb-reachable on standard smartphone screens
- Test video for watchability with sound off — most users scroll with audio muted

---

## Quality Criteria

Output from this skill meets the standard when:

- Every hypothesis follows the exact format: "Changing [element] from [A] to [B] will increase
  [metric] because [reason]" — no vague or untestable hypotheses are accepted
- The one-variable rule is enforced without exception — each test isolates exactly one element
- The tracking sheet template is populated with column guidance specific to the client's platform
  and metric, not left as a generic blank
- Every test design includes a precise decision rule with a numeric threshold (e.g., 10% improvement,
  1,000 impressions minimum) — no open-ended "we'll see how it goes" declarations
- Budget recommendations are calibrated to EA realities: micro-budget paid tests (UGX 50,000–200,000)
  or organic-only templates when no paid budget exists
- Minimum sample sizes are stated explicitly (50 conversions or 1,000 impressions for paid;
  200 organic reach or 48 hours for organic) and applied to the specific platform in scope
- The testing calendar flags at least the Uganda-specific blackout periods relevant to the
  client's product category and audience

---

## References

- **`meta-reporting/SKILL.md`** — use after test completion to interpret results within the
  broader monthly reporting cycle and format findings for client presentation
- **`meta-roi-framework/SKILL.md`** — apply the ROI formula when evaluating whether a test's
  potential upside justifies the time and budget investment before designing the test
- **`09-campaign-strategy/SKILL.md`** — consult when test results need to be translated into
  campaign strategy decisions or when structuring a test within a broader campaign architecture

**Academic references:**
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book.* Hoboken: Wiley.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice.* 8th edn. Harlow: Pearson.
- Kotler, P. et al. (2023) *Marketing Management.* 16th edn. Harlow: Pearson.

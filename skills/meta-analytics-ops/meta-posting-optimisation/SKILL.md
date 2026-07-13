---
name: meta-posting-optimisation
description: "Use when testing posting times and frequency against account-level performance data. Produces posting optimisation test plan and evidence-led schedule; use `meta-algorithm-guide` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Meta — Posting Time and Frequency Optimisation

## Purpose

"Best time to post on Instagram" articles report global averages that are wrong for most
individual accounts and systematically wrong for Ugandan and East African audiences, who
use social media at different times than US or UK users. The correct answer comes from
the client's own analytics, not published studies.

This skill produces a client-specific posting schedule — including day, time (EAT),
platform, format, and content direction — derived from native analytics data, EA market
context, and a 4-week structured test.

**Cross-reference:**
- `meta-algorithm-guide` — algorithm ranking factors that interact with posting timing
- `11-content-calendar` — use the output schedule to populate the editorial calendar

---


<!-- dual-compat-start -->
## Use When

- Use this skill for testing posting times and frequency against account-level performance data.
- Confirm that `meta-algorithm-guide` is not the closer route before proceeding.

## Do Not Use When

- Use `meta-algorithm-guide` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Timestamped post performance, audience timezone and production capacity | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Posting optimisation test plan and evidence-led schedule | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified posting optimisation test plan and evidence-led schedule. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Timestamped post performance, audience timezone and production capacity is current and attributable | Produce the full posting optimisation test plan and evidence-led schedule and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `meta-algorithm-guide` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `meta-algorithm-guide` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the posting optimisation test plan and evidence-led schedule, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the posting optimisation test plan and evidence-led schedule without timestamped post performance. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `meta-algorithm-guide` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified timestamped post performance, the skill produces a posting optimisation test plan and evidence-led schedule with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`meta-algorithm-guide`](../meta-algorithm-guide/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Input

Before generating any output, ask the client or consultant for:

1. **Client business name** and **industry**
2. **Country and city** of primary audience
3. **Platforms in scope** (list all active platforms)
4. **Current posting frequency** per platform (posts per week)
5. **Access to native analytics** — can the consultant log in directly, or are screenshots
   provided?
6. **Team capacity** — hours per week available for content production
7. **Primary audience age range and city** (affects EA time window assumptions)

Do not proceed until all seven inputs are confirmed.

---

## Section 1: Read Your Own Analytics First

Before recommending any posting schedule, extract peak activity data from native analytics
on each platform in scope.

### Facebook — Meta Business Suite

Navigate to: **Meta Business Suite → Insights → Audience → When Your Fans Are Online**

Extract:
- The 3 highest-activity hours for each weekday (Monday–Friday)
- The 1 highest-activity hour for Saturday and Sunday separately
- Note any consistent daily pattern (e.g., morning spike every weekday)

**Important:** this shows when fans are online, not necessarily when they engage. Use it
as the starting point; the 4-week test (Section 3) confirms whether online presence
translates to engagement.

### Instagram — Professional Dashboard

Navigate to: **Professional Dashboard → Insights → Total Followers → Most Active Times**

Extract:
- Hourly activity by day of week
- Compare directly to Facebook findings — the same audience is often active at different
  times on each platform, even if the demographics overlap

### LinkedIn — Company Page Analytics

Navigate to: **Company Page → Analytics → Followers → Follower Activity**

LinkedIn shows follower activity by **day of week only**, not by hour. Use this for
day-of-week decisions rather than time-of-day decisions.

EA LinkedIn baseline: Monday–Thursday are the highest-activity days; Friday drops
noticeably; weekend activity is minimal. Confirm against the client's own follower data
before applying this assumption.

### TikTok — Creator Tools

Navigate to: **Creator Tools → Analytics → Followers → Follower Activity**

Extract:
- Hourly activity chart
- Use this for TikTok post timing and for Instagram Reels cross-posting decisions

### YouTube — YouTube Studio

Navigate to: **YouTube Studio → Analytics → Audience → When viewers are on YouTube**

Extract:
- Hour-by-hour activity chart across the week
- Use to schedule video publication times and, where applicable, Premiere scheduling

---

## EA Baseline Windows (Use When No Prior Analytics Exist)

Apply these windows for new accounts or accounts with fewer than 90 days of analytics
data. Replace with native data as soon as it is available.

All times are **East Africa Time (EAT — UTC+3)**.

| Platform | EA Peak Windows |
|---|---|
| Facebook | 07:00–09:00 (morning commute), 12:00–13:30 (lunch), 20:00–22:00 (evening) |
| Instagram | 12:00–14:00, 19:00–21:00 |
| TikTok | 19:00–23:00 |
| LinkedIn | 07:00–09:00 Monday–Thursday only |
| WhatsApp Broadcast | 07:00–08:30 or 19:00–20:30 |
| X/Twitter | 07:00–10:00 (news cycle), 17:00–19:00 |

### Why EA Times Differ from Global Benchmarks

- Uganda is UTC+3. Global "optimal time" studies typically report US Eastern or UK times,
  which are 8–11 hours behind EAT. Applying those figures directly produces the wrong
  schedule.
- **Boda-boda commuting culture:** mobile usage spikes at 07:00–09:00 during the commute
  across all income segments.
- **Afternoon dip:** 14:00–17:00 is a productivity window for office workers; social
  media engagement is low.
- **Evening spike:** 19:00–22:00 is the highest-engagement window for consumer content.
  Users are home, often on WiFi, with discretionary time.
- **Data cost sensitivity:** usage patterns cluster around WiFi access — office in the
  morning, home in the evening. Mobile data costs shape when people scroll.

---

## Section 2: Frequency Decision Framework

The correct posting frequency is the highest frequency at which full quality can be
maintained. Quantity without quality destroys engagement rate, which reduces algorithmic
reach, which degrades performance of every subsequent post.

### Frequency Floors and Ceilings by Platform

| Platform | Minimum (viable) | Optimal (EA context) | Maximum (before quality drops) |
|---|---|---|---|
| Facebook | 3/week | 5/week | 7/week |
| Instagram Feed | 3/week | 5/week | 7/week |
| Instagram Stories | 3/week | 5–7/week | Daily |
| Instagram Reels | 1/week | 3/week | 5/week |
| TikTok | 3/week | 5/week | Daily |
| LinkedIn | 2/week | 3–4/week | 5/week |
| YouTube | 1/week | 1–2/week | 3/week |
| WhatsApp Broadcast | 1/week | 2/week | 3/week |
| X/Twitter | 3/week | 5/week | Multiple daily |

**WhatsApp Broadcast note:** exceeding 3 broadcasts per week materially increases
opt-outs in EA markets, where users treat broadcast lists as a trusted inner circle.
Protect that relationship by keeping frequency conservative and content genuinely useful.

### Three Questions Before Setting Frequency

Ask and record answers for each platform in scope:

1. Can the team produce this many posts per week at full quality — brand voice, visual
   standards, and QC passed — given confirmed capacity?
2. Is there enough to say at this frequency, or does it force filler content that dilutes
   the editorial value of the account?
3. Has engagement per post dropped as frequency has increased in the past? If yes, reduce
   frequency before running the optimisation test.

---

## Section 3: The 4-Week Optimisation Test

Run this test when establishing a new posting schedule or reviewing an underperforming
one. Each week isolates one variable so the cause of any change in performance is clear.

### Week 1 — Baseline

Post at the existing schedule (or EA baseline windows if the account is new). Record for
each platform in scope:

- Impressions
- Reach
- Engagement rate (engagements ÷ reach × 100)
- Best-performing post: format, day, time, topic
- Worst-performing post: format, day, time, topic

This week produces the benchmark against which Weeks 2–4 are measured.

### Week 2 — Time Shift

Keep posting frequency identical to Week 1. Move all posts to the peak activity windows
identified from native analytics (or EA baseline if analytics are unavailable). Record
the same five metrics.

Compare engagement rate and reach against Week 1. A meaningful lift (5 percentage points
or more on engagement rate) confirms the time shift is working.

### Week 3 — Frequency Test

Keep the optimised timing from Week 2. Increase frequency by **1 post per week** on the
primary platform only. Record the same metrics.

- If engagement rate per post holds or improves: frequency increase is sustainable.
- If engagement rate per post declines: the frequency ceiling has been reached; revert to
  Week 2 frequency.

### Week 4 — Content Type Test

Keep the optimised timing and confirmed frequency from Weeks 2 and 3. Replace 2 static
image posts with 2 Reels (or equivalent format test relevant to the platform). Record the
same metrics plus save rate and shares, which indicate content format preference.

### Decision Rule at End of Week 4

Apply this rule without discretion:

- Engagement rate improved vs Week 1 → adopt the new schedule permanently
- Engagement rate held but reach increased → maintain the change (more reach is a net
  gain even at the same engagement rate)
- Engagement rate declined → identify which specific variable (timing, frequency, or
  content type) caused the drop; revert only that variable

---

## Section 4: Output — Posting Schedule Document

Produce a weekly posting schedule as a table. Each row specifies one post slot.

Include columns for: day of week, platform, time (EAT), format, content pillar, and a
brief content direction note.

**Template:**

| Day | Platform | Time (EAT) | Format | Pillar | Content Direction |
|---|---|---|---|---|---|
| Monday | Instagram | 12:00 | Carousel | [Pillar name] | [Topic and angle] |
| Monday | Facebook | 20:00 | Video | [Pillar name] | [Topic and angle] |
| Tuesday | LinkedIn | 08:00 | Static image | [Pillar name] | [Topic and angle] |
| Wednesday | Instagram | 19:30 | Reel | [Pillar name] | [Topic and angle] |
| Wednesday | WhatsApp | 19:00 | Broadcast message | [Pillar name] | [Topic and angle] |
| Thursday | Facebook | 12:30 | Static image | [Pillar name] | [Topic and angle] |
| Thursday | X/Twitter | 08:00 | Text post | [Pillar name] | [Topic and angle] |
| Friday | Instagram | 13:00 | Story | [Pillar name] | [Topic and angle] |
| Saturday | TikTok | 20:00 | Short video | [Pillar name] | [Topic and angle] |

Populate every cell. Do not leave pillar or content direction blank. Use the content
pillars established in `10-content-pillars` and schedule them into `11-content-calendar`
once confirmed.

**Below the table, include three summary notes:**

1. **Analytics source** — state whether times are derived from native analytics or EA
   baseline, and which analytics export date was used
2. **Review trigger** — state when the schedule should next be reviewed (recommend: after
   4 weeks of data, or if engagement rate drops more than 10% in any rolling 2-week
   period)
3. **WhatsApp frequency cap** — explicitly note the broadcast frequency agreed with the
   client and the rationale for the cap

---

## Quality Criteria

- Timing recommendations are derived from native analytics data, not global benchmark
  articles; EA baseline is used only when analytics are unavailable and is labelled as
  provisional
- EA baseline posting windows are provided for all six platforms with UTC+3 times and
  documented rationale for why they differ from published global studies
- Frequency recommendations are specific per platform; no single "post X times per week"
  instruction is given across all channels
- The 4-week test is structured with discrete weekly variables so the cause of any
  performance change can be attributed to a specific change
- The Week 4 decision rule is binary (adopt / maintain / revert specific variable) — not
  open-ended "evaluate performance"
- The output posting schedule is a fully populated weekly table ready for use in
  `11-content-calendar` without further editing
- WhatsApp Broadcast timing and the 3/week frequency ceiling are explicitly addressed,
  with the opt-out risk noted
- All times in the schedule are expressed in EAT (East Africa Time, UTC+3)

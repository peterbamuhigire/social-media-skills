---
name: strategy-pdca-workflow-design
description: Use when the main deliverable concerns daily, weekly, and monthly Plan-Do-Check-Act operations; use playbook-daily-operations-routine when that neighbouring workflow owns the primary decision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# PDCA Workflow Design for Social Media Management

<!-- dual-compat-start -->
## Use When

- Use this skill for daily, weekly, and monthly Plan-Do-Check-Act operations.
- Use it when the requested deliverable needs the domain decisions and acceptance checks below.

## Do Not Use When

- Use `playbook-daily-operations-routine` when that neighbouring workflow owns the main decision or deliverable.
- Do not proceed when required evidence, approval, or safety review is absent; return the missing-input path instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, market, and intended decision | Client or approved brief | yes | Ask for it or state a narrow working assumption |
| Existing channel, content, commercial, or performance evidence relevant to daily, weekly, and monthly Plan-Do-Check-Act operations | Client systems, supplied files, or verified research | conditional | Mark the check unassessed and avoid performance claims |
| Approval, policy, budget, access, or risk constraints | Accountable client owner | conditional | Stop before publishing, spending, collecting data, or making regulated claims |

## Workflow

1. Confirm the decision, consumer, market, and evidence boundary; distinguish the request from `playbook-daily-operations-routine`.
2. Inspect supplied artefacts and record missing or unverified inputs before drafting.
3. Apply the domain framework in this skill and use the decision rule below at each branch.
4. Stop for approval before publishing, spending, contacting people, changing live systems, or making regulated claims.
5. Review the deliverable against the quality and anti-slop gates; if a check fails, correct it and rerun the affected check.
6. Hand off the artefacts, assumptions, evidence, and unresolved risks to the named consumer.
7. At the weekly and monthly review, apply the Kaizen campaign learning loop: observe the audience and process, baseline the decision, select one small improvement, test it, check guardrails, standardise verified learning, teach it into the operating template, and re-measure.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Daily, weekly, and monthly plan-do-check-act operations deliverable | Client decision-maker or delivery team | Names the chosen route, owners, sequence, assumptions, and measurable acceptance checks |
| Decision and risk record | Reviewer or implementer | Links each recommendation to supplied evidence or labels it as an assumption |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Input and assumption register | Table or annotated brief | Missing and unverified items are visible, not treated as passed |
| Release check | Completed quality checklist | All blocking findings are fixed or the deliverable is explicitly withheld |

## Capability and Permission Boundaries

Read and search are the minimum capabilities. Analysis and planning remain read-only. Edit only files placed in scope; publishing, outreach, spend, personal-data processing, production changes, and certification claims require explicit authority and evidence of success.

## Degraded Mode

If files, tools, network, current evidence, rendering, or authorised access are unavailable, return the narrowest useful qualified deliverable. Mark each unavailable check `not assessed`; never convert it into a pass or invent market facts.

## Decision Rules

| Choice condition | Action | Failure or risk avoided |
|---|---|---|
| The team needs decision triggers and continuous improvement, not only a task list | Define owner, cadence, threshold, action, and learning record | A routine repeats activity without changing underperformance |
| Evidence is contradictory or materially incomplete | Pause the affected recommendation and request the accountable source | Confident advice built on an unresolved premise |
| Authority is limited to analysis or planning | Deliver a read-only plan and approval checklist | Unauthorised publication, spend, outreach, or data use |

## Quality Standards

- Keep Uganda/East Africa, British English, EAT, UGX, and WhatsApp-first assumptions explicit where they apply.
- Tie recommendations to observed evidence, a named assumption, or a verification action.
- Give the next operator enough detail to execute without guessing ownership, sequence, or acceptance.
- Apply `ai-marketing/anti-ai-slop` during drafting and block release on an F from `ai-marketing/ai-slop-audit`.
- Record the audience problem, narrative job, metric denominator, accessibility/readability guardrail, owner, stop rule, rollback, and next baseline for each optimisation.

## Anti-Patterns

- Inventing a client metric, audience fact, price, partner, or platform rule. Fix: verify it or label the decision provisional.
- Treating a missing tool, source, render, or approval as a passed check. Fix: mark it `not assessed` and narrow the output.
- Producing channel tactics before defining the decision and consumer. Fix: state the required outcome and handoff first.
- Copying a global template without adapting Uganda/East Africa access, language, payment, or trust conditions. Fix: record which local assumptions apply.
- Recommending publication, outreach, spend, data collection, or a regulated claim without authority. Fix: stop at an approval-ready draft.
- Reporting activity as success without an acceptance condition. Fix: name the observable result and evidence source.
- Repeating a calendar because it is familiar while the audience signal is worsening. Fix: select one bounded countermeasure and record the result.

## References

- [AGENTS.md](../../../AGENTS.md)
- [Kaizen campaign learning loop](../../meta-analytics-ops/meta-testing-framework/references/kaizen-campaign-learning-loop.md)
<!-- dual-compat-end -->

Based on Neal Schaffer, *Maximize Your Social* (Wiley, 2013).

---


## Overview

The PDCA cycle (Plan-Do-Check-Act) is a continuous improvement loop applied to
social media management. It runs on three timeframes simultaneously:

- **Daily** — Do + Light Check (execute tasks, catch urgent issues)
- **Weekly** — Check + Act (review metrics, make small adjustments)
- **Monthly** — Plan + Act in full (reset strategy, document learnings)

The output of this skill is an operational manual. It tells the client — or
their team — exactly what to do, when to do it, and what to do when something
is not working.

---

## Required Input

Before generating the workflow manual, ask for:

1. **Client business name** and industry
2. **Country and city** (affects timing defaults and platform mix)
3. **Platforms in scope** (e.g., Facebook, Instagram, LinkedIn, TikTok, WhatsApp)
4. **Who manages day-to-day**: client themselves / in-house team member / consultant
5. **Available time per day** for social media management
6. **Existing analytics access**: Meta Business Suite, Google Analytics 4, TikTok Analytics, LinkedIn Analytics, other
7. **Current pain points**: what is disorganised or falling through the cracks?

---

## Section 1 — Daily Routine (Do + Light Check)

Time defaults are East Africa Time (EAT). Adjust for the client's timezone.

### Morning Block — 30 minutes (08:00–08:30 EAT)

1. Check overnight notifications: comments, DMs, mentions — respond to anything urgent
2. Review what is scheduled to publish today — confirm content is ready and accurate
3. Post any content not pre-scheduled (Stories, quick updates, timely content)
4. Check for any negative mentions or complaints requiring immediate response
5. Brief review of competitor activity — any significant posts or announcements in the past 24 hours?

### Midday Block — 10 minutes (12:30–13:00 EAT)

1. Respond to comments and DMs received since the morning block
2. Engage with the audience on current posts (acknowledge genuine comments, reply to questions)
3. Confirm today's scheduled post has gone live

### End-of-Day Block — 10 minutes (17:00–17:30 EAT)

1. Final check of comments and DMs
2. Log any content ideas or audience questions that emerged today into the content ideas file
3. Confirm tomorrow's scheduled content is ready in the queue

### Daily Time Investment

| Scope | Total Daily Time |
|---|---|
| One active platform | 50 minutes |
| Two active platforms | 65 minutes |
| Three active platforms | 80 minutes |
| Each additional platform | +15 minutes |

State the client's total daily time investment at the top of their manual so
expectations are set from day one.

---

## Section 2 — Weekly Routine (Check + Act)

**Schedule:** Every Monday, 45 minutes.

### Step 1 — Pull Weekly Metrics (20 minutes)

Pull from native analytics for each active platform:

- Reach and impressions for the week
- Engagement rate per post (average and per individual post)
- Follower change (net gain or loss)
- Best-performing post: screenshot it, note the format, topic, and time posted
- Worst-performing post: note what to avoid repeating

### Step 2 — Compare to Previous Week (10 minutes)

- Is the primary metric improving, stable, or declining?
- Is engagement rate above or below the EA benchmark for this platform?
- Is follower growth on trend with the monthly target?

### Step 3 — Review and Prepare the Coming Week (15 minutes)

- Check the content queue — are all posts for the coming week written, approved, and scheduled? (Cross-reference `11-content-calendar`)
- Identify one optimisation action for the week — for example: test a different posting time, add a stronger CTA to promotional posts, or experiment with a new content format
- Note any timely content opportunities (events, awareness days, news) to add to the queue

### Weekly Review Note

At the end of every Monday review, write one paragraph (internal, not client-facing):

> "This week: [best post and why]. [Platform] engagement was [up/down X%].
> Next week: try [one specific change]."

This note becomes the working memory of the social media programme. File it in
a running weekly log document.

### WhatsApp Note

WhatsApp community management is not tracked in native analytics. Add a manual
WhatsApp log to the weekly routine:

- Number of inbound messages received
- Number resolved
- Any recurring questions to address in content
- Any complaints or escalations

---

## Section 3 — Monthly Routine (Plan + Act in Full)

**Total monthly time investment:** 3 hours, spread across the month.

### Week 1 — Review (60 minutes)

- Pull the monthly analytics report for all platforms (Cross-reference `meta-reporting` and `meta-social-metrics-framework`)
- Calculate Net Sentiment Score (NSS) from the month's comments: (positive comments − negative comments) ÷ total comments × 100
- Compare primary metrics to the SMART targets set at the start of the month
- Answer: which content pillar performed best? Which underperformed?
- Answer: which platform drove the most results against the primary metric?

### Weeks 1–2 — Plan (60 minutes)

- Review next month's content calendar (Cross-reference `11-content-calendar`)
- Adjust pillar balance based on last month's performance data
- Plan any campaign content or seasonal moments for the coming month
- Identify three evergreen posts to recycle this month
- Set one optimisation hypothesis to test: "If we [change X], we expect [result Y] to improve by [measure Z] within [timeframe]."

Write the hypothesis down in the PDCA documentation log before the month begins.

### Week 4 — Act (60 minutes)

- Prepare the monthly client report (cross-reference `meta-reporting`)
- Record the optimisation hypothesis result in the log: did the change work? Why or why not?
- Document one learning from this month: "We learned that [audience insight]. Next month we will [action]."
- Book the next monthly review session before closing out the month

---

## Section 4 — Optimisation Decision Triggers

These signals should prompt an Act decision immediately — do not wait for the
monthly review cycle.

| Signal | Action |
|---|---|
| Engagement rate drops below EA benchmark for 2 consecutive weeks | Review content quality — is it relevant, well-timed, and visually strong? |
| Follower count declining for 3 or more consecutive weeks | Review recent content — has tone, topic, or posting frequency changed? |
| Complaint volume increases noticeably | Check community management response time and quality of replies |
| One post significantly outperforms all others | Analyse and replicate the format, topic, and timing in future posts |
| One platform consistently underperforms relative to others | Consider reducing posting frequency or deprioritising the platform |
| Primary metric (enquiries or leads) drops for 2 consecutive months | Review the full content-to-conversion path — identify where the drop-off occurs |

Cross-reference `playbook-daily-operations-routine` for escalation procedures
when multiple triggers fire simultaneously.

---

## Section 5 — The PDCA Documentation Log

Every Act decision must be documented. Create a simple optimisation log and
update it every month without exception.

### Log Template

| Month | Hypothesis | Change Made | Result | Next Action |
|---|---|---|---|---|
| [Month Year] | [If we do X, Y will improve] | [Exact change made] | [Measured outcome] | [Continue / reverse / iterate] |

### Worked Example

| Month | Hypothesis | Change Made | Result | Next Action |
|---|---|---|---|---|
| March 2026 | Posting at 19:30 EAT will increase ER vs 12:00 EAT | Moved 3 posts/week to 19:30 for 4 weeks | ER increased from 2.8% to 3.4% | Continue 19:30 for all evening content |

This log is the institutional memory of the client's social media performance.
It prevents repeating the same mistakes and builds a picture of what works for
this specific audience, on these specific platforms, in this specific market.

Store the log in the same shared folder as the content calendar and monthly reports.

---

## Section 6 — East Africa-Specific Workflow Notes

Apply these adjustments for clients operating in Uganda, Kenya, Tanzania,
Rwanda, and neighbouring markets.

**Peak engagement timing:**
Monday morning is the highest-traffic time for professional content in East
Africa. For B2B clients, prioritise posting on Sunday evening (20:00–21:00 EAT)
or Monday morning (07:30–09:00 EAT) to catch the start-of-week audience.

**Mobile-first review:**
Most East African social media managers check analytics on a smartphone rather
than a desktop. Confirm that all analytics dashboards — Meta Business Suite,
TikTok Analytics, LinkedIn — are accessible and readable on mobile before
handing the workflow to an in-house team.

**Load-shedding and power disruptions:**
Scheduled power cuts in parts of Uganda, Kenya, and Tanzania can disrupt
scheduled posts if the scheduling tool loses connectivity. Mitigate this by:
- Always maintaining mobile data as a backup to Wi-Fi
- Enabling push notifications from the scheduling tool so missed posts are flagged immediately
- Adding a midday confirmation step to the daily routine (already included above) to catch any posts that did not go live

**WhatsApp management:**
WhatsApp is the dominant customer communication channel across East Africa.
It operates outside native social analytics and requires a manual tracking
process. Include the WhatsApp weekly log (see Section 2) from day one.

**Public holidays and cultural calendar:**
Uganda and East Africa have a distinct public holiday and cultural calendar.
Build these into the monthly planning step: Eid al-Fitr, Eid al-Adha,
Liberation Day (Uganda, 26 January), Independence Day (Uganda, 9 October),
Christmas, Easter, and major regional sporting and cultural events.

---

## Quality Criteria

- Daily routine has named tasks with specific time estimates for each block (morning, midday, end-of-day)
- Weekly routine produces a documented one-paragraph note — not merely a prompt to "review analytics"
- Monthly routine follows the Plan-Review-Act structure clearly mapped across four weeks
- Optimisation decision triggers are specific signals with specific, actionable responses
- PDCA documentation log template is included with a fully worked example
- EA-specific notes address mobile-first management, load-shedding risk, and WhatsApp tracking
- Total daily time investment is stated numerically for one platform and for each additional platform
- All Act decisions are logged — the skill does not permit undocumented changes to strategy

---

## Cross-References

| Skill | When to use |
|---|---|
| `11-content-calendar` | Review and populate the content queue during weekly and monthly planning |
| `meta-reporting` | Generate the monthly analytics report in Week 4 of the monthly cycle |
| `meta-social-metrics-framework` | Define which metrics constitute the primary metric and EA benchmarks |
| `playbook-daily-operations-routine` | Escalation procedures when multiple optimisation triggers fire at once |

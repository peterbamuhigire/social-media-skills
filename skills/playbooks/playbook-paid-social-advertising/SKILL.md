---
name: playbook-paid-social-advertising
description: Use when planning, specifying, auditing or reporting paid social campaigns on Meta, TikTok or LinkedIn, including objectives, audiences, budgets, creative briefs, tracking and optimisation rules; use paid-search-advertising for Google Ads and strategy-organic-paid-hybrid for boosting organic winners.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Paid Social Advertising Playbook

Plan and specify paid social campaigns end to end: objective, audience temperature, budget split, campaign build, creative brief, tracking, testing, optimisation rules and monthly reporting. The engine plans, specifies, audits and reports; spending money, editing live ad accounts and publishing require explicit client authority and a named operator.

<!-- dual-compat-start -->
## Use When

- A client needs a paid social plan or build specification for Meta (Facebook, Instagram, Messenger, WhatsApp destinations), TikTok or LinkedIn.
- An existing paid social account needs a read-only audit, a diagnostic or an optimisation plan.
- A monthly paid social report or a scale, pause or refresh recommendation is required.
- Click-to-WhatsApp or lead-form campaigns need designing for an East African business.

## Do Not Use When

- The work is Google Ads search, Performance Max or Demand Gen; use `paid-search-advertising`.
- The question is overall budget, media mix or channel choice across media; use `advertising-strategy-and-budget` and `media-planning`.
- The need is concepts or copy; use `creative-brief-and-big-idea` and `ad-copy-and-hook-lab`.
- The request is to change live campaigns, budgets or audiences without written authority; stop at an approval-ready specification.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective as a SMART goal, conversion definition and value | Client owner; `advertising-strategy-and-budget` | Yes | Stop and request the missing decision. |
| Monthly paid budget, gross margin and allowable cost per result | Client finance owner | Yes | Compute a break-even line if margin is given; otherwise mark targets `not assessed`. |
| Current activity and exports (read-only) | Client ad accounts | Conditional | Plan from research only; mark audit checks `not assessed`. |
| Destination: website with tracking, lead form or WhatsApp Business number | Client, website team | Yes | Brief tracking and destination through `ad-to-site-journey-handoff` or `playbook-post-click-strategy`. |
| Special-category status (housing, employment, financial products, social issues/elections/politics) | Client, legal | Yes | Treat as a special ad category until confirmed otherwise (AD-03). |
| Operator (in-house, media buyer, agency) and approval limits | Client | Yes for execution | Deliver the plan only; do not build or spend. |

## Workflow

1. Confirm objective, conversion, value, market and special-category status; stop if the conversion or authority is unclear.
2. Select the platform objective from the current objective list (Meta six objectives, AD-01; TikTok by stage, AD-06; LinkedIn, AD-07; checked 2026-09-23) and record the reason ([Meta campaign build spec](references/meta-campaign-build-spec.md)).
3. Define audiences by temperature (cold, warm, retargeting) with lawful-basis notes for any customer list; set the starting budget split as a hypothesis.
4. Specify tracking: Pixel and Conversions API events, lead-form or WhatsApp conversion handling, UTMs; hand destination requirements to `ad-to-site-journey-handoff`. Withhold conversion campaigns until tracking QA passes.
5. Brief creative by audience temperature and awareness with register-checked specs (AD-08); copy from `ad-copy-and-hook-lab`; disclosures for creator or partnership ads (AD-09).
6. Write the test plan with lines in the sand via `ad-testing-and-scaling`.
7. Deliver the build specification for written approval. After an authorised operator launches, run the weekly diagnostic ([diagnostics and reporting](references/paid-social-diagnostics-and-reporting.md)); correct and rerun checks after each change; recover by returning to the last stable configuration when a change breaks performance.
8. Report monthly with spend, results against the break-even line, learnings and next month's plan.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Paid social plan and build specification | Client approver, authorised operator | Objective, audiences, budgets, placements, creative briefs, tracking and tests listed; volatile platform details carry a check date |
| Tracking brief | Developer or tag owner | Events, parameters and QA method defined |
| Creative brief per ad | Designer, copywriter | Audience tier, awareness level, format spec source, one CTA |
| Weekly diagnostic and optimisation log | Operator, account lead | Decisions tied to lines in the sand; one variable per change |
| Monthly report | Client | Spend, results vs targets, audience and creative learnings, next plan |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Platform check log | Claim, source (register ID or help URL), date | No undated platform rule in the plan |
| Tracking QA record | Event tests with dates | Each conversion fires once per real action |
| Decision record | Table | Each objective, audience and budget choice has a reason |

## Capability and Permission Boundaries

Read and search exports, plans and live help pages. Planning, auditing and reporting are read-only. Creating or editing campaigns, audiences, budgets or pixels, uploading customer lists, publishing ads and spending money require explicit written authority and a named operator. Customer lists need a lawful basis (Uganda PL-01; Kenya PL-02).

## Degraded Mode

Without account access, current platform checks or tracking, return the narrowest useful qualified plan with platform-specific lines marked `not assessed` and a discovery list. Never quote CPM, CPC, CTR or learning-phase thresholds from memory; derive the client's own baseline in the first weeks.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Client wants leads or sales but runs boosted posts | Specify Ads Manager campaigns with a conversion objective | Paying for engagement that does not convert |
| No working tracking | Run messaging or lead-form objectives with native tracking, or fix tracking first | Optimising on unmeasured outcomes |
| Ads concern housing, jobs, financial products or social issues/politics | Declare the special ad category; apply targeting limits where they apply; no political/social-issue ads in the EU (AD-03); authorisation and "Paid for by" for political ads (AD-04) | Rejection, account restriction or breach |
| Customer list upload proposed | Confirm lawful basis and notice first | Data-protection breach |
| Retargeting pool too small to read | Hold retargeting budget; build warm pools with video and engagement | Wasted spend on tiny audiences |
| Cost per result above the break-even line for the agreed window | Diagnose creative, audience, destination, offer in order; pause if unresolved | Scaling losses |
| Uganda-billed ad accounts | Budget for 18% VAT on Meta invoices without a registered TIN, pending finance-engine verification (PL-05, partial) | Budget shortfall |

## Quality Standards

- Objective chosen from the platform's current list with a stated reason; Advantage+ described as a campaign state (audience, budget and placement automation all on), not a separate campaign type (AD-02).
- Every volatile platform detail carries a register ID or a dated help-centre check.
- Budgets in UGX with the break-even cost per result stated.
- Creative briefed by temperature and awareness; captions on video; mobile-first; 4:5 feed and 9:16 Stories/Reels with safe zones (AD-08).
- Disclosures for paid partnerships and creator ads meet the strictest applicable rule (AD-09; AD-10 for Uganda/Kenya remains a check).
- Apply `anti-ai-slop` and the ethics filter to every ad.

## Anti-Patterns

- Quoting "typical" UGX CPMs or CPCs from memory. Fix: read the client's own first weeks and set lines from margin.
- Teaching the retired rule that images with more than 20% text are suppressed. Fix: follow current Meta creative guidance and the safe zones (AD-08).
- 1:1 1080×1080 as the default feed size. Fix: 4:5 for feed and 9:16 for Stories/Reels (AD-08).
- Changing audience, creative and budget in one week. Fix: one variable per window.
- Promising results before data exists. Fix: state targets as lines to be tested.
- Leaving WhatsApp enquiries unanswered. Fix: agree a response SLA and staffing before launch.
- Uploading a bought contact list. Fix: never; only lawful first-party lists.

## References

- [Meta campaign build spec](references/meta-campaign-build-spec.md) — read when choosing objectives, structure, audiences, tracking and specs on Meta.
- [Paid social diagnostics and reporting](references/paid-social-diagnostics-and-reporting.md) — read for weekly optimisation, kill/scale decisions and monthly reports.
- [TikTok and LinkedIn paid notes](references/tiktok-and-linkedin-paid-notes.md) — read when either platform is in scope.
- [Ad testing and scaling](../../advertising/ad-testing-and-scaling/SKILL.md); [ad copy and hook lab](../../advertising/ad-copy-and-hook-lab/SKILL.md); [creative brief and big idea](../../advertising/creative-brief-and-big-idea/SKILL.md).
- [Ad-to-site journey handoff](../../advertising/ad-to-site-journey-handoff/SKILL.md); [post-click strategy](../playbook-post-click-strategy/SKILL.md); [UTM tracking](../../meta-analytics-ops/meta-utm-tracking/SKILL.md).
- [Legal/market release gate](../../../docs/quality-gates/legal-market-release-gate.md); [creative review gate](../../../docs/quality-gates/creative-review-gate.md); [anti-AI-slop gate](../../ai-marketing/anti-ai-slop/SKILL.md).
<!-- dual-compat-end -->

## Required Input (intake questions)

1. Business name, industry and country/city (default Uganda/East Africa).
2. Primary objective as one SMART goal (e.g. "40 qualified enquiries a month from Wakiso parents by 30 November at no more than UGX [x] each").
3. Monthly paid budget in UGX and gross margin per sale or value per lead.
4. Current activity: objectives, spend, results; exports if available.
5. Destination: website (tracking status), lead form, or WhatsApp Business number (monitored, with response SLA).
6. Platforms in scope (default Meta for Uganda/EA; TikTok and LinkedIn by audience).
7. Special-category status and any regulated claims (health, finance, alcohol, betting, children, politics).
8. Who operates the account and who approves spend.

## Section 1 — Objective selection

Meta's current objectives are Awareness, Traffic, Engagement, Leads, App promotion and Sales (AD-01, checked 2026-09-23). Map the business goal to the objective the platform should optimise for:

| Business goal | Objective | Notes |
|---|---|---|
| Be known in a new market | Awareness | Judge on reach, frequency and brand-lift or recall checks, not clicks |
| Qualified visits to content | Traffic | Only when the visit itself matters; watch landing-page views |
| Conversations on WhatsApp/Messenger, video views, engagement | Engagement | Click-to-WhatsApp sits here or under Leads depending on current setup options; check on the day |
| Enquiries via instant form or messaging | Leads | Add one qualifying question where sales capacity is limited |
| Purchases, bookings, qualified conversions | Sales | Requires working Pixel/Conversions API events |

Boosted posts suit amplification of proven organic posts (see `strategy-organic-paid-hybrid`); business outcomes use Ads Manager campaigns.

## Section 2 — Audience temperature and starting split

| Tier | Signals | Message | Starting share (heuristic) |
|---|---|---|---|
| Cold | Location, age, interests, broad targeting, lookalikes from consented buyer lists | Problem, story, proof; no hard offer first | ~50% |
| Warm | Video viewers, engagers, page/profile followers, WhatsApp conversation starters | Specific offer, demonstration, objection answer | ~30% |
| Retargeting | Site visitors (pixel), lead-form openers, abandoners | Proof for the objection, real deadline or incentive | ~20% |

The 50/30/20 split is an engine starting heuristic, not a benchmark; re-allocate from the client's cost per qualified result after the first read. Where retargeting pools are too small to deliver, hold that budget and grow warm pools with video.

Video viewers are the most practical warm pool for EA clients without a website pixel; set the view threshold per objective and check current audience options on the day.

## Section 3 — Budget and pacing

- Use daily budgets for always-on programmes; lifetime budgets for dated campaigns (events, seasonal offers).
- Start with ad-set budgets while reading which tier performs; move to campaign-level (Advantage+ campaign budget) once one structure is proven; Advantage+ is on when audience, budget and placement automation are all enabled (AD-02).
- Platform behaviour after budget changes (learning periods, instability) is checked on the live help centre with the date; scale in steps via `ad-testing-and-scaling`.
- Micro budgets: one campaign, one objective, one or two ad sets; fewer, stronger ads.

## Section 4 — Click-to-WhatsApp ads (East Africa)

Use when the business sells by conversation, has no strong website, or trust must be built before purchase (health, finance, professional services). Set a pre-filled opening message that is short and specific ("Hi, I'd like the price list for [service] in [area]"). Staff replies within an agreed SLA (the engine's default planning figure is two hours in business hours, adjustable per client); route to `playbook-chatbot-strategy` when volume outgrows the team. Business-initiated follow-up messages need opt-in and approved templates under the current WhatsApp Business policy (check on the day).

## Section 5 — Monthly report structure

1. Executive summary: objective, spend, the one result that matters against its line.
2. Spend and results by campaign vs target.
3. Audience-tier performance with recommendations.
4. Creative performance: top and bottom three, what carries forward.
5. Downstream quality: leads to customers, response times.
6. Tests run and decisions.
7. Next month: plan, budget split in UGX, lines in the sand, required approvals.

## Sources

- Cooper, M.D. (2019) *Help! My Facebook Ads Suck!* (2nd ed.) and Marshall, P. (2024) *Ultimate Guide to Facebook Advertising* (4th ed.) — structural practices retained (objective discipline, awareness-matched creative, one variable per test, Three Cs of creative); their numeric thresholds and the retired 20% text rule are removed.
- Currentness register 2026-09-23: AD-01, AD-02, AD-03, AD-04, AD-06, AD-07, AD-08, AD-09, AD-10, PL-01, PL-02, PL-05, MK-01, MK-02, MK-03.

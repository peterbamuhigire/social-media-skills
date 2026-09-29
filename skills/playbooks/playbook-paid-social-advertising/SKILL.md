---
name: playbook-paid-social-advertising
description: 'Use when a client wants Meta, TikTok or LinkedIn ads planned, audited or reported: objectives, audiences, budget split, click-to-WhatsApp and lead forms, pixel tracking and rules for switching off losers; produces the paid social plan, build specification, audit or monthly report; not for Google search ads (use `paid-search-advertising`).'
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
- An existing paid social account needs a read-only audit, a diagnosis of weak results or an optimisation plan.
- The client wants a monthly paid social report and a recommendation on what to scale, pause or refresh.
- Click-to-WhatsApp or lead-form campaigns need designing for an East African business, with audience temperature and budget split.
- Sponsored posts or Reels and Stories ads need ad sets, custom audiences, a budget in UGX or KES, pixel and Conversions API tracking, and a rule for switching off losing ads.

## Do Not Use When

- `paid-search-advertising` for Google Ads search, Performance Max or Demand Gen.
- `advertising-strategy-and-budget` and `media-planning` for overall budget, media mix or channel choice across media.
- `ad-copy-and-hook-lab` for headlines, hooks and primary text.
- Stop before changing live campaigns, budgets or audiences without written authority; deliver an approval-ready specification.

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

| Artefact | Consumer | Acceptance condition |
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

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Creating or editing campaigns, audiences, budgets or pixels, uploading customer lists, publishing ads and spending money require explicit written authority and a named operator; customer lists need a lawful basis (Uganda PL-01; Kenya PL-02); exports, plans and live help pages may be read and searched.

## Degraded Mode

Without account access, current platform checks or working tracking, return the narrowest qualified result and mark the affected checks `not assessed`. A plan with platform-specific lines marked `not assessed` and a discovery list can still be delivered; never quote CPM, CPC, CTR or learning-phase thresholds from memory, and derive the client's own baseline in the first weeks.

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

- [Paid social planning method](references/paid-social-planning-method.md): read when asking the intake questions, mapping goals to objectives, setting the 50/30/20 temperature split, budgets and pacing, click-to-WhatsApp ads, the monthly report structure, or the Cooper (2019) and Marshall (2024) sources and register list.
- [Meta campaign build spec](references/meta-campaign-build-spec.md): read when choosing objectives, structure, audiences, tracking and specs on Meta.
- [Paid social diagnostics and reporting](references/paid-social-diagnostics-and-reporting.md): read for weekly optimisation, kill/scale decisions and monthly reports.
- [TikTok and LinkedIn paid notes](references/tiktok-and-linkedin-paid-notes.md): read when either platform is in scope.
- [Ad testing and scaling](../../advertising/ad-testing-and-scaling/SKILL.md), [ad copy and hook lab](../../advertising/ad-copy-and-hook-lab/SKILL.md) and [creative brief and big idea](../../advertising/creative-brief-and-big-idea/SKILL.md): read when writing the test plan, ad copy or creative briefs.
- [Ad-to-site journey handoff](../../advertising/ad-to-site-journey-handoff/SKILL.md), [post-click strategy](../playbook-post-click-strategy/SKILL.md) and [measurement tracking plan](../../meta-analytics-ops/measurement-tracking-plan/SKILL.md): read when specifying the destination and tracking.
- [Legal/market release gate](../../../docs/quality-gates/legal-market-release-gate.md), [creative review gate](../../../docs/quality-gates/creative-review-gate.md) and [anti-AI-slop gate](../../ai-marketing/anti-ai-slop/SKILL.md): read before releasing any plan with special-category, disclosure or copy claims.
<!-- dual-compat-end -->

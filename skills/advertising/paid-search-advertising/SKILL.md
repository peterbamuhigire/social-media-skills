---
name: paid-search-advertising
description: Use when planning, specifying, auditing or reporting Google Ads search, Performance Max or Demand Gen campaigns, keyword and intent research, RSA assets or search conversion tracking; use playbook-paid-social-advertising for Meta, TikTok and LinkedIn ads.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Paid Search Advertising

Plan and specify Google Ads programmes that harvest existing demand: intent-led keyword architecture, responsive search ads, Performance Max and Demand Gen used for the right job, clean conversion tracking, and landing pages that match the query. Output is a build specification and optimisation plan; changes to live accounts require explicit client authority.

<!-- dual-compat-start -->
## Use When

- A client needs a search advertising plan, account structure, keyword map or build specification.
- An existing Google Ads account needs a read-only audit and a prioritised fix list.
- RSA assets, sitelinks, callouts or search-theme inputs need writing for a campaign.
- The team must decide whether Search, Performance Max or Demand Gen fits an objective.
- Search is being used to test propositions or keywords before investing in SEO or product builds.

## Do Not Use When

- The work is Meta, TikTok or LinkedIn advertising; use `playbook-paid-social-advertising`.
- The work is organic search or AI-search visibility; use `seo-geo-optimisation` or `ai-generative-search-optimisation`.
- The deliverable is landing-page implementation; hand off through `ad-to-site-journey-handoff` to website-skills.
- The request is to change bids, budgets or campaigns in a live account without written authority; stop at an approval-ready specification.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, conversion definition and value per conversion | Client owner, `advertising-strategy-and-budget` | Yes | Stop; a search plan without a conversion definition optimises for clicks. |
| Budget, allowable CPA or target return and gross margin | Client finance owner; `advertising-attribution-and-measurement` | Yes | Compute the break-even line from margin if supplied; otherwise mark the target `not assessed`. |
| Account access (read-only) or exports: search terms, keywords, conversions | Client Google Ads account | Conditional (audits) | Produce a plan from research only and mark audit checks `not assessed`. |
| Landing pages and tracking status | Client website, tag manager, website-skills | Yes | Plan a tracking brief and landing-page brief before launch. |
| Keyword research data | Google Ads Keyword Planner or an approved tool, run on the day | Yes | Record the tool, date and locale; never invent search volumes. |
| Market and consent context (EEA/UK/CH traffic?) | Client, media plan | Conditional | Treat consent requirements as unassessed and block EEA-targeted launch. |

## Workflow

1. Confirm the objective, conversion action, value, margin and geography; stop if the conversion cannot be tracked or defined.
2. Map intent: list the buyer's search jobs (problem, solution, brand, competitor, local, price) and build keyword themes from research run on the day ([search build specification](references/search-build-specification.md)).
3. Choose campaign types by job: Search for known intent; Performance Max for inventory-wide conversion with feeds or strong assets; Demand Gen for visual demand generation (register AD-05, checked 2026-09-23).
4. Draft the account structure, negatives, budgets and bidding approach; phrase bidding and match-type behaviour as checks against the live help centre.
5. Write RSA assets and extensions with `ad-copy-and-hook-lab`; check message match against each landing page through `ad-to-site-journey-handoff`.
6. Specify tracking: conversion actions, values, offline import if relevant, UTMs, and consent handling (Consent Mode v2 for EEA/UK/CH users, register CW-10). Withhold launch if tracking fails QA.
7. Set the test and optimisation cadence ([search optimisation and audit](references/search-optimisation-and-audit.md)); define kill and scale lines from the break-even CPA.
8. Deliver the build specification for approval. After approval and launch by the authorised operator, review search terms, conversions and quality diagnostics on cadence; correct and rerun the checks after each change.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Search build specification | Authorised account operator, client approver | Campaigns, ad groups or asset groups, keywords, negatives, budgets, bidding approach, assets, URLs and tracking listed; volatile behaviour flagged as checks |
| Keyword and intent map | Strategist, website team | Themes by intent with source tool and date; no invented volumes |
| Tracking and consent brief | Web developer or tag owner | Conversion actions, values, test method and consent handling defined |
| Audit report (existing accounts) | Client owner | Findings ranked by money at risk, each with evidence and a fix |
| Optimisation plan | Operator and reporting owner | Cadence, lines in the sand, kill and scale rules |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Research log | Tool, locale, date, queries | Reproducible |
| Tracking QA record | Test conversion screenshots or exports, date | Each conversion action fires once per real action |
| Decision record | Table of choices with rationale | Every campaign-type and bidding choice has a reason and a check owner |

## Capability and Permission Boundaries

Read and search supplied exports, websites and live help pages. Audits and plans are read-only. Creating or editing campaigns, budgets, bids, conversion settings or tags, and spending money, require explicit written client authority and a named operator. Uploading customer lists requires a lawful basis and consent under the client's data-protection obligations (PL-01, PL-02 for Uganda and Kenya).

## Degraded Mode

Without account access, current help-centre checks or keyword tools, return the narrowest useful qualified specification: intent themes without volumes, structure without bids, and all platform-behaviour lines marked `not assessed`. Never state a CPC, CTR, conversion rate or Quality Score benchmark from memory.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| No working conversion tracking | Build tracking first; launch only for measured tests | Optimising for clicks and wasting budget |
| Brand terms mixed with generic terms | Separate brand and non-brand campaigns | Brand clicks masking poor generic performance |
| Performance Max proposed without feeds, assets or conversion volume | Start with Search on core intent; add PMax once signals exist | Opaque spend with no learning |
| Standalone Display campaign requested | Plan new display work in Demand Gen (AD-05, Display moving into Demand Gen from June 2026) | Building on a format being retired |
| Search terms show irrelevant queries | Add negatives and tighten themes before raising budget | Paying for the wrong intent |
| CPA above break-even for the agreed window | Diagnose query, ad, landing page and offer in that order; pause if unresolved | Scaling a losing campaign |
| EEA/UK/CH traffic in scope and consent not implemented | Block launch to those users until Consent Mode v2 and a CMP are live (CW-10) | Audience exclusion and compliance risk |

## Quality Standards

- Every keyword theme maps to one landing page whose headline echoes the query.
- CPA = CPC ÷ conversion rate; set the allowable CPA from margin and lifetime value before launch.
- Separate demand harvesting (search) from demand generation (Demand Gen, video, social) in targets and reports.
- Record the date of every platform check; re-check before each build.
- Apply `anti-ai-slop` to all ad text; apply the ethics filter to offers.

## Anti-Patterns

- Judging campaigns on clicks. Fix: judge on qualified conversions and CPA against break-even.
- One ad group for every service. Fix: themes by intent with matching ads and pages.
- Sending all ads to the home page. Fix: one landing page per theme via the journey handoff.
- Broad targeting with no negatives. Fix: weekly search-terms review and a shared negative list.
- Copying a US benchmark for Uganda. Fix: derive the client's own baseline in the first 2–4 weeks.
- Changing bids and ads in the same week. Fix: one variable per test window.
- Automated bidding on almost no conversions. Fix: check the current minimum-data guidance and use manual or simpler strategies until signals exist.

## References

- [Search build specification](references/search-build-specification.md) — read when structuring a new account or campaign.
- [Search optimisation and audit](references/search-optimisation-and-audit.md) — read for existing accounts and weekly optimisation.
- [Ad copy and hook lab](../ad-copy-and-hook-lab/SKILL.md) for RSA assets; [ad-to-site journey handoff](../ad-to-site-journey-handoff/SKILL.md) for landing pages.
- [Advertising attribution and measurement](../advertising-attribution-and-measurement/SKILL.md); [UTM tracking](../../meta-analytics-ops/meta-utm-tracking/SKILL.md).
- [Legal/market release gate](../../../docs/quality-gates/legal-market-release-gate.md); [source register](../../../docs/source-registers/source-register.json).
<!-- dual-compat-end -->

## Campaign-type guide (register AD-05, checked 2026-09-23)

| Type | What it is | Use for | Watch |
|---|---|---|---|
| Search with responsive search ads | Text ads on search results; 3–15 headlines of up to 30 characters, 2–4 descriptions of up to 90 characters, two 15-character paths | Known intent, local services, B2B lead generation | Query relevance, message match |
| Performance Max | One campaign across Search, YouTube, Display, Discover, Gmail and Maps; now supports negative keywords, brand exclusions, search themes and channel performance reporting | E-commerce with feeds, lead generation with strong conversion signals | Brand cannibalisation; review channel reporting; exclusions |
| Demand Gen | YouTube (including Shorts), Discover, Gmail, Maps and the display network; video action campaigns have been upgraded to it; standalone Display is being folded in (announced 2026-05-26; migration tool from June 2026) | Visual demand generation, retargeting-style reach | Judge on assisted and view-through outcomes carefully; incrementality |

## Using search to test before building

Weinberg & Mares (2014) describe running small search tests on candidate propositions and keywords before building content or products: if a proposition converts on paid search, organic effort on it is more likely to pay. Use the same method for SEO priorities and service launches (localised example: test "O-level maths revision" vs "A-level physics crash course" vs "PLE coaching" ads to see which proposition has cheaper qualified demand before hiring tutors).

## East Africa adaptation

- Many local categories (schools, clinics, hotels, property, B2B services) have search demand with limited competition; verify on the day rather than assuming low costs.
- Use click-to-call and WhatsApp destinations where the business converts by conversation; track calls and WhatsApp clicks as conversion actions.
- Mobile-first landing pages; test under a throttled Slow 4G/3G profile as a constrained-network stress test, not as a measured median; every source found for Uganda is higher (UCC operator averages 5-16 Mbps, SpeedOf.Me median 8.4 Mbps; register CW-04, MK-04, NET-05).
- Ugandan invoices for non-resident digital services may attract 18% VAT unless a TIN is registered (PL-05, partial); budget impact goes to `chwezi-accounting-doctrine` for verification.

## Sources

- Weinberg, G. and Mares, J. (2014) *Traction*, S-curves Publishing — SEM tests, CPA formula, demand harvesting vs generation.
- Currentness register 2026-09-23: AD-05 (Google Ads formats), CW-10 (Consent Mode v2 and GA4), CW-04/MK-04 (throttling profiles), PL-05 (Uganda tax, route to finance engine).

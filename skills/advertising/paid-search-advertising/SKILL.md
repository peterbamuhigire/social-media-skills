---
name: paid-search-advertising
description: 'Use when a client wants to appear on Google when people search: Google Ads search, Performance Max or Demand Gen plans, keyword and intent maps, RSA assets, account audits and conversion tracking; produces a search build specification and prioritised fix list; not for Meta, TikTok or LinkedIn ads (use `playbook-paid-social-advertising`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Paid Search Advertising

Plans and specifies Google Ads programmes that harvest existing demand: intent-led keyword architecture, responsive search ads, Performance Max and Demand Gen used for the right job, clean conversion tracking, and landing pages that match the query. Output is a build specification and optimisation plan; changes to live accounts require explicit client authority.

<!-- dual-compat-start -->
## Use When

- We need a Google search advertising plan, account structure, keyword map or build specification.
- Audit our existing Google Ads account read-only and give a fix list ranked by money at risk.
- Write RSA headlines and descriptions, sitelinks, callouts or search-theme inputs for a campaign.
- Should this objective run on Search, Performance Max or Demand Gen?
- Test propositions or keywords with search ads before investing in SEO or a product build.

## Do Not Use When

- `playbook-paid-social-advertising` for Meta, TikTok or LinkedIn advertising.
- `seo-geo-optimisation` or `ai-generative-search-optimisation` for organic search or AI-search visibility.
- `ad-to-site-journey-handoff` for the landing-page brief handed to website-skills.
- Stop at an approval-ready specification when asked to change bids, budgets or campaigns in a live account without written authority.

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

| Artefact | Consumer | Acceptance condition |
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

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Creating or editing campaigns, budgets, bids, conversion settings or tags also needs a named operator, and uploading customer lists requires a lawful basis and consent under the client's data-protection obligations (PL-01, PL-02 for Uganda and Kenya).

## Degraded Mode

Without account access, current help-centre checks or keyword tools, return the narrowest qualified result and mark the affected checks `not assessed`. Intent themes without volumes and structure without bids can still be delivered, with all platform-behaviour lines marked; never state a CPC, CTR, conversion rate or Quality Score benchmark from memory.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| No working conversion tracking | Build tracking first; launch only for measured tests | Optimising for clicks and wasting budget |
| Brand terms mixed with generic terms | Separate brand and non-brand campaigns | Brand clicks masking poor generic performance |
| Performance Max proposed without feeds, assets or conversion volume | Start with Search on core intent; add PMax once signals exist | Opaque spend with no learning |
| The client sells physical products and wants Shopping, free listings or Performance Max with a feed | Build and audit the Merchant Center feed with [shopping and feeds](references/shopping-and-feeds.md): required attributes, GTIN rules and diagnostics; target Uganda, Kenya or Tanzania only (Rwanda is not a supported Shopping country) (register `MERCHANT-CENTER-PRODUCT-DATA`) | Disapproved products, invented GTINs and campaigns aimed at an unsupported country |
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

- [Search build specification](references/search-build-specification.md): read when structuring a new account or campaign.
- [Search optimisation and audit](references/search-optimisation-and-audit.md): read when auditing an existing account or running weekly optimisation.
- [Campaign types, search testing and East Africa notes](references/campaign-types-and-east-africa.md): read when choosing a campaign type, testing propositions with search ads, or adapting the programme for East Africa.
- [Shopping and feeds](references/shopping-and-feeds.md): read when building or auditing a Merchant Center feed, fixing GTIN or diagnostics issues, or checking Shopping availability in East Africa.
- [Ad copy and hook lab](../ad-copy-and-hook-lab/SKILL.md): read when writing RSA assets; [ad-to-site journey handoff](../ad-to-site-journey-handoff/SKILL.md): read when briefing landing pages.
- [Advertising attribution and measurement](../advertising-attribution-and-measurement/SKILL.md) and [measurement tracking plan](../../meta-analytics-ops/measurement-tracking-plan/SKILL.md): read when setting break-even CPA or specifying tracking and consent.
- [Legal/market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when ad claims or regulated categories need clearance; [source register](../../../docs/source-registers/source-register.json): read when checking the dated register entries (AD-05, CW-10, PL-01, PL-02).
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting any ad text.
<!-- dual-compat-end -->

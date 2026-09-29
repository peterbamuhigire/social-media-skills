---
name: programmatic-and-brand-safety
description: Use when buying display, video, connected TV, digital screens or audio through a DSP, private deal or exchange and the client fears fraud, unseen ads, hidden fees or bad placements; produces a programmatic buying brief with supply-path, viewability, fraud and brand-safety controls; not for cross-channel reach and flighting (use `media-planning`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Programmatic and Brand Safety

Decides how to buy automated display, video, connected TV (CTV), digital out-of-home (DOOH) and digital audio so that the ads are real, seen, placed next to acceptable content and bought through a supply path whose costs are known. Written for the media buyer, the client's marketing lead and the finance owner who must sign off on where the money goes; the skill specifies and audits, and never trades.

<!-- dual-compat-start -->
## Use When

- Spend is about to go through a DSP, a private marketplace or a programmatic guaranteed deal, and the controls must be written down first.
- The agency reports millions of impressions, yet nobody can say what share was seen by people or was bot traffic.
- Which share of every shilling lands with the publisher, and which intermediaries take the rest?
- Keep our bank's ads off harmful content without starving Monitor, Nation or New Vision news pages of our spend.
- Connected TV, digital billboards in Kampala or Nairobi, or podcast and streaming audio slots are on offer, and delivery must be proved.
- A vendor is selling attention metrics; decide whether they add anything beyond viewability.

## Do Not Use When

- `media-planning` for the cross-channel plan: channel mix, reach and frequency, GRPs, flighting and classic radio, TV and outdoor weights.
- `playbook-paid-social-advertising` for Meta, TikTok or LinkedIn campaign builds, and `paid-search-advertising` for Google Search, Shopping and Performance Max.
- `08-influencer-marketing-strategy` for creator vetting and influencer brand safety; `advertising-attribution-and-measurement` for proving sales impact.
- Stop before any deal ID, insertion order, DSP change or spend without the client's written authority; return the brief and the questions for the seller instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, markets, flight dates and budget line for programmatic | Approved media plan (`media-planning`) or brief | Yes | Stop; request the plan line |
| Brand risk appetite: floor, sensitive categories, regulated-category rules | Client marketing and legal owners | Yes | Apply the default floor and "medium" suitability; label as assumption |
| Seller and path data: DSP and SSP names, seller IDs, ads.txt or app-ads.txt, sellers.json entries, deal IDs, fee schedule | Agency, trading desk, SSPs, publishers | Conditional | Mark every supply-path check `NOT_ASSESSED`; return the data request |
| Verification reports: viewability, IVT (GIVT and SIVT), brand-safety blocks, placement or app lists | Accredited verification vendor or ad server | Conditional | Plan the tags and reporting; mark delivery quality `NOT_ASSESSED` |
| Channel proof: CTV app and device lists, DOOH play logs and site list, podcast download logs | Seller, screen owner, podcast host | Conditional per channel | Require it in the deal terms; mark the channel `NOT_ASSESSED` until received |
| Inclusion list or local publisher list | Client, agency or publishers | No | Build one from direct publisher contacts; see [brand safety](references/brand-safety-and-suitability.md) |

## Workflow

1. Confirm the job: take the programmatic line from the approved plan and restate objective, audience, markets and budget. Stop if there is no plan line, no brand-risk owner or no authority to buy; return the brief skeleton and the questions.
2. Choose the buying route per line: open exchange, private marketplace, preferred deal, programmatic guaranteed or a direct insertion order, weighing control, price and scale (see [buying routes and supply path](references/buying-routes-and-supply-path.md)). In East Africa, check whether the premium local inventory is sold programmatically at all before designing around it.
3. Set the supply-path rules: authorised sellers only (ads.txt and app-ads.txt), seller IDs checked in sellers.json, the SupplyChain object complete, the fewest hops, and a fee disclosure per layer. Ask for log-level data so spend can be matched to publisher revenue; without it, record each SPO check `NOT_ASSESSED`.
4. Set delivery quality: MRC viewability as the floor (register `MRC-VIEWABILITY-2015`), GIVT and SIVT filtration with TAG-certified partners (registers `MRC-IVT-2020`, `TAG-CERTIFIED-AGAINST-FRAUD`), and attention only as an extra layer on viewable impressions (register `IAB-MRC-ATTENTION-2025`) (see [viewability, IVT and attention](references/viewability-ivt-and-attention.md)).
5. Set brand safety and suitability: a floor that no ad funds, suitability tiers by content category, an inclusion list for news and local-language publishers, and a short exclusion list; state that GARM was discontinued on 9 Aug 2024 and its framework is used as a legacy vocabulary (register `WFA-GARM-DISCONTINUED-2024`).
6. Add channel rules for CTV, DOOH and audio: CTV app and device transparency and ad-pod rules, DOOH proof of play against the MRC OOH standards, and podcast delivery against IAB Tech Lab v2.2 (see [CTV, DOOH and audio](references/ctv-dooh-and-audio.md)). Radio stays in `media-planning`.
7. Write the reporting rules: which metrics are billed, which are diagnostic, the denominators, the make-good trigger and the post-flight transparency report.
8. Run the quality and anti-slop gates; where a check fails (a missing seller ID, an unaccredited vendor, a floor gap), correct the brief and rerun that check before release.

## Core terms at a glance

| Term | Meaning | Check |
|---|---|---|
| Open exchange | Real-time auction open to any buyer | Highest reach, lowest control; SIVT and resale risk |
| Private marketplace (PMP) | Invitation-only auction with a deal ID | Named sellers; price floor; still auction-based |
| Preferred deal | Fixed price, first look, not guaranteed | Volume varies; check fill |
| Programmatic guaranteed | Fixed price and volume, bought through the DSP | Closest to a direct booking; needs the publisher's set-up |
| Working media | Share of spend that reaches the publisher | Needs log-level matching; otherwise `NOT_ASSESSED` |
| Unknown delta | Spend that cannot be traced to any disclosed fee or publisher revenue | 15% average in the 2020 UK study (register `ISBA-PWC-PROGRAMMATIC-2020`); not a benchmark for East Africa |
| Viewable impression | 50% of pixels for 1 continuous second (display) or 2 seconds (video) | Register `MRC-VIEWABILITY-2015` |
| GIVT / SIVT | Invalid traffic found by routine lists / by advanced analytics | Register `MRC-IVT-2020` |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Programmatic buying brief | Media buyer, client approver | Each line has route, deal type, targeting, supply-path rules, quality floors and reporting owner |
| Supply-path and fee audit | Client finance owner, agency | Each hop named with seller ID, relationship (DIRECT or RESELLER), fee and status, or `NOT_ASSESSED` |
| Brand-safety and suitability policy | Client marketing and legal, verification vendor | Floor, tiers per category, inclusion and exclusion lists, news and local-language rule |
| Delivery-quality specification | Verification vendor, buyer | Viewability standard, IVT filtration, attention method (if any) and make-good trigger |
| Post-flight transparency report template | Client and agency | Spend, working media, fees, unknown share, viewable rate, IVT rate and blocks per line |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Supply-path record | Table per seller and deal | ads.txt, sellers.json and schain checks shown with date and source, or `NOT_ASSESSED` |
| Verification record | Vendor export summary | Vendor, accreditation status, measured rate and viewable rate stated separately |
| Suitability decision log | Table | Each tier choice and each exclusion has an owner and a reason |
| Source register citations | Inline register IDs | Every standard or market figure carries a register ID and date |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Creating deal IDs, changing DSP settings, uploading audience or device lists, signing insertion orders or contacting sellers also needs that authority, and regulated categories (gambling, alcohol, financial services, health, political) route to the [legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md).

## Degraded Mode

Without seller IDs, log-level data or fee disclosure, return the narrowest qualified result and mark the affected checks `not assessed`. The buying route, quality floors, suitability policy and a data request to the agency and SSPs can still be delivered; record each supply-path optimisation check as `NOT_ASSESSED` and never estimate a working-media share for the client.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The best local publishers are not sold programmatically | Buy them direct or through a programmatic guaranteed deal where offered; use the exchange only for scale | Paying for the long tail while missing the audience |
| A seller is not listed as authorised in the publisher's ads.txt or app-ads.txt, or its seller ID is absent from sellers.json | Exclude the path | Spoofed inventory and resold impressions |
| Mobile-app inventory with high volume, low price and unknown developers | Require app-ads.txt, a bundle-ID list and SIVT filtration; cap spend until results are checked | Made-for-advertising apps and device fraud |
| Keyword blocking would remove most news pages | Replace blanket keywords with suitability tiers and a news inclusion list | Defunding news publishers and losing reach |
| Attention or "quality" scores offered without viewability | Refuse as a billing metric; accept as diagnostic on viewable impressions only | Paying for unseen ads under a new name |
| CTV or DOOH delivery cannot be proved (no app list, no play logs) | Buy only with proof-of-play or device-level reporting in the terms, or pause the line | Paying for screens nobody watched or ads that never ran |
| The agency trades as principal (resells media it bought) | Ask for written disclosure of margin and of the principal role before approval | Undisclosed resale margin |

## Quality Standards

- Every line names its buying route and deal type; open-exchange spend has a reason.
- Viewability, IVT and suitability thresholds cite the standard and register ID; vendor figures are labelled "(Vendor)" and are never targets.
- The supply-path audit shows each hop or `NOT_ASSESSED`; no working-media share is invented.
- The suitability policy protects news and local-language publishers with an inclusion list, not only exclusions.
- CTV, DOOH and audio each have a named proof-of-delivery source.
- British English; UGX or named currency; East African supply limits stated, not assumed away.

## Anti-Patterns

- Buying the open exchange by default because it is cheap. Fix: price the same audience through PMP or direct publisher deals and compare cost per viewable, valid impression.
- Reporting served impressions as delivery. Fix: report measured rate, viewable rate and IVT rate separately.
- Blocking "election", "Covid" or "attack" across the whole buy. Fix: use suitability tiers and a news inclusion list.
- Calling GARM a live standard or quoting its "certification". Fix: say GARM was discontinued in 2024 and name the framework as legacy vocabulary.
- Treating attention scores as a replacement for viewability. Fix: require the viewability floor first, then use attention as a diagnostic.
- Accepting "transparent pricing" without seller IDs or log-level data. Fix: request the path data and mark checks `NOT_ASSESSED` until it arrives.

## References

- [Buying routes and supply path](references/buying-routes-and-supply-path.md): read when choosing deal types, auditing fees or checking ads.txt, sellers.json and the SupplyChain object.
- [Viewability, IVT and attention](references/viewability-ivt-and-attention.md): read when setting quality floors, choosing a verification vendor or judging attention offers.
- [Brand safety and suitability](references/brand-safety-and-suitability.md): read when writing the floor, tiers, inclusion and exclusion lists.
- [CTV, DOOH and audio](references/ctv-dooh-and-audio.md): read when a line is connected TV, digital screens, podcast or streaming audio.
- [Media planning](../media-planning/SKILL.md), [advertising attribution and measurement](../advertising-attribution-and-measurement/SKILL.md) and [influencer marketing strategy](../../pipeline/08-influencer-marketing-strategy/SKILL.md): read when the plan, the sales proof or creator safety is the real question.
- [Anti-AI slop gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting client-facing text.
<!-- dual-compat-end -->

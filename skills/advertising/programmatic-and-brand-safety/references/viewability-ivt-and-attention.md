# Viewability, invalid traffic and attention

Read when setting delivery-quality floors, choosing or briefing a verification vendor, or judging an attention-metric offer. Parent: [programmatic-and-brand-safety](../SKILL.md).

## 1. Viewability (MRC)

The MRC Viewable Ad Impression Measurement Guidelines (v1.0, dated 30 Jun 2014, hosted by IAB in 2015; register `MRC-VIEWABILITY-2015`) set the industry floor:

| Format | Pixel requirement | Time requirement | Note |
|---|---|---|---|
| Display | At least 50% of the ad's pixels in view on an in-focus tab | At least 1 continuous second after render | Pixel test first, then the clock starts |
| Large display (242,500 pixels or more, e.g. 970x250) | At least 30% of pixels | At least 1 continuous second | Allowed only if disclosed to data users |
| In-stream video | At least 50% of the ad's pixels | At least 2 continuous seconds of play | Any 2 continuous, unduplicated seconds, not only the first two |

Reporting rules to write into the brief:

- Three buckets per campaign: viewable, non-viewable and undetermined. Report the **measured rate** ((viewable + non-viewable) ÷ served), the **viewable rate** (viewable ÷ measured) and the impression distribution.
- Undetermined impressions are not non-viewable; a viewable rate calculated on all served impressions is understated and must not be called the viewable rate.
- Report desktop web, mobile web and in-app separately.
- A legitimate click may count as viewable under the user-interaction rule; such impressions are reported separately.

Buying on viewable impressions (vCPM) or setting a minimum viewable rate is a contract choice. Set any threshold from the client's own past campaigns or a named, dated source; vendor benchmarks are labelled "(Vendor)" and are never targets.

## 2. Invalid traffic (IVT)

MRC's IVT 2.0 addendum (June 2020 update; register `MRC-IVT-2020`) defines two categories:

| Category | Found by | Examples |
|---|---|---|
| GIVT (general invalid traffic) | Routine list-based or standard parameter checks | Known invalid data-centre traffic, declared bots and spiders, non-browser user agents, pre-fetch or pre-render traffic, invalid placements |
| SIVT (sophisticated invalid traffic) | Advanced analytics, multipoint corroboration or human review | Hijacked devices, malware and adware, spoofed domains or apps, incentivised or manipulated activity, misappropriated content |

The April 2024 MRC interim update added requirements on domain and inventory mismatch and bundle-ID spoofing in CTV, and on privacy effects on IVT detection (register `MRC-IVT-INTERIM-2024`).

Brief requirements:

- IVT is filtered before billing: pre-bid avoidance plus post-bid measurement by an accredited vendor, with GIVT and SIVT reported separately.
- Partners hold TAG Certified Against Fraud status; CAF requires filtering 100% of monetisable transactions, compliance with the MRC IVT addendum and use of TAG's data-centre IP list (register `TAG-CERTIFIED-AGAINST-FRAUD`).
- Agree the make-good rule before launch: IVT impressions are not billable, and a line above the agreed IVT ceiling is paused and credited.

## 3. Attention (IAB/MRC, November 2025)

The IAB and MRC Attention Measurement Guidelines v1.0 (November 2025; register `IAB-MRC-ATTENTION-2025`) recognise four method families (data signals; visual tracking; physiological and neurological observation; panels and surveys) and predictive models that combine them. Points that shape the brief:

- Viewability comes first. The data-signal and visual-tracking methods require ads to meet MRC viewability (and OOH or audibility rules where they apply); attention reported on non-viewable impressions must be flagged as diagnostic.
- Attention is not a standalone measure of ad effectiveness or business results. Sales and brand effects still need the methods in [advertising attribution and measurement](../../advertising-attribution-and-measurement/SKILL.md).
- Ask any attention vendor: which method, what panel or data underlies the model, sample and coverage by device and market, whether East African audiences are in the calibration data, and whether the service is audited against the guidelines. If the vendor cannot say, the metric is diagnostic only.

## 4. East Africa realism

- Mobile-app and mobile-web inventory dominates what is geotargetable in Uganda, Kenya, Tanzania and Rwanda. Many apps are not measurable by browser viewability tags; in-app measurement needs the vendor's SDK or Open Measurement support, so check coverage before setting a viewable-rate floor.
- Made-for-advertising (MFA) sites and apps (high ad density, arbitraged traffic, low content value) are a real risk in cheap geotargeted supply. Controls: inclusion lists, app-ads.txt, bundle-ID lists, SIVT filtration and a frequency cap.
- Verification vendors' country-level benchmarks for East Africa, and their device coverage, are `NOT_ASSESSED`; ask each vendor for measured-rate coverage in the target country before relying on its numbers.
- Where no accredited verification is available on a line (for example a direct local-publisher deal), require the publisher's ad-server delivery report and screenshots, and label viewability and IVT `NOT_ASSESSED`.

## Sources

Register IDs: `MRC-VIEWABILITY-2015`, `MRC-IVT-2020`, `MRC-IVT-INTERIM-2024`, `TAG-CERTIFIED-AGAINST-FRAUD`, `IAB-MRC-ATTENTION-2025`.

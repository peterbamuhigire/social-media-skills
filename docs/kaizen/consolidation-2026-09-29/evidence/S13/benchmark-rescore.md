# S13 benchmark re-score (plan `02-world-class-benchmark.md`: 133 matrix rows + 23 East Africa rows)

- **Date:** 29 September 2026. Tree: `e7d68fd` (S12) plus the uncommitted S13 working-tree edits at the time of the check.
- **Task:** S13-T04. It extends the S10 re-score ([../S10/benchmark-rescore.md](../S10/benchmark-rescore.md)).
- **Method.** Each of the 156 rows was given one or more closing files at their final paths under `skills/`, with key terms (method words, register IDs) that must appear. A read-only script checked that each file exists and contains every term. The script is `bench_verify.py`, kept in the executor's scratchpad and summarised here.
  - 137 rows passed on the first run.
  - The 19 that did not were resolved by reading the files. In every case the content had moved to a sibling reference, sat in a co-owner skill, or cited a register ID folded in S11. None was missing (see "Resolved checks" below).
  - Rows that S10 marked "carried" (the S04 tracking plan, the S06 merges and the S10-T01 legal currency) were checked against the files in this pass. They no longer rest on the earlier phase's word.
- **Ratings.** The plan's meanings apply:
  - STRONG: an owner skill has an explicit procedure with a current source.
  - THIN: the topic is mentioned or only partly covered.
  - GAP: the topic is absent.

  Every THIN row names its `NOT_ASSESSED` evidence gap.
- **Coverage, not behaviour.** Whether the guidance produces world-class output in a live session is `NOT_ASSESSED (zero-spend rule)`.

## Totals

| Measure | Plan baseline (29 Sep 2026) | After S10 | After S13 (this check) |
|---|---|---|---|
| Matrix rows | 133 | 133 | 133 |
| STRONG | 44 | 129 | **129** |
| THIN | 54 | 4 | **4** (each bound to a named `NOT_ASSESSED` gap) |
| GAP | 35 | 0 | **0** |
| East Africa rows | 23 | 23 | 23 |
| East Africa STRONG | 5 | 16 | **16** |
| East Africa THIN | 13 | 7 | **7** (each bound to a named `NOT_ASSESSED` gap) |
| East Africa GAP | 3 | 0 | **0** |
| East Africa DEFECT | 2 | 0 | **0** |

**No row changed rating and no closing file is missing.** There are no downgrades. There are also no upgrades: every THIN row's evidence gap is still open in the register (see below).

## THIN rows and their `NOT_ASSESSED` gaps

| Row | Gap (register ID, status) |
|---|---|
| SL01-C5 budget vs peer data | Gartner CMO Spend Survey unreadable (HTTP 403): `GARTNER-CMO-SPEND-2025` not_assessed |
| SL07-C6 CTV buying | IAB Tech Lab Dec 2025 CTV release returned HTTP 403: `IAB-TECHLAB-CTV-2025` partial; East African CTV penetration unverified |
| SL12-C7 Kenya gambling (influencers) | BCLB directive text not read: `KE-BCLB-GAMBLING-ADS-2025` partial |
| SL19-C4 CIM competencies | CIM primary page not located: `CIM-PROFESSIONAL-MARKETING-2024` partial |
| EA Payments law | Uganda NPS Act text (ULII) HTTP 403: `UG-NPS-ACT-2020` partial |
| EA Tanzania PDPA | Statute text not read: `TZ-PDPA-REGISTRATION-2026` partial |
| EA Uganda advertising standards | UCC Advertising Standard text not read: `UG-UCC-ADS-2019` (currentness wave 2) |
| EA Uganda online publishers | Influencer coverage and enforcement: `UG-UCC-ONLINE-PUBLISHERS` verified for the page only |
| EA Kenya gambling | Directive text: `KE-BCLB-GAMBLING-ADS-2025` partial |
| EA Uganda taxes | Excise schedule and URA guidance not read: `UG-DATA-EXCISE` partial |
| EA Tanzania online content | 2021 amendment content not read: `TZ-TCRA-ONLINE-CONTENT-AMEND-2021` not_assessed |

## Plan-text corrections (verified here; the parent edits the plan file)

1. **SL21-C6, the East Africa "WhatsApp economics" row, and gap #7.** "72-hour click-to-WhatsApp window" is stale. The engine text is already correct: `platform-whatsapp/references/whatsapp-platform-pricing-and-templates.md` §3, lines 28–29, says the free entry-point window lasts up to 7 days and is opened by click-to-WhatsApp ads only. The same file's §4 records the 1 Oct 2026 change, under which service replies become chargeable after 1,000 a month per number. Register `WHATSAPP-PRICING-2025` is verified, with its next review on 29 Dec 2026.
2. **SL13-C2.** The CIPR stages are mitigate, prepare, **ramp-up**, manage and recover; "arm" is wrong. The engine text is correct: `playbook-crisis-communications/references/crisis-response-procedures.md` lines 213 and 219 cite `CIPR-CRISIS-SOCIAL-2024`.
3. **SL09-C6 and SL15-C5 (clean rooms).** Register ID `IAB-TECHLAB-CLEAN-ROOM` **exists** in `docs/source-registers/source-register.json`. Its status is partial (the standards listing was read, not the full guidance), and its next review is 29 Mar 2027. The engine cites it in `marketing-mix-modelling/references/triangulation-and-decision-governance.md` §4, together with PAIR and the July 2024 guidance, and no longer depends on the MarTech secondary. The plan's source list still shows S13 as the MarTech secondary, so the upgrade belongs in the plan file.

## Resolved checks (content found elsewhere; no rating change)

These are the 19 rows where a first-pass term was absent from the file S10 named. Each was resolved by reading the files. The full resolution is in the "Verified how" column below. Four points are worth recording:

- **Folded register IDs (S11).** `PREMIUM-ICC-2026` was folded into `ICC-CODE-2024-TEXT`, and `06-digital-marketing-strategy` now cites the latter (SL01-C6).
- **Legacy register labels (traceability finding, not a coverage defect).** Several files still cite pre-register labels that are **not IDs in `source-register.json`**; the register maps them only inside `verification_note` text:
  - `08-influencer-marketing-strategy` SKILL.md and `playbook-paid-social-advertising` SKILL.md cite `AD-08`, `AD-09` and `AD-10`;
  - the 08 term-sheet reference cites `KE-01`, `UG-01`, `UG-03`, `TZ-01` and `KE-07`–`KE-09`;
  - `media-planning/references/east-african-media-mix.md` cites `MK-02`.

  Affected rows are SL12-C1, SL12-C2 and SL05-C4. Repair is recommended as a next opportunity: add the full IDs, such as `UK-ASA-CMA-INFLUENCER-2026` and `FTC-ENDORSEMENTS-REVIEWS-2026`, beside the labels.
- **Register ID not cited by ID.** `UG-UCC-ADS-2019` is not cited by ID in any active file; the standard is named in prose only. The row stays THIN regardless.
- **Content in co-owners or references.** In these rows the content sits in a co-owner or in a sibling reference rather than in the named SKILL.md:
  - Partnership Ads: `playbook-paid-social-advertising`;
  - Thought Leader Ads: the social-selling reference `employee-advocacy-programme.md`;
  - Conversion Lift: the attribution geo reference;
  - LTV: `meta-roi-framework/references/retention-cohorts-and-ltv.md`;
  - fake reviews: the `strategy-ewom-reviews` references;
  - personal data in DMs: the social-media-policy governance reference;
  - authentic mentions: the `ai-generative-search-optimisation` rules reference;
  - Boomplay: the programmatic `ctv-dooh-and-audio.md` reference.

## Per-row table

Paths are under `skills/`. "S10" is the S10 "Now" rating.

| Row | S10 | S13 | Closing file(s) at final path | Verified how |
|---|---|---|---|---|
| SL01-C1 | STRONG | STRONG | `strategy/brand-strategy-and-distinctive-assets/references/long-short-balance-and-reach.md`; `advertising/advertising-strategy-and-budget/SKILL.md`; `pipeline/06-digital-marketing-strategy/SKILL.md` | exists; terms found: 60:40, 60:40, 60:40 |
| SL01-C2 | STRONG | STRONG | `strategy/brand-strategy-and-distinctive-assets/references/brand-tracking.md`; `advertising/advertising-strategy-and-budget/references/objectives-and-measurement-architecture.md` | exists; terms found: ladder, WARC-EFFECTIVENESS-CODE-2020 |
| SL01-C3 | STRONG | STRONG | `strategy/brand-strategy-and-distinctive-assets/references/long-short-balance-and-reach.md`; `platforms/platform-linkedin/SKILL.md`; `advertising/media-planning/SKILL.md` | `media-planning` SKILL.md carries the 95:5 rule; its register ID `LINKEDIN-B2B-95-5` is cited in `platform-linkedin`, `playbook-paid-social-advertising` and the brand skill, not in media-planning (traceability note, no downgrade) |
| SL01-C4 | STRONG | STRONG | `advertising/advertising-strategy-and-budget/SKILL.md` | exists; terms found: measurement |
| SL01-C5 | THIN | THIN | `meta-analytics-ops/meta-budget-planner/SKILL.md` | exists; terms found: benchmark |
| SL01-C6 | STRONG | STRONG | `pipeline/06-digital-marketing-strategy/SKILL.md` | S11 folded `PREMIUM-ICC-2026` into `ICC-CODE-2024-TEXT`; `06-digital-marketing-strategy` Decision Rules now cite `ICC-CODE-2024-TEXT` + legal-market release gate |
| SL01-C7 | STRONG | STRONG | `strategy/traction-channel-bullseye/SKILL.md`; `strategy/strategy-channel-architecture/SKILL.md` | exists; terms found: bullseye, role |
| SL02-C1 | STRONG | STRONG | `strategy/brand-strategy-and-distinctive-assets/references/cep-and-mental-availability.md` | exists; terms found: EBI-CATEGORY-ENTRY-POINTS, mental availability |
| SL02-C2 | STRONG | STRONG | `strategy/brand-strategy-and-distinctive-assets/references/distinctive-asset-audit.md` | exists; terms found: EBI-DISTINCTIVE-ASSETS, fame, unique |
| SL02-C3 | STRONG | STRONG | `strategy/brand-strategy-and-distinctive-assets/references/long-short-balance-and-reach.md` | exists; terms found: penetration |
| SL02-C4 | STRONG | STRONG | `advertising/creative-brief-and-big-idea/references/creative-effectiveness-and-pretesting.md` | exists; terms found: IPA-LONG-SHORT-2013, emotional |
| SL02-C5 | STRONG | STRONG | `strategy/brand-strategy-and-distinctive-assets/references/brand-tracking.md`; `meta-analytics-ops/meta-reporting/references/effectiveness-ladder-review.md` | exists; terms found: track, brand |
| SL02-C6 | STRONG | STRONG | `strategy/marketing-foundations-stp-positioning/SKILL.md` | exists; terms found: segment, position |
| SL02-C7 | STRONG | STRONG | `pipeline/04-brand-voice-intake/SKILL.md` | exists; terms found: voice |
| SL03-C1 | STRONG | STRONG | `pipeline/05-social-media-strategy/SKILL.md`; `pipeline/10-content-pillars/SKILL.md` | exists; terms found: strategy, pillar |
| SL03-C2 | STRONG | STRONG | `seo-discovery/seo-geo-optimisation/SKILL.md`; `content-writing/blog-writer/SKILL.md` | exists; terms found: GOOGLE-SPAM-POLICIES, GOOGLE-SPAM-POLICIES |
| SL03-C3 | STRONG | STRONG | `platforms/platform-facebook/SKILL.md`; `meta-analytics-ops/meta-content-repurposing/SKILL.md` | exists; terms found: META-UNORIGINAL-CONTENT-2025, META-UNORIGINAL-CONTENT-2025 |
| SL03-C4 | STRONG | STRONG | `advertising/ad-copy-and-hook-lab/references/abcd-video-craft-and-ai-volume.md`; `strategy/strategy-video-content/SKILL.md` | `strategy-video-content` SKILL.md names ABCD; the `YOUTUBE-ABCD` register ID sits in the ABCD reference only |
| SL03-C5 | STRONG | STRONG | `policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md` | exists; terms found: C2PA, AI info |
| SL03-C6 | STRONG | STRONG | `playbooks/playbook-content-production/SKILL.md` | exists; terms found: approval |
| SL04-C1 | STRONG | STRONG | `platforms/platform-facebook/SKILL.md`; `platforms/platform-linkedin/SKILL.md` | exists; terms found: Use when, Use when |
| SL04-C2 | STRONG | STRONG | `pipeline/08-influencer-marketing-strategy/SKILL.md` | Partnership Ads procedure lives in `playbook-paid-social-advertising` SKILL.md; 08 carries creator discovery and term sheet |
| SL04-C3 | STRONG | STRONG | `pipeline/08-influencer-marketing-strategy` | 08 Decision Rules: up-front 'Ad'/'Paid partnership' label plus the platform branded-content tool (wording 'branded-content tool', not 'toggle') |
| SL04-C4 | STRONG (carried) | STRONG | `playbooks/playbook-social-selling/SKILL.md` | Thought Leader Ads in `playbook-social-selling/references/employee-advocacy-programme.md` (carried from S06, now checked) |
| SL04-C5 | STRONG | STRONG | `meta-analytics-ops/meta-social-listening/SKILL.md` | exists; terms found: escalat |
| SL05-C1 | STRONG | STRONG | `playbooks/playbook-paid-social-advertising/SKILL.md` | exists; terms found: Advantage+ |
| SL05-C2 | STRONG (carried) | STRONG | `meta-analytics-ops/measurement-tracking-plan/references` | exists; terms found: dedup, event_id |
| SL05-C3 | STRONG | STRONG | `advertising/advertising-attribution-and-measurement/SKILL.md`; `advertising/advertising-attribution-and-measurement/references/geo-power-and-incrementality-hierarchy.md` | exists; terms found: holdout, geo |
| SL05-C4 | STRONG | STRONG | `playbooks/playbook-paid-social-advertising/SKILL.md` | social-issue/political ad rules in `playbook-paid-social-advertising` SKILL.md + `meta-campaign-build-spec.md`; `META-SIEP-AD-LIBRARY-2026` cited in the policy provenance ref, not the paid-social skill (traceability note) |
| SL05-C5 | STRONG | STRONG | `advertising/ad-copy-and-hook-lab/references/abcd-video-craft-and-ai-volume.md`; `content-writing/prompt-engineering-library/SKILL.md` | exists; terms found: label, label |
| SL05-C6 | STRONG | STRONG | `platforms/platform-linkedin/SKILL.md` | exists; terms found: 95:5 |
| SL05-C7 | STRONG | STRONG | `playbooks/playbook-agency-operations/references/certification-and-competency-register.md`; `business-development/biz-dev-credentials/SKILL.md` | exists; terms found: Meta, certif |
| SL06-C1 | STRONG | STRONG | `advertising/paid-search-advertising/SKILL.md` | exists; terms found: Performance Max |
| SL06-C2 | STRONG | STRONG | `advertising/paid-search-advertising/references/shopping-and-feeds.md` | exists; terms found: MERCHANT-CENTER-PRODUCT-DATA, GTIN |
| SL06-C3 | STRONG (carried) | STRONG | `meta-analytics-ops/measurement-tracking-plan/references` | exists; terms found: enhanced conversions |
| SL06-C4 | STRONG (carried) | STRONG | `meta-analytics-ops/measurement-tracking-plan/references` | exists; terms found: Consent Mode |
| SL06-C5 | STRONG | STRONG | `advertising/advertising-attribution-and-measurement/SKILL.md` | Conversion Lift in attribution ref `geo-power-and-incrementality-hierarchy.md` |
| SL06-C6 | STRONG | STRONG | `playbooks/playbook-agency-operations/references/certification-and-competency-register.md` | exists; terms found: GOOGLE-ADS-CERTIFICATIONS |
| SL07-C1 | STRONG | STRONG | `advertising/programmatic-and-brand-safety/references/viewability-ivt-and-attention.md` | exists; terms found: viewab, MRC |
| SL07-C2 | STRONG | STRONG | `advertising/programmatic-and-brand-safety/references/viewability-ivt-and-attention.md` | exists; terms found: MRC-IVT-2020, TAG-CERTIFIED-AGAINST-FRAUD |
| SL07-C3 | STRONG | STRONG | `advertising/programmatic-and-brand-safety/references/buying-routes-and-supply-path.md` | exists; terms found: ads.txt, sellers.json |
| SL07-C4 | STRONG | STRONG | `advertising/programmatic-and-brand-safety/references/brand-safety-and-suitability.md` | exists; terms found: WFA-GARM-DISCONTINUED-2024, suitability |
| SL07-C5 | STRONG | STRONG | `advertising/programmatic-and-brand-safety/references/viewability-ivt-and-attention.md` | exists; terms found: IAB-MRC-ATTENTION-2025 |
| SL07-C6 | THIN | THIN | `advertising/programmatic-and-brand-safety/references/ctv-dooh-and-audio.md` | exists; terms found: CTV, pod |
| SL07-C7 | STRONG | STRONG | `advertising/programmatic-and-brand-safety/references/ctv-dooh-and-audio.md`; `advertising/media-planning/references/east-african-media-mix.md` | exists; terms found: MRC-OOH-STANDARDS, outdoor |
| SL07-C8 | STRONG | STRONG | `advertising/programmatic-and-brand-safety/references/ctv-dooh-and-audio.md`; `strategy/strategy-video-content/references/podcast-and-audio-series.md`; `advertising/media-planning/references/east-african-media-mix.md` | exists; terms found: audio, IAB-TECHLAB-PODCAST-2-2, AFROBAROMETER-UG-RADIO-2026 |
| SL08-C1 | STRONG | STRONG | `advertising/creative-brief-and-big-idea/references/creative-effectiveness-and-pretesting.md` | exists; terms found: pre-test, System1 |
| SL08-C2 | STRONG | STRONG | `advertising/ad-copy-and-hook-lab/references/abcd-video-craft-and-ai-volume.md` | exists; terms found: ABCD |
| SL08-C3 | STRONG | STRONG | `advertising/creative-brief-and-big-idea/references/creative-effectiveness-and-pretesting.md` | exists; terms found: rational |
| SL08-C4 | STRONG | STRONG | `meta-analytics-ops/meta-reporting/references/effectiveness-ladder-review.md` | exists; terms found: ladder |
| SL08-C5 | STRONG | STRONG | `meta-analytics-ops/meta-testing-framework/references/trustworthy-experiments-srm-power-holdouts.md`; `advertising/ad-testing-and-scaling/references/test-rigour-srm-and-preregistration.md` | exists; terms found: SRM, pre-regist, SRM |
| SL08-C6 | STRONG | STRONG | `advertising/creative-brief-and-big-idea/references/creative-effectiveness-and-pretesting.md`; `strategy/brand-strategy-and-distinctive-assets/references/distinctive-asset-audit.md` | exists; terms found: distinctive, creative |
| SL08-C7 | STRONG | STRONG | `policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md` | exists; terms found: risk |
| SL08-C8 | STRONG | STRONG | `advertising/creative-brief-and-big-idea/SKILL.md` | exists; terms found: big idea |
| SL09-C1 | STRONG | STRONG | `advertising/marketing-mix-modelling/SKILL.md`; `advertising/marketing-mix-modelling/references/meridian-and-robyn-choice.md` | exists; terms found: Meridian, Robyn, Meridian, Robyn |
| SL09-C2 | STRONG | STRONG | `advertising/marketing-mix-modelling/references/calibration-and-geo-experiments.md` | exists; terms found: prior, calibrat |
| SL09-C3 | STRONG | STRONG | `advertising/advertising-attribution-and-measurement/references/geo-power-and-incrementality-hierarchy.md` | exists; terms found: power, META-GEOLIFT |
| SL09-C4 | STRONG | STRONG | `advertising/advertising-attribution-and-measurement/references/geo-power-and-incrementality-hierarchy.md`; `advertising/marketing-mix-modelling/references/triangulation-and-decision-governance.md` | exists; terms found: hierarchy, IAB-INCREMENTAL-COMMERCE-MEDIA-2025 |
| SL09-C5 | STRONG (carried) | STRONG | `meta-analytics-ops/measurement-tracking-plan/references` | exists; terms found: Consent Mode, enhanced conversions, Conversions API |
| SL09-C6 | STRONG (note, low priority) | STRONG | `advertising/marketing-mix-modelling/references/triangulation-and-decision-governance.md` | exists; terms found: IAB-TECHLAB-CLEAN-ROOM, clean room |
| SL09-C7 | STRONG | STRONG | `advertising/marketing-mix-modelling/references/triangulation-and-decision-governance.md` | exists; terms found: triangulat |
| SL09-C8 | STRONG | STRONG | `meta-analytics-ops/meta-roi-framework/SKILL.md`; `advertising/direct-response-economics/SKILL.md` | LTV in `meta-roi-framework/references/retention-cohorts-and-ltv.md`; `direct-response-economics` carries break-even/CAC economics |
| SL10-C1 | STRONG | STRONG | `meta-analytics-ops/meta-testing-framework/references/trustworthy-experiments-srm-power-holdouts.md`; `playbooks/playbook-post-click-strategy/SKILL.md` | exists; terms found: SRM, guardrail, trustworthy |
| SL10-C2 | STRONG | STRONG | `advertising/ad-to-site-journey-handoff/references/landing-page-brief-template.md` | exists; terms found: WEBDEV-CORE-WEB-VITALS, INP |
| SL10-C3 | STRONG | STRONG | `playbooks/playbook-post-click-strategy/references/ecommerce-and-whatsapp-conversion-diagnosis.md` | exists; terms found: GOOGLE-OPTIMIZE-SUNSET-2023 |
| SL10-C4 | STRONG (carried) | STRONG | `meta-analytics-ops/measurement-tracking-plan/references` | exists; terms found: server-side, experiment |
| SL10-C5 | STRONG | STRONG | `playbooks/playbook-post-click-strategy/SKILL.md` | exists; terms found: WhatsApp |
| SL11-C1 | STRONG | STRONG | `ai-marketing/ai-generative-search-optimisation/SKILL.md` | exists; terms found: AI Overviews |
| SL11-C2 | STRONG | STRONG | `ai-marketing/ai-generative-search-optimisation/SKILL.md` | exists; terms found: llms.txt |
| SL11-C3 | STRONG | STRONG | `content-writing/blog-writer/SKILL.md` | exists; terms found: expert |
| SL11-C4 | STRONG | STRONG | `seo-discovery/seo-geo-optimisation/SKILL.md` | exists; terms found: spam |
| SL11-C5 | STRONG | STRONG | `seo-discovery/seo-geo-optimisation/SKILL.md` | exists; terms found: GOOGLE-AI-FEATURES-2025, GOOGLE-EXTENDED-2026 |
| SL11-C6 | STRONG | STRONG | `meta-analytics-ops/meta-reporting/references/effectiveness-ladder-review.md` | exists; terms found: Search Console |
| SL11-C7 | STRONG | STRONG | `seo-discovery/seo-geo-optimisation/SKILL.md` | exists; terms found: Core Web Vitals |
| SL12-C1 | STRONG | STRONG | `pipeline/08-influencer-marketing-strategy` | UK ASA/CMA row in 08 ref `influencer-term-sheet-and-disclosure.md` (jurisdiction table); SKILL.md cites legacy label AD-09, which the register maps to `UK-ASA-CMA-INFLUENCER-2026` in `verification_note` only (traceability note) |
| SL12-C2 | STRONG | STRONG | `pipeline/08-influencer-marketing-strategy` | FTC row in the same 08 ref; `FTC-ENDORSEMENTS-REVIEWS-2026` cited in `strategy-ewom-reviews` refs; 08 uses legacy label AD-09 (traceability note) |
| SL12-C3 | STRONG | STRONG | `strategy/strategy-ewom-reviews/SKILL.md` | fake-review rule in `strategy-ewom-reviews/references/*` (three files) |
| SL12-C4 | STRONG | STRONG | `pipeline/08-influencer-marketing-strategy/references/influencer-term-sheet-and-disclosure.md` | exists; terms found: ICC-CODE-2024-TEXT, virtual |
| SL12-C5 | STRONG | STRONG | `pipeline/08-influencer-marketing-strategy` | as SL04-C3 |
| SL12-C6 | STRONG | STRONG | `pipeline/08-influencer-marketing-strategy/SKILL.md` | as SL04-C2 |
| SL12-C7 | THIN (carried from T01) | THIN | `pipeline/08-influencer-marketing-strategy` | `KE-BCLB-GAMBLING-ADS-2025` (partial) in 08 term-sheet ref and 09 contests ref; directive text `NOT_ASSESSED` |
| SL13-C1 | STRONG | STRONG | `playbooks/playbook-community-management/SKILL.md` | exists; terms found: response |
| SL13-C2 | STRONG | STRONG | `playbooks/playbook-crisis-communications/references/crisis-response-procedures.md` | exists; terms found: CIPR-CRISIS-SOCIAL-2024, ramp-up |
| SL13-C3 | STRONG | STRONG | `platforms/platform-whatsapp/references/whatsapp-platform-pricing-and-templates.md`; `playbooks/playbook-chatbot-strategy/SKILL.md` | exists; terms found: 24-hour, service, WHATSAPP-PRICING-2025 |
| SL13-C4 | STRONG | STRONG | `playbooks/playbook-social-media-policy/SKILL.md` | personal data in DMs: `playbook-social-media-policy/references/governance-roles-access-and-approvals.md` (DPPA) |
| SL14-C1 | STRONG | STRONG | `pipeline/07-email-marketing-strategy/references/deliverability-and-lifecycle-holdouts.md` | exists; terms found: GMAIL-SENDER-GUIDELINES, YAHOO-SENDER-REQUIREMENTS, DMARC, one-click |
| SL14-C2 | STRONG | STRONG | `business-development/biz-dev-lawful-prospecting-outreach/SKILL.md`; `pipeline/07-email-marketing-strategy/SKILL.md` | exists; terms found: consent, consent |
| SL14-C3 | STRONG | STRONG | `platforms/platform-whatsapp/references/whatsapp-platform-pricing-and-templates.md` | exists; terms found: template, opt-in |
| SL14-C4 | STRONG (carried) | STRONG | `meta-analytics-ops/measurement-tracking-plan/references` | exists; terms found: first-party |
| SL14-C5 | STRONG | STRONG | `pipeline/07-email-marketing-strategy/references/deliverability-and-lifecycle-holdouts.md`; `meta-analytics-ops/meta-testing-framework/references/trustworthy-experiments-srm-power-holdouts.md` | exists; terms found: holdout, holdout |
| SL14-C6 | STRONG | STRONG | `pipeline/07-email-marketing-strategy/SKILL.md`; `meta-analytics-ops/meta-sales-marketing-alignment/SKILL.md` | exists; terms found: win-back, scor |
| SL15-C1 | STRONG (carried) | STRONG | `meta-analytics-ops/measurement-tracking-plan/references` | exists; terms found: BigQuery |
| SL15-C2 | STRONG (carried) | STRONG | `meta-analytics-ops/measurement-tracking-plan/references` | exists; terms found: server-side, GTM |
| SL15-C3 | STRONG (carried) | STRONG | `meta-analytics-ops/measurement-tracking-plan/references` | exists; terms found: GOOGLE-CMP-TCF-2026 |
| SL15-C4 | STRONG (carried) | STRONG | `meta-analytics-ops/measurement-tracking-plan/references` | exists; terms found: UG-PDPO-OFFSHORE-2025 |
| SL15-C5 | STRONG (note) | STRONG | `advertising/marketing-mix-modelling/references/triangulation-and-decision-governance.md` | exists; terms found: clean room |
| SL15-C6 | STRONG | STRONG | `meta-analytics-ops/meta-social-metrics-framework/SKILL.md`; `meta-analytics-ops/measurement-tracking-plan/references` | exists; terms found: KPI, UTM |
| SL16-C1 | STRONG | STRONG | `meta-analytics-ops/meta-tools-stack-evaluation/SKILL.md` | exists; terms found: audit |
| SL16-C2 | STRONG | STRONG | `ai-marketing/ai-use-case-mapping/SKILL.md`; `playbooks/playbook-marketing-automation/SKILL.md` | exists; terms found: agent, agent |
| SL16-C3 | STRONG | STRONG | `playbooks/playbook-agency-operations/references/commercial-governance-and-contracts.md` | exists; terms found: audit right, CSFA |
| SL16-C4 | STRONG (carried) | STRONG | `meta-analytics-ops/measurement-tracking-plan/references` | exists; terms found: server-side, tag |
| SL16-C5 | STRONG | STRONG | `playbooks/playbook-marketing-automation/SKILL.md` | exists; terms found: human |
| SL17-C1 | STRONG | STRONG | `policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md` | exists; terms found: 42001 |
| SL17-C2 | STRONG | STRONG | `policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md` | exists; terms found: 600-1 |
| SL17-C3 | STRONG | STRONG | `policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md` | exists; terms found: IAB, Disclosure Framework |
| SL17-C4 | STRONG | STRONG | `policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md` | exists; terms found: Art, 50 |
| SL17-C5 | STRONG | STRONG | `policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md` | exists; terms found: AI info, TikTok |
| SL17-C6 | STRONG | STRONG | `policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md` | exists; terms found: ICC |
| SL17-C7 | STRONG | STRONG | `business-development/biz-dev-proposal/references/pitch-conduct-and-ai-clauses.md` | exists; terms found: clause |
| SL17-C8 | STRONG | STRONG | `ai-marketing/anti-ai-slop/SKILL.md`; `ai-marketing/ai-slop-audit/SKILL.md` | exists; terms found: slop, score |
| SL18-C1 | STRONG | STRONG | `business-development/biz-dev-pricing-menu/references/remuneration-models-evidence.md` | exists; terms found: payment by results |
| SL18-C2 | STRONG | STRONG | `playbooks/playbook-agency-operations/references/commercial-governance-and-contracts.md` | exists; terms found: ANA |
| SL18-C3 | STRONG | STRONG | `business-development/biz-dev-proposal/references/pitch-conduct-and-ai-clauses.md` | exists; terms found: Pitch Positive |
| SL18-C4 | STRONG | STRONG | `playbooks/playbook-agency-operations/references/commercial-governance-and-contracts.md`; `advertising/media-planning/SKILL.md` | exists; terms found: principal, principal |
| SL18-C5 | STRONG | STRONG | `advertising/programmatic-and-brand-safety/references/buying-routes-and-supply-path.md` | exists; terms found: transparency report |
| SL18-C6 | STRONG | STRONG | `meta-analytics-ops/meta-reporting/references/effectiveness-ladder-review.md` | exists; terms found: ladder |
| SL18-C7 | STRONG | STRONG | `business-development/biz-dev-credentials/SKILL.md` | exists; terms found: credential |
| SL19-C1-C2 | STRONG | STRONG | `playbooks/playbook-agency-operations/references/certification-and-competency-register.md` | exists; terms found: Skillshop, Meta |
| SL19-C3 | STRONG | STRONG | `playbooks/playbook-agency-operations/references/certification-and-competency-register.md` | exists; terms found: IPA |
| SL19-C4 | THIN | THIN | `playbooks/playbook-agency-operations/references/certification-and-competency-register.md` | exists; terms found: CIM |
| SL19-C5 | STRONG | STRONG | `training/training-client-team/SKILL.md` | exists; terms found: train |
| SL20-C1 | STRONG | STRONG | `playbooks/playbook-pr-publicity/references/pr-evaluation.md` | exists; terms found: Barcelona, AVE |
| SL20-C2 | STRONG | STRONG | `playbooks/playbook-crisis-communications/SKILL.md` | exists; terms found: minute |
| SL20-C3 | STRONG | STRONG | `playbooks/playbook-reputation-management/SKILL.md` | exists; terms found: monitor |
| SL20-C4 | STRONG | STRONG | `playbooks/playbook-crisis-communications/references/synthetic-media-and-deepfake-protocol.md` | exists; terms found: deepfake |
| SL20-C5 | STRONG | STRONG | `playbooks/playbook-pr-publicity/SKILL.md` | `ai-generative-search-optimisation/references/ai-search-and-social-discovery-rules.md` (never manufacture mentions; inauthentic mentions); PR skill: genuine news only |
| SL21-C1 | STRONG | STRONG | `strategy/social-commerce-strategy/references/commerce-media-and-marketplaces.md` | exists; terms found: IAB-MRC-RETAIL-MEDIA-2024 |
| SL21-C2 | STRONG | STRONG | `strategy/social-commerce-strategy/references/commerce-media-and-marketplaces.md` | exists; terms found: incremental |
| SL21-C3 | STRONG | STRONG | `advertising/paid-search-advertising/references/shopping-and-feeds.md` | exists; terms found: feed |
| SL21-C4 | STRONG | STRONG | `playbooks/playbook-paid-social-advertising/SKILL.md`; `advertising/paid-search-advertising/SKILL.md` | exists; terms found: Advantage+, Performance Max |
| SL21-C5 | STRONG | STRONG | `strategy/social-commerce-strategy/references/commerce-media-and-marketplaces.md` | exists; terms found: Jumia, Jiji |
| SL21-C6 | STRONG | STRONG | `platforms/platform-whatsapp/references/whatsapp-platform-pricing-and-templates.md`; `strategy/social-commerce-strategy/SKILL.md` | exists; terms found: 7 days, click-to-WhatsApp, WhatsApp |
| SL21-C7 | STRONG | STRONG | `strategy/social-commerce-strategy/SKILL.md` | exists; terms found: mobile money |
| EA Market size | STRONG | STRONG | `advertising/media-planning/references/east-african-media-mix.md` | exists; terms found: DATAREPORTAL-TZ-2026, DATAREPORTAL-RW-2026 |
| EA Mobile-first | STRONG | STRONG | `advertising/media-planning/references/east-african-media-mix.md` | exists; terms found: GSMA-SSA-MOBILE-ECONOMY |
| EA Mobile money | STRONG (Secondary label) | STRONG | `strategy/social-commerce-strategy/references/commerce-media-and-marketplaces.md` | exists; terms found: GSMA-MOBILE-MONEY-2025 |
| EA M-Pesa | STRONG | STRONG | `strategy/social-commerce-strategy/references/commerce-media-and-marketplaces.md` | exists; terms found: SAFARICOM-FY2026-MPESA |
| EA Payments law | THIN | THIN | `strategy/social-commerce-strategy/references/commerce-media-and-marketplaces.md` | exists; terms found: UG-NPS-ACT-2020 |
| EA Radio | STRONG | STRONG | `advertising/media-planning/references/east-african-media-mix.md` | exists; terms found: AFROBAROMETER-UG-RADIO-2026 |
| EA WhatsApp economics | STRONG | STRONG | `platforms/platform-whatsapp/references/whatsapp-platform-pricing-and-templates.md` | exists; terms found: WHATSAPP-RATE-CARD-EA, Rest of Africa, 1 Oct |
| EA WhatsApp opt-in | STRONG | STRONG | `platforms/platform-whatsapp/SKILL.md` | exists; terms found: opt-in |
| EA Uganda DPPA | STRONG | STRONG | `business-development/biz-dev-lawful-prospecting-outreach/SKILL.md` | exists; terms found: DPPA |
| EA Kenya DPA | STRONG | STRONG | `business-development/biz-dev-lawful-prospecting-outreach/SKILL.md` | `KE-ODPC-DIRECT-MARKETING-2026` cited in lawful-prospecting ref `personalised-video-outreach.md`, 07 deliverability ref and the tracking-plan consent refs |
| EA Tanzania PDPA | THIN (carried from T01) | THIN | see note | `TZ-PDPA` in lawful-prospecting ref `data-protection-checks-for-outreach.md`, tracking-plan consent refs and 08 term-sheet ref; statute text `NOT_ASSESSED` (`TZ-PDPA-REGISTRATION-2026` partial) |
| EA Rwanda | STRONG (carried from T01) | STRONG | see note | `RW-DPP-REGISTRATION-2026` in tracking-plan `consent-mode-and-cmp.md`, `consent-retention-and-sharing-review.md` and 08 term-sheet ref |
| EA Uganda advertising standards | THIN | THIN | see note | UCC Advertising Standard named in 08 term-sheet ref and agency governance ref; register ID `UG-UCC-ADS-2019` not cited by ID in any active file (traceability note); text `NOT_ASSESSED` |
| EA Uganda online publishers | THIN | THIN | see note | `UG-UCC-ONLINE-PUBLISHERS` in 08 ref `influencer-term-sheet-and-disclosure.md`; influencer coverage and enforcement `NOT_ASSESSED` |
| EA Kenya advertising code | STRONG (carried from T01) | STRONG | see note | `KE-ASBK-CODE-2003` in 08 term-sheet ref, agency governance ref, policy provenance ref |
| EA Kenya gambling | THIN (carried from T01) | THIN | see note | `KE-BCLB-GAMBLING-ADS-2025` (partial) in 08 term-sheet ref and 09 ref `contests-promotions-and-gaming-rules.md`; directive text `NOT_ASSESSED` |
| EA Kenya bulk SMS | STRONG (carried from T01, scope corrected) | STRONG | see note | `KE-CA-POLITICAL-BULK-SMS-2017` in `platform-whatsapp/references/whatsapp-platform-pricing-and-templates.md` (political bulk SMS scope) |
| EA Uganda cyber law | STRONG (carried from T01) | STRONG | see note | no active file cites the 2022 Amendment Act as law; 08 term-sheet ref, deepfake protocol and social-media-policy governance ref state it was declared void on 17 Mar 2026 |
| EA Facebook in Uganda | STRONG (carried from T01) | STRONG | see note | `AGENTS.md` router row: status unstable, verify at campaign date (`UG-FACEBOOK-ACCESS-2026`); same caution in ad-testing, lawful-prospecting and persona refs; no active file says 'blocked' as current |
| EA Internet shutdowns | STRONG (carried from T01) | STRONG | `playbooks/playbook-crisis-communications/references/internet-shutdown-contingency.md` | exists; terms found: shutdown |
| EA Uganda taxes | THIN | THIN | see note | `UG-DATA-EXCISE` (partial) in `meta-algorithm-guide/references/platform-ranking-reference.md`; URA and Act text `NOT_ASSESSED` |
| EA Tanzania online content | THIN (carried from T01) | THIN | see note | `TZ-ONLINE-CONTENT-2020` in 09 ref `contests-promotions-and-gaming-rules.md`; 2021 amendment content `NOT_ASSESSED` (`TZ-TCRA-ONLINE-CONTENT-AMEND-2021`) |
| EA Marketplaces and streaming | STRONG | STRONG | `strategy/social-commerce-strategy/references/commerce-media-and-marketplaces.md` | Jumia/Jiji in commerce ref §3; Boomplay (streaming audio, figures UNVERIFIED) in programmatic ref `ctv-dooh-and-audio.md` §3 |

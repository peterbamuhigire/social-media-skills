# S10 benchmark re-score (plan `02-world-class-benchmark.md`, 133 matrix rows + 23 East Africa rows)

- **Date:** 29 September 2026. Working tree on `3416d0b` (S09) plus the S10 change set.
- **Method:** each row re-rated against the file and section that now owns it. Ratings keep the plan's meaning (STRONG = an owner skill has an explicit procedure with a current source; THIN = mentioned or partial; GAP = absent). A row whose remaining weakness is an evidence gap carries the `NOT_ASSESSED` reason. Rows closed by earlier phases (S04 tracking plan, S06 merges, S10-T01 legal currency) are carried from those phases' evidence and marked "carried"; they were not re-read in S10.
- **Coverage, not behaviour:** whether the guidance produces world-class output in a live session is `NOT_ASSESSED (zero-spend rule)`.

## Totals

| Measure | Plan baseline | After S10 |
|---|---|---|
| Matrix rows | 133 | 133 |
| STRONG | 44 | **129** |
| THIN | 54 | **4** (each with a `NOT_ASSESSED` reason) |
| GAP | 35 | **0** |
| East Africa rows | 5 STRONG, 13 THIN, 3 GAP, 2 DEFECT | **16 STRONG, 7 THIN (each `NOT_ASSESSED`-bound), 0 GAP, 0 DEFECT** |

## Matrix rows (skill paths are under `skills/`; "ref" = that skill's `references/` file)

| Row | Was | Now | Closed by (file § section) |
|---|---|---|---|
| SL01-C1 60:40 as a start | GAP | STRONG | `brand-strategy-and-distinctive-assets` Decision Rules + ref `long-short-balance-and-reach.md` §1; `advertising-strategy-and-budget` Decision Rules + ref `objectives-and-measurement-architecture.md` §7; `06-digital-marketing-strategy` Decision Rules |
| SL01-C2 effectiveness ladder objectives | THIN | STRONG | brand ref `brand-tracking.md` §1; `advertising-strategy-and-budget` ref §7 (`WARC-EFFECTIVENESS-CODE-2020`) |
| SL01-C3 95:5 | GAP | STRONG | brand ref `long-short-balance-and-reach.md` §3; `platform-linkedin` Decision Rules; `media-planning` References line (`LINKEDIN-B2B-95-5`) |
| SL01-C4 measurement plan in brief | STRONG | STRONG | unchanged |
| SL01-C5 budget vs peer data | THIN | THIN | `meta-budget-planner` Decision Rules (peer benchmark is context, not a target). `NOT_ASSESSED`: Gartner CMO Spend Survey unreadable (HTTP 403), `GARTNER-CMO-SPEND-2025` not_assessed |
| SL01-C6 compliance by design | THIN | STRONG | `06-digital-marketing-strategy` Decision Rules (`PREMIUM-ICC-2026`, legal-market release gate) |
| SL01-C7 channel choice | STRONG | STRONG | unchanged |
| SL02-C1 CEPs / mental availability | GAP | STRONG | brand ref `cep-and-mental-availability.md` §2–4 (`EBI-CATEGORY-ENTRY-POINTS`) |
| SL02-C2 distinctive-asset audit | GAP | STRONG | brand ref `distinctive-asset-audit.md` §2–4 (`EBI-DISTINCTIVE-ASSETS`); visual execution to the design engine |
| SL02-C3 penetration and broad reach | GAP | STRONG | brand ref `long-short-balance-and-reach.md` §2; `media-planning` References line |
| SL02-C4 emotional creative, long term | THIN | STRONG | `creative-brief-and-big-idea` ref `creative-effectiveness-and-pretesting.md` §1 (`IPA-LONG-SHORT-2013`) |
| SL02-C5 brand and business tracking | GAP | STRONG | brand ref `brand-tracking.md` §2–4; `meta-reporting` ref `effectiveness-ladder-review.md` §3 |
| SL02-C6 STP | STRONG | STRONG | unchanged |
| SL02-C7 verbal identity | STRONG | STRONG | unchanged |
| SL03-C1 content strategy | STRONG | STRONG | unchanged |
| SL03-C2 people-first, spam policy | STRONG (spam once) | STRONG | `seo-geo-optimisation` Decision Rules; `blog-writer` Anti-Patterns (`GOOGLE-SPAM-POLICIES`) |
| SL03-C3 Meta unoriginal content | THIN | STRONG | `platform-facebook`, `meta-content-repurposing` Decision Rules (`META-UNORIGINAL-CONTENT-2025`) |
| SL03-C4 ABCD | THIN | STRONG | `ad-copy-and-hook-lab` ref `abcd-video-craft-and-ai-volume.md` §1; `strategy-video-content` Workflow 4 (`YOUTUBE-ABCD`) |
| SL03-C5 C2PA / AI info | THIN | STRONG | `policy-ai-content-ethics` ref `ai-transparency-and-provenance.md` §5–6 |
| SL03-C6 production workflow | STRONG | STRONG | unchanged |
| SL04-C1 platform-native operation | STRONG | STRONG | unchanged (S08 descriptions) |
| SL04-C2 creator discovery | STRONG | STRONG | unchanged |
| SL04-C3 disclosure toggles | STRONG | STRONG | unchanged |
| SL04-C4 employee advocacy + TLA | THIN | STRONG (carried) | S06 merge into `playbook-social-selling` |
| SL04-C5 listening with escalation | STRONG | STRONG | unchanged |
| SL05-C1 automated campaigns | STRONG | STRONG | unchanged |
| SL05-C2 CAPI dedupe | THIN | STRONG (carried) | S04 NEW `measurement-tracking-plan` |
| SL05-C3 holdout / geo validation | STRONG | STRONG | plus attribution ref `geo-power-and-incrementality-hierarchy.md` |
| SL05-C4 SIEP ads | STRONG | STRONG | unchanged |
| SL05-C5 AI creative volume, labelled | THIN | STRONG | `ad-copy-and-hook-lab` ref `abcd-video-craft-and-ai-volume.md` §2; `prompt-engineering-library` Decision Rules; policy ref §3, §6 |
| SL05-C6 B2B 95:5 in paid social | THIN | STRONG | `platform-linkedin` Decision Rules; `playbook-paid-social-advertising` References |
| SL05-C7 certifications | THIN | STRONG | `playbook-agency-operations` ref `certification-and-competency-register.md` §1–2; `biz-dev-credentials` Decision Rules (Meta validity `NOT_ASSESSED`) |
| SL06-C1 PMax | STRONG | STRONG | unchanged |
| SL06-C2 Merchant Center / GTIN | THIN | STRONG | `paid-search-advertising` ref `shopping-and-feeds.md` §1–3 (`MERCHANT-CENTER-PRODUCT-DATA`) |
| SL06-C3 enhanced conversions | GAP | STRONG (carried) | S04 `measurement-tracking-plan` |
| SL06-C4 Consent Mode v2 | THIN | STRONG (carried) | S04 `measurement-tracking-plan` |
| SL06-C5 Conversion Lift | STRONG | STRONG | plus `GOOGLE-CONVERSION-LIFT` |
| SL06-C6 Skillshop | THIN | STRONG | certification register §1 (`GOOGLE-ADS-CERTIFICATIONS`) |
| SL07-C1 MRC viewability | GAP | STRONG | `programmatic-and-brand-safety` ref `viewability-ivt-and-attention.md` §1 |
| SL07-C2 IVT / TAG | GAP | STRONG | same ref §2 (`MRC-IVT-2020`, `TAG-CERTIFIED-AGAINST-FRAUD`) |
| SL07-C3 SPO, ads.txt, sellers.json, schain | GAP | STRONG | programmatic ref `buying-routes-and-supply-path.md` §3–4 |
| SL07-C4 brand safety / suitability | GAP | STRONG | programmatic ref `brand-safety-and-suitability.md` §1–5 (GARM discontinued, `WFA-GARM-DISCONTINUED-2024`); `08-influencer-marketing-strategy` Workflow 3 pointer. Successor shared floor `NOT_ASSESSED` |
| SL07-C5 attention | GAP | STRONG | viewability ref §3 (`IAB-MRC-ATTENTION-2025`) |
| SL07-C6 CTV | GAP | THIN | programmatic ref `ctv-dooh-and-audio.md` §1. `NOT_ASSESSED`: IAB Tech Lab Dec 2025 release returned HTTP 403 (record partial); East African CTV penetration unverified |
| SL07-C7 DOOH (MRC OOH) | GAP | STRONG | `ctv-dooh-and-audio.md` §2 (`MRC-OOH-STANDARDS`); `media-planning` ref `east-african-media-mix.md` outdoor split |
| SL07-C8 podcast measurement; radio | THIN | STRONG | `ctv-dooh-and-audio.md` §3; `strategy-video-content` ref `podcast-and-audio-series.md` Procedure 8 (`IAB-TECHLAB-PODCAST-2-2`); radio `AFROBAROMETER-UG-RADIO-2026` |
| SL08-C1 pre-testing | THIN | STRONG | creative ref `creative-effectiveness-and-pretesting.md` §3 (System1 labelled Vendor) |
| SL08-C2 ABCD | THIN | STRONG | ABCD ref §1 |
| SL08-C3 emotional vs rational | THIN | STRONG | creative ref §1 |
| SL08-C4 post-campaign ladder review | GAP | STRONG | `meta-reporting` ref `effectiveness-ladder-review.md` §1–2 |
| SL08-C5 pre-registration, SRM, guardrails | THIN | STRONG | `meta-testing-framework` ref `trustworthy-experiments-srm-power-holdouts.md` §1–5; `ad-testing-and-scaling` ref `test-rigour-srm-and-preregistration.md` |
| SL08-C6 distinctive assets early | THIN | STRONG | creative ref §2; brand ref `distinctive-asset-audit.md` §4 |
| SL08-C7 risk-based AI disclosure | THIN | STRONG | policy ref `ai-transparency-and-provenance.md` §3 |
| SL08-C8 creative brief | STRONG | STRONG | unchanged |
| SL09-C1 Meridian / Robyn | GAP | STRONG | `marketing-mix-modelling` Workflow 2–5; ref `meridian-and-robyn-choice.md` §1–3 |
| SL09-C2 calibration priors | GAP | STRONG | MMM ref `calibration-and-geo-experiments.md` §1–2, §5 |
| SL09-C3 geo power and market selection | THIN | STRONG | attribution ref `geo-power-and-incrementality-hierarchy.md` §3–4 (`META-GEOLIFT`) |
| SL09-C4 IAB incrementality hierarchy | THIN | STRONG | same ref §1–2; MMM ref `triangulation-and-decision-governance.md` §1, §3 (`IAB-INCREMENTAL-COMMERCE-MEDIA-2025`) |
| SL09-C5 privacy-safe signals | THIN/GAP | STRONG (carried) | S04 `measurement-tracking-plan` |
| SL09-C6 clean rooms | GAP | STRONG (note, low priority) | MMM triangulation ref §4 (`IAB-TECHLAB-CLEAN-ROOM`, partial) |
| SL09-C7 triangulation governance | GAP | STRONG | MMM triangulation ref §2; Workflow 8 |
| SL09-C8 ROI / LTV:CAC | STRONG | STRONG | unchanged |
| SL10-C1 trustworthy A/B tests | THIN | STRONG | testing ref §1–5; `playbook-post-click-strategy` References pointer |
| SL10-C2 Core Web Vitals thresholds | THIN | STRONG | `ad-to-site-journey-handoff` Quality Standards + ref `landing-page-brief-template.md` (`WEBDEV-CORE-WEB-VITALS`) |
| SL10-C3 testing tool with GA4 | THIN | STRONG | post-click ref `ecommerce-and-whatsapp-conversion-diagnosis.md` rule 6 (`GOOGLE-OPTIMIZE-SUNSET-2023`) |
| SL10-C4 server-side experiment measurement | GAP | STRONG (carried) | S04 `measurement-tracking-plan` |
| SL10-C5 post-click diagnosis | STRONG | STRONG | unchanged |
| SL11-C1 AI features eligibility | STRONG | STRONG | unchanged |
| SL11-C2 GEO myths | STRONG | STRONG | unchanged |
| SL11-C3 expert content | STRONG | STRONG | unchanged |
| SL11-C4 spam policy | THIN | STRONG | `seo-geo-optimisation` Decision Rules |
| SL11-C5 preview controls | THIN | STRONG | `seo-geo-optimisation` Decision Rules (`GOOGLE-AI-FEATURES-2025`, `GOOGLE-EXTENDED-2026`) |
| SL11-C6 AI-feature traffic reporting | THIN | STRONG | `meta-reporting` ref `effectiveness-ladder-review.md` §4 (separate product filter `NOT_ASSESSED`) |
| SL11-C7 technical health / CWV boundary | THIN | STRONG | `seo-geo-optimisation` boundary row; `12-website-content-plan` |
| SL12-C1 ASA/CMA | STRONG | STRONG | unchanged |
| SL12-C2 FTC | STRONG | STRONG | unchanged |
| SL12-C3 fake reviews | STRONG | STRONG | unchanged |
| SL12-C4 ICC influencer articles | THIN | STRONG | 08 ref `influencer-term-sheet-and-disclosure.md` ICC block (`ICC-CODE-2024-TEXT`) |
| SL12-C5 toggles | STRONG | STRONG | unchanged |
| SL12-C6 Partnership Ads | STRONG | STRONG | unchanged |
| SL12-C7 Kenya gambling ban | THIN | THIN (carried from T01) | `KE-BCLB-GAMBLING-ADS-2025` partial; directive text `NOT_ASSESSED` |
| SL13-C1 response SLAs | STRONG | STRONG | unchanged |
| SL13-C2 crisis escalation (CIPR) | STRONG | STRONG | `playbook-crisis-communications` ref `crisis-response-procedures.md` §8 (`CIPR-CRISIS-SOCIAL-2024`; stages are mitigate, prepare, ramp-up, manage, recover — the plan's "arm" was wrong) |
| SL13-C3 WhatsApp service window | THIN | STRONG | `platform-whatsapp` ref `whatsapp-platform-pricing-and-templates.md` §3–4; `playbook-chatbot-strategy` Decision Rules |
| SL13-C4 personal data in DMs | STRONG | STRONG | unchanged |
| SL14-C1 bulk-sender rules | GAP | STRONG | `07-email-marketing-strategy` ref `deliverability-and-lifecycle-holdouts.md` §1–2 (`GMAIL-SENDER-GUIDELINES`, `YAHOO-SENDER-REQUIREMENTS`) |
| SL14-C2 consent by jurisdiction | STRONG | STRONG | unchanged |
| SL14-C3 WhatsApp templates and opt-in | THIN | STRONG | WhatsApp ref §2, §6 |
| SL14-C4 first-party data under consent | THIN | STRONG (carried) | S04 |
| SL14-C5 lifecycle holdouts | GAP | STRONG | email ref §5; testing ref §6 |
| SL14-C6 lifecycle map | STRONG | STRONG | unchanged |
| SL15-C1 GA4→BigQuery | GAP | STRONG (carried) | S04 |
| SL15-C2 server-side GTM | THIN | STRONG (carried) | S04 |
| SL15-C3 CMP | THIN | STRONG (carried) | S04 (`GOOGLE-CMP-TCF-2026`) |
| SL15-C4 registration and transfers | THIN | STRONG (carried) | S04 (`UG-PDPO-OFFSHORE-2025`) |
| SL15-C5 clean rooms | GAP | STRONG (note) | MMM triangulation ref §4 |
| SL15-C6 KPI dictionary, UTM | STRONG | STRONG | unchanged |
| SL16-C1 martech audit | STRONG | STRONG | unchanged |
| SL16-C2 AI agents case | STRONG | STRONG | unchanged |
| SL16-C3 contracts and audit rights | THIN | STRONG | `playbook-agency-operations` ref `commercial-governance-and-contracts.md` §2–3 (CSFA and ANA template texts member-only: summaries used) |
| SL16-C4 server-side tag governance | THIN | STRONG (carried) | S04 |
| SL16-C5 automation specs | STRONG | STRONG | unchanged |
| SL17-C1 ISO/IEC 42001 | THIN | STRONG | policy ref §9; `ai-readiness-diagnostic` (clause mapping `NOT_ASSESSED`) |
| SL17-C2 NIST AI 600-1 | THIN | STRONG | policy ref §9 |
| SL17-C3 IAB AI disclosure v2 | GAP | STRONG | policy ref §3–5 (v2 PDF read; method verified) |
| SL17-C4 EU AI Act Art. 50 | THIN | STRONG | policy ref §7 (Commission FAQ; EUR-Lex text `NOT_ASSESSED`) |
| SL17-C5 platform AI labels | THIN | STRONG | policy ref §6 (ad-policy pages `NOT_ASSESSED`) |
| SL17-C6 ICC accountability | THIN | STRONG | policy ref §2 |
| SL17-C7 AI contract clauses | GAP | STRONG | `biz-dev-proposal` ref `pitch-conduct-and-ai-clauses.md` §3 |
| SL17-C8 anti-slop | STRONG | STRONG | unchanged |
| SL18-C1 remuneration models | THIN | STRONG | `biz-dev-pricing-menu` ref `remuneration-models-evidence.md` §2–4 |
| SL18-C2 contract terms | THIN | STRONG | governance ref §2–3 |
| SL18-C3 Pitch Positive | THIN | STRONG | proposal ref §1 |
| SL18-C4 principal media | GAP | STRONG | governance ref §3; `media-planning` References line (ISBA position `NOT_ASSESSED`) |
| SL18-C5 supply-chain transparency report | GAP | STRONG | programmatic ref `buying-routes-and-supply-path.md` §4; Outputs |
| SL18-C6 ladder outcome reporting | THIN | STRONG | `meta-reporting` ref §1–2, Workflow 6 |
| SL18-C7 biz-dev set | STRONG | STRONG | unchanged |
| SL19-C1–C2 certifications current | THIN | STRONG | certification register §1–2 (Meta validity `NOT_ASSESSED`) |
| SL19-C3 IPA qualifications | GAP | STRONG | certification register §4 |
| SL19-C4 CIM competencies | GAP | THIN | certification register §3. `NOT_ASSESSED`: CIM primary page not read (secondary only) |
| SL19-C5 curricula | STRONG | STRONG | unchanged |
| SL20-C1 Barcelona Principles 4.0, no AVEs | GAP | STRONG | `playbook-pr-publicity` ref `pr-evaluation.md` §1–5; AVE line removed from `publicity-kit-and-release-method.md` |
| SL20-C2 social-first crisis | STRONG | STRONG | unchanged |
| SL20-C3 reputation monitoring | STRONG | STRONG | unchanged |
| SL20-C4 deepfake protocol | THIN | STRONG | crisis ref `synthetic-media-and-deepfake-protocol.md` §1–6 (report-form routes `NOT_ASSESSED`) |
| SL20-C5 authentic mentions | STRONG | STRONG | unchanged |
| SL21-C1 retail-media measurement | GAP | STRONG | `social-commerce-strategy` ref `commerce-media-and-marketplaces.md` §1 (`IAB-MRC-RETAIL-MEDIA-2024`) |
| SL21-C2 commerce incrementality | GAP | STRONG | same ref §2 |
| SL21-C3 feed operations | THIN | STRONG | shopping ref §1–3 |
| SL21-C4 catalogue automation | STRONG | STRONG | unchanged |
| SL21-C5 Jumia / Jiji | GAP | STRONG | commerce ref §3 (fees `NOT_ASSESSED`; Rwanda marketplaces `NOT_ASSESSED`) |
| SL21-C6 click-to-WhatsApp window | THIN | STRONG | WhatsApp ref §3; `social-commerce-strategy` Decision Rules. **Benchmark correction:** the live pricing page (updated 28 Sep 2026) gives a free entry-point window of up to 7 days, opened by click-to-WhatsApp ads; "72 hours" is stale |
| SL21-C7 mobile-money checkout | STRONG | STRONG | unchanged |

## East Africa rows

| Topic | Was | Now | Closed by |
|---|---|---|---|
| Market size | THIN | STRONG | `media-planning` ref `east-african-media-mix.md` §2 (`DATAREPORTAL-TZ-2026`, `DATAREPORTAL-RW-2026`) |
| Mobile-first | STRONG | STRONG | same §2 (`GSMA-SSA-MOBILE-ECONOMY`, 2024 edition; newer edition `NOT_ASSESSED`, HTTP 403) |
| Mobile money | STRONG | STRONG (Secondary label) | commerce ref §4 (`GSMA-MOBILE-MONEY-2025`) |
| M-Pesa | THIN | STRONG | commerce ref §4 (`SAFARICOM-FY2026-MPESA`, verified) |
| Payments law | GAP | THIN | commerce ref §5 screening note; Act text `NOT_ASSESSED` (`UG-NPS-ACT-2020`, partial) |
| Radio | THIN | STRONG | media-mix §2 (`AFROBAROMETER-UG-RADIO-2026`) |
| WhatsApp economics | THIN | STRONG | WhatsApp ref §5 (`WHATSAPP-RATE-CARD-EA`: UG, KE, TZ, RW in "Rest of Africa"; 1 Oct 2026 change recorded) |
| WhatsApp opt-in | STRONG | STRONG | plus `WHATSAPP-OPT-IN-2026` |
| Uganda DPPA | STRONG | STRONG | unchanged |
| Kenya DPA | STRONG | STRONG | unchanged |
| Tanzania PDPA | THIN | THIN (carried from T01) | registration duty recorded; statute text `NOT_ASSESSED` |
| Rwanda | THIN | STRONG (carried from T01) | `RW-DPP-REGISTRATION-2026` |
| Uganda advertising standards | THIN | THIN | UCC Advertising Standard text `NOT_ASSESSED` (currentness wave 2) |
| Uganda online publishers | THIN | THIN | 08 term-sheet row + gate row (`UG-UCC-ONLINE-PUBLISHERS`); influencer coverage and enforcement `NOT_ASSESSED` |
| Kenya advertising code | THIN | STRONG (carried from T01) | `KE-ASBK-CODE-2003` (later edition `NOT_ASSESSED`) |
| Kenya gambling | THIN | THIN (carried from T01) | directive text `NOT_ASSESSED` |
| Kenya bulk SMS | THIN | STRONG (carried from T01, scope corrected) | `KE-CA-POLITICAL-BULK-SMS-2017` |
| Uganda cyber law | DEFECT | STRONG (carried from T01) | void Amendment Act no longer cited as law |
| Facebook in Uganda | DEFECT | STRONG (carried from T01) | "status unstable; verify at campaign date" |
| Internet shutdowns | GAP | STRONG (carried from T01) | crisis ref `internet-shutdown-contingency.md` |
| Uganda taxes | THIN | THIN | release-gate row "Consumer data cost (Uganda)" (`UG-DATA-EXCISE`, partial: PwC summary; URA and Act text `NOT_ASSESSED`) |
| Tanzania online content | THIN | THIN (carried from T01) | 2021 amendment content `NOT_ASSESSED` |
| Marketplaces and streaming | GAP | STRONG | commerce ref §3 (Boomplay figures stay UNVERIFIED) |

Counts: 16 STRONG, 7 THIN (all bound to a named `NOT_ASSESSED` evidence gap), 0 GAP, 0 DEFECT.

## Corrections to the plan's benchmark text (for S13)

1. SL21-C6 / "WhatsApp economics": "72-hour click-to-WhatsApp window" is stale; the live page says up to 7 days, ads only (`WHATSAPP-PRICING-2025`).
2. SL13-C2: the CIPR guide's stages are mitigate, prepare, ramp-up, manage, recover ("arm" is wrong).
3. S13 (clean rooms): upgrade the secondary MarTech source to the IAB Tech Lab standards page (`IAB-TECHLAB-CLEAN-ROOM`).
4. E28 scope already corrected in T01 (political bulk SMS only).

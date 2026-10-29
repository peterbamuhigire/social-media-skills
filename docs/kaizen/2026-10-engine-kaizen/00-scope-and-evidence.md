# Social-media engine — scope and practitioner evidence

**As of:** 2026-10-29. **Starting revision:** `750982a` on a clean `main` checkout. The baseline evidence was collected before functional implementation. The branch `kaizen/2026-10` is used for this cycle. No paid model call, account access, posting, spend, or publication occurred. No uncommitted policy files were present at preflight.

## Scope and source discipline

The requested work is a four-week launch calendar with first-week channel-native copy, a media plan with transparent budget/reach/frequency arithmetic, and a fictional paid-service outage response (Social Media Skills Engine Kaizen prompt 11, October 2026). The engine's router assigns calendar and measures to `pipeline/11-content-calendar` and `meta-analytics-ops/measurement-tracking-plan`; integrated strategy to `pipeline/06-digital-marketing-strategy`; LinkedIn, Instagram and TikTok channel work to their `platforms/platform-*` skills; paid-media budget and plan to `advertising/advertising-strategy-and-budget` and `advertising/media-planning`; incident sequence to `playbooks/playbook-crisis-communications`. This route fits the task (inference from the router and the requested deliverables).

The anti-slop ship gate and direct-marketing ethics filter are required for applicable copy. I applied the former to all copy below. Because this is owned-product content and no third-party endorsement or paid creator is assumed, influencer-specific disclosure is not triggered in the fixture; any later creator relationship requires a new review.

## Practitioner task 1 — four-week launch calendar

**Synthetic fixture:** “Kite Ledger” is an invented Ugandan SaaS product for small organisations to organise invoice records. It has no real customers, performance data, integrations, certifications, testimonials, pricing or live account. The objective is to explain the workflow and invite an opt-in product walkthrough. This fiction is not evidence about a real product. No audience size, conversion rate or outcome is assumed.

| Week | LinkedIn | Instagram | TikTok | Objective / measure |
|---|---|---|---|---|
| 1 — explain the problem | Text post: show a fictional manual invoice handoff; CTA: request a walkthrough. | 4-panel carousel: “capture → check → organise → review”; caption CTA to profile link. | Short, presenter-led screen-free sketch of a record handoff; caption CTA to learn more. | Establish baseline reach, saves, qualified profile/link visits and opt-in walkthrough requests; record denominator and source. |
| 2 — show the process | Document post outline with four workflow steps; no outcome claim. | Carousel with one step per card; add alt text to final production asset. | Voiceover walkthrough using synthetic sample rows labelled “demo data”. | Measure completion/retention where native analytics expose it, saves and qualified visits; do not compare unlike platform counters. |
| 3 — answer objections | Post with three questions: who owns records, how to correct a mistake, how to request a demo. | Story question prompt; answer only questions the product team can verify. | “What happens if a record is wrong?” scripted response: show a correction workflow only after product owner confirms it exists; otherwise use a transparent “we are validating this step”. | Measure substantive questions, response time and qualified visits; classify unresolved questions for product review. |
| 4 — invite action | Recap post with demo CTA and clearly stated current product scope. | Carousel recap and profile-link CTA. | Short “what we learned from building the workflow” script; no customer/result claim. | Measure qualified walkthrough requests, opt-in rate against a recorded landing-page denominator, and unresolved claims. |

### Week 1 ready-to-review copy

**LinkedIn — text post**

> An invoice record can pass through several hands before anyone is sure what needs attention. In our demo, we are showing a simple way to capture a record, check it and keep it organised for review.
>
> Kite Ledger is a fictional product concept for this exercise. The walkthrough uses sample data and does not demonstrate a live customer result.
>
> Want to see the proposed workflow? Request a walkthrough through the link on our page.

**Instagram — four-card carousel script and caption**

1. **A record arrives. What happens next?**
2. **Capture** the invoice details in one place.
3. **Check** the fields before the record is filed.
4. **Review** the organised record when it is needed.

Caption: “A useful workflow should make the next step clear. This fictional Kite Ledger demo shows a simple invoice-record flow using sample data. It is a concept exercise, not a customer result or a claim about a live product. Would you like to review the proposed flow? Request a walkthrough from the profile link.”

**TikTok — short spoken script**

> “Here is a small workflow question: when an invoice record arrives, who checks that it is complete before it gets filed? In this fictional Kite Ledger demo, we show three steps: capture, check, organise. The rows are sample data, not customer records. If you want to review the proposed workflow, use the link on our profile.”

**Production and release checks:** Do not publish this copy as-is: the brand, product existence, landing page, offer, profile, speaker rights and account status are fictional/unverified. If adapted to a real product, replace or remove every synthetic claim and route it through product-owner verification, current platform checks, disclosure review, accessibility review, and the engine's legal-market release gate. TikTok states commercial content requires its disclosure setting, including content promoting one's own business; applicability must be checked on the live post and current market-specific policy before publication ([TikTok Help Center, accessed 2026-10-29](https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/promoting-a-brand-product-or-service?lang=en); search result was accessible, direct open redirected to an inaccessible FAQ—policy content beyond the surfaced result is not independently re-opened).

## Practitioner task 2 — synthetic media plan and arithmetic check

This is a planning exercise, not a rate card or forecast. Every budget and CPM below is an explicit synthetic assumption. No platform inventory, ad-account eligibility, audience reach or actual CPM was checked. Gross impressions and modeled reach are arithmetic outputs only; reach is not deduplicated across platforms. All numeric outputs derive from `tasks/media-plan-check.py` and are reproduced in `tasks/media-plan-check.json`.

| Channel | Assumed spend (UGX) | Assumed CPM (UGX) | Impressions = spend ÷ CPM × 1,000 | Assumed frequency | Implied gross reach = impressions ÷ frequency |
|---|---:|---:|---:|---:|---:|
| LinkedIn | 4,000,000 | 25,000 | 160,000 | 2.5 | 64,000 |
| Instagram / Meta | 5,000,000 | 10,000 | 500,000 | 3 | 166,666.67 |
| TikTok | 3,000,000 | 8,000 | 375,000 | 3 | 125,000 |
| **Total** | **12,000,000** | — | **1,035,000** | — | **355,666.67 gross platform-reach sum** |

Reproducible arithmetic: `tasks/media-plan-check.py`; output: `tasks/media-plan-check.json`. Assumptions are deliberately labeled synthetic in the input script. Per-platform frequency and CPM are user-supplied assumptions inside this fixture; they are not claimed as observed or typical market values. Deduplicated reach is **NOT_ASSESSED**; adding platform reach rows does not estimate unique people.

**Platform-format/specification check:**

- LinkedIn: the official Single Image Ads page gives placement-specific file, aspect-ratio and text guidance; applicability to a live account, current campaign objective and Uganda inventory still needs in-account validation ([LinkedIn Single Image Ads specs](https://business.linkedin.com/advertise/ads/sponsored-content/single-image-ads-specs?src=re-pmktg), accessed 2026-10-29). Do not transfer its single-image specifications to other formats.
- Instagram/Meta: official Meta advertising standards page returned HTTP 429 in this research session; the Meta Business Help Centre spec page redirected to a login/access block. **Current exact creative specifications and ad-policy interpretation: NOT_ASSESSED.** Do not use third-party spec tables as authority. This is also why the overdue `META-AD-STANDARDS` register entry remains an open currentness defect.
- TikTok: the official current result confirms commercial disclosure setting requirements for brand/product/service promotion ([TikTok help result](https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/promoting-a-brand-product-or-service?lang=en), accessed 2026-10-29); its exact organic-video format limits and current Uganda-specific ad inventory specs were not verified. **Paid-placement specifications: NOT_ASSESSED.**

For launch approval, obtain a client-approved budget, current account-specific forecast, placement and eligibility preview, frequency controls, actual conversion definitions, landing page, consent basis and deduplication method. No spend or account change is authorised by this fixture.

## Practitioner task 3 — paid-service outage response

**Fictional incident:** the invented Kite Ledger demo environment cannot display its sample invoice workspace. The exercise does not define a cause or recovery time. No live service, real customer, production system or personal data is affected. This is a scenario for response practice, not an actual incident.

1. **Internal verify:** incident lead records first known report, affected service component, evidence, who can confirm scope, update owner and next check time. Privacy/security lead is paged if evidence suggests personal data exposure; retain the separate statutory assessment rather than implying an outage automatically is or is not a breach.
2. **Scenario-only holding statement:** “We are investigating an interruption to access to the fictional Kite Ledger demo workspace. We have not confirmed the cause or a recovery time. No live customer service is affected in this exercise. We will add an update after the exercise reviewer verifies new information.” This is complete synthetic copy, not a statement for public use.
3. **Customer support response:** acknowledge the interruption, ask only for the minimum diagnostic details through an approved support route, do not request passwords/payment credentials in public, and avoid promising compensation or data recovery without an approved policy and case-specific facts.
4. **Update:** distinguish observed impact from investigation hypotheses. Correct any earlier statement visibly, preserve the timestamp and owner, and publish a new estimate only when the incident lead has evidence and confidence to support it.
5. **Scenario-only resolution example:** “Access to the fictional demo workspace is available again in this exercise. The reviewer confirmed the sample invoice screen opens. The cause has not been established, and this scenario involved no production service or customer data.” For a real incident, use this form only after the service owner confirms recovery and the validation performed; do not claim “all clear” or “no data affected” absent the relevant investigation.
6. **After-action:** reconcile incident timeline and support cases, document evidence and decision owners, assess notice obligations with qualified local privacy counsel if personal-data exposure may be involved, and publish follow-up only when scope and corrective actions are verified.

**Claim, tone and disclosure review:** no invented cause, customer count, restoration time, breach conclusion, refund, or service-performance claim. Plain, calm, empathetic and accountable. No influencer or paid-promotion context is assumed. If a creator or paid media amplifies the response, add the applicable commercial disclosures and platform policy check before activation.

## Defects observed in the three tasks

- **Major, currentness/release blocker:** platform-policy and local legal register entries used by the task were overdue on the run date; checked entries and official-source access limits are listed in `03-currentness.md`. Existing freshness validator exits non-zero with 23 overdue records.
- **Major, evidence:** campaign performance and platform reach cannot be claimed from copy or assumed CPMs; the fictional fixture avoids those claims, and no live account or campaign export is available.
- **Minor, output readiness:** exact Meta and TikTok paid placement specifications were not independently verified in this session; no format limits are carried into the media plan.
- **Minor, product handoff:** multiple publish-time dependencies remain fictional (brand, product proof, landing page, support route, account, rights and owner). They are explicit release blockers, not blank deliverable stubs.

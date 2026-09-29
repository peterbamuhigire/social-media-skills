---
name: 08-influencer-marketing-strategy
description: Use when a brand wants creators, influencers or its own customers to promote it, including vetting for fake followers, AI discovery tools, virtual influencers and UGC; produces the influencer strategy, selection criteria, term sheet and activation plan; not for a creator building their own income (use `strategy-creator-monetisation`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Influencer Marketing Strategy Generator

Produces a complete influencer marketing strategy whose tiers, engagement screens and outreach norms reflect Uganda/East African market realities, not global averages. It covers strategy and execution guidance only; formal influencer agreements go to a lawyer.

<!-- dual-compat-start -->
## Use When

- A brand wants local content creators or influencers to promote a product and needs who to pick, tiers, fit criteria, outreach, briefs, usage rights and measures.
- Creators need vetting (are their follower numbers real?), pricing, deal terms and a term sheet with ad disclosure before any offer is made.
- The client wants AI tools to find influencers, screen out fake followers and bot engagement, or weigh a human creator against a virtual CGI influencer.
- The client wants customers posting photos, videos and reviews of its products (UGC) that the brand can reshare: a branded hashtag, testimonial collection, a permissions log and reposting rules.

## Do Not Use When

- `strategy-creator-monetisation` for a creator's own rate card, revenue streams and brand partnerships.
- `09-campaign-strategy` for the wider campaign that a creator activation sits inside.
- `strategy-ewom-reviews` for reviews, referrals and word-of-mouth programmes.
- Stop before contacting, contracting or paying any creator without client authority and a signed disclosure and rights agreement.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, industry and sub-sector, country/city | Client brief or `01-client-brief` | Yes | Default the location to Kampala, Uganda; return the intake questions for the rest. |
| Target audience (age range, gender split, location, key interests) | `03-audience-personas` or client | Yes | Describe a provisional audience and score creator audience fit `not assessed`. |
| Campaign objective (awareness, product trial, event, sales or community growth) | Client lead | Yes | Stop tier and fee decisions; ask for the primary objective. |
| Budget per month or per campaign, in UGX by default, split into barter value and cash fees | Client | Yes | Plan nano and barter options only and draft fee ranges without figures. |
| Platforms in scope (Instagram, TikTok, YouTube, Facebook, X/Twitter, WhatsApp) | Client or channel plan | Yes | Default to where the persona spends time and label it provisional. |
| Creator long-list with dated audience-insight screenshots | Research, rosters, inbound pitches | For selection | Build the list by manual discovery; hold any shortlist until insights arrive. |

## Workflow

1. Ask the intake questions in [influencer-strategy-document-sections](references/influencer-strategy-document-sections.md) § Intake questions; route to `09-campaign-strategy` when the activation sits inside a wider campaign.
2. Define the tiers with EA characteristics, including WhatsApp community admins, and label engagement figures as screening heuristics.
3. Find and vet creators: audience match and location, the manual engagement-rate formula, content quality, platform fit and brand safety, then the due-diligence scorecard in [creator-due-diligence-and-pricing](references/creator-due-diligence-and-pricing.md); set the brand-suitability floor and tiers with [programmatic-and-brand-safety](../../advertising/programmatic-and-brand-safety/SKILL.md); stop on any red line.
4. Price each shortlisted creator from distribution fee plus talent fee, with usage, exclusivity and season priced explicitly.
5. Plan outreach by tier, then complete the term sheet, creator brief and disclosure checks in [influencer-term-sheet-and-disclosure](references/influencer-term-sheet-and-disclosure.md) before any offer.
6. Set usage-rights terms, lawyer triggers, performance metrics and at least two attribution methods before the campaign starts.
7. Check the strategy against the quality standards; correct failing sections and rerun the check.
8. Run the anti-slop and legal release gates and hand the strategy to the client lead; withhold release while a disclosure, rights or evidence defect remains.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Influencer strategy document (seven sections plus creator-economy principles) | Client lead | All seven sections present and client-specific; engagement figures labelled as heuristics. |
| Vetted creator shortlist with scorecards and fee build-ups | Client lead; campaign owner | Each creator has a dated scorecard, no red line breached, and a fee split into its component lines. |
| Term sheet and creator brief per micro or macro creator | Client's lawyer; creator | Term sheet complete before lawyer drafting; brief fill-in-the-blanks ready with disclosure and usage terms. |
| Measurement plan | Client lead | Targets set before launch; UTM links and unique discount codes assigned per creator. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Creator vetting record | Table: creator, dated insights, engagement calculation, red-flag checks | Every figure is dated and calculated from the creator's own posts, not self-reported. |
| Disclosure and jurisdiction register | Table citing register IDs (AD-09, AD-10, KE-01, UG-01, TZ-01) | Unverified jurisdictions stay `NOT_ASSESSED`; no disclosure claim passes without a cited row. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Contacting, contracting, gifting product to or paying any creator needs that authority plus a signed disclosure and rights agreement.

## Degraded Mode

Without dated creator audience insights or a confirmed budget, return the narrowest qualified result and mark the affected checks `not assessed`. Tier definitions, selection criteria, outreach and brief templates and a measurement plan can still be delivered.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A creator's engagement falls below the tier's red-flag threshold (nano below 3%, micro below 2%, macro below 0.5%) or looks bought | Walk away; cross-check with HypeAuditor or modash.io only if budget allows. | Paying for purchased audiences. |
| The creator's audience is mainly outside the campaign geography | Do not commit; ask for audience location data first. | Spend reaching people who cannot buy. |
| Creators are found or vetted with AI tools, fraud is suspected, or a virtual influencer is proposed | Apply the tool tiers, fraud thresholds and Parasocial Interaction Scale in [ai-assisted-influencer-discovery-and-virtual-creators](references/ai-assisted-influencer-discovery-and-virtual-creators.md). | Paying for purchased audiences or an uncanny-valley virtual character. |
| The programme uses customer-created content | Run the audit, collection tiers, permissions log and curation and republishing workflow in [ugc-creator-and-customer-content](references/ugc-creator-and-customer-content.md). | Republishing customer content without documented consent. |
| A macro deal with cash fees above UGX 1 million, paid-ad usage rights, a multi-month retainer or an exclusivity clause | Complete the term sheet and involve a lawyer before signing. | Unenforceable or disputed rights and fees. |
| Content goes live | Require an up-front "Ad" or "Paid partnership" label plus the platform's branded-content tool; keep Rwanda, Kenya BCLB and UCC items as `NOT_ASSESSED` checks. | Undisclosed advertising and regulator or platform action. |
| Content is not posted within 48 hours of the agreed date | Apply the brief's catch-up clause: reclaim product or withhold payment. | Paying for undelivered content. |
| The activation belongs to a wider campaign | Route to `09-campaign-strategy` and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Quality Standards

- Tier definitions label EA engagement figures as unsourced screening heuristics, not benchmarks, and WhatsApp group admins are explicitly identified as a nano-influencer category relevant to the EA context.
- Selection uses the creator due-diligence scorecard (bought audience, undisclosed past ads, hateful content and safety risk are red lines); the 3R check is not attributed to Hennessy.
- Pricing is built from distribution fee + talent fee, with usage, exclusivity and season priced explicitly; the term sheet is completed before lawyer drafting.
- Disclosure guidance cites the register (AD-09, AD-10) and keeps Uganda/Kenya items as checks.
- Audience match criteria include a clear instruction to verify audience location before committing, and the engagement rate calculation method is specified and can be performed manually without paid tools.
- The outreach message template sounds personal and human, not corporate, and the campaign brief template is complete and fill-in-the-blanks ready for immediate use.
- Usage rights guidance explicitly notes it is not legal advice and specifies when to involve a lawyer.
- Performance metrics include at least two trackable attribution methods (UTM links and discount codes), and the red flags section addresses bought followers with a concrete detection method.

Further checks (British English, UGX) are in [influencer-strategy-document-sections](references/influencer-strategy-document-sections.md) § Quality checklist.

## Anti-Patterns

- Choosing a creator on follower count alone. Fix: screen in Hennessy's order and score authentic fit and the five influence mechanisms (Falls, 2021).
- Sending a generic campaign brief as the first contact. Fix: open with a short, personal message that names a specific post; use WhatsApp or Instagram DM.
- Chasing a silent creator repeatedly. Fix: send one brief follow-up after 5 days, then move on; never more than two contact attempts.
- Boosting creator content as a paid ad under a post-only deal. Fix: negotiate and pay for paid-advertising usage rights separately.
- Buying one sponsored post and expecting endorsement. Fix: where budget allows, plan 3–4 touchpoints across 4–6 weeks.
- Promising that micro-creators will outperform larger ones. Fix: test with tracked codes and links and let the client's data decide.
- Contacting, gifting or paying creators during planning. Fix: hand over the plan; outreach and payment need separate authority.

## References

- [Influencer strategy document method](references/influencer-strategy-document-sections.md): read when asking the intake questions or writing the tier, identification, outreach, brief, usage-rights, metrics and red-flag sections and the creator-economy principles.
- [Creator due diligence, typology and pricing](references/creator-due-diligence-and-pricing.md): read when shortlisting, vetting or budgeting creators.
- [Influencer term sheet, brief and disclosure register](references/influencer-term-sheet-and-disclosure.md): read before any offer, brief, contract hand-off or go-live.
- [ai-assisted-influencer-discovery-and-virtual-creators](references/ai-assisted-influencer-discovery-and-virtual-creators.md): read when using AI discovery tools, screening fraudulent engagement, or weighing a human against a virtual influencer.
- [AI transparency and provenance](../../policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md): read when a virtual or AI-generated influencer is used; label it in every appearance (§3).
- [ugc-creator-and-customer-content](references/ugc-creator-and-customer-content.md): read when building a customer UGC programme, permissions log or curation and republishing workflow.
- [`09-campaign-strategy`](../09-campaign-strategy/SKILL.md): read when the creator activation sits inside a wider campaign.
- [Creator monetisation](../../strategy/strategy-creator-monetisation/SKILL.md): read when the work is the creator-side counterpart (rate card, revenue streams).
- [Legal, privacy and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read before go-live and whenever disclosure or rights claims are made.
- [Creative review gate](../../../docs/quality-gates/creative-review-gate.md): read when approving creator drafts.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

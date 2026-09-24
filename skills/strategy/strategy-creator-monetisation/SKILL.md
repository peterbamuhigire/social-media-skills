---
name: strategy-creator-monetisation
description: Use when the main deliverable concerns creator revenue options, eligibility, rate cards, partnerships, and owned products; use premium-social-selling when that neighbouring workflow owns the primary decision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Creator Monetisation Strategy — East Africa

<!-- dual-compat-start -->
## Use When

- Use this skill for creator revenue options, eligibility, rate cards, partnerships, and owned products.
- Use it when the requested deliverable needs the domain decisions and acceptance checks below.

## Do Not Use When

- Use `premium-social-selling` when that neighbouring workflow owns the main decision or deliverable.
- Do not proceed when required evidence, approval, or safety review is absent; return the missing-input path instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, market, and intended decision | Client or approved brief | yes | Ask for it or state a narrow working assumption |
| Existing channel, content, commercial, or performance evidence relevant to creator revenue options, eligibility, rate cards, partnerships, and owned products | Client systems, supplied files, or verified research | conditional | Mark the check unassessed and avoid performance claims |
| Approval, policy, budget, access, or risk constraints | Accountable client owner | conditional | Stop before publishing, spending, collecting data, or making regulated claims |

## Workflow

1. Confirm the decision, consumer, market, and evidence boundary; distinguish the request from `premium-social-selling`.
2. Inspect supplied artefacts and record missing or unverified inputs before drafting.
3. Apply the domain framework in this skill and use the decision rule below at each branch.
4. Stop for approval before publishing, spending, contacting people, changing live systems, or making regulated claims.
5. Review the deliverable against the quality and anti-slop gates; if a check fails, correct it and rerun the affected check.
6. Hand off the artefacts, assumptions, evidence, and unresolved risks to the named consumer.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Creator revenue options, eligibility, rate cards, partnerships, and owned products deliverable | Client decision-maker or delivery team | Names the chosen route, owners, sequence, assumptions, and measurable acceptance checks |
| Decision and risk record | Reviewer or implementer | Links each recommendation to supplied evidence or labels it as an assumption |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Input and assumption register | Table or annotated brief | Missing and unverified items are visible, not treated as passed |
| Release check | Completed quality checklist | All blocking findings are fixed or the deliverable is explicitly withheld |

## Capability and Permission Boundaries

Read and search are the minimum capabilities. Analysis and planning remain read-only. Edit only files placed in scope; publishing, outreach, spend, personal-data processing, production changes, and certification claims require explicit authority and evidence of success.

## Degraded Mode

If files, tools, network, current evidence, rendering, or authorised access are unavailable, return the narrowest useful qualified deliverable. Mark each unavailable check `not assessed`; never convert it into a pass or invent market facts.

## Decision Rules

| Choice condition | Action | Failure or risk avoided |
|---|---|---|
| Audience proof and platform eligibility can be verified | Rank feasible revenue streams and mark platform facts for current verification | Projected income relies on unavailable or stale monetisation programmes |
| Evidence is contradictory or materially incomplete | Pause the affected recommendation and request the accountable source | Confident advice built on an unresolved premise |
| Authority is limited to analysis or planning | Deliver a read-only plan and approval checklist | Unauthorised publication, spend, outreach, or data use |

## Quality Standards

- Keep Uganda/East Africa, British English, EAT, UGX, and WhatsApp-first assumptions explicit where they apply.
- Tie recommendations to observed evidence, a named assumption, or a verification action.
- Give the next operator enough detail to execute without guessing ownership, sequence, or acceptance.
- Apply `ai-marketing/anti-ai-slop` during drafting and block release on an F from `ai-marketing/ai-slop-audit`.

## Anti-Patterns

- Inventing a client metric, audience fact, price, partner, or platform rule. Fix: verify it or label the decision provisional.
- Treating a missing tool, source, render, or approval as a passed check. Fix: mark it `not assessed` and narrow the output.
- Producing channel tactics before defining the decision and consumer. Fix: state the required outcome and handoff first.
- Copying a global template without adapting Uganda/East Africa access, language, payment, or trust conditions. Fix: record which local assumptions apply.
- Recommending publication, outreach, spend, data collection, or a regulated claim without authority. Fix: stop at an approval-ready draft.
- Reporting activity as success without an acceptance condition. Fix: name the observable result and evidence source.

## References

- [AGENTS.md](../../../AGENTS.md)
- [Brand partnership guide (creator side)](../strategy-personal-brand/references/brand-partnership-guide.md) — read when building the press kit, one-sheet and partnership page.
- [Creator due diligence and pricing (brand side)](../../pipeline/08-influencer-marketing-strategy/references/creator-due-diligence-and-pricing.md) — how buyers vet and price creators.
<!-- dual-compat-end -->

*Based on Dallas, M. (2022) Social Media Marketing Algorithms. Cross-reference: `platform-youtube`, `platform-tiktok`, `08-influencer-marketing-strategy`.*

---


## Required Input

Before generating any deliverable, ask the client for:

1. **Creator name** — the individual's name or creator brand name
2. **Platforms and following** — list each active platform and current follower/subscriber count
3. **Content niche** — be specific (e.g. "personal finance for Ugandan salaried workers", not "lifestyle")
4. **Engagement rate per platform** — average likes, comments, shares as a percentage of followers
5. **Primary audience demographics** — age range, city/region, income level or purchasing behaviour
6. **Monetisation goal** — primary income / supplemental income / building toward full-time
7. **Payment capability** — local bank account / MTN MoMo or Airtel Money / Payoneer / USD card

---

## Section 1: EA Creator Monetisation Landscape

Frame the strategy with honest context for the Ugandan and East African market:

- **Platform monetisation programmes** (for example YouTube's Partner Programme and whatever creator-reward programme TikTok currently runs) have eligibility thresholds, country lists and payout rules that change often, and usually pay in USD. Receiving this income requires a USD bank account, Payoneer, or Wise account — assess the client's payment capability first.
- **Brand partnerships** are the most accessible and highest-value monetisation route for most EA creators. A nano-creator with a tightly defined audience can secure brand deals before reaching any platform monetisation threshold.
- **Affiliate marketing** works for creators whose audience actively purchases online. Confirm audience purchasing behaviour before recommending it.
- **Digital products** offer the highest margin — created once, sold repeatedly — but require genuine audience trust and a frictionless local payment mechanism (Mobile Money).
- Combine streams: recommend a prioritised mix based on the creator's current audience size, niche, engagement, and payment infrastructure.

Assess each of the five streams below against the client's profile and provide a recommendation for each: **Priority / Secondary / Not Yet / Not Applicable**.

### Income and job-claim safety

Do not repeat guaranteed daily earnings, effortless work-from-home claims, pay-to-access vacancy claims or platform eligibility statements without evidence. For every material claim, record the source, access date, market, role level, contract or payment condition, and whether the claim is an estimate or a verified programme rule. Separate entry-level tasks from professional strategy, analytics, content production, community operations and safety work. A credible recommendation should show the skills, portfolio evidence, client acquisition route and payment risks required; it should never promise income.

---

## Section 2: YouTube Partner Programme (YPP)

*See `platform-youtube` for full channel optimisation guidance.*

### Eligibility check (run before setting YPP as a goal)

YouTube's Partner Programme thresholds, tiers, country availability and payout routes change. Do not state them from memory or from this skill. Before advising:
1. Open YouTube's official Partner Programme help pages and record the current thresholds for each tier, the list of available countries, and the date checked.
2. Confirm the creator's country is listed; if Uganda (or the named market) is not listed, say so and drop YPP as a goal.
3. Confirm the payout route (AdSense payment method, bank or intermediary) the creator can actually use.
4. Record all three in the decision register as a dated platform claim; if the source cannot be opened, mark the check `not assessed`.

### Revenue expectations

Ad revenue per thousand views varies widely by audience country, niche and season, and no verified figure for Ugandan audiences is held in this engine. Estimate only from the creator's own YouTube Analytics once monetised, and treat ad revenue as supplemental until the creator's own data shows otherwise. Prioritise sponsorships and owned products.

### Path to 1,000 Subscribers: Month-by-Month Plan

Generate a personalised timeline using the creator's niche. Use this model as the default:

| Period | Actions | Target |
|---|---|---|
| Month 1–2 | Define niche precisely. Publish 8 videos (2/week). Optimise titles, thumbnails, and descriptions for search (SEO). | 0 → 100 subscribers |
| Month 3–4 | Analyse watch time; improve retention by shortening intros. Publish 8 more videos. Share on WhatsApp communities and Facebook Groups. | 100 → 300 subscribers |
| Month 5–6 | Algorithm begins recommending well-retained videos. Maintain 2 videos/week. Create one keyword-targeted video per month targeting a high-search-volume question in the niche. | 300 → 600 subscribers |
| Month 7–8 | Compound growth from earlier uploads. Begin outreach to nano-sponsors. Apply for YPP when thresholds are met. | 600 → 1,000 subscribers |

**Niche growth note:** Education, how-to, and personal finance content grows faster in EA than entertainment. Adjust the timeline upward (12–18 months) for entertainment, music, or vlog formats.

---

## Section 3: TikTok Creator Monetisation

*See `platform-tiktok` for full platform guidance.*

### TikTok platform monetisation (check before advising)

TikTok's creator programmes have been replaced and renamed over time (check whether the programme named in older guides, such as the original Creator Fund, still exists), and eligibility, follower thresholds, country availability, LIVE gifting rules, paid-content features and withdrawal methods differ by market and change often. Before recommending any TikTok platform income:
1. Check TikTok's official creator and LIVE help pages for the creator's country; record the programme name, thresholds and date checked.
2. If the programme is not available in the creator's country, do not recommend it.
3. Treat LIVE gifting as suitable only for creators who already have a loyal, returning audience.
4. Mark any unverifiable feature `not assessed`.

### EA TikTok Monetisation Reality

Treat brand deals, not platform programmes, as the working hypothesis for East African TikTok creators, and test it against the creator's own enquiries and earnings. Introduce brand partnerships once the creator has a clearly defined, engaged audience; set the engagement and audience thresholds from the creator's own analytics and the buyer's brief, not from a fixed benchmark (engine heuristic, unsourced).

---

## Section 4: Affiliate Marketing

Affiliate marketing pays a commission for every sale or lead generated through the creator's unique link. Suitable for creators with an audience that purchases products or services online.

### Candidate affiliate programmes (verify terms before use)

Commission rates, country eligibility and payout methods change frequently, so this skill holds no rates. Shortlist candidates by category, then open each programme's current terms and record rate, cookie window, country eligibility, payout method and date checked:

| Category | Candidate programmes to check | What to confirm |
|---|---|---|
| East African e-commerce | Regional marketplaces' affiliate programmes (for example Jumia, Kilimall) | Country eligibility, commission by category, Mobile Money or bank payout |
| Global e-commerce | Large marketplace associate programmes | Whether the creator's country can join and be paid |
| Travel | Accommodation and booking-platform partner programmes | Commission basis and payout currency |
| Online learning | Course-platform affiliate programmes | Rates, cookie length, payout method |
| Local brands | Direct agreements with a named business | Negotiated rate in writing, tracking method, Mobile Money payout, tax treatment (route to `chwezi-accounting-doctrine`) |

### Eligibility and Fit Criteria

- Readiness (engine heuristic, not a platform rule): a clearly defined audience that already asks where to buy what the creator shows; follower count alone is not a readiness signal.
- Product-audience fit: the product must be genuinely relevant to the audience's life and purchasing behaviour. Do not recommend a creator promote Jumia if their audience does not shop online.
- Niche alignment: recommend one or two programmes maximum — do not scatter affiliate links across unrelated categories.

### Affiliate Disclosure (best practice; check local law)

Disclose affiliate relationships in every post or video that carries an affiliate link, up front and in plain words, for example: *"This post contains affiliate links. I may earn a commission if you buy through my link, at no extra cost to you."* The Uganda Data Protection and Privacy Act 2019 governs personal data, not advertising disclosure, and no influencer- or affiliate-specific disclosure law was found for Uganda or Kenya as of 2026-09-23 (Kaizen register AD-10); apply the US FTC and UK ASA/CMA standard as best practice (register AD-09) and check consumer-protection and sector rules before each campaign. If the creator collects personal data (giveaway entries, email lists), the data-protection law does apply.

### Earnings Estimate

Illustrative arithmetic only (all inputs are assumptions to replace with the creator's own data and the programme's verified rate): 5,000 engaged followers × 2% who buy in a month × UGX 100,000 average order × 10% commission ≈ UGX 100,000 a month. Show the formula with the client's numbers; never present the illustration as an expected income.

---

## Section 5: Digital Products

High-margin income: created once, sold repeatedly. Prioritise for creators with genuine expertise and an audience that trusts them as a source of knowledge.

### Digital Product Types for EA Creators

| Product Type | Production Effort | Price Range | Best For |
|---|---|---|---|
| PDF guide or e-book | Low (2–4 weeks) | UGX 20,000–150,000 | Education, how-to, financial literacy creators |
| Online course (video) | High (4–12 weeks) | UGX 100,000–500,000 | Skills and professional training creators |
| Template pack | Medium (2–3 weeks) | UGX 30,000–100,000 | Business, productivity, design creators |
| Coaching or consultation | Ongoing (low setup) | UGX 100,000–500,000 per session | Expert or professional creators |
| Membership community | Ongoing | UGX 20,000–50,000 per month | Community-first creators with loyal audiences |

### EA Digital Product Sales Channels

| Channel | How It Works | Best For |
|---|---|---|
| WhatsApp direct sale | Share payment link (MTN MoMo or Airtel Money); confirm via chat | Any digital product; low-tech audience |
| Gumroad | International platform; accepts cards and PayPal; USD pricing; accessible in EA | Creators with an international or USD-earning audience |
| Selar | African digital products marketplace; bank transfer in Uganda | PDF guides, e-books, templates |
| Teachable / Thinkific | Full course platforms; USD pricing | Online courses; requires USD payment method from the creator |

**Recommendation logic:** If the creator's audience pays primarily in Mobile Money, start with WhatsApp direct sales and Selar. Introduce Gumroad only when the creator has set up Payoneer or a USD account.

---

## Section 6: Brand Partnerships

Usually the most accessible monetisation route for East African creators (a working hypothesis; confirm with the creator's own deal history).

### Types of Brand Deals

- **Sponsored post (single):** One-off payment for a specific post or story. Lowest commitment, easiest to sell.
- **Campaign:** Multi-post deal over a defined period (typically 1–4 weeks). Includes a content brief and deliverables list.
- **Ambassador:** Ongoing relationship (3–12 months). Highest value; requires demonstrated loyalty to the brand and audience alignment.
- **Product seeding:** Receive free products with no guaranteed payment. Generally not recommended unless the product is genuinely valuable to the creator — it sets a low-value precedent.

### Pricing Brand Work: Distribution Fee + Talent Fee

No verified local rate card exists; do not publish follower-tier price bands as benchmarks. Build each quote from scope, using the method in Hennessy, B. (2018) *Influencer*, Citadel Press:

- **Distribution fee** (value of placement on the creator's channels): follower count; engagement, especially sponsored engagement compared with organic; content quality; name, face and special skills; audience precision.
- **Talent fee** (cost to create): production costs (photographer or editor, location, props, wardrobe, make-up, transport, data) + the creator's hours (negotiation, brief research, scouting, mood board, shoot, edit).
- **Price explicitly for:** usage beyond the brand's own channels (paid social, pre-roll, print, in-store); exclusivity beyond a narrow baseline (about one month against the top three competitors is Hennessy's fair baseline); high-season timing (Christmas, Easter, Eid, school-term openings, Valentine's, festivals); rush turnaround.
- **When the fee cannot move:** ask for a deposit, a split payment or shorter payment terms, or non-cash value (a brand feature, reshares).
- Record the creator's own past quotes and outcomes to build a dated, evidence-based rate history over time. Check withholding tax on payments with `chwezi-accounting-doctrine`.

### Offer Triage and Graceful Declines

- **Coverage or campaign?** A publicist offering gifted product with no talking points is seeking coverage; a campaign has talking points, hashtags and a go-live window. Price campaigns; treat coverage as optional.
- **Unpaid campaign test:** accept only for a dream brand, travel that lifts content quality, or real promotion by the brand. Otherwise decline: unpaid work displaces organic content and can tie the creator to one brand for free.
- **Below-rate offer:** apply the "would I advise a friend to take this?" test; counter politely ("For this scope my rate is closer to [amount], mainly because of [usage/exclusivity/production]") or accept with non-cash value.
- **Always ask for the contract before accepting**; terms and usage decide the true price.
- **Decline gracefully** — buyers keep do-not-book lists:
  - Budget: "I appreciate the offer. At this budget I can't deliver the quality the campaign deserves. If the budget changes, I'd be glad to revisit."
  - Off-brand: "Thank you for considering me. I don't think this would resonate with my audience, and I'd rather you got a strong return elsewhere."

### Brand Partnership Pitch Template

Produce a pitch document with these five sections for the creator:

1. **Introduction (1 paragraph):** Who the creator is, their content niche, and a one-sentence description of their audience and why brands benefit from reaching them.
2. **Audience numbers (1 table):** Followers per platform, average engagement rate, monthly reach, and audience demographics (age range, primary city, gender split).
3. **Case study (1 example):** A previous brand partnership result — or, if no prior partnerships exist, an organic post demonstrating brand-fit content (screenshot, caption, and result metrics).
4. **Ways we can work together (1 table, no prices):** ambassadorships, sponsored posts and videos, live coverage, events, shoots — with the line "Rates depend on scope, usage and exclusivity; I'm happy to hear about any budget." Keep a separate rate sheet that is shared only on request, after scope is known (Hennessy, 2018: never put prices in the press kit or one-sheet). Do not show a wall of past-client logos; link to a sponsored-work archive instead.
5. **Contact:** WhatsApp number and professional email address.

*See `08-influencer-marketing-strategy` for brand partnership negotiation frameworks and contract checklist.*

---

## Quality Criteria

Output is of professional standard when it meets all of the following:

- All five monetisation streams are assessed with EA-specific eligibility criteria and payment method information relevant to the client's payment capability.
- The YPP path includes a month-by-month growth timeline tailored to the creator's niche.
- Brand-work pricing uses the distribution-fee + talent-fee method with usage, exclusivity and season priced explicitly; no unsourced follower-tier rate card is presented as a benchmark.
- Digital product pricing is in UGX with production effort estimates per product type.
- The affiliate programme table includes EA-accessible options with Mobile Money payment noted where available.
- The brand partnership pitch template is complete with all five sections populated for the client, and the default pitch and press kit contain no prices.
- Affiliate and sponsorship disclosure follows the FTC/ASA standard as best practice with register AD-09/AD-10 cited; the data-protection law is invoked only for personal-data collection.
- Earnings, job access, eligibility and payment claims are sourced, dated and qualified; no guaranteed income or pay-to-access opportunity is presented.
- Each monetisation stream is assessed with a clear recommendation: Priority / Secondary / Not Yet / Not Applicable, based on the creator's current profile.

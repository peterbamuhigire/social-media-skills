---
name: strategy-customer-value-journey
description: >
  Maps a client's social media activity to the 8-stage Customer Value Journey (CVJ) framework
  (DigitalMarketer / Ryan Deiss). Produces a structured content plan showing what to create at
  each stage — Aware, Engage, Subscribe, Convert, Excite, Ascend, Advocate, Promote — with
  platform guidance, CTAs, and metrics. Invoke when a client posts either all promotional content
  (no awareness funnel) or all awareness content (no conversion mechanism), or when building a
  new social media strategy from scratch and a full-funnel plan is needed.
---
# Customer Value Journey Strategy

<!-- dual-compat:start -->
## Use when
- Maps a client's social media activity to the 8-stage Customer Value Journey (CVJ) framework (DigitalMarketer / Ryan Deiss). Produces a structured content plan showing what to create at each stage — Aware, Engage, Subscribe, Convert, Excite, Ascend, Advocate, Promote — with platform guidance, CTAs, and metrics. Invoke when a client posts either all promotional content (no awareness funnel) or all awareness content (no conversion mechanism), or when building a new social media strategy from scratch and a full-funnel plan is needed.
- Use this skill when it is the closest match to the requested deliverable or workflow.

## Do not use when
- Do not use this skill for graphic design, video production, software development, or legal advice beyond the repository's stated scope.
- Do not use it when another skill in this repository is clearly more specific to the requested deliverable.

## Workflow
1. Collect the required inputs or source material before drafting, unless this skill explicitly generates the intake itself.
2. Follow the section order and decision rules in this `SKILL.md`; do not skip mandatory steps or required fields.
3. Review the draft against the quality criteria, then deliver the final output in markdown unless the skill specifies another format.

## Anti-Patterns
- Do not invent client facts, performance data, budgets, or approvals that were not provided or clearly inferred from evidence.
- Do not skip required inputs, mandatory sections, or quality checks just to make the output shorter.
- Do not drift into out-of-scope work such as code implementation, design production, or unsupported legal conclusions.

## Outputs
- A structured markdown document, plan, playbook, or strategy ready for client-facing or internal use.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Framework Attribution

This skill applies the **Customer Value Journey (CVJ)** framework developed by Ryan Deiss and
DigitalMarketer. The CVJ maps every customer interaction — from first encounter to active referral
— across 8 sequential stages. It is distinct from the RACE framework (Reach / Act / Convert /
Engage, Chaffey 2024): RACE focuses on acquisition and conversion; the CVJ extends into
post-purchase stages (Excite, Ascend, Advocate, Promote) that drive repeat revenue and referrals.
For East African SMEs, these post-purchase stages are the most neglected and the highest-ROI
opportunity.

---

## Required Input

Ask for the following before generating any deliverable:

1. **Client business name** — trading name used on social media
2. **Industry / sector** — e.g. professional services, retail, hospitality, agribusiness
3. **Country / city** — defaults to Uganda / Kampala if not specified
4. **Primary goal** — e.g. increase sales, grow WhatsApp subscriber list, improve repeat purchases
5. **Current platforms** — which platforms the client is active on and approximate follower counts
6. **Current content mix** — rough description of what they post (promotional, educational, mixed)
7. **Existing offers** — what entry-point and ascension offers exist, or whether these need to be designed
8. **Customer lifetime value (approximate)** — to calibrate entry-point offer strategy

---

## The Two Most Common EA SME Failure Modes

Before mapping the journey, diagnose which failure mode applies to the client.

**Failure Mode 1 — All Promotional (Stuck at Convert)**
The client posts discounts, product shots, and price lists. Reach is limited to people already
ready to buy. No content builds awareness or nurtures interest. Follower growth is slow; engagement
is low; every post asks for money before trust is established.

**Failure Mode 2 — All Awareness (No Conversion Mechanism)**
The client posts tips, motivational quotes, and educational content. Engagement metrics look
healthy but sales do not follow. There is no Subscribe mechanism (no WhatsApp opt-in, no follow
prompt) and no Convert offer. The audience consumes content and moves on.

Both failure modes stem from the same root cause: treating social media as a single-stage
activity rather than a multi-stage journey. The CVJ provides the corrective structure.

---

## The 8 Stages of the Customer Value Journey

Apply Ryan Deiss / DigitalMarketer's CVJ to understand what the customer is thinking and feeling
at each stage, and what social media must do to move them forward.

**Stage 1 — Aware**
The customer encounters the brand for the first time. They are not looking for the client
specifically; they are scrolling, watching, or being referred. The goal is to stop the scroll and
create a relevant first impression. Customer mindset: *"Who is this?"*

**Stage 2 — Engage**
The customer consumes content — watches a video, reads a post, saves a tip. They are evaluating
whether the brand is worth their continued attention. No purchase intent yet. Customer mindset:
*"This looks useful / interesting."*

**Stage 3 — Subscribe**
The customer opts in to an ongoing relationship: follows the page, joins the WhatsApp broadcast
list, subscribes to a newsletter, or saves the number. This is the first active commitment. In
East Africa, WhatsApp opt-in is the highest-value subscribe action. Customer mindset:
*"I want to hear more from this brand."*

**Stage 4 — Convert**
The customer makes a first transaction — often a low-risk, low-cost entry-point offer. The goal
is to convert a prospect into a buyer, not to maximise profit on this transaction. Customer
mindset: *"Let me try this."*

**Stage 5 — Excite**
Immediately post-purchase, the customer needs confirmation they made the right decision. This
stage removes buyer's remorse, delivers a fast win, and sets expectations. Poor post-purchase
experience kills Ascend and Advocate potential. Customer mindset: *"Did I make the right choice?"*

**Stage 6 — Ascend**
The customer has trust established through a positive first experience. They are receptive to
higher-value offers, retainers, or premium packages. This is where revenue is made. Customer
mindset: *"What else can this brand do for me?"*

**Stage 7 — Advocate**
The customer shares positive experience unprompted — a testimonial, a WhatsApp mention to a
friend, a positive comment. Advocacy is organic and cannot be forced, only enabled. Customer
mindset: *"I want others to know about this."*

**Stage 8 — Promote**
The customer actively refers new customers, participates in a referral programme, or becomes a
brand ambassador. This is structured, incentivised advocacy. Customer mindset:
*"I will tell people about this and here is why they should use it."*

---

## Entry-Point Offers vs. Ascension Offers

**Entry-Point Offers (Stage 4 — Convert)**
Designed to remove friction and acquire a first-time buyer. Profit is not the objective.
The offer must feel low-risk relative to the customer's current level of trust.

Examples for the EA context:
- Free 30-minute consultation (professional services)
- Free WhatsApp guide or checklist (coaching, marketing, legal)
- Low-cost trial session (fitness, tutoring, therapy)
- Discounted first order with a minimum spend threshold (retail, food)
- Free audit or site visit (construction, agriculture, IT services)

Design rule: the entry-point offer must deliver genuine value so that Stage 5 (Excite) happens
naturally. A cheap-feeling offer produces buyer's remorse, not advocacy.

**Ascension Offers (Stage 6 — Ascend)**
Designed to monetise established trust. Presented only after Stage 5 (Excite) is confirmed.
Never pitch ascension offers to first-time buyers before they have had a positive experience.

Examples for the EA context:
- Monthly retainer or subscription (services)
- Premium package or bundle (products)
- Annual contract with a loyalty discount
- Referral reward programme (cash, discount, free month)
- Exclusive membership or community access

---

## Mapping Social Media Content to the CVJ

| Stage | Goal | Primary Platform / Channel | Content Type | CTA |
|---|---|---|---|---|
| Aware | Stop the scroll; create first impression | Facebook, TikTok, Instagram, YouTube | Short video, reel, boosted post, referral content | No hard CTA — invite to follow or watch more |
| Engage | Build interest; demonstrate expertise | Facebook, Instagram, YouTube, LinkedIn | Educational post, how-to video, carousel, blog excerpt | "Save this", "Comment your question", "Read more" |
| Subscribe | Capture opt-in for ongoing communication | Facebook (page follow), WhatsApp, Email | Lead magnet post, free guide offer, WhatsApp link in bio | "Join our WhatsApp list", "Follow for weekly tips" |
| Convert | Drive first transaction | WhatsApp broadcast, Facebook, Instagram | Entry-point offer post, limited availability, social proof | "Message us to book", "Order here", "Claim your free consult" |
| Excite | Confirm the right decision; deliver fast win | WhatsApp (1-to-1 or broadcast), Email | Welcome message, onboarding guide, quick-win tip, thank-you post | "Here is what happens next" |
| Ascend | Present premium or repeat offer | WhatsApp, Email, Facebook Retargeting | Upgrade offer, bundle, case study, results post | "Ready for the next step?", "Upgrade your package" |
| Advocate | Enable and capture social proof | Facebook, Instagram, WhatsApp | Testimonial request, review prompt, user-generated content repost | "Share your experience", "Tag us in your results" |
| Promote | Activate structured referral | WhatsApp, Facebook, Email | Referral programme announcement, incentive post, ambassador content | "Refer a friend and earn…", "Share this link" |

---

## WhatsApp in the CVJ

WhatsApp is the dominant Subscribe and Convert engine in East Africa and must be treated as a
first-class channel in the CVJ, not an afterthought.

**Subscribe stage — WhatsApp opt-in**
- Include a WhatsApp link or number in every bio, post caption, and Story CTA
- Offer a specific reason to opt in: a free guide, a price list, a consultation booking
- Use a welcome message that delivers the promised value immediately
- Segment broadcast lists by interest or purchase stage where possible

**Convert stage — WhatsApp broadcast**
- Send entry-point offers to the broadcast list with clear, friction-free CTAs
- Personalise where possible ("Hi [name]" in bulk messages increases open rates)
- Respond to enquiries within two hours; delayed responses collapse conversion

**Excite and Ascend — WhatsApp follow-up sequences**
- Send a post-purchase welcome message within 24 hours of the first transaction
- Include a quick-win resource (guide, checklist, tip) to deliver immediate value
- Follow up at Day 3 and Day 7 to check in and introduce the ascension offer
- Keep broadcast messages under 150 words; use voice notes for warmth where appropriate

**Boundary:** WhatsApp broadcast management (scheduling, list hygiene, automation tools) is out
of scope for this skill. This skill produces the content strategy and message outlines only.

---

## CVJ Audit — Assessing the Client's Current Content

Before building the plan, audit where the client's existing content sits across the 8 stages.

**Step 1 — Content inventory**
Review the last 30 posts across all active platforms. Categorise each post by CVJ stage using the
content type column in the mapping table above.

**Step 2 — Stage distribution**
Count how many posts fall into each stage. Express as a percentage of total posts.

**Step 3 — Gap identification**
Identify stages with 0% or under 10% of content. These are the gaps the content plan must fill.

**Step 4 — Mechanism audit**
Check whether the following mechanisms exist:
- Subscribe: Is there a WhatsApp opt-in link or follow CTA on every platform? (Yes / No)
- Convert: Is there a current entry-point offer? Is it clearly communicated? (Yes / No)
- Excite: Is there a post-purchase welcome sequence? (Yes / No)
- Promote: Is there an active referral mechanism? (Yes / No)

**Step 5 — Failure mode classification**
Based on Steps 2 and 4, classify the client as Failure Mode 1 (all promotional), Failure Mode 2
(all awareness), or Mixed (gaps in specific stages).

---

## Building the CVJ Content Plan

Apply the following recommended content ratio as a starting point. Adjust based on audit results:
clients with a large Aware/Engage deficit should weight more heavily toward the top of the
journey; clients with low conversion rates should weight toward Convert and Excite.

| Journey Zone | Stages | Recommended Content Share |
|---|---|---|
| Top of journey | Aware + Engage | 40% |
| Opt-in | Subscribe | 15% |
| Conversion | Convert | 15% |
| Retention and growth | Excite + Ascend | 20% |
| Referral | Advocate + Promote | 10% |

**For each gap identified in the audit, generate:**
1. Three to five specific content ideas for that stage, matched to the client's industry
2. The platform and format best suited to that stage (use the mapping table)
3. The CTA that moves the customer to the next stage
4. The WhatsApp integration point, where applicable

**Content sequencing rule:** A customer cannot be moved from Aware to Convert in a single post.
Design content flows where each stage has at least two to three touchpoints before the CTA
advances the customer. Exception: warm referrals (arriving via Stage 8 — Promote) may enter at
Subscribe or Convert directly.

---

## Referral Loop Design (Advocate and Promote)

The referral loop is the highest-ROI section of the CVJ for EA SMEs because word-of-mouth is the
dominant trust mechanism in markets with limited consumer review infrastructure.

**Enabling Advocate (unprompted sharing):**
- Deliver a result so clearly positive that sharing feels natural
- Make it easy to share: provide a WhatsApp-forwardable message, a shareable graphic, a quote card
- Ask for testimonials at the moment of highest satisfaction (immediately after a result is
  achieved, not weeks later)
- Repost and celebrate customer results publicly to signal that advocacy is valued

**Activating Promote (structured referral):**
- Design a referral mechanism with a specific incentive: cash reward, discount on next purchase,
  free session, or loyalty points
- Communicate the referral programme clearly and repeatedly — most customers do not refer because
  they were never asked
- Create a WhatsApp message template the customer can forward verbatim ("Tell your friend to
  mention your name and they get X")
- Track referral sources so the incentive can be honoured and the programme can be optimised

**Referral loop content cadence:**
- Post a testimonial or case study every two weeks minimum
- Send a referral programme reminder via WhatsApp broadcast once per month
- Acknowledge and thank referrers publicly (with permission) to reinforce the behaviour

---

## Metrics Per CVJ Stage

Map vanity metrics to their correct stage so clients understand what each number actually measures.

| Stage | Primary Metric | Secondary Metric | Vanity Metric Trap |
|---|---|---|---|
| Aware | Reach, impressions, new accounts reached | Video views, shares | Likes (measure engagement, not awareness) |
| Engage | Post saves, comments, shares, watch time | Profile visits, link clicks | Total likes (does not indicate intent) |
| Subscribe | WhatsApp opt-ins, page follows, email sign-ups | Lead magnet downloads | Follower count (measures Subscribe accumulation, not rate) |
| Convert | First purchases, consultation bookings, enquiries that convert | Cost per acquisition | Enquiry volume (high enquiries with low conversions = friction problem) |
| Excite | Repeat WhatsApp engagement, positive reply rate, Day-7 retention | Return visit rate | Post-purchase likes (does not measure satisfaction) |
| Ascend | Upsell conversion rate, average order value, retainer sign-ups | Revenue per existing customer | Total revenue (does not isolate ascension performance) |
| Advocate | Testimonials received, user-generated content tags, unprompted shares | Review volume, positive sentiment | Comment volume (not all comments are advocacy) |
| Promote | Referrals attributed, referral conversion rate, referral revenue | Referral programme participation rate | Shares (shares do not always produce referral actions) |

---

## Quality Criteria

Output meets the standard of this skill if it:

1. **Correctly attributes the CVJ framework** to Ryan Deiss / DigitalMarketer and does not
   conflate it with the RACE framework or other funnel models.
2. **Diagnoses the failure mode** before prescribing content — the plan is specific to whether
   the client is over-indexed on promotional or awareness content, or has specific stage gaps.
3. **Integrates WhatsApp as a primary channel** at Subscribe, Convert, and Excite stages, not as
   an optional add-on; reflects the EA market reality.
4. **Provides actionable content ideas** for each gap stage, matched to the client's industry and
   platform mix — not generic descriptions of content types.
5. **Includes a referral mechanism** with specific, incentivised steps for Advocate and Promote
   stages; does not treat referrals as organic and unmanageable.
6. **Maps metrics to stages correctly** and explicitly identifies which metrics are vanity metrics
   at the wrong stage (e.g. likes as a measure of conversion).
7. **Respects the content ratio** as a starting point and adjusts it to the client's audit results
   with a clear rationale for any deviation.
8. **Stays within scope** — this skill produces content strategy and message outlines; it does not
   produce graphic design briefs, paid ad campaign structures, or WhatsApp automation code.

---

## References

- Deiss, R. and DigitalMarketer (2023) *The Customer Value Journey*. DigitalMarketer.com
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Wiley
- Kotler, P. et al. (2023) *Marketing Management*. Pearson

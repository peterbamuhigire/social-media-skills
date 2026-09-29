# Quarterly Marketing-Mix Review (7 Ps)

Merged from skills/meta-analytics-ops/meta-social-marketing-mix-review on 2026-09-29 at 8eacccb; preservation map: [meta-social-marketing-mix-review.md](../../../../docs/kaizen/consolidation-2026-09-29/preservation/meta-social-marketing-mix-review.md)

## When to use this reference

Read this reference at a quarterly decision point, when the client needs a diagnosis of social media's contribution across the 7 Ps marketing mix rather than a monthly performance report. Uses: a quarterly review meeting, a new-account baseline, or a cause-of-decline investigation. The framework is the 7 Ps as applied to social media by Dallas (2022). The output is a scored one-page summary. If the client wants the strategy itself rewritten, route to [`05-social-media-strategy`](../../../pipeline/05-social-media-strategy/SKILL.md) and hand over the verified evidence. Route any presentation design to the design engine (https://github.com/peterbamuhigire/chwezi-design-engine) after the evidence is approved.

## Inputs

Ask for the following before generating the review:

| Input | What to capture |
|---|---|
| Client business name | Trading name as it appears on social media |
| Industry | Sector and sub-sector (for example hospitality: boutique hotel) |
| Country / city | Primary market (default Uganda / East Africa) |
| Review period | Quarter and year (for example Q1 2026: January–March) |
| Access to analytics | Whether platform insights, reach and engagement data are available |
| Access to content archive | Whether recent posts (last 90 days) are available for review |
| Primary business goal this quarter | For example grow followers, drive WhatsApp enquiries, increase walk-in footfall |
| Known issues or client concerns | Complaints, observations or hunches the client has already raised |

Also require current offer, channel activity, customer evidence and performance data. Without the current offer, stop the affected decision or issue a clearly bounded partial output; mark any P you cannot assess `not assessed`, never scored by default.

## Decision rules

| Situation | Action | Failure avoided |
|---|---|---|
| Any P | Assess all 7 Ps with at least 3 diagnostic questions each; skip none. | Blind spot in the mix. |
| Writing red flags | Make them specific to the client's situation, not generic marketing advice. | Boilerplate review. |
| Place, People and Physical Evidence | Include the East Africa red flags below for at least these 3 Ps. | Review that ignores the market. |
| Promotion section | Cite the 10-4-1 rule (Bodnar and Cohen, 2012) explicitly. | Unsourced ratio. |
| Recommended action exists in this repository | Name the owning skill. | Action with no follow-through route. |
| Lowest-scoring P identified | Recommend the next skill to run for that P (for example Process scoring 1–2 → [`11-content-calendar`](../../../pipeline/11-content-calendar/SKILL.md)). | Review with no next step. |

## Procedure — the 7 Ps diagnostic

Work through each P in sequence. For each P, apply the diagnostic questions, note red flags, select the most relevant recommended action(s) and score the P from 1 to 5.

| P | Diagnostic questions | Red flags | Recommended actions (owner skill) |
|---|---|---|---|
| **1. Product** — what the brand sells via social media, and how clearly that is communicated | Is it immediately clear from the profile what this business sells? Does content show the product or service in use, or only describe it? Does content communicate the customer benefit, not just features? Is the product suited to social promotion (visual, demonstrable, shareable)? | Bio does not state what the business does or whom it serves. All product content is "buy now" copy with no demonstration or benefit story. Product is complex but no content explains it simply or shows it working. | Rewrite the bio using a WHO-WHAT-WHO-CTA structure ([`02-platform-audit`](../../../pipeline/02-platform-audit/SKILL.md)). Add benefit-led content (before/after, results, customer outcomes) to all promotional posts. Create a simple explainer post or short-form video for complex or unfamiliar products. |
| **2. Price** — how price is communicated or withheld, and whether that serves the brand | Does the brand communicate price or price ranges publicly? If not, is there a clear alternative CTA (for example WhatsApp for enquiries)? Is pricing competitive for the market position social media creates? Do offers appear consistently, or randomly and reactively? | No price information anywhere: EA audiences expect at least a range or a clear enquiry route. Offers inconsistent or desperate; constant discounting signals weak value. Pricing content contradicts the premium positioning. | Adopt a price-transparency policy: publish ranges if not exact prices; add a "DM / WhatsApp for pricing" CTA on all product posts. Create a promotional calendar; plan offers in advance, not ad-hoc discounts. Audit pricing positioning against the visual quality and tone of existing content. |
| **3. Place** — where and how the audience engages with and buys from the brand | Is the path from post to purchase clear (for example link in bio → WhatsApp → Mobile Money)? Are the right platforms used for the right segments? Is location or physical presence communicated where relevant (retail, hospitality, events)? Is WhatsApp integrated as the primary conversion channel? | *EA-specific:* posts drive traffic to a website that does not load on mobile or on a 3G connection. No WhatsApp CTA despite an East African market where WhatsApp is the dominant messaging and commerce channel. A brick-and-mortar business never mentions its physical location. | Map the full post-to-purchase journey and remove friction points ([`playbook-post-click-strategy`](../../../playbooks/playbook-post-click-strategy/SKILL.md)). Add a WhatsApp Click-to-Chat link (wa.me/256XXXXXXXXX) as the primary CTA on all platforms. Pin a Google Maps link and physical address to all relevant profiles; tag location on every relevant post. |
| **4. Promotion** — the mix and structure of promotional versus non-promotional content | What is the ratio of educational or entertaining to promotional content? (Target: the 80/20 rule, or the 10-4-1 rule, Bodnar and Cohen, 2012.) Is promotional content spread through the week or bunched? Are there campaigns with a clear start, middle and end, or is promotion continuous and undifferentiated? Is paid social used to amplify organic content that is already performing? | More than 30% of posts are direct promotion: audiences disengage from feeds that feel like catalogues. No planned campaigns: promotion is reactive, unstructured and event-driven only. Boosted posts with no targeting rationale or defined objective. | Apply the 10-4-1 rule (Bodnar and Cohen, 2012): for every 15 posts, 10 shares of others' content, 4 original non-promotional posts and 1 promotional post. Build a quarterly campaign calendar with 2–3 major and 4–6 minor campaigns per quarter. Decide which organic posts warrant paid amplification with [`ad-testing-and-scaling`](../../../advertising/ad-testing-and-scaling/SKILL.md). |
| **5. People** — who represents the brand, visibly and behind the scenes | Is there a consistent brand voice across content and platforms? Is there a human face (founder, team member, employee) in the content? Who responds to comments and DMs, and is the style consistent? Are spokespeople or ambassadors used appropriately and briefed on brand standards? | *EA-specific:* all content is product imagery or graphics only, with no human presence; EA audiences trust people, not logos. Multiple people post with different voices, tones and quality levels. DM responses slow, inconsistent, or handled by different people with no shared script. | Feature the founder or a named team member in at least one post per week. Create a brand voice guide and brief everyone who posts or responds ([`04-brand-voice-intake`](../../../pipeline/04-brand-voice-intake/SKILL.md); [`brand-voice-ai-training`](../../../ai-marketing/brand-voice-ai-training/SKILL.md)). Assign one named community-management owner per account with defined response-time standards. |
| **6. Process** — how content is planned, produced, approved and published | Is a content calendar in place and followed? Is there an approval process with defined turnaround times? Is content scheduled in advance or published ad hoc? Is a quality-control checklist applied before any post goes live? | No content calendar: posting is irregular, reactive and dependent on one person's availability. No approval process: content goes live without client review or brand sign-off. Frequent unplanned posting gaps of three or more days (planned gaps such as holidays or campaigns excepted). | Implement a monthly content calendar covering all platforms and content pillars ([`11-content-calendar`](../../../pipeline/11-content-calendar/SKILL.md)). Establish an approval workflow with a 24-hour client review window before scheduled publication. Use a scheduling tool (Buffer, FeedHive or Meta Business Suite) to keep posting consistent regardless of team availability; tool availability verify before stating (no register record). |
| **7. Physical Evidence** — the visual and reputational signals that make the brand believable | Is the visual identity (colours, fonts, photography style) consistent across platforms? Are reviews, testimonials and case studies featured regularly? Does content look professional enough for the price point and positioning? Is East African market credibility visible (local clients, local context, local language)? | *EA-specific:* stock imagery with no local context looks generic and untrustworthy to EA audiences who recognise global stock photos. No social proof: no reviews, customer stories or before/after content. Inconsistent visual quality: some posts professional, others rushed or off-brand. | Introduce a visual system with defined templates, colour palette and photography standards ([`platform-instagram`](../../../platforms/platform-instagram/SKILL.md) for the Instagram visual system; [`04-brand-voice-intake`](../../../pipeline/04-brand-voice-intake/SKILL.md) for the brand style guide; visual execution through the design engine). Launch a "Customer Stories" series using real client testimonials, photos and outcomes ([`08-influencer-marketing-strategy`](../../../pipeline/08-influencer-marketing-strategy/SKILL.md) for UGC). Publish at least one social-proof post every two weeks: a review screenshot, a client testimonial or a case-study summary. |

## Output template — one-page quarterly review summary

Complete one row per P from the diagnostic above.

| P | Score (1–5) | Top red flag | Priority action |
|---|---|---|---|
| Product | | | |
| Price | | | |
| Place | | | |
| Promotion | | | |
| People | | | |
| Process | | | |
| Physical Evidence | | | |
| **Overall score** | **/35** | | |

**Score interpretation:**

| Band | Score | Meaning |
|---|---|---|
| Strong | 28–35 | Strategy is fundamentally sound: maintain momentum and refine |
| Developing | 21–27 | 2–3 targeted improvements will produce measurable results |
| Weak | 14–20 | Systematic overhaul required across multiple Ps |
| Critical | Below 14 | Fundamental strategy reset recommended before further content investment |

After the table, include:

- **3 priority actions** ranked by expected impact; these become the client's 90-day focus.
- **One-sentence overall assessment** the consultant can read aloud in a review meeting.
- **Recommended next skill to run**, based on the lowest-scoring P.
- A decision and source register: each material claim records its source and date or is labelled unverified.

## Checklist

- [ ] All 7 Ps assessed with at least 3 diagnostic questions each; none skipped.
- [ ] Red flags specific to the client's situation, not generic marketing advice.
- [ ] Every recommended action names an owning skill in this repository where one applies.
- [ ] Scoring table totals out of 35 with a written interpretation band.
- [ ] EA-specific red flags included for at least 3 Ps (Place, People and Physical Evidence).
- [ ] Output fits on one page: a business owner can read the summary in under 5 minutes.
- [ ] 10-4-1 rule (Bodnar and Cohen, 2012) cited explicitly in the Promotion row.
- [ ] Read-only: no publishing, spend or live-account edits without separate explicit authority.

## Sources

- Dallas, M. (2022) *Social Media Marketing Algorithms*
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Hoboken, NJ: Wiley
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. 8th edn. Harlow: Pearson

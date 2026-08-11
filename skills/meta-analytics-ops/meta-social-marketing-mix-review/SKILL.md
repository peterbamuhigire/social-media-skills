---
name: meta-social-marketing-mix-review
description: "Use when reviewing the social-media contribution across the 7 Ps at a quarterly decision point. Produces quarterly social marketing-mix review; use `05-social-media-strategy` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Social Media Marketing Mix Review — 7 Ps Diagnostic

## Purpose

Use this skill to systematically diagnose the health of a client's social media strategy using the 7 Ps marketing mix framework, as applied to social media by Dallas (2022). The output is a scored one-page summary — suitable for a quarterly review meeting, a new account baseline, or a cause-of-decline investigation.

**Related skills:** `05-social-media-strategy`, `meta-reporting`; route any presentation design handoff to `design-system-skills` after the evidence is approved.

---


<!-- dual-compat-start -->
## Use When

- Use this skill for reviewing the social-media contribution across the 7 Ps at a quarterly decision point.
- Confirm that `05-social-media-strategy` is not the closer route before proceeding.

## Do Not Use When

- Use `05-social-media-strategy` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Current offer, channel activity, customer evidence and performance data | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Quarterly social marketing-mix review | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. This is read-only by default: inspect and report without changing source records, accounts, skills or campaigns. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified quarterly social marketing-mix review. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Current offer, channel activity, customer evidence and performance data is current and attributable | Produce the full quarterly social marketing-mix review and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `05-social-media-strategy` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `05-social-media-strategy` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the quarterly social marketing-mix review, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the quarterly social marketing-mix review without current offer. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `05-social-media-strategy` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified current offer, the skill produces a quarterly social marketing-mix review with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`05-social-media-strategy`](../../pipeline/05-social-media-strategy/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Inputs

Before generating the review, ask for:

1. **Client business name** — trading name as it appears on social media
2. **Industry** — sector and sub-sector (e.g., hospitality — boutique hotel)
3. **Country / city** — primary market (default: Uganda / East Africa)
4. **Review period** — which quarter and year (e.g., Q1 2026: January–March)
5. **Access to analytics** — confirm whether platform insights, reach, and engagement data are available
6. **Access to content archive** — confirm whether recent posts (last 90 days) are available for review
7. **Primary business goal this quarter** — e.g., grow followers, drive WhatsApp enquiries, increase walk-in footfall
8. **Known issues or client concerns** — any specific complaints, observations, or hunches the client has already raised

---

## Diagnostic Framework — The 7 Ps

Work through each P in sequence. For each P, apply the diagnostic questions, note any red flags, and select the most relevant recommended action(s).

---

### 1. Product

*What the brand is selling via social media — and how clearly that is communicated.*

**Diagnostic questions:**
- Is it immediately clear from the social media profile what this business sells?
- Does the content show the product or service in use, or does it only describe it?
- Does the content communicate the benefit to the customer, not just the features?
- Is the product well-suited to social media promotion — is it visual, demonstrable, or shareable?

**Red flags:**
- Profile bio does not state what the business does or who it serves
- All product content is "buy now" copy with no demonstration or benefit story
- The product is complex but no content explains it simply or shows it working

**Recommended actions:**
- Rewrite the profile bio using a WHO-WHAT-WHO-CTA structure (reference `playbook-profile-optimisation`)
- Add "benefit-led" content — before/after, results, customer outcomes — to all promotional posts
- Create a simple explainer post or short-form video for complex or unfamiliar products

**Score this P (1–5):** ___

---

### 2. Price

*How price is communicated — or withheld — on social media, and whether that serves the brand.*

**Diagnostic questions:**
- Does the brand communicate price or pricing ranges publicly?
- If price is not shared, is there a clear alternative CTA (e.g., WhatsApp for enquiries)?
- Is pricing competitive relative to the market position the social media creates?
- Do promotional offers appear consistently, or are they random and reactive?

**Red flags:**
- No price information anywhere — audiences in EA expect at least a range or a clear enquiry route
- Promotional offers are inconsistent or feel desperate; constant discounting signals weak value
- Pricing content contradicts the premium positioning the brand is trying to create

**Recommended actions:**
- Adopt a price transparency policy: publish price ranges if not exact prices; add "DM / WhatsApp for pricing" CTA on all product posts
- Create a promotional calendar — plan offers in advance rather than running ad-hoc discounts
- Audit pricing positioning against the visual quality and tone of existing content

**Score this P (1–5):** ___

---

### 3. Place

*Where and how the audience engages with and purchases from the brand.*

**Diagnostic questions:**
- Is the path from social post to purchase clear? (e.g., link in bio → WhatsApp → Mobile Money)
- Are the right platforms being used for the right audience segments?
- Is location or physical presence communicated where relevant (retail, hospitality, events)?
- Is WhatsApp integrated as the primary conversion channel?

**Red flags (EA-specific):**
- Posts drive traffic to a website that does not load on mobile or on a 3G connection
- No WhatsApp CTA despite operating in an East African market where WhatsApp is the dominant messaging and commerce channel
- A brick-and-mortar business never mentions its physical location on social media

**Recommended actions:**
- Map the full post-to-purchase journey and remove friction points (reference `playbook-post-click-strategy`)
- Add a WhatsApp Click-to-Chat link (wa.me/256XXXXXXXXX) as the primary CTA across all platforms
- Pin a Google Maps link and physical address to all relevant profiles; tag location on every relevant post

**Score this P (1–5):** ___

---

### 4. Promotion

*The mix and structure of promotional versus non-promotional content.*

**Diagnostic questions:**
- What is the ratio of educational or entertaining content to promotional content? (Target: 80/20 rule, or apply the 10-4-1 rule — Bodnar and Cohen, 2012)
- Is promotional content spread throughout the week or bunched together?
- Are there campaigns with a clear start, middle, and end — or is promotion continuous and undifferentiated?
- Is paid social used to amplify organic content that is already performing?

**Red flags:**
- More than 30% of posts are direct promotional content — audiences disengage from feeds that feel like catalogues
- No planned campaigns — promotion is reactive, unstructured, and event-driven only
- Boosted posts with no targeting rationale or defined objective

**Recommended actions:**
- Apply the 10-4-1 rule (Bodnar and Cohen, 2012): for every 15 posts, use 10 shares of others' content, 4 original non-promotional posts, and 1 promotional post
- Build a quarterly campaign calendar with 2–3 major campaigns and 4–6 minor campaigns per quarter
- Use `strategy-organic-paid-hybrid` to determine which organic posts warrant paid amplification

**Score this P (1–5):** ___

---

### 5. People

*Who represents the brand on social media — visibly and behind the scenes.*

**Diagnostic questions:**
- Is there a consistent brand voice across all content and platforms?
- Is there a human face — founder, team member, or employee — visible in the content?
- Who is responding to comments and DMs, and is the response style consistent?
- Are brand spokespeople or ambassadors used appropriately and briefed on brand standards?

**Red flags (EA-specific):**
- All content is product imagery or graphics only — no human presence; EA audiences trust people, not logos
- Multiple people post with completely different voices, tones, and quality levels
- DM responses are slow, inconsistent, or handled by different team members with no shared script

**Recommended actions:**
- Feature the founder or a named team member in at least one post per week
- Create a brand voice guide and brief all team members who post or respond (reference `brand-voice-ai-training`)
- Assign one named community management owner per account with defined response-time standards

**Score this P (1–5):** ___

---

### 6. Process

*How content is planned, produced, approved, and published.*

**Diagnostic questions:**
- Is there a content calendar in place and being followed?
- Is there a content approval process with defined turnaround times?
- Is content scheduled in advance, or published reactively and ad hoc?
- Is there a quality control checklist applied before any post goes live?

**Red flags:**
- No content calendar — posting is irregular, reactive, and dependent on one person's availability
- No approval process — content goes live without client review or brand sign-off
- Frequent posting gaps of three or more days that are not planned (e.g., holidays, campaigns)

**Recommended actions:**
- Implement a monthly content calendar covering all platforms and content pillars (reference `11-content-calendar`)
- Establish a content approval workflow with a 24-hour client review window before scheduled publication
- Use a scheduling tool (Buffer, FeedHive, or Meta Business Suite) to maintain posting consistency regardless of team availability

**Score this P (1–5):** ___

---

### 7. Physical Evidence

*The visual and reputational signals that make the brand believable and trustworthy.*

**Diagnostic questions:**
- Is the visual identity — colours, fonts, photography style — consistent across all platforms?
- Are reviews, testimonials, and case studies featured regularly?
- Does the content look professional enough for the brand's price point and market positioning?
- Is the brand's East African market credibility visible — local clients, local context, local language?

**Red flags (EA-specific):**
- Stock imagery with no local context — looks generic and untrustworthy to EA audiences who recognise global stock photos
- No social proof: no reviews, no customer stories, no before/after content
- Inconsistent visual quality — some posts look professional, others look rushed or off-brand

**Recommended actions:**
- Introduce a visual system with defined templates, colour palette, and photography standards (reference `platform-instagram-visual-system` or `playbook-social-media-brand-style-guide`)
- Launch a "Customer Stories" content series using real client testimonials, photos, and outcomes (reference `playbook-ugc-strategy`)
- Publish at least one social proof post every two weeks: a review screenshot, a client testimonial, or a case study summary

**Score this P (1–5):** ___

---

## Output — One-Page Quarterly Review Summary

Generate the following table as the primary deliverable. Complete one row per P based on the diagnostic above.

| P | Score (1–5) | Top Red Flag | Priority Action |
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
| Strong | 28–35 | Strategy is fundamentally sound — maintain momentum and refine |
| Developing | 21–27 | 2–3 targeted improvements will produce measurable results |
| Weak | 14–20 | Systematic overhaul required across multiple Ps |
| Critical | Below 14 | Fundamental strategy reset recommended before further content investment |

After the table, include:
- **3 priority actions** ranked by expected impact — these become the client's 90-day focus
- **One-sentence overall assessment** the consultant can read aloud in a review meeting
- **Recommended next skill to run** based on the lowest-scoring P (e.g., if Process scores 1–2, recommend `11-content-calendar` next)

---

## Quality Criteria

- All 7 Ps are assessed with at least 3 diagnostic questions each; no P is skipped
- Red flags are specific to the client's situation — not generic marketing advice
- Every recommended action references a named skill in this repository where applicable
- The scoring table produces a total out of 35 with a written interpretation band
- EA-specific red flags are included for at least 3 Ps (Place, People, and Physical Evidence)
- The final output fits on one page — a business owner can read the summary in under 5 minutes
- The 10-4-1 rule (Bodnar and Cohen, 2012) is cited explicitly in the Promotion section

---

## References

- Dallas, M. (2022) *Social Media Marketing Algorithms*
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Hoboken, NJ: Wiley
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. 8th edn. Harlow: Pearson

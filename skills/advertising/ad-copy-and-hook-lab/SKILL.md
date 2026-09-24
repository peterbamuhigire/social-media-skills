---
name: ad-copy-and-hook-lab
description: Use when writing or testing ad headlines, hooks, primary text, offers, proof lines and guarantees for paid social, search, print, radio or outdoor; use creative-brief-and-big-idea for the platform idea and caption-writer for organic captions.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Ad Copy and Hook Lab

Generate, screen and test advertising copy from an approved brief: offer first, proof early, one message, headline and hook mechanisms, and an ethics filter that removes classic direct-response tricks that are now unlawful or off-brand.

<!-- dual-compat-start -->
## Use When

- An approved brief or concept needs headlines, video hooks, primary text, descriptions, calls to action or end-card lines.
- A campaign needs a headline bank and a test plan for the top candidates.
- An offer needs to be built or repaired before copy (promise, proof, sweetener, risk reversal, real deadline).
- Existing ads need a copy diagnosis: weak hook, buried offer, no proof, clever-but-unclear, or unsafe claims.
- Responsive search ad assets, lead-ad forms or click-to-WhatsApp opening messages need writing.

## Do Not Use When

- There is no approved brief or platform idea; use `creative-brief-and-big-idea` first.
- The deliverable is organic captions or community posts; use `caption-writer`.
- The deliverable is a long-form sales letter, VSL or funnel sequence; use `direct-response-funnel-copy`.
- The claim cannot be substantiated or the category is regulated and unchecked; stop and route to the legal/market release gate.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Approved brief: audience, single message, action, mandatories | `creative-brief-and-big-idea` or client | Yes | Stop and request it; do not write to a guessed audience. |
| Offer facts: price, terms, deadline, stock or capacity, guarantee | Client commercial owner | Yes for offer copy | Write benefit-only variants and mark the offer lines `not assessed`. |
| Proof: testimonials with consent, results with source, certifications, reviews | Client records, CRM, review platforms | Conditional | Use no proof lines; never invent or paraphrase testimonials into quotes. |
| Channel and format list with current character limits and specs | Media plan; register claims AD-05 and AD-08 or live platform help | Yes | Write to the register limits where available; otherwise mark length "check current spec". |
| Voice-of-customer language | Reviews, DMs, sales notes, listening | Recommended | Draft from the brief and flag the missing customer language. |

## Workflow

1. Confirm the brief, audience awareness level (unaware, problem-aware, solution-aware, product-aware, most aware) and single action; stop if any is missing.
2. Run the offer workshop ([offer, proof and guarantee kit](references/offer-proof-and-guarantee-kit.md)): immense promise, believability ceiling, proof, sweetener, risk reversal, real limited offer or scarcity with its reason.
3. Collect the raw material: top benefit, hidden benefit, main fear, news angle, strongest proof number, customer phrases.
4. Run the 60-minute headline sprint ([headline and hook families](references/headline-and-hook-families.md)): at least five lines per mechanism; then short-video hooks and first lines of primary text.
5. Screen every candidate: pre-flight questions, standalone test, "dull to whom?", specificity, the [direct-marketing ethics filter](../../content-writing/references/direct-marketing-ethics-filter.md) and `anti-ai-slop`. Withhold any line that fails the ethics filter; correct and rerun the screen.
6. Fit copy to formats: per-format limits from the register (checked 2026-09-23) or a "check current spec" flag; proof in the first frame or first line; one CTA.
7. Shortlist the top three per test cell and hand them to `ad-testing-and-scaling` with the hypothesis for each.
8. Record claims and their evidence in the claim register; deliver the copy deck with approval status.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Offer block (4–6 short paragraphs or bullet form) | Client commercial owner, copywriter | Promise, proof, sweetener, risk reversal and reason-why are all present and true |
| Headline and hook bank by mechanism | Creative lead, media buyer | At least five per mechanism; each screened; top three per cell marked |
| Format-fitted ad copy set | Media buyer, designer | Fits the stated limits or carries a "check current spec" flag; one CTA per ad |
| Claim register | Approver, legal/market gate | Every claim links to evidence and a date, or is removed |
| Test hand-off note | `ad-testing-and-scaling` | Hypothesis, variable and success metric per variant |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Screening record | Table: line, mechanism, tests passed, decision | No shortlisted line fails the ethics filter |
| Claim register | Table: claim, evidence, date, owner | Evidence is current (within 12 months) or the claim is dropped |
| Spec source note | Register claim ID and date, or "check current spec" | No invented character limit or dimension |

## Capability and Permission Boundaries

Read and search the brief, proof material and register. Writing and screening copy is drafting work. Uploading ads, editing live campaigns, publishing, sending messages or committing budget requires explicit client authority. Personal data in testimonials needs recorded consent.

## Degraded Mode

If offer facts, proof or current specs are unavailable, return the narrowest useful qualified copy: benefit-led variants without offer or proof lines, flagged `not assessed`, plus the list of evidence needed. Never fill gaps with invented numbers, quotes or deadlines.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Offer is unclear or weak | Fix the offer before writing headlines | Polishing copy on a deal nobody wants |
| Cold audience (unaware or problem-aware) | Lead with the problem, story or proof; no hard offer first | Wasted impressions and early fatigue |
| Warm or retargeting audience | Lead with the specific offer, objection answer or testimonial | Repeating awareness copy to ready buyers |
| Pun or clever line without a benefit | Test it only against a plain benefit line; never ship it untested | Lower response from a line nobody understands |
| Scarcity, deadline or "new" not literally true | Remove it | Consumer-protection breach and lost trust |
| Testimonial lacks consent or attribution | Do not use it; never put quotation marks around your own words | Misleading endorsement |
| Premium or corporate audience | Keep the structure; drop hype register (capitals, triple exclamation marks, "get rich") | Damaging premium positioning |

## Quality Standards

- Offer and proof before cleverness; specific beats general ("37 bookings in 9 days" only from verified data).
- One message and one CTA per ad; the headline could run alone as a classified ad and still pull.
- Every price shown with its terms; discounts show old price, new price and saving together.
- Understatement for premium and B2B audiences; warmer urgency only where it is real.
- British English; UGX by default; local place names only when true.
- Apply `anti-ai-slop` in real time and the ethics filter before any shortlist.

## Anti-Patterns

- Opening with the company name or "From the desk of…". Fix: open with the reader's outcome or pain.
- Testimonials at the end, vague ("Great service!"). Fix: specific, consented, attributed results early.
- Fake countdowns or "only 3 left" with no stock limit. Fix: real deadline with its reason, or no deadline.
- Writing the headline last and fast. Fix: generate 50+ candidates, incubate, test the top three.
- Tool language to owners ("We do SEO, PPC, SMM"). Fix: outcome language (calls, bookings, orders).
- Borrowing a competitor's exact words. Fix: swipe the idea's structure, never the words.
- Specific benefit that shrinks the audience unintentionally. Fix: test intrigue against specificity.

## References

- [Headline and hook families](references/headline-and-hook-families.md) — read for every headline sprint and hook bank.
- [Offer, proof and guarantee kit](references/offer-proof-and-guarantee-kit.md) — read before copy when the offer or proof is weak.
- [Format copy fitting](references/format-copy-fitting.md) — read when fitting copy to search, social, radio, OOH and WhatsApp formats.
- [Direct-marketing ethics filter](../../content-writing/references/direct-marketing-ethics-filter.md) — mandatory screen.
- [Creative brief and big idea](../creative-brief-and-big-idea/SKILL.md); [ad testing and scaling](../ad-testing-and-scaling/SKILL.md); [caption writer](../../content-writing/caption-writer/SKILL.md); [direct-response funnel copy](../../content-writing/direct-response-funnel-copy/SKILL.md).
<!-- dual-compat-end -->

## Craft notes

### Awareness-matched openings

| Awareness | Lead with | Example slot |
|---|---|---|
| Unaware | Story or striking observation | "Most [audience] lose [thing] before they even [action]." |
| Problem-aware | Name the pain precisely; not their fault | "If [specific pain] keeps happening at your [business], it isn't your fault." |
| Solution-aware | Mechanism and proof | "Here's how [n] [peers] in [town] fixed [problem] in [time]." |
| Product-aware | Offer, guarantee, reason to act now | "Until [date], [offer] — because [true reason]." |
| Most aware | Direct offer and CTA | "[Product], [price], delivered in [place] within [time]." |

### Choosing the first thing the reader meets

Open with whichever the buyer values most right now: the offer itself, a customer's verified result, the loss they are trying to avoid, or the gain they want. Losses usually weigh more than equal gains, so test a loss-led opening against a gain-led one. Openings can be combined — for example a customer result, then the loss it removed, then the offer.

### Reading-path devices for longer primary text and radio scripts

The first sentence exists to get the second read. Use bridges ("Here's why this matters…", "But consider this…"), short connective fragments, and a skim path where the first line of each block carries the story. Close the loop by returning to the opening benefit in the last line.

### Premium register adjustment

Keep the direct-response structure (offer, proof, specificity, risk reversal); drop the carnival register. Kampala and Nairobi corporate buyers read hype as unprofessional.

Before → after:
- "Buy now! Limited offer!!!" → "The June price holds until 30 June because our print run closes that week."
- "Our product is the best on the market." → "Tested against [n] competitors by [independent body]; results on our website."
- "Welcome to XYZ, a leading provider of innovative marketing solutions." → "Kampala retailers we work with get [verified figure] more WhatsApp orders in 90 days. Here's the method."

### East Africa notes

- Click-to-WhatsApp opening messages: short, specific, low effort ("Hi, I'd like a quote for [service] in [area]").
- Radio: say the WhatsApp number twice and name the station in the CTA only when it helps recall; state prices in UGX words and numerals for clarity.
- Local-language variants are transcreated by fluent reviewers (`swahili-native-copy`, `french-native-copy`, `east-african-english`), not machine-translated.

## Sources

- Serling, B. (ed.) (2002) *How to Write Million Dollar Ads, Sales Letters & Web Marketing Pieces*, The Internet Marketing Center — contributors include Caples (via Halbert), Bly, Vitale, Kennedy, Nicholas, Petersen, Voiles, Eker, Gage, Hauptman.
- Wiebe, J. (2011) *Copy Hackers: 6 Persuasion Strategies*, Copy Hackers — price timing and discount display.
- Stutts, P. (2021) *The Undefeated Marketing System*, Scribe — comparative ("punch up") rules.

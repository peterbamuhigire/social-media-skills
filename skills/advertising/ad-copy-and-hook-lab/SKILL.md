---
name: ad-copy-and-hook-lab
description: 'Use when a paid ad needs its words: headlines, video hooks, primary text, offers, proof and guarantees for Meta, TikTok, Google search, radio or outdoor; produces a headline and hook bank, fitted ad copy and a claim register; not for organic post captions (use `caption-writer`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Ad Copy and Hook Lab

Generates, screens and tests advertising copy from an approved brief for the creative lead and media buyer: offer first, proof early, one message, headline and hook mechanisms, and an ethics filter that removes classic direct-response tricks that are now unlawful or off-brand.

<!-- dual-compat-start -->
## Use When

- The concept is approved and the ads now need headlines, opening hooks, primary text, descriptions, calls to action or end-card lines.
- We need a bank of headlines with the three strongest marked for testing.
- The offer feels weak: build the promise, proof, sweetener, risk reversal and a genuine deadline before any copy is written.
- Our current ads are not converting; diagnose the copy for a weak hook, a buried offer, missing proof or claims we cannot back.
- Responsive search ad assets, lead-form wording or click-to-WhatsApp opening messages need writing.

## Do Not Use When

- `caption-writer` for organic captions and community posts.
- `creative-brief-and-big-idea` when there is no approved brief or platform idea yet.
- `direct-response-funnel-copy` for long-form sales letters, VSLs or funnel sequences.
- Stop when a claim cannot be substantiated or a regulated category is unchecked; return the claim register to the legal/market release gate.

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

| Artefact | Consumer | Acceptance condition |
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

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Writing and screening copy from the brief, proof material and register is drafting work; uploading ads, editing live campaigns or sending messages is not, and personal data in testimonials needs recorded consent.

## Degraded Mode

Without verified offer facts, proof or current specs, return the narrowest qualified result and mark the affected checks `not assessed`. Benefit-led variants without offer or proof lines can still be delivered, with the list of evidence needed; never fill gaps with invented numbers, quotes or deadlines.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Offer is unclear or weak | Fix the offer before writing headlines | Polishing copy on a deal nobody wants |
| Cold audience (unaware or problem-aware) | Lead with the problem, story or proof; no hard offer first | Wasted impressions and early fatigue |
| Warm or retargeting audience | Lead with the specific offer, objection answer or testimonial | Repeating awareness copy to ready buyers |
| Pun or clever line without a benefit | Test it only against a plain benefit line; never ship it untested | Lower response from a line nobody understands |
| Scarcity, deadline or "new" not literally true | Remove it | Consumer-protection breach and lost trust |
| Testimonial lacks consent or attribution | Do not use it; never put quotation marks around your own words | Misleading endorsement |
| Video ad script or AI-generated variants in the set | Run the ABCD check and the AI provenance and disclosure rule in [ABCD video craft and AI volume](references/abcd-video-craft-and-ai-volume.md) | Late branding, no call to action, or undisclosed synthetic creative |
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

- [Headline and hook families](references/headline-and-hook-families.md): read when running a headline sprint or building a hook bank.
- [AI transparency and provenance](../../policies/policy-ai-content-ethics/references/ai-transparency-and-provenance.md): read when generated variants include synthetic people, voices or realistic scenes that may need a label (§3, §6).
- [Offer, proof and guarantee kit](references/offer-proof-and-guarantee-kit.md): read when the offer or proof is weak, before any copy.
- [ABCD video craft and AI volume](references/abcd-video-craft-and-ai-volume.md): read when writing video hooks and end cards, or producing many variants with AI tools.
- [Format copy fitting](references/format-copy-fitting.md): read when fitting copy to search, social, radio, OOH and WhatsApp formats.
- [Craft notes and sources](references/craft-notes-and-sources.md): read when matching the opening to awareness, writing longer primary text or radio scripts, adjusting to a premium register or adapting for East Africa.
- [Direct-marketing ethics filter](../../content-writing/references/direct-marketing-ethics-filter.md): read when screening every candidate line (mandatory screen).
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting any client-facing line.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when a claim, testimonial or regulated category needs clearance.
- [Creative brief and big idea](../creative-brief-and-big-idea/SKILL.md): read when there is no approved brief.
- [Ad testing and scaling](../ad-testing-and-scaling/SKILL.md): read when handing the shortlist over for testing.
- [Caption writer](../../content-writing/caption-writer/SKILL.md) and [direct-response funnel copy](../../content-writing/direct-response-funnel-copy/SKILL.md): read when the job is organic captions or long-form funnel copy.
<!-- dual-compat-end -->

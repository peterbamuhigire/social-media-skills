---
name: biz-dev-video-outreach
description: Use when Personalised Video Audit Outreach is needed to produce a video outreach deliverable for social-media or digital-marketing work; use `biz-dev-positioning` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Personalised Video Audit Outreach

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **video outreach deliverable** and the supplied brief falls within personalised video audit outreach.

## Do Not Use When
- Use `biz-dev-positioning` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Commercial brief, target buyer, offer, proof and requested next step | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified video outreach deliverable; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Buyer problem, proof strength and commercial objective align | Choose the offer and proof sequence that supports the requested buying decision. | A generic sales asset with unsupported claims or the wrong ask. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact video outreach deliverable, consumer, market, channel and approval boundary; route to `biz-dev-positioning` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete video outreach deliverable; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Video outreach deliverable | Requester, client reviewer or delivery team | The video outreach deliverable addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
| Decision and gap note | Approver or next workflow | Names the chosen route, evidence used, unresolved inputs and any action requiring authority. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Source/assumption register and completed release checklist | Inline table, checklist or linked source note | Every material claim, decision and unavailable check is traceable. |

## Quality Standards
- Preserve the domain guidance and East African market context below; replace it only when the requester names another market.
- Use British English unless the target language or market requires otherwise, and verify names, figures, quotations and platform rules before use.
- Make the key choice visible, cover failure and edge cases, and keep the result ready for its named consumer.
- Run the repository's `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested video outreach deliverable, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [biz-dev-positioning](../biz-dev-positioning/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

> **Why this works:** Every prospect assumes agencies send generic pitches.
> A 3-minute screen recording of their own website, Facebook Page, or
> Instagram account — narrated with specific observations — signals three
> things immediately: this person has looked at my business, they know
> something I do not, and they are not asking for anything yet. The
> response rate to personalised video audits is 5–10x higher than a
> cold email (Fihn, 2025). Conversion rate: approximately 1 paying client
> per 10 videos sent.

## Required Input
Ask for the following before generating the audit script:

1. **Prospect business name and industry** — trading name and sector
2. **Country / city** — defaults to Uganda/Kampala if not specified
3. **Prospect's digital presence to audit** — provide the URL(s) or
   handle(s): website, Facebook Page, Instagram, Google Business
   Profile, or WhatsApp Business number
4. **What you have observed** — list 2–3 specific things you noticed
   about their digital presence (gaps, missed opportunities, or quick
   wins). If you have not audited them yet, the skill will prompt you
   through the audit framework
5. **Your proposed improvement** — what one thing could be improved
   in 7–10 days with immediate results?
6. **How you will send the video** — email (Loom link), WhatsApp
   (voice note or video message), or LinkedIn message
7. **Any existing relationship** — is this a cold prospect, a referral
   from a mutual contact, or someone who has engaged with your content?

## Section 1 — The Pre-Video Audit Framework
Complete this checklist before recording. Each item takes under 2
minutes. Review the prospect's presence across whichever platforms
they use.

**Facebook Page audit (2 minutes):**
- [ ] Does the Page have a complete About section with WhatsApp number?
- [ ] Is the CTA button set to the right action (WhatsApp / Book Now)?
- [ ] When was the last post? How often are they posting?
- [ ] Are comments going unanswered?
- [ ] Is the cover photo current and does it include a CTA?
- [ ] Is there a pinned post with an offer or welcome message?

**Instagram audit (2 minutes):**
- [ ] Does the bio describe what the business does and for whom?
- [ ] Is there a keyword in the username or display name?
- [ ] Is the link-in-bio set up and current?
- [ ] When was the last post? Are there any Reels?
- [ ] Do they respond to comments?
- [ ] Are Highlights set up with covers?

**Website audit (2 minutes):**
- [ ] Does the homepage load in under 3 seconds on mobile?
- [ ] Is there a clear above-the-fold CTA?
- [ ] Is there a WhatsApp chat widget?
- [ ] Is the contact information easy to find on the first screen?
- [ ] Is there social proof (testimonials, reviews, logos)?

**Google Business Profile audit (1 minute):**
- [ ] Does a GBP listing exist and is it claimed?
- [ ] Are there recent reviews? Are they responded to?
- [ ] Are the opening hours and description up to date?
- [ ] Are there photos uploaded?

**The golden rule of video audits:** identify only 2–3 observations.
More than 3 is overwhelming and signals that you are listing problems
rather than demonstrating expertise. Choose the 2–3 that are most
impactful and most fixable in a short campaign.

## Section 2 — The Video Audit Script
Generate a narration script based on the observations from Section 1.
This is spoken, not read aloud — write it in natural spoken language.

**Video structure (3–5 minutes total):**

**Opening (20 seconds)**
> "Hi [First Name], my name is [Your Name] — I'm a social media and
> digital marketing consultant. I was doing some research and came
> across [Business Name], and I noticed a few things that I think
> could make a real difference for you quickly. I'm going to do a
> quick 3-minute walkthrough — nothing to buy, no commitment needed.
> I just thought it was worth sharing."

[Begin screen share of their Facebook Page / website / Instagram]

**Observation 1 — The Quick Win (60–90 seconds)**
Choose the improvement with the most immediate impact and the
simplest fix. Lead with the positive:
> "First — I want to say, [genuine compliment: 'your product photography
> is excellent' / 'your reviews are really strong' / 'I can see you've
> built a good community here']. That's a real asset.
>
> The thing I noticed is [specific observation]. For example, when I
> tried to message you, I couldn't find a WhatsApp number. On this
> button here — [click it on screen] — it takes me to a form rather
> than straight to a conversation. In Uganda, most customers won't
> fill a form; they'll just move on to a competitor who has a WhatsApp
> link. That's a 5-minute fix that could meaningfully change how many
> enquiries come through."

**Observation 2 — The Opportunity (60–90 seconds)**
The second observation should be slightly larger — a missed opportunity
rather than a broken element:
> "The second thing I noticed is [observation]. I'm looking at your
> last 30 posts — [scroll through] — and there's really strong content
> here. But there are no Reels. Reels are how Instagram shows your
> content to people who don't already follow you. Everything you're
> posting right now is only reaching your existing followers. A simple
> Reel — even filmed on a phone — would open this up to a much wider
> audience. I've seen accounts in [their industry] in Kampala double
> their enquiries in 30 days just from adding 2 Reels a week."

**Observation 3 (optional) — The Untapped Asset (30–45 seconds)**
Only include if there is a clear third insight. Do not force it:
> "One more thing — and this is the one I find most businesses don't
> realise. You have [X followers / X past customers / a WhatsApp
> database]. That's a warm audience that already knows and trusts you.
> Most businesses advertise to strangers when the easiest revenue is
> from people who've already bought from them. There's a specific
> campaign type that works very well here."

**Close (30 seconds)**
> "That's it — those are the three things I'd look at first. I have
> a specific idea for a test I'd like to run for you to address
> [Observation 1 or 2] — it's a 7-day exercise, no upfront cost, and
> you can see whether it's worth a longer conversation. Would it be
> useful if I sent you a one-page outline?
>
> No pressure either way — happy to answer questions too. Thanks for
> your time."

## Section 3 — The Outreach Message (Sent With the Video)
Generate this short message to accompany the video link. Keep it under
5 lines. The video does the work — the message is just a delivery
wrapper.

**Email version:**
> Subject: Quick video on [Business Name] — 3 minutes
>
> Hi [First Name],
>
> I noticed a few things on [their platform] that I thought were worth
> sharing — recorded a short walkthrough: [Loom link]
>
> Takes 3 minutes. No ask, no pitch.
>
> [Your name]

**WhatsApp version:**
> *"Hi [First Name], I'm [Your Name] — a social media consultant. I
> noticed a couple of things on your [Facebook / Instagram / website]
> that could help you get more enquiries. I made a short video —
> 3 minutes — would it be OK to send it over?"*

Note: always ask permission before sending a video on WhatsApp — it
signals respect and dramatically increases the likelihood the video
is watched. Send the video only after they reply "yes."

**LinkedIn version:**
> "Hi [First Name] — I was researching [industry] businesses in
> [city] and came across [Business Name]. I put together a 3-minute
> video with two or three observations about your online presence.
> Not pitching anything — just thought it was genuinely worth sharing.
> Happy to send it if you're open to it."

## Section 4 — Follow-Up Sequence
Send these follow-up messages if there is no response after the video
is sent. Maximum 2 follow-ups.

**Follow-up 1 (Day 3):**
> "Hi [First Name] — just checking you received the video. Totally
> fine if it's not a fit. Just want to make sure it reached you."

**Follow-up 2 (Day 7):**
> "Hi [First Name] — last message from me on this. I've since worked
> with [describe a similar business anonymously: 'a Kampala salon' /
> 'an NGO in Nairobi' / 'a school in Entebbe'] and got [brief result:
> 'their enquiries doubled in 10 days']. If the timing is ever right,
> you know where to find me."

No third follow-up. Move on. A non-responder is a not-yet, not a no —
keep them in the awareness pipeline by posting useful content they
can find organically.

## Quality Criteria
Output meets the standard for this skill when:

- The video script is in natural spoken language (not formal written
  language) and can be delivered conversationally without reading
- Exactly 2–3 specific observations are identified from the pre-video
  audit framework — not more, not less
- Each observation names a specific element of the prospect's actual
  digital presence (not a generic critique of "most businesses")
- The close ends with a soft, low-commitment question — not a pitch
  or a request to book a call
- The outreach message versions for email, WhatsApp, and LinkedIn are
  all present and each is under 5 lines
- WhatsApp version asks permission before sending the video
- Follow-up messages are present, limited to two, and the second
  includes a brief third-party result for credibility
- British English throughout; no American spelling variants

## References
- Fihn, F. (2025) *Beyond the Agency Box: The Phoneless Meet*

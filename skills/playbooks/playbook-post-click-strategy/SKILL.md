---
name: playbook-post-click-strategy
description: 'Use when people click but do not buy: link-in-bio, WhatsApp click-to-chat, lead magnet delivery, mobile landing pages, post-click tracking, or a shop or WhatsApp enquiry path that loses buyers before payment; produces the conversion path audit and fix list; not for briefing a web team on a new page (use `ad-to-site-journey-handoff`).'
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Post-Click Conversion Strategy Playbook

Closes the post-click gap, the space between a follower seeing a post and taking a commercial action, which in East Africa is wider than in markets with high website penetration; every extra step between post and action reduces conversion.

<!-- dual-compat-start -->
## Use When
- Posts get clicks but few sales; the journey from social post to paid order needs reviewing.
- Fix the link-in-bio on Instagram or TikTok so every click lands somewhere useful.
- An ad or post opens a WhatsApp chat instead of a website and buyers drop off after the tap; fix the reply scripts and follow-up.
- Make WhatsApp the sales channel: click-to-chat links, pre-filled opening messages and a three-message qualification sequence.
- Deliver a lead magnet through social and track it with UTM parameters and conversion events.
- Work out why online-shop carts or WhatsApp enquiries do not become paid orders (Mobile Money, delivery, trust), win back abandoned enquiries and rank conversion tests.

## Do Not Use When
- `ad-to-site-journey-handoff` for the landing-page brief and tracking handover to website-skills.
- `social-commerce-strategy` for setting up catalogue, DM selling and Mobile Money checkout from scratch.
- `measurement-tracking-plan` for the full event map, consent mode and server-side tagging.
- Stop before changing a live shop, checkout or ad destination without the client's approval; deliver the audit and the ranked fixes.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client business name, industry, product or service and price point | Client brief | Yes | Ask; offer and price shape the qualifying question and lead magnet. |
| Country/city | Client | Yes | Default to Uganda; name the region if relevant (Nairobi, Dar es Salaam). |
| Primary goal: WhatsApp enquiries, form submissions, direct sales, email opt-ins or calls | Client owner | Yes | Default to WhatsApp enquiries and state the assumption. |
| Current conversion path: what happens when someone clicks today | Cold-start audit on a mobile device | Yes | Run the audit yourself; mark any step you cannot reach `not assessed`. |
| Website status and WhatsApp Business or personal WhatsApp | Client or web team | Yes | Plan for no website and a WhatsApp Business setup. |
| Primary platforms (Instagram, Facebook, TikTok, YouTube, WhatsApp Status) | Client | Yes | Audit Instagram, Facebook and WhatsApp Status first. |

## Workflow

1. Ask the intake questions in [post-click path method](references/post-click-path-method.md) and confirm the owner and approval boundary; stop if the goal or owner is missing.
2. Run the cold-start conversion path audit on a mobile device: bio link, top 10 posts' CTAs, a DM enquiry, a WhatsApp chat and any landing page; record every point where a real customer would abandon.
3. Complete the friction checklist and rank fixes in the priority order below.
4. Redesign the path with three steps or fewer: bio link choice, `wa.me` link with pre-filled message, three-message qualification sequence and WhatsApp Business setup.
5. Add a lead magnet with a delivery method and platform promotion, and a single-CTA, mobile-first landing page where one exists or is needed.
6. Define the conversion events, UTM parameters and `wa.me` click tracking, and what goes in the monthly report.
7. If traffic arrives but orders do not, apply [e-commerce and WhatsApp conversion diagnosis](references/ecommerce-and-whatsapp-conversion-diagnosis.md) one measurable test at a time.
8. Run the quality checks and the anti-slop gate; correct any failed item and rerun before handing over the audit and fix list.

## Priority fix order

1. Replace a broken or outdated bio link immediately.
2. Add a `wa.me` click-to-chat link as the primary or sole CTA.
3. Activate WhatsApp Business greeting and away messages.
4. Compress landing page images; test load time on 3G.
5. Add social proof (testimonials, photos) above the fold on the landing page.
6. Set up Bit.ly tracking on the WhatsApp link.
7. Introduce a lead magnet with a simple delivery mechanism.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Conversion path audit with completed friction checklist | Client owner | Each of the 10 checklist items is marked pass, fail or `not assessed` from a mobile, cold-start test. |
| Ranked fix list | Client owner and delivery team | Fixes follow the priority order and are specific to this client's broken path. |
| Redesigned conversion path per platform | Delivery team | Three steps or fewer from post to action; `wa.me` links carry a pre-filled message. |
| Lead magnet and landing-page recommendations | Delivery team | Delivery method named; page is mobile-first, single-CTA, with social proof above the fold. |
| Measurement plan and monthly report items | Client owner | Each tactic has at least one trackable signal. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Cold-start audit log | Table: step, what loaded, time taken, response time and quality | Each audit step is recorded from a real mobile test or marked `not assessed`. |
| Tracking set-up record | Table: event and how it is tracked | Every conversion event defined at the start has a named tracking method. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. A test DM or WhatsApp enquiry during the audit is sent only with the client's agreement.

## Degraded Mode

Without a mobile walk-through of the client's current path, return the narrowest qualified result and mark the affected checks `not assessed`. The friction checklist, a recommended path design and the tracking plan can still be delivered from the client's description.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| An advert promise is not repeated above the landing-page fold | Correct message match before sending traffic. | Paid clicks lost to confusion. |
| One product or service, WhatsApp primary | Put a direct `wa.me` click-to-chat link with pre-filled message in the bio. | Extra choices and lost enquiries. |
| Multiple services, no website | Use Linktree with 3–4 options maximum; update destinations inside it, never the bio URL. | Choice overload and broken saved links. |
| A TikTok account has under 1,000 followers and no bio link | Use "DM us" as the fallback exit and verbal or text-overlay CTAs. | A post with no route to conversion. |
| The client handles 50+ enquiries per day | Recommend the WhatsApp Business API through a provider (e.g., Twilio, Bird, Africa's Talking) for webhook tracking and CRM integration. | Untracked and unanswered leads. |
| Traffic exists but purchase or enquiry completion is weak | Apply the e-commerce and WhatsApp conversion diagnosis: find the highest-evidence friction, one measurable test at a time. | Changing brand strategy when the loss is in the transaction path. |
| An action publishes, spends, contacts people or changes production state | Require explicit approval before action. | Unauthorised external impact. |

## Quality Standards

- The strategy addresses the client's actual conversion gap identified at intake, not a generic template.
- Every recommended path has three steps or fewer between the social post and the completed action.
- WhatsApp is the default conversion channel unless the client has a specific reason otherwise; links use the correct `wa.me` format with pre-filled messages.
- Tool and platform recommendations match the client's website status and team size; free or low-cost options are offered for SME clients.
- Every tactic includes at least one trackable signal (Bit.ly clicks, form submissions, WhatsApp message count).
- All landing-page and link-in-bio recommendations are assessed against 3G load time and mid-range Android usability.
- The audit produces a prioritised list of fixes specific to the client, not a generic review.
- British English and EA market context throughout: pricing in UGX or KES as appropriate, platform defaults reflecting EA penetration, locally recognisable business types.

## Anti-Patterns

- A bio link to a homepage with no clear next step, or to an expired promotion. Fix: point it at the current offer or a `wa.me` link.
- "DM us" with no further instruction and no reply. Fix: give an explicit instruction and answer DMs within 1 business hour.
- A landing page that takes 12 seconds to load on 3G. Fix: compress images, drop video autoplay, keep scripts minimal and load in under 3 seconds.
- A personal WhatsApp number with no automated response to 2 am messages. Fix: set up WhatsApp Business greeting, away message, quick replies and catalogue.
- Several CTAs on one page, or forms with more than three fields. Fix: one button, one action, as few fields as possible.
- A Facebook page phone number without click-to-call. Fix: set the Page CTA button or add the `wa.me` link.
- Auditing on desktop. Fix: behave as a new customer on a mid-range Android phone.

## References

- [Post-click path method](references/post-click-path-method.md): read when asking intake questions, setting up link-in-bio, `wa.me` links, WhatsApp Business, lead magnets, landing pages, UTM and WhatsApp tracking, platform paths or the audit steps and friction checklist.
- [E-commerce and WhatsApp conversion diagnosis](references/ecommerce-and-whatsapp-conversion-diagnosis.md): read when an existing shop or WhatsApp sales path loses buyers before payment, or the client needs buyer modalities, test prioritisation, enquiry recovery or an e-commerce KPI dashboard.
- [`measurement-tracking-plan`](../../meta-analytics-ops/measurement-tracking-plan/SKILL.md): read for full UTM parameter conventions and a UTM builder template.
- [`ad-to-site-journey-handoff`](../../advertising/ad-to-site-journey-handoff/SKILL.md): read when a web team needs a landing-page brief.
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when writing captions, pre-filled messages and reply scripts.
- [East African English standard](../../language/east-african-english/SKILL.md): read when checking tone and local examples.
<!-- dual-compat-end -->

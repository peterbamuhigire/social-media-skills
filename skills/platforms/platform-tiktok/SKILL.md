---
name: platform-tiktok
description: Use when creating a Tiktok channel plan covering account setup, content, community and measurement for Uganda or East Africa. Use a playbook for cross-channel operations and a strategy skill for channel selection.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# TikTok Presence Plan

<!-- dual-compat-start -->
## Use When
- Create or revise a Tiktok-specific presence, growth or publishing plan.
- Translate a confirmed audience, offer and objective into channel decisions.

## Do Not Use When
- The task is cross-channel operating procedure; use the closest `playbook-*` skill.
- The task is choosing channels or business direction; use `strategy-channel-architecture`.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client objective, audience and offer | Approved brief or client interview | Yes | Stop and request the missing decision; do not invent it |
| Current account and content evidence | Native account export, screenshots or supplied audit | Conditional | Mark the account baseline unassessed and qualify recommendations |
| Current platform rules and feature limits | Official Tiktok help or policy source | Conditional | Omit volatile specifications or flag them for live verification |

## Capability and Permission Boundaries
Read supplied artefacts and search relevant evidence. Treat review, audit and planning as read-only. Editing the requested draft is allowed; publishing, messaging, production changes, personal-data processing, spending, destructive actions and certification claims require explicit authority. Use network access only for authorised verification.

## Degraded Mode
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Tiktok channel plan plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| A trend conflicts with the brand, audience or safeguarding duty | Skip it and use a native format built around the offer | Trend chasing that damages trust |
| Account is absent or not accessible | Produce a setup plan with assumptions labelled | False optimisation against invented history |
| Evidence shows an established account | Prioritise measured gaps and retained strengths | Destructive reset of working assets |
| A rule, limit or feature is time-sensitive | Verify against the official platform source before stating it | Stale platform advice |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply the decision rules, preserve useful existing material and draft the Tiktok channel plan.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Tiktok channel plan | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
| Assumption and gap register | Approver or next workflow | Every missing source, unassessed check and required approval has an owner or next action |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and verification record | Inline table or appendix | Each material choice traces to an input, source or labelled assumption |
| Release-gate result | Completed checklist | No blocking policy, factual, permission or anti-slop finding remains |

## Quality Standards
Use British English and the specified market context. Recommendations must be executable with the stated capacity, current claims must be verified or qualified, and acceptance conditions must be observable. A worked example must use a labelled scenario, not fabricated client evidence.

## Anti-Patterns
- Inventing a client fact, benchmark, budget or approval. Fix: cite the source or label the assumption and its effect.
- Copying one channel or client pattern unchanged. Fix: tie each choice to the named audience, objective and evidence.
- Stating volatile platform or legal details from memory. Fix: verify the current official source or omit the claim.
- Treating an inaccessible account, file or metric as healthy. Fix: mark it `not assessed` and bound the conclusion.
- Publishing, spending, messaging or changing production state from planning authority. Fix: obtain explicit action authority.
- Delivering actions without owner, timing or acceptance. Fix: assign all three or return the item as an unresolved gap.

## References
- [Anti-AI-slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- [East African English standard](../../language/east-african-english/SKILL.md)
- Use the directly cited sources and companion skills in the domain guidance below; verify time-sensitive claims before use.
<!-- dual-compat-end -->

## Required Input

Before generating this plan, collect the following from the client:

- **Client name** and trading name (if different)
- **Industry** and primary products/services sold
- **Country/city** (default: Uganda/East Africa)
- **Primary goal** (brand awareness / follower growth / direct sales / community building)
- **Target audience age range** (TikTok EA skews 16–30 — confirm if client's audience differs)
- **Tone** (serious / educational / entertaining / mix — be specific)
- **Posting frequency capacity** (how many videos can the client realistically produce per week?)
- **Existing TikTok account** stats if one exists (followers, average views, top videos)
- **Any content already produced** that can be repurposed

---

## EA Market Context

TikTok in Uganda and the wider East African market is growing fastest among 16–30 year olds. Entertainment, humour, and relatable everyday-life content consistently outperforms polished, corporate-style production. Authenticity is the primary differentiator — audiences in this market are acutely sensitive to content that feels scripted or inauthentic.

Most users consume TikTok on low-bandwidth mobile connections. Shorter videos (15–45 seconds) perform better for EA audiences than long-form content. Keep videos tight, front-load the value, and never pad for length.

---

## 1. Account Setup and Profile Optimisation

**Username**
Match the handle used on Instagram, Facebook, and X. Consistency across platforms makes the brand searchable and memorable. If the preferred handle is taken, add a location suffix (e.g. @BrandUG or @BrandKampala) rather than numbers.

**Profile Photo**
200×200px minimum. Use the brand logo or founder's face. Founder photos typically generate higher follow rates on TikTok because the platform is personality-driven.

**Bio**
80 characters maximum — no wasted words. Structure: hook (what you do) + value offer + one CTA.
Example: "Skincare for Ugandan skin 🌿 Tips every week. DM for orders."

**Link in Bio**
One link only. Use a link-in-bio aggregator (Linktree, Beacons, or a simple landing page) if multiple destinations are needed. Direct to the most important action: WhatsApp chat, website, or order form.

**Account Type**
Select Business account for access to analytics, commercial music library, and the ability to run ads in future. Creator accounts have access to the Creator Fund (not available in all EA markets as of 2024 — check current availability).

**Category Selection**
Choose the most specific category that accurately describes the business. Avoid broad categories like "Entertainment" unless that genuinely describes the account — specificity helps TikTok distribute content to the right audience.

**TikTok Shop**
TikTok Shop availability in East Africa is limited as of 2024. Check current rollout status before recommending. If not available, direct purchase enquiries to WhatsApp or website via the link in bio.

---

## 2. Content Strategy Philosophy

Apply these principles to every video produced for this account.

**Entertain first, inform second, sell third**
If the first 3 seconds of a video do not create a reason to keep watching, the video fails. TikTok's algorithm measures completion rate — videos that are skipped early are shown to fewer people.

**Authenticity over production quality**
A video shot on a smartphone in good natural light, with genuine energy, will outperform a polished studio production on TikTok. The platform's culture actively rewards realness. Do not wait for perfect conditions to post.

**Show, do not tell**
Demonstrate products in use. Show processes in real time. Show before and after. Narrating what you do is far less engaging than showing it happening.

**Teach something in every video**
Even pure entertainment content must leave the viewer with something — a feeling, an idea, a laugh, new information. Content that gives nothing is forgotten immediately.

**EA-specific authenticity cues**
Ugandan humour, relatable daily situations (matatu rides, market day, power cuts, mobile money), local-language cameos (Luganda phrases, Swahili expressions) increase engagement significantly. Use with genuine cultural awareness — not as a gimmick. If the brand voice does not naturally include local language, do not force it.

---

## 3. Video Structure Templates

Use these templates as the foundation for every video. Select the template that fits the content before scripting.

**Template A: Quick Value (15–30 seconds)**
For: tips, product showcases, quick demonstrations, reactions

- **0–3s — Hook:** Bold claim, surprising visual, or question on screen. Pair text overlay with action. Example: "This one mistake is costing Ugandan businesses customers every day."
- **3–15s — Deliver:** Give the value fast. No preamble, no "welcome back to my channel." Get straight to it.
- **15–25s — CTA:** One specific action. "Follow for more tips." "Link in bio to order." "Comment your question."

**Template B: Story Arc (30–60 seconds)**
For: brand story, customer journeys, before/after, founder moments, day-in-the-life

- **0–3s — Hook:** What happened or what was discovered. "I almost shut down my business last year. Here's what saved it."
- **3–40s — Story:** Problem → turning point → result. Keep cuts frequent (every 4–6 seconds) to maintain attention.
- **40–55s — Lesson:** The takeaway. What should the viewer do or think differently?
- **55–60s — CTA:** Follow, share, comment, or click link.

**Template C: Educational Series (45–90 seconds)**
For: tutorials, how-to guides, step-by-step processes, myth-busting

- **0–3s — Hook:** State the problem or question. "Three steps to [outcome] that actually work in Uganda."
- **3–15s — Context:** Why this matters. One sentence on the problem, one on the stakes.
- **15–60s — Steps:** One step per cut. Vary the visual with each step — cut to a close-up, change angle, use text overlay for the step number. Variation prevents scroll-off.
- **60–80s — Summary and CTA:** Recap the steps in one sentence. One CTA.

---

## 4. Content Series Concepts

Repeatable series build a return audience. Viewers come back for the next episode. This is the most effective organic growth strategy for business accounts on TikTok. Generate 4–5 series concepts that fit the client's industry.

**Structure for each series entry below:**
Series name / Concept / Template / Frequency / First 3 episode ideas

---

**Series 1: "[Industry] in 30 Seconds"**
Concept: One industry insight, tip, or fact delivered in under 30 seconds — fast, punchy, and shareable.
Template: A (Quick Value)
Frequency: Weekly (every Tuesday)
Episodes:
1. The single biggest mistake [target customer] makes when buying [product/service]
2. How to spot a quality [product] vs. a cheap imitation — what to look for
3. Why [common industry practice] is actually costing you money

**Series 2: "A Day in the Life"**
Concept: Unscripted, behind-the-scenes look at how the business operates — from sourcing to delivery.
Template: B (Story Arc)
Frequency: Fortnightly
Episodes:
1. 5am market run — what goes into sourcing the day's stock
2. How we handle a large order from start to finish
3. What happens when something goes wrong — an honest day

**Series 3: "Ask [Business Name]"**
Concept: Answer one real customer question per video. Source questions from WhatsApp, DMs, and comments.
Template: A or C depending on complexity
Frequency: Weekly (every Thursday)
Episodes:
1. "How long does delivery take?" — the honest answer + why it varies
2. "Is [product] suitable for [specific concern]?" — full explanation
3. "What's the difference between [Option A] and [Option B]?" — side-by-side comparison

**Series 4: "Before and After"**
Concept: Show the transformation — product use, business process, customer results. No narration needed; visual storytelling only.
Template: B (Story Arc)
Frequency: Weekly (every Saturday)
Episodes:
1. Product transformation: raw materials to finished product
2. Customer result: before using service vs. after
3. Workspace transformation: setup, production, delivery

**Series 5: "[Number] Things You Didn't Know About [Industry]"**
Concept: Surprising or counterintuitive facts that challenge assumptions. High share potential.
Template: C (Educational)
Frequency: Fortnightly
Episodes:
1. 3 things Ugandan consumers don't know about [product category]
2. Why [popular belief about the industry] is actually a myth
3. The one ingredient / step / detail that separates good from great [product/service]

---

## 5. Sound and Music Approach

**Trending sounds**
Using trending audio increases TikTok's algorithmic distribution. A video using a trending sound is pushed to the sound's existing audience as well as the account's followers. Check the Discover tab weekly to identify trending sounds. Match the mood — do not apply a comedy audio track to a serious topic.

**Original audio**
Original voice-over and in-video audio is better for brand recall and for tutorials, explainers, and testimonial content. Original audio also builds a catalogue that other creators can use — a small but compounding reach multiplier.

**Process for sound selection**
Check trending sounds weekly. Test 2–3 different sounds per month on similar content types. Note which sound-content combinations produce the highest completion rates and replicate. Do not recommend specific tracks — these change weekly and any list produced here will be outdated within days.

**Captions**
Add captions to every video. A significant proportion of TikTok videos are watched with sound off, particularly in public spaces. EA mobile users frequently watch videos on silent in shared spaces. Use TikTok's auto-caption feature and review for accuracy before posting.

---

## 6. Duet and Stitch Content Ideas

**Duet**
Displays two videos side-by-side simultaneously. Use for:
- Reacting to relevant industry news or viral content in the client's topic area
- Adding expert commentary to a popular video about the industry
- Joining a trending format while keeping it relevant to the brand

**Stitch**
Clips the first 5 seconds of another video into the start of yours. Use for:
- Answering common questions that a popular video raised but did not fully address
- Debunking industry myths that are circulating on the platform
- Adding a local (Ugandan/EA) perspective to a global trend or topic

**Three specific Duet/Stitch ideas (adapt for client's industry)**

1. **"They said [common misconception about the industry] — here's the truth"** — Stitch a video that repeats the misconception, then provide the correct information with evidence.

2. **"This is what it looks like in Uganda"** — Duet with international content showing the same product, service, or process, contrasting it with the local version. Celebrates local context rather than positioning it as inferior.

3. **"Answering the question [popular creator] didn't answer"** — Stitch a video in the topic area that raised a question relevant to the client's expertise and provide a complete, practical answer.

---

## 7. Posting Frequency Guide

| Growth phase | Followers | Frequency | Notes |
|---|---|---|---|
| Launch / Growth | 0–5,000 | 1–2 videos per day, 7 days/week | Volume is the primary growth lever at this stage. Quantity teaches the algorithm what the account is about. |
| Steady growth | 5,000–50,000 | 1 video per day, 6 days/week | Begin prioritising quality. Maintain one rest day. |
| Maintenance | 50,000+ | 4–5 videos per week | Consistency matters more than frequency at this stage. |

**Critical note on consistency**
TikTok's algorithm penalises posting gaps more harshly than other platforms. Missing 3+ consecutive days in the early growth phase resets distribution momentum. It is better to post one lower-quality video per day than to skip a day waiting for a high-quality video to be ready.

---

## 8. 30-Day Video Content Plan

Post 4 videos per week across Weeks 1–4 (minimum). Adjust frequency based on the client's production capacity.

| Week | Day | Series / Content type | Hook (first 3 seconds) | Video concept | CTA | Template |
|---|---|---|---|---|---|---|
| 1 | Mon | Account launch / brand intro | "We've been in [industry] for [X years]. Here's what we've learned." | Founder introduces the business, who it serves, and what the TikTok will cover. Keep under 30 seconds. | Follow for tips every week | B |
| 1 | Wed | [Industry] in 30 Seconds — Ep. 1 | "[The biggest mistake our customers make] — and how to avoid it." | One specific, actionable tip. No padding. | Comment if this happened to you | A |
| 1 | Fri | Before and After — Ep. 1 | Text on screen: "Watch this." Visual opens on the before state. | Show a product transformation, service result, or workspace reveal. Silent or minimal narration. | Follow to see next week's transformation | B |
| 1 | Sat | Ask [Business Name] — Ep. 1 | "You asked: '[Real customer question].' Here's the real answer." | Answer one genuine customer question with full context. | Send your question — link in bio | A |
| 2 | Tue | [Industry] in 30 Seconds — Ep. 2 | "Most people in Uganda don't know this about [product/service]." | Surprising or counterintuitive industry fact with a practical takeaway. | Save this for later | A |
| 2 | Thu | Day in the Life — Ep. 1 | "5am. [Location]. Here's how [Business Name] starts the day." | Behind-the-scenes of a key operational moment — sourcing, prep, or production. | Follow to see more of this | B |
| 2 | Fri | Before and After — Ep. 2 | "Same [product/service]. Two completely different results. Here's why." | Contrast high-quality vs. low-quality execution. Educational framing. | Share with someone who needs to see this | B |
| 2 | Sun | Things You Didn't Know — Ep. 1 | "3 things I wish I knew before starting in [industry]." | Three fast, honest insights. One cut per insight. | Comment the one that surprised you most | C |
| 3 | Mon | Ask [Business Name] — Ep. 2 | "[Question from comments or DMs]? Great question." | Pull the question from real engagement — name the person if they consent. | Drop your question below | A |
| 3 | Wed | [Industry] in 30 Seconds — Ep. 3 | "This one detail separates a good [product] from a great one." | Deep-dive on quality indicator. Practical and visual. | Follow for weekly quality tips | A |
| 3 | Fri | Day in the Life — Ep. 2 | "What happens when an order goes wrong — honest version." | Show a real challenge and how it was resolved. Vulnerability builds trust. | Comment if this has happened to you | B |
| 3 | Sat | Stitch / Duet — industry reaction | Text: "They said [claim]. Here's the truth." | Stitch or Duet with relevant content. Provide the expert counter-perspective. | Follow for more honest takes | A |
| 4 | Tue | Things You Didn't Know — Ep. 2 | "Why [common industry belief] is actually wrong." | Myth-busting format. Three myths, one per cut, with brief correction. | Share this with someone who believes this | C |
| 4 | Thu | Before and After — Ep. 3 | "30 days ago vs. today — the difference [product/service] makes." | Customer result or business milestone. Use real data or real customer permission. | DM us to get started | B |
| 4 | Fri | Ask [Business Name] — Ep. 3 | "Our most asked question this month — answered properly." | Consolidate 3 related questions into one educational video. | Save this. You'll need it. | C |
| 4 | Sun | Month-end recap / CTA | "One month on TikTok. Here's what we learned." | Honest reflection on the first month. What performed, what did not. Invite the audience in. | Follow to come with us on this | B |

---

## 9. TikTok-specific KPIs

Track weekly in a spreadsheet for the first 90 days. Review monthly thereafter.

| KPI | Target / Benchmark | Signal |
|---|---|---|
| Video views | Baseline in Week 1; target 20% growth per month | Raw reach |
| Completion rate | 40%+ for videos under 30 seconds; 25%+ for videos over 30 seconds | Content quality and hook effectiveness |
| Follower growth | Track weekly; acceleration indicates a viral or high-performing video | Audience building |
| Profile visits | Track weekly; high profile visits with low follows signals a weak bio or CTA | Intent measurement |
| Link clicks (bio) | Track monthly; set a baseline in Month 1 | Commercial intent |
| Shares | Any content with a share rate above 5% of views is high-performing — make more like it | Highest-value virality signal |
| Comments | Quality signal — are comments questions, praise, debate, or spam? Engage with every comment in the first 30 minutes after posting | Community health |
| Saves | Strong intent signal — saved content is reviewed again. High saves on educational content signals strong topic relevance | Content utility |

---

## Quality Criteria

Output from this skill meets the standard when it:

- Every section contains specific, actionable guidance — no placeholders and no instructions to "add your content here"
- The 30-day content plan includes a complete hook, video concept, CTA, and template reference for every entry
- Content series concepts include the first three episode ideas in enough detail that a content creator could start producing without further briefing
- Video structure templates are written in production-ready language that a non-expert videographer can follow from the first day
- EA market context (mobile-first consumption, Ugandan cultural references, low-bandwidth considerations, 16–30 demographic) is reflected throughout — not added as a footnote
- KPI targets are realistic and benchmarked — completion rate, share rate, and follower growth targets are based on platform norms, not aspirational figures
- The strategy is consistent with the client's stated posting frequency capacity — a client who can produce two videos per week receives a plan built for two videos per week, not five
- The authenticity-first philosophy is evident in the content series and video structure guidance — the skill does not recommend polished, corporate-style content for an EA TikTok audience

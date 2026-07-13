---
name: meta-algorithm-guide
description: "Use when building or refreshing a platform-ranking reference from current evidence. Produces platform algorithm guide and pre-publication checklist; use `meta-posting-optimisation` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Platform Algorithm Guide — Organic Reach Reference

> **Scope:** This is an operational reference document, not a strategy document. It covers ranking signals, penalised behaviours, favoured formats, and posting benchmarks for the six primary platforms used in the East African market. Use the pre-publication checklist (Section 8) before every post. For platform-specific strategy, use the relevant `platform-*` skill.

---


<!-- dual-compat-start -->
## Use When

- Use this skill for building or refreshing a platform-ranking reference from current evidence.
- Confirm that `meta-posting-optimisation` is not the closer route before proceeding.

## Do Not Use When

- Use `meta-posting-optimisation` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Dated first-party platform guidance and account analytics | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Platform algorithm guide and pre-publication checklist | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. This is read-only by default: inspect and report without changing source records, accounts, skills or campaigns. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified platform algorithm guide and pre-publication checklist. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Dated first-party platform guidance and account analytics is current and attributable | Produce the full platform algorithm guide and pre-publication checklist and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `meta-posting-optimisation` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `meta-posting-optimisation` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the platform algorithm guide and pre-publication checklist, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the platform algorithm guide and pre-publication checklist without dated first-party platform guidance and account analytics. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `meta-posting-optimisation` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified dated first-party platform guidance and account analytics, the skill produces a platform algorithm guide and pre-publication checklist with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`meta-posting-optimisation`](../meta-posting-optimisation/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Input

Before generating this guide for a specific client or team, collect the following:

- **Client business name** — trading name as it appears on social profiles
- **Industry** — sector and sub-sector (e.g. retail: fashion boutique)
- **Country / city** — default: Uganda / Kampala
- **Primary goal** — organic reach growth / engagement rate improvement / content team training / reach recovery after algorithm drop
- **Active platforms** — list every platform the client currently posts on
- **Current posting frequency per platform** — how many times per week on each
- **Primary content format** — video / photo / text / mixed
- **Team size** — solo operator, small team (2–4), or agency setting

---

## 1. How Social Media Algorithms Work — Core Principles

Every major platform uses a machine-learning ranking system that predicts whether a given user will engage with a given piece of content. The algorithm is not a fixed rulebook — it is a probability engine trained on billions of interactions. However, consistent signals influence rankings across all platforms.

**Universal ranking signals (all platforms):**

| Signal | What it measures |
|---|---|
| Completion rate | Did users watch/read to the end? |
| Saves / bookmarks | High-intent signal — user wants to return |
| Shares / re-shares | Distribution signal — user vouches for the content |
| Comments (meaningful) | Conversation signal — not emoji-only |
| Likes / reactions | Weakest signal but still counted |
| Profile click-throughs | Interest in the creator beyond the post |
| Dwell time | How long a user paused on the post |

**Principle:** Platforms serve content that keeps users on the platform. Any format or behaviour that achieves this is rewarded. Any format or behaviour that drives users away is penalised.

---

## 2. Per-Platform Algorithm Ranking Signals

### 2.1 Facebook

Facebook uses a feed ranking model that weighs four primary factors: inventory (all eligible posts), signals (engagement data), predictions (likelihood a user engages), and relevance score.

**Key ranking signals:**

| Signal | Weight | Notes |
|---|---|---|
| Meaningful interactions | High | Comments and shares outweigh likes |
| Video completion | High | Native video watched past 60 seconds strongly rewarded |
| Post type relevance | High | Facebook learns what format each user engages with |
| Recency | Medium | Fresh content boosted within first 2–3 hours |
| Profile relationship | High | Pages with consistent interaction history ranked higher |
| Link posts | Low | Outbound links reduce reach — Facebook penalises posts sending users off-platform |

**Facebook-specific notes:**
- Facebook Groups posts reach further than Page posts in most niches — consider a community group as a supplementary owned channel.
- Stories do not appear in the main feed algorithm but reset daily and keep the page avatar at the front of the Stories bar.
- Reels on Facebook draw reach from both Facebook and Instagram inventory when cross-posted natively (not via third-party tools).

---

### 2.2 Instagram

Instagram's algorithm operates separately across Feed, Reels, Stories, and Explore. Each surface has its own ranking logic.

**Key ranking signals:**

| Signal | Feed | Reels | Explore |
|---|---|---|---|
| Completion rate | High | Very High | High |
| Saves | Very High | High | High |
| Shares (DM shares) | High | Very High | Medium |
| Comments | High | Medium | High |
| Recency | Medium | Medium | Low |
| Account history with user | High | Medium | Low |
| Hashtag relevance | Low | Medium | High |

**The engagement window:**
Instagram's algorithm evaluates a post's early performance in the first **30 minutes** after publication. High engagement in this window signals the algorithm to push the post to a wider audience. Low early engagement suppresses reach. Post when the target audience is most active (see Section 6).

**Instagram-specific notes:**
- Relevance, Recency, and Resonance (the "3 Rs") are Instagram's own published ranking criteria for Feed.
- Reels between 15–30 seconds outperform longer formats for completion rate in bandwidth-constrained markets.
- Carousels generate repeat views (users swipe back) — this dwell time signals quality.
- Do not post a Reel and then post a static image within 2 hours — Instagram favours spacing posts to prevent self-competition.

---

### 2.3 TikTok

TikTok uses the most transparent ranking model of the major platforms. Its primary signal is **completion rate** — the percentage of viewers who watch a video from beginning to end. Everything else is secondary.

**Key ranking signals (in order of weight):**

1. **Completion rate** — the single most important signal
2. **Re-watches** — users who replay the video
3. **Shares** — especially off-platform shares (WhatsApp, SMS) which signal viral pull
4. **Comments** — open-ended videos that invite response perform best
5. **Likes** — weakest signal but still counted
6. **Follows from the video** — indicates the content converted a non-follower

**TikTok distribution model:**
TikTok shows every video to a small test cohort (typically 300–500 users). If completion rate exceeds threshold, it is shown to progressively larger cohorts. This means a new account with zero followers can achieve massive reach on a single video — follower count is not a gating factor.

**TikTok-specific notes:**
- Keep videos under 45 seconds for EA audiences — data costs mean users rarely watch long-form TikTok on mobile data.
- Use on-screen captions. Many users watch without sound in public spaces (matatus, offices, queues).
- Hook in the first 2 seconds. The algorithm measures whether users skip past the first frame.
- Trending audio accelerates distribution — use audio from the Creative Library or trending local sounds.
- Posting at low-data-cost times (early morning before commute, evening after 8 PM EAT when users are on Wi-Fi) improves completion rates.

---

### 2.4 YouTube

YouTube's algorithm optimises for **watch time** and **session time** — how long a viewer watches a video and how many subsequent videos they watch in the same session.

**Key ranking signals:**

| Signal | Notes |
|---|---|
| Click-through rate (CTR) | Percentage of impressions that resulted in a click — thumbnail and title are critical |
| Average view duration | Absolute minutes watched, not percentage |
| Watch percentage | Percentage of the video watched |
| Likes and dislikes | Sentiment signal |
| Comments | Engagement depth signal |
| Saves to playlist | Strong long-term signal |
| Subscribers from video | Conversion signal |

**Series playlists as algorithm signals:**
Organising videos into series playlists signals topical authority to YouTube's algorithm. When a viewer finishes one video in a playlist, YouTube auto-queues the next, increasing session time and directly rewarding the channel. Create a playlist for every content series, campaign, or topic cluster.

**YouTube-specific notes:**
- Thumbnails drive CTR — test two thumbnail variants where possible.
- The first 30 seconds determine whether a viewer stays. Front-load the value.
- Low-bandwidth EA audiences often watch YouTube on mobile data — keep videos under 10 minutes for educational content; longer only if the audience is Wi-Fi-dominant (corporate, campus).
- Shorts (under 60 seconds) are ranked separately and drive channel discovery — use them to attract new subscribers who then watch long-form content.
- Consistent upload schedule (same day and time each week) trains YouTube's recommendation engine to push content at predicted release times.

---

### 2.5 LinkedIn

LinkedIn uses three layered graphs to rank content: the **identity graph** (who you are), the **interest graph** (what topics you follow), and the **knowledge graph** (content quality signals). A post is shown first to your direct connections, then to second-degree connections if it performs well.

**Key ranking signals:**

| Signal | Notes |
|---|---|
| Early engagement velocity | Engagement in the first 60 minutes is critical |
| Comment depth | Replies-to-comments (threads) score higher than top-level comments |
| Dwell time | LinkedIn tracks how long users pause on a post |
| Content format | Native posts > articles > documents > links > polls |
| Hashtag relevance | Use 3–5 relevant hashtags — more than 5 suppresses reach |
| Creator mode | Accounts with Creator Mode active get broader distribution |
| Native documents (PDFs) | Carousel-style document posts generate high dwell time |

**LinkedIn-specific notes:**
- LinkedIn penalises posts with outbound links in the main text. Move the link to the first comment and reference it in the post ("Link in the first comment").
- Native video autoplay on LinkedIn is silent — include captions.
- LinkedIn's algorithm favours personal profiles over Company Pages for organic reach. Encourage team members to share or comment — employee advocacy multiplies reach without ad spend.
- The professional context of LinkedIn means posts that teach a skill, share a genuine lesson, or offer a professional insight outperform promotional posts.

---

### 2.6 X / Twitter

X uses a ranked feed (For You) and a chronological feed (Following). The For You algorithm is the primary distribution engine.

**Key ranking signals:**

| Signal | Notes |
|---|---|
| Engagement velocity | The first **2–3 hours** after posting are the critical window |
| Replies | Conversations started by the post signal quality |
| Reposts (RTs) | Distribution signal |
| Likes | Standard engagement signal |
| Bookmarks | High-intent saves signal |
| Profile authority | Verified accounts and accounts with high follower-to-engagement ratios ranked higher |
| Media inclusion | Posts with images or short video outperform text-only |

**X-specific notes:**
- Threads perform well for educational or narrative content — post the thread as a sequence and reply to the first tweet to extend reach.
- Do not include links in the first tweet of a thread — X suppresses reach for posts with outbound links. Add the link in a reply.
- The For You feed now surfaces content from accounts the user does not follow — this is the primary discovery mechanism for new audience growth.
- X is the dominant platform for journalists, politicians, and public discourse in Uganda — useful for PR, reputation management, and media relations rather than direct commerce.

---

## 3. Engagement Window Reference

| Platform | Critical engagement window | What happens after |
|---|---|---|
| Instagram | First 30 minutes | Algorithm decides wider distribution based on early signal |
| Facebook | First 2–3 hours | Feed ranking locks in based on initial engagement rate |
| LinkedIn | First 60 minutes | First-degree network determines whether second-degree sees it |
| X / Twitter | First 2–3 hours | For You algorithm scores and distributes based on velocity |
| TikTok | First cohort (300–500 views) | Completion rate in first cohort determines next cohort size |
| YouTube | First 48 hours | CTR and watch time in this period shape long-term search ranking |

**Implication:** Post when the target audience is online. Do not post and immediately go offline — respond to early comments to signal activity to the algorithm.

---

## 4. Favoured Content Formats by Platform

| Platform | Most favoured | Second | Least favoured |
|---|---|---|---|
| Facebook | Native video / Reels | Stories, Carousels | Link posts |
| Instagram | Reels | Carousels | Static single image |
| TikTok | Short vertical video | Stitches / Duets | Static images (limited) |
| YouTube | Long-form video | Shorts | Community posts |
| LinkedIn | Native text posts, Documents | Native video | External links |
| X / Twitter | Threads with media | Short posts with image/video | Link-only posts |

**Universal rule:** Native content (uploaded directly to the platform) outperforms content linked from external sources on every platform. Never post a YouTube link on Facebook if the goal is reach — upload the video natively.

---

## 5. Posting Frequency Benchmarks

| Platform | Minimum | Recommended | Maximum before quality drops |
|---|---|---|---|
| Facebook | 3× per week | 5× per week | 1–2× per day |
| Instagram | 3× per week | 4–5× per week (inc. Stories daily) | 2× per day |
| TikTok | 3× per week | 5–7× per week | 3× per day |
| YouTube | 1× per week | 2× per week | 1× per day |
| LinkedIn | 2× per week | 3–4× per week | 1× per day |
| X / Twitter | 3× per week | 5× per week | Multiple per day (threads count as one) |

**Note:** Consistency beats volume. Posting 3 times per week every week outperforms posting 7 times in one week and going silent for two weeks.

---

## 6. EA-Specific Considerations

### 6.1 Peak Activity Times (East Africa Time — EAT, UTC+3)

| Platform | Weekday peaks | Weekend peaks |
|---|---|---|
| Facebook | 07:00–09:00, 12:00–13:00, 19:00–21:00 | 10:00–12:00, 19:00–21:00 |
| Instagram | 07:00–08:30, 12:00–13:30, 20:00–22:00 | 11:00–13:00, 20:00–22:00 |
| TikTok | 06:30–08:00, 12:30–14:00, 20:00–23:00 | 10:00–14:00, 19:00–23:00 |
| YouTube | 19:00–23:00 (Wi-Fi hours) | 10:00–23:00 |
| LinkedIn | 07:00–09:00, 12:00–13:00, 17:00–18:30 | Low activity |
| X / Twitter | 07:00–09:00, 12:00–14:00, 20:00–22:00 | 10:00–12:00 |

### 6.2 Data Costs and Video Consumption

Mobile data costs in Uganda remain a significant barrier to video consumption. 1 GB of data costs approximately UGX 3,000–5,000 on most networks (2026 rates).

**Implications for content:**
- Keep TikTok and Instagram Reels under 45 seconds — longer videos consume more data and are abandoned before completion, hurting the completion rate signal.
- For YouTube, keep educational content under 10 minutes unless the target audience is Wi-Fi-dominant (universities, corporates, Kampala CBD offices).
- Add on-screen captions to all video — users frequently watch without sound to avoid data drain.
- Compress video files before upload — a 720p video performs equivalently to 1080p on mobile screens and loads faster.
- Schedule video posts for evening hours (after 19:00 EAT) when users are more likely to be on Wi-Fi at home.

### 6.3 WhatsApp as a Near-Zero-Cost Distribution Channel

WhatsApp operates on negligible data relative to video platforms. For many EA businesses, WhatsApp is the primary customer communication and content distribution channel.

- Share links to published content (blog posts, YouTube videos, Facebook posts) via WhatsApp Business broadcast lists.
- WhatsApp Status (24-hour Stories equivalent) reaches opted-in contacts at near-zero data cost.
- WhatsApp does not have an algorithm — delivery is chronological and universal to the contact list. Use this to guarantee reach to the highest-value contacts (existing customers, warm leads).
- WhatsApp engagement (replies, reactions) does not count towards social platform algorithm signals. Use WhatsApp to drive traffic to the platform post, not as a replacement for it.

---

## 7. Algorithm-Penalised Behaviours

Avoid the following. Each behaviour either directly suppresses reach or trains the algorithm to associate the account with low-quality content.

| Behaviour | Platforms affected | Why it is penalised |
|---|---|---|
| Engagement bait ("Like if you agree", "Tag 3 friends to win") | Facebook, Instagram | Facebook explicitly demotes engagement bait posts |
| Outbound links in post body | Facebook, LinkedIn, X | Sends users off-platform — algorithms suppress |
| Cross-posting identical content | All | Algorithms detect duplicate content; native upload always preferred |
| Clickbait headlines | YouTube, X, LinkedIn | CTR drops when viewer does not stay — algorithm penalises mismatch |
| Buying followers or likes | All | Inflates metrics without engagement; signals low-quality content to algorithm |
| Posting in bursts then going silent | All | Inconsistency reduces algorithmic trust and scheduling priority |
| Hashtag stuffing (30 tags on every post) | Instagram, LinkedIn | Instagram reduced hashtag weight significantly in 2024; LinkedIn caps effective reach above 5 tags |
| Reposting competitors' viral content without adding value | TikTok, X | Flagged as low-effort duplication |
| Ignoring comments | All | Non-response to comments signals low engagement depth; algorithm deprioritises |

---

## 8. Pre-Publication Checklist

Use this checklist before every post goes live. Adapt to platform as indicated.

---

**BEFORE YOU POST — QUICK REFERENCE CHECKLIST**

**Content fundamentals**
- [ ] Does the post serve the audience first (inform, entertain, inspire) before it serves the business?
- [ ] Is the hook clear in the first line / first 2 seconds of video?
- [ ] Is the call to action specific and single (one CTA per post)?
- [ ] Is the copy free from spelling errors and in British English?

**Format and upload**
- [ ] Is the content uploaded natively to the platform (not linked from another platform)?
- [ ] Is the video under the recommended length for this platform and audience context?
- [ ] Are captions / subtitles included if the post contains video?
- [ ] Is the image or video resolution correct for the platform and placement?

**Algorithm signals**
- [ ] Is there a reason for the audience to comment, save, or share (not engagement bait)?
- [ ] Are outbound links in the first comment, not the post body? (LinkedIn, Facebook, X)
- [ ] Are hashtags relevant, specific, and within the platform limit (3–5 for LinkedIn, up to 10 for Instagram)?
- [ ] Is the posting time within the platform's peak activity window for EAT? (see Section 6.1)

**Penalised behaviours — confirm none are present**
- [ ] No engagement bait phrases ("Tag a friend", "Like if you agree", "Comment YES")
- [ ] No direct outbound link in the post body (Facebook, LinkedIn, X)
- [ ] Content is original or properly adapted — not copy-pasted from another platform
- [ ] Headline / caption accurately represents the content (no clickbait)

**Post-publication (first 30–60 minutes)**
- [ ] Monitor and respond to all comments within 30 minutes of posting
- [ ] Share to WhatsApp Business broadcast list if content is relevant to existing customers
- [ ] Share to relevant Facebook Groups if applicable (with group permission)
- [ ] Check early analytics (reach, views in first 30 min) to gauge early signal

---

## Quality Criteria

Output produced by this skill meets the standard when:

1. **Platform specificity** — every platform section identifies its unique primary signal (completion rate for TikTok, saves for Instagram, watch time for YouTube) rather than giving generic advice applicable to all platforms.
2. **EA market grounding** — data cost constraints, WhatsApp distribution logic, and EAT peak times are integrated into the operational guidance, not appended as an afterthought.
3. **Checklist usability** — the pre-publication checklist in Section 8 is formatted so a content producer can print it or pin it to their screen and use it without reading the full document.
4. **Penalised behaviours are specific** — each penalised behaviour names the platforms affected and explains the mechanism of penalisation, not just that it "hurts reach".
5. **Engagement windows are actionable** — the timing guidance in Sections 3 and 6.1 gives specific EAT times, not vague recommendations like "post when your audience is active".
6. **Formats table is decision-ready** — a content producer can look at Section 4 and immediately know which format to prioritise for their platform without further research.
7. **No strategy bleed** — this document does not recommend content pillars, audience personas, or brand voice. Those belong in the relevant strategy skills. This skill stays operational.
8. **British English throughout** — organisation, behaviour, favoured, recognise, analyse — no American spellings anywhere in the document.

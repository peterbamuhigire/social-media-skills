---
name: playbook-question-engine
description: Use when designing or improving a Question Engine operating playbook with roles, ordered actions, controls and measures. Use platform skills for channel plans and strategy skills for upstream direction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# The Question Engine Playbook

**Sources:** Westergaard (2016) *Get Scrappy*; Marcus Sheridan's River Pools case study

---

<!-- dual-compat-start -->
## Use When
- Build or improve a repeatable Question Engine workflow for a client or delivery team.
- Turn an approved objective into roles, controls, handoffs and measurable actions.

## Do Not Use When
- The task is a single-channel presence plan; use the closest `platform-*` skill.
- The task is upstream positioning or channel choice; use the closest `strategy-*` skill.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience and success measure | Approved client brief or accountable owner | Yes | Stop and request the missing decision |
| Current workflow, assets and performance evidence | Team records, platform exports or supplied artefacts | Conditional | Label the baseline unassessed and use a minimum viable workflow |
| Roles, budget, timing and approval limits | Delivery owner | Yes for execution | Produce a draft only; do not schedule, spend or publish |

## Capability and Permission Boundaries
Read supplied artefacts and search relevant evidence. Treat review, audit and planning as read-only. Editing the requested draft is allowed; publishing, messaging, production changes, personal-data processing, spending, destructive actions and certification claims require explicit authority. Use network access only for authorised verification.

## Degraded Mode
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Question Engine playbook plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| A question invites sensitive disclosure or has no response plan | Replace it with a safer, answerable prompt | Engagement that creates unmanaged risk |
| Inputs and authority are complete | Produce an execution-ready playbook | Unowned actions and hidden assumptions |
| Evidence or tooling is incomplete | Produce the narrowest qualified draft and a gap list | Treating an unassessed check as passed |
| Action publishes, spends, contacts people or changes production state | Require explicit approval before action | Unauthorised external impact |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply the decision rules, preserve useful existing material and draft the Question Engine playbook.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Question Engine playbook | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
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

## Required Inputs

Ask for the following before generating any deliverable:

1. **Client business name**
2. **Industry**
3. **Country / city** (defaults to Uganda / East Africa)
4. **Primary goal** (e.g. generate content ideas, build an FAQ library, identify blog post topics, reduce sales call objections)
5. **Existing content** (blog posts, FAQ page, WhatsApp saved replies, video library — or confirm none exists)
6. **Customer-facing team members** (receptionist, sales staff, customer service, technicians — whoever hears customer questions)
7. **Primary search and discovery channels** (Google, YouTube, Facebook search, WhatsApp word of mouth — affects content format priority)
8. **Google Search Console access** (Yes / No — determines whether search query data is available)

---

## The Core Principle

The most effective content answers the questions customers are already asking. Marcus Sheridan's River Pools company grew from near-bankruptcy to the most-visited swimming pool website in the world by one method: answering every customer question in writing — including the uncomfortable ones. "How much does a pool cost?" "What are the problems with fibreglass pools?" "How do we compare to [competitor]?" Answering the questions competitors avoid is the highest-leverage content tactic available (Westergaard, 2016).

**The East African equivalent:** Be the business in the market that everyone goes to when they have a question. In communities where trust is built through information-sharing, the business that gives away knowledge freely is the business people recommend.

---

## Why This Works

- **Search engines reward specific answers:** A blog post titled "How much does solar panel installation cost in Kampala?" ranks for searches that a generic "Our Services" page never will
- **Pre-educated buyers close faster:** A prospect who reads the answer to their question before calling arrives at the conversation already partially sold — the sales call shortens by 30–50%
- **Competitors avoid price and problem questions:** This creates a gap that any willing business can occupy — and the gap is large
- **WhatsApp saved replies become content:** Every saved reply is evidence of a question customers ask repeatedly — turn it into a content piece and reduce the need to answer it manually

---

## The Five Question Sources

Collect questions from all five sources each month. Target: 20 raw questions per month minimum.

### Source 1 — Frontline Staff

The receptionist, sales team, and customer service team hear customer questions daily. These people are a gold mine. Many businesses never ask them.

**Action:** Brief every customer-facing team member to capture one question per week that a customer asked which is not yet answered in the business's content. Use a shared WhatsApp group or a simple Google Sheet.

**Sample briefing message:** "Every time a customer asks you something this week, note it down. We're going to turn those questions into content. There are no silly questions — the more specific, the better."

### Source 2 — Social Media Comments and DMs

Mine Instagram, Facebook, TikTok, and WhatsApp for recurring questions. A question asked by 10 different people in different ways is a content gap, not an individual customer query.

**Action:** Review the last 90 days of social media comments and DMs. Identify questions that appear more than twice. Export to the question list.

**Tool:** Meta Business Suite comment history; TikTok Creator Studio comments; WhatsApp Business chat search.

### Source 3 — Search Data

Use Google Search Console (free) to identify the search queries bringing visitors to the website — including partial matches and long-tail phrases. These are real searches from real people who want the answer.

**Action:**
1. Open Google Search Console → Performance → Search Results
2. Filter by query type: questions only (queries containing "how", "what", "why", "can I", "is it", "how much")
3. Export the top 50 question queries by impression volume
4. Add to the question list

**If Google Search Console is not yet set up:** Use Google's "People Also Ask" box — search for the client's main service or product and record every question that appears in the PAA box. These are Google's most common related queries.

### Source 4 — FAQ Logs and Saved Replies

Review the business's existing FAQ page, WhatsApp saved replies, email template library, and any printed customer information documents. Every saved reply is evidence of a recurring question.

**Action:** List every saved WhatsApp reply and email template. Treat each as an answered question. Cross-reference against the content library — if the answer exists as a saved reply but not as a blog post or social post, it is a content gap.

### Source 5 — Sales Call Notes

Review the notes or recordings from the last 20 sales enquiry conversations. What objections came up? What did the prospect not understand before they spoke to the business? What question, if answered in advance, would have reduced hesitation?

**Action:** Interview the owner or sales lead with this question: "In the last month, what question came up most often in sales conversations that slowed down the decision?" That question becomes the first content piece.

---

## The Question Engine Process — Six Steps

### Step 1 — Collect
Run all five source reviews in the first week of each month. Collect raw questions without filtering. Target 20+ questions per month. Record every question exactly as the customer asked it — in their language, not the business's language.

### Step 2 — Cluster
Group similar questions together. "How much does X cost?", "What is the price of X?", "Is X expensive?", and "Can I afford X?" are all the same question — cluster them into one content brief.

### Step 3 — Prioritise Using the Big 5 Framework (Sheridan, 2019)

The Big 5 are the five question categories that generate the highest search volume and the greatest sales acceleration. Prioritise content from these categories before any other topic:

| Category | What buyers are asking | Why this is urgent |
|---|---|---|
| **Pricing and Cost** | "How much does [product/service] cost?" "What affects the price?" "Is there a cheaper option?" | Price is the most-searched topic in almost every industry; businesses that answer it first own the category in search |
| **Problems and Limitations** | "What are the problems with [product/service]?" "When does [solution] not work?" | Buyers conduct due diligence before purchase; honest answers build trust faster than silence |
| **Comparisons** | "[Brand A] vs [Brand B]" "What is the difference between [option 1] and [option 2]?" | Buyers in the consideration stage actively compare; appear in their research or lose the sale to whoever does |
| **Reviews** | "Is [company/product] any good?" "What do customers say about [brand]?" "Best [product category]" | Social proof is the deciding factor for many buyers; reviews content appears in Google and YouTube search |
| **Best in Class** | "Best [product type] in [city/country]" "Which [service] should I choose?" "Top [service providers] in Uganda" | Buyers seeking the best option are close to a decision; ranking content at this stage converts directly |

Score each question cluster against the Big 5: Big 5 questions get highest priority. Non-Big 5 questions fill the calendar after the primary gaps are addressed.

Also score on:
| Dimension | Scoring |
|---|---|
| **Search volume / enquiry frequency** | How often is this question asked? (High / Medium / Low) |
| **Sales relevance** | If this question were answered, would it accelerate a purchase decision? (High / Medium / Low) |

Prioritise questions that score High on both dimensions. Price and cost questions, comparison questions, and problem questions typically score highest on both.

### Step 4 — Assign Format
Match each prioritised question to the best content format:

| Question type | Best format | Distribution |
|---|---|---|
| Pricing and cost | Blog post + short video | Website, YouTube, Facebook |
| Comparison ("us vs. competitor") | Long-form article | Website, LinkedIn |
| Problems / limitations | Honest FAQ (text) | Website, WhatsApp saved reply |
| How-to / process | Video + checklist | YouTube, Instagram, WhatsApp |
| Best in category / buyer's guide | Long-form article or PDF | Website, email newsletter |
| Quick facts | Instagram carousel or Facebook post | Social media only |

### Step 5 — Publish and Index
- Publish blog content on the website; submit to Google Search Console for indexing
- Publish video content on YouTube with a description that includes the exact question as the title
- Share each piece across all active social platforms within 48 hours of publication
- Add the answer to WhatsApp saved replies for the sales team — so they can share the content link when the question arises in a conversation

### Step 6 — Review Quarterly
Every 90 days, review content performance:
- Which pieces generated the most organic traffic, enquiries, or shares?
- Which question topics have not yet been addressed?
- Are there new questions from the five sources that did not exist 90 days ago?

Double down on the topics and formats generating the most enquiry traffic. Retire or update content that no longer reflects current pricing, processes, or services.

---

## The "Answer What Competitors Avoid" Rule

Most businesses refuse to answer:
- **Price questions** — afraid to scare away prospects or reveal rates to competitors
- **Comparison questions** — afraid to name a competitor or appear defensive
- **Problem questions** — afraid that admitting a limitation undermines credibility

These are the highest-value content pieces precisely because competitors avoid them. A prospect searching "how much does [service] cost in [city]" and finding an honest, detailed answer from the client's website arrives at the conversation pre-qualified and ready to proceed.

**Answering limitations builds trust:** "Here is when our service is not the right fit for you" is counterintuitive but highly effective — it signals confidence, honesty, and selectivity. Prospects who continue after reading a limitation are more committed buyers.

---

## Monthly Question Engine Output

Generate a monthly Question Engine report containing:

1. **Question harvest** — the 20+ raw questions collected this month from all five sources
2. **Clustered question list** — questions grouped by theme; number of clusters
3. **Priority content brief (top 5)** — for each: question cluster, recommended format, target platform, suggested headline, 3-bullet outline
4. **Content backlog** — all remaining questions ranked by priority for future months
5. **Last month's performance** — if applicable: which published pieces generated traffic, enquiries, or shares?

---

## Assignment Selling — Using Content to Close Deals (Sheridan, 2019)

Once the content library is built, deploy it proactively in the sales process. This is called Assignment Selling: the practice of assigning specific content pieces to prospects before key sales conversations, so that the conversation begins at a higher level of shared understanding.

**How Assignment Selling works:**
1. Identify the two or three most important questions a prospect needs to answer before they can make a purchase decision
2. Ensure content exists that answers each of those questions (Big 5 content is ideal)
3. Before any sales meeting, email or WhatsApp the prospect: "Before we speak on [date], I'd like to share [article/video] — it will make our conversation much more productive."
4. Begin every sales conversation by confirming: "Did you get a chance to review the content I sent?" If yes, the conversation can skip the basics. If no, revisit the assignment.

**The 30-page principle:** Sheridan (2019) found that prospects who read 30 or more pages of a company's content before a sales conversation closed at an 80% rate. Those who had read fewer than 10 pages closed at a significantly lower rate. Content is not only a marketing tool — it is a pre-sale qualification and conversion instrument. Track which content pieces the prospect has viewed before each sales appointment.

**Pre-qualification questions to include in every lead form:**
- "Which article or video brought you to us today?" (tracks source)
- "What is the most important question you'd like answered before deciding?" (surfaces unmet content gaps)
- "How did you hear about us?" (attribution)

**Insourcing content creation:** The most effective answer to "we don't have time to create content" is to involve the people who already have the answers — the sales team, customer service staff, and subject matter experts within the business. They answer questions every day. A content manager with a journalist's instincts can turn those answers into published content with a 20-minute monthly interview per staff member. One filming session with four employees on a job site can produce five or more videos. No specialist knowledge is required to create content — only a willingness to share what is already known.

---

## Quality Criteria

Output meets the standard for this skill if:

- All five question sources are addressed — the output does not rely on one source alone
- The question collection process specifies a monthly cadence with a 20-question minimum target
- The prioritisation matrix scores questions on both search frequency and sales relevance
- Content format is matched to question type — not assigned generically
- The "answer what competitors avoid" principle is applied explicitly: price, comparison, and problem questions are prioritised, not avoided
- WhatsApp saved replies are addressed as both a question source and a distribution channel
- The six-step process is included in full — collect, cluster, prioritise, assign, publish, review
- Language is British English throughout; imperative in all instructional sections

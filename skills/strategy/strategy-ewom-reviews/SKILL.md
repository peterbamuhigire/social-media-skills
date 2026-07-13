---
name: strategy-ewom-reviews
description: Use when the main deliverable concerns proactive review generation, referral conditions, advocacy, and electronic word of mouth; use playbook-reputation-management when that neighbouring workflow owns the primary decision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# eWOM and Reviews Strategy

<!-- dual-compat-start -->
## Use When

- Use this skill for proactive review generation, referral conditions, advocacy, and electronic word of mouth.
- Use it when the requested deliverable needs the domain decisions and acceptance checks below.

## Do Not Use When

- Use `playbook-reputation-management` when that neighbouring workflow owns the main decision or deliverable.
- Do not proceed when required evidence, approval, or safety review is absent; return the missing-input path instead.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Objective, audience, market, and intended decision | Client or approved brief | yes | Ask for it or state a narrow working assumption |
| Existing channel, content, commercial, or performance evidence relevant to proactive review generation, referral conditions, advocacy, and electronic word of mouth | Client systems, supplied files, or verified research | conditional | Mark the check unassessed and avoid performance claims |
| Approval, policy, budget, access, or risk constraints | Accountable client owner | conditional | Stop before publishing, spending, collecting data, or making regulated claims |

## Workflow

1. Confirm the decision, consumer, market, and evidence boundary; distinguish the request from `playbook-reputation-management`.
2. Inspect supplied artefacts and record missing or unverified inputs before drafting.
3. Apply the domain framework in this skill and use the decision rule below at each branch.
4. Stop for approval before publishing, spending, contacting people, changing live systems, or making regulated claims.
5. Review the deliverable against the quality and anti-slop gates; if a check fails, correct it and rerun the affected check.
6. Hand off the artefacts, assumptions, evidence, and unresolved risks to the named consumer.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Proactive review generation, referral conditions, advocacy, and electronic word of mouth deliverable | Client decision-maker or delivery team | Names the chosen route, owners, sequence, assumptions, and measurable acceptance checks |
| Decision and risk record | Reviewer or implementer | Links each recommendation to supplied evidence or labels it as an assumption |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Input and assumption register | Table or annotated brief | Missing and unverified items are visible, not treated as passed |
| Release check | Completed quality checklist | All blocking findings are fixed or the deliverable is explicitly withheld |

## Capability and Permission Boundaries

Read and search are the minimum capabilities. Analysis and planning remain read-only. Edit only files placed in scope; publishing, outreach, spend, personal-data processing, production changes, and certification claims require explicit authority and evidence of success.

## Degraded Mode

If files, tools, network, current evidence, rendering, or authorised access are unavailable, return the narrowest useful qualified deliverable. Mark each unavailable check `not assessed`; never convert it into a pass or invent market facts.

## Decision Rules

| Choice condition | Action | Failure or risk avoided |
|---|---|---|
| The goal is new advocacy rather than incident response | Design ethical prompts and proof capture; route active damage control to reputation management | Manipulated reviews or a growth plan built on unresolved complaints |
| Evidence is contradictory or materially incomplete | Pause the affected recommendation and request the accountable source | Confident advice built on an unresolved premise |
| Authority is limited to analysis or planning | Deliver a read-only plan and approval checklist | Unauthorised publication, spend, outreach, or data use |

## Quality Standards

- Keep Uganda/East Africa, British English, EAT, UGX, and WhatsApp-first assumptions explicit where they apply.
- Tie recommendations to observed evidence, a named assumption, or a verification action.
- Give the next operator enough detail to execute without guessing ownership, sequence, or acceptance.
- Apply `ai-marketing/anti-ai-slop` during drafting and block release on an F from `ai-marketing/ai-slop-audit`.

## Anti-Patterns

- Inventing a client metric, audience fact, price, partner, or platform rule. Fix: verify it or label the decision provisional.
- Treating a missing tool, source, render, or approval as a passed check. Fix: mark it `not assessed` and narrow the output.
- Producing channel tactics before defining the decision and consumer. Fix: state the required outcome and handoff first.
- Copying a global template without adapting Uganda/East Africa access, language, payment, or trust conditions. Fix: record which local assumptions apply.
- Recommending publication, outreach, spend, data collection, or a regulated claim without authority. Fix: stop at an approval-ready draft.
- Reporting activity as success without an acceptance condition. Fix: name the observable result and evidence source.

## References

- [AGENTS.md](../../../AGENTS.md)
<!-- dual-compat-end -->

**Source:** Hanlon and Tuten (2022) *The SAGE Handbook of Digital Marketing*

---


## Required Inputs

Ask for the following before generating any deliverable:

1. **Client business name**
2. **Industry**
3. **Country / city** (defaults to Uganda / East Africa)
4. **Primary goal** (e.g. increase Google review volume, build a referral programme, measure NPS for the first time)
5. **Current review platforms active** (Google, Facebook, TripAdvisor, industry-specific platforms)
6. **Current monthly review volume** (how many new reviews per month across all platforms?)
7. **Current NPS or CSAT score** (if available — or confirm that no measurement exists yet)
8. **Primary customer communication channel** (WhatsApp, email, phone — affects activation tactic design)

---

## eWOM vs. Reputation Management

Reputation management is **reactive** — it responds to what customers say after they say it. eWOM strategy is **proactive** — it designs conditions that cause satisfied customers to talk before they are prompted by a negative experience or an external review platform.

The goal of an eWOM programme is to engineer a stream of authentic, voluntary advocacy from real customers — not to manufacture or fake reviews.

---

## The GST Framework (Hanlon and Tuten, 2022)

Consumers engage in three eWOM behaviours. A strong eWOM programme activates all three:

| Behaviour | Definition | Programme goal |
|---|---|---|
| **Give** | Share their own experience — write a review, post a photo, mention the brand in conversation | Create the conditions for satisfied customers to share easily and promptly |
| **Seek** | Look for others' experiences before making a purchase decision | Ensure the client's reviews and advocacy are visible where seekers look |
| **Transmit** | Share others' content — repost a review, forward a recommendation, tag a friend | Create shareable assets (screenshot-friendly quotes, shareable posts) that transmitters can pass on |

---

## Identifying eWOM Transmitters

Transmitters are not always the same people as top reviewers. Some customers write excellent reviews but never share them. Others share everything without writing reviews. Identify both types using:

- **Social listening:** Who is mentioning the brand without being prompted? Use `meta-social-listening` to monitor brand mentions across platforms.
- **Survey data:** Ask "Have you recommended us to anyone in the past 3 months?" in an NPS survey — those who answer Yes are active transmitters.
- **CRM data:** Which customers have the highest referral rates? Which contacts are sending new enquiries?

Build a separate **Advocate List** in the CRM — a tagged segment of verified transmitters who receive early access to new offerings, exclusive updates, and referral incentives.

---

## Activation Tactics

### At Peak Satisfaction Moments

Identify and map the client's peak satisfaction moments — points in the customer journey where positive emotion is highest. Common examples:

- Project completion or delivery (services)
- Product unboxing or first use (e-commerce)
- Problem resolution after a complaint
- A milestone reached (client hits a goal with the service's help)

**At each peak moment:** Ask for a review within 48 hours. Use a single-tap review link sent via WhatsApp — do not require the customer to search for the review platform or log in to a platform they do not already use. Response rates drop by approximately 80% after 48 hours.

**WhatsApp review request template:**
"Hi [Name], I'm really glad [positive outcome]. Could I ask a quick favour? If you have 2 minutes, a Google review would mean a lot to us — here's the link: [direct link]. Just share your honest experience. Thank you!"

### Incentivised Advocacy (Where Applicable)

Offer a non-monetary incentive for general advocacy (social sharing, referrals — not Google reviews, which prohibit incentivisation):

- Early access to new services or products
- Entry into a monthly recognition draw
- Public recognition: feature the customer in a social post or case study
- A handwritten or WhatsApp thank-you note (in EA, personal recognition is often more motivating than a discount)

**Important:** Google's review guidelines explicitly prohibit incentivised Google reviews. Design advocacy incentives for referrals and social sharing — not for Google review submission.

---

## The Objectivity Principle

Display negative reviews alongside positive ones. The counterintuitive evidence is robust (Rageh, 2026): a 4.3-star rating with a mix of reviews is more trusted than a 5.0 rating with uniformly perfect reviews. Consumers interpret a perfect record as manipulation or selective deletion.

**Response to negative reviews:**
- Respond to every negative review within 24 hours
- Acknowledge the experience without being defensive
- Offer a direct channel to resolve the issue (WhatsApp number or email — not a public argument)
- After resolution, invite the customer to update their review if they feel their experience has changed

Responding professionally to a 2-star review demonstrates genuine accountability. This increases trust more than the 2-star review costs — and is visible to every future prospect who reads the review thread.

---

## eWOM Measurement Framework

Track the following metrics monthly:

| Metric | Definition | Target |
|---|---|---|
| Review velocity | New reviews per month across all platforms | Increasing month-on-month |
| Sentiment ratio | Positive : neutral : negative reviews | Target 85:10:5 or better |
| Net Promoter Score (NPS) | % promoters minus % detractors on a 0–10 scale | 50+ is strong; 70+ is exceptional |
| Share rate | % of published social content shared by audience members (not just liked) | Track trend over time |
| Referral rate | % of new enquiries that cite an existing customer as the source | Track via CRM source field |
| Review platform spread | How many platforms have active, recent reviews | Minimum 2 platforms; Google is always one |

Review all six metrics monthly. Prioritise review velocity and NPS as the two most actionable leading indicators.

---

## Platform Priority for EA Clients

| Platform | Priority | Notes |
|---|---|---|
| Google Reviews | Essential | Highest search visibility; influences Google Maps ranking |
| Facebook Recommendations | High | Highest platform penetration in EA; trusted by all demographics |
| TripAdvisor | For hospitality and tourism clients only | Sector-specific but important for hotel, restaurant, and travel clients |
| Industry directories | Context-dependent | Health, legal, construction: check sector-specific directories |
| Instagram and TikTok UGC | Supplementary | User-generated content and tags build social proof without structured reviews |

Do not spread eWOM effort across too many platforms. Focus on Google and Facebook first. Expand only after review velocity on both is strong.

---

## eWOM Programme Build Sequence

Follow this sequence when building an eWOM programme from zero:

1. **Audit current proof** — inventory all existing reviews, testimonials, and social mentions. Identify which peak satisfaction moments currently generate unsolicited advocacy.
2. **Set up review links** — create a short-link (bit.ly or similar) for each priority review platform. Test on a mobile device before deploying.
3. **Train the team** — brief every customer-facing team member on the 48-hour review request window and the WhatsApp request template. Role-play the conversation.
4. **Implement NPS measurement** — send an NPS survey to all active clients in the first month. Identify promoters (score 9–10) and add them to the Advocate List.
5. **Launch referral mechanic** — create a simple referral prompt for promoters: a WhatsApp message or email with a referral request and a small recognition incentive.
6. **Build the review response routine** — assign one team member to check and respond to all new reviews weekly. Draft response templates for common positive and negative themes.
7. **Report monthly** — review the six eWOM metrics monthly; adjust tactics based on what is generating the highest review velocity and NPS movement.

---

## Quality Criteria

Output meets the standard for this skill if:

- The GST Framework (Give / Seek / Transmit) is applied — the strategy activates all three eWOM behaviours, not just review generation
- Peak satisfaction moments are identified for the specific client — not generic timing recommendations
- The 48-hour review request window and WhatsApp-first request channel are specified
- The objectivity principle is applied — the strategy includes negative review response, not just positive review generation
- All six eWOM measurement metrics are included with monthly tracking cadence
- Google's prohibition on incentivised reviews is flagged — incentives are directed at referrals and social sharing
- Platform priority is ranked with EA context: Google first, Facebook second
- Language is British English throughout; imperative in all instructional sections

---
name: 01-client-brief
description: "Use when turning confirmed discovery answers into the full brief and one-page client card. Produces approved client brief and at-a-glance card; use `00-client-intake` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Client Brief Generator

Produce two outputs: (1) a full client brief document and (2) a one-page client at-a-glance card. The questionnaire doubles as a fillable document to send to the client and as a discovery call guide for the consultant. Apply the `east-african-english` skill for tone throughout. Do not begin generating content until the questionnaire has been completed.


<!-- dual-compat-start -->
## Use When

- Use this skill for turning confirmed discovery answers into the full brief and one-page client card.
- Confirm that `00-client-intake` is not the closer route before proceeding.

## Do Not Use When

- Use `00-client-intake` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Completed 00-client-intake answers and unresolved follow-up responses | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Approved client brief and at-a-glance card | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified approved client brief and at-a-glance card. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Completed 00-client-intake answers and unresolved follow-up responses is current and attributable | Produce the full approved client brief and at-a-glance card and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `00-client-intake` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `00-client-intake` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the approved client brief and at-a-glance card, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the approved client brief and at-a-glance card without completed 00-client-intake answers and unresolved follow-up responses. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `00-client-intake` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified completed 00-client-intake answers and unresolved follow-up responses, the skill produces a approved client brief and at-a-glance card with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`00-client-intake`](../00-client-intake/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Input

This skill generates the questionnaire itself — no prior input is required. The client (or the consultant on the client's behalf) fills in the questionnaire. If the consultant provides partial information upfront, pre-fill what is known and flag remaining gaps clearly.

---

## Part A: Questionnaire — Send to Client or Use in Discovery Call

Present each section as a clearly labelled block. Use the exact question wording below.

---

### Section 1: Business Overview

1. What is the full legal name of your business and the trading name (if different)?
2. What industry or sector does your business operate in?
3. In which year was the business founded?
4. How many full-time employees or team members does the business have? *(Ranges: 1–5 / 6–20 / 21–50 / 51–200 / 200+)*
5. Where is the business based? *(City, country — and any other locations if relevant)*
6. In one or two sentences, what is your unique value proposition — what do you offer that your competitors do not?
7. What is your primary business goal for the next 12 months?

---

### Section 2: Target Audience

8. Who is your primary customer? Describe them in terms of:
   - Age range
   - Gender (if relevant to your market)
   - Location (city, region, or national)
   - Approximate income level or economic segment *(e.g. middle income, upper middle, high net worth)*
   - Occupation or sector
9. Is your business B2C (selling to individuals), B2B (selling to other businesses), or both?
10. Are there secondary audiences you also want to reach? If yes, describe them briefly.

---

### Section 3: Current Social Media Presence

Complete one row per active platform. If you are not active on a platform, leave it blank.

| Platform | Handle / URL | Approx. follower count | How often do you post? | Date of last post | Who currently manages the account? |
|---|---|---|---|---|---|
| Facebook | | | | | |
| Instagram | | | | | |
| WhatsApp Business | | | | | |
| TikTok | | | | | |
| LinkedIn | | | | | |
| X / Twitter | | | | | |
| YouTube | | | | | |
| Other | | | | | |

11. How would you rate the current performance of your social media overall? *(1 = very poor, 5 = very good)*
12. What has worked well on social media so far, if anything?
13. What has not worked or what problems have you encountered?

---

### Section 4: Competitors

14. List 3–5 direct competitors. For each, provide:

| Competitor name | Industry / what they sell | Their main social media platform and handle |
|---|---|---|
| 1. | | |
| 2. | | |
| 3. | | |
| 4. *(optional)* | | |
| 5. *(optional)* | | |

15. Which competitor's social media presence do you most admire and why?
16. Which competitor's approach do you want to be clearly different from?

---

### Section 5: Content Goals

17. Tick all content goals that apply to your business:
    - [ ] Brand awareness — more people knowing who you are
    - [ ] Lead generation — driving enquiries, sign-ups, or bookings
    - [ ] Customer retention — keeping existing customers engaged
    - [ ] Event or product promotion — announcing specific launches or events
    - [ ] Community building — creating a loyal, engaged following
    - [ ] Recruitment — attracting talent
    - [ ] Thought leadership — positioning your team as industry experts
    - [ ] Other *(please specify)*

18. If you had to choose just one primary goal, which would it be?

---

### Section 6: Tone of Voice

19. Choose three adjectives that best describe how your brand should sound on social media:

   Example words to choose from (or provide your own): *Professional, Warm, Bold, Friendly, Authoritative, Approachable, Energetic, Calm, Innovative, Traditional, Playful, Serious, Inspiring, Practical, Premium, Accessible*

   Your three words: _________________ / _________________ / _________________

20. List two or three brands — anywhere in the world — whose social media tone you admire. What do you like about each?
21. List two or three brands whose tone you absolutely do NOT want to sound like. What puts you off?

---

### Section 7: Brand Guidelines

22. Do you have existing brand guidelines? *(Yes / No / In progress)*
23. Logo files available? *(Yes — please share / No — we will work with what you have)*
24. Brand colours: *(Provide hex codes if known, e.g. #1A73E8; or describe: "dark green and gold")*
    - Primary colour: _______________
    - Secondary colour: _______________
    - Accent colour *(if any)*: _______________
25. Fonts: *(Name the fonts used in your brand, if known)*
    - Heading font: _______________
    - Body font: _______________
26. Are there any visual styles you want to avoid? *(e.g. certain colours, stock photography, cluttered layouts)*

---

### Section 8: Posting Frequency and Expectations

27. How often do you expect content to be posted per week, per platform? *(Your expectation)*
28. Are there particular days or times you believe your audience is most active?
29. Do you have a content calendar already, or will one need to be built from scratch?

---

### Section 9: Budget for Paid Social Media

30. Do you have a budget available for paid social media advertising (boosted posts, Facebook/Instagram ads)?
    - [ ] No budget at this stage
    - [ ] Under $200 per month
    - [ ] $200–500 per month
    - [ ] $500–1,000 per month
    - [ ] $1,000+ per month
    - [ ] Not sure yet — I would like guidance on what is appropriate

31. If yes, is the budget intended for boosting organic content, running dedicated ad campaigns, or both?

---

### Positioning Questions

**USP / Differentiation:**
> "What is the one thing your business does or delivers that your closest competitor does not — or cannot — do as well?"

**Mission:**
> "In one sentence: what does your business do, for whom, and what outcome does it deliver?"

**Vision:**
> "Where do you want this business to be in three years? What does success look like specifically?"

**Niche:**
> "Describe your single most ideal client — their sector, size, location, and the specific problem they have that you solve best."

*These answers feed directly into `biz-dev-positioning` and all strategy and content work. Collect them at intake and store in the client file.*

---

### Section 10: Internal Approval Workflow

32. Who must approve content before it is published? *(Name and role)*
33. What is the expected turnaround time for approvals? *(e.g. 24 hours, 48 hours)*
34. Will approvals happen via a shared tool (e.g. Google Drive, Trello, email), or do you have a preferred method?
35. Are there multiple approval stages? *(e.g. team lead reviews first, then director approves)*

---

### Section 11: Content Restrictions

36. Are there any topics your business must never post about on social media?
37. What is your policy on mentioning competitors? *(Never / Only positively / Can reference if factual)*
38. Does your business operate in a regulated industry? *(e.g. financial services, healthcare, alcohol, legal services, education)* If yes, are there specific disclaimers or compliance requirements that apply to social media content?
39. Are there any past incidents — public complaints, PR issues, or sensitive situations — that the content team should be aware of?

---

### Section 12: Reporting Preferences

40. How often would you like to receive performance reports? *(Weekly / Fortnightly / Monthly)*
41. What format do you prefer for reports? *(PDF summary / Shared Google Doc / In-person review meeting / All three)*
42. Who should receive reports? *(Names and email addresses)*
43. What metrics matter most to you? *(e.g. follower growth, engagement rate, reach, website clicks, leads generated)*

---

## Part B: Outputs — Generate After Questionnaire is Complete

Once the questionnaire is filled in, generate the following two documents in order.

---

### Output 1: Full Client Brief Document

Structure the completed brief as a professional document with the following sections. Write in full sentences where appropriate; use tables for structured data.

1. **Business Overview** — name, industry, founding year, size, location, unique value proposition, 12-month business goal
2. **Target Audience** — primary and secondary audience profiles using the demographics provided; note whether B2B, B2C, or both
3. **Social Media Presence** — reproduce the platform table with a one-line consultant commentary on each active platform
4. **Competitors** — named competitors with handles; note the one the client most admires and the one they want to differ from
5. **Content Goals** — primary goal in bold; all secondary goals listed; note any tensions between goals
6. **Tone of Voice** — three brand adjectives; admired brands summary; brands to avoid and why
7. **Brand Guidelines** — colours, fonts, logo status; note any visual restrictions
8. **Posting Frequency** — client's expectation vs. the consultant's recommended starting frequency (see note below)
9. **Budget for Paid Social** — selected budget band; intended use
10. **Approval Workflow** — approver name and role, turnaround time, approval method
11. **Content Restrictions** — topics to avoid, competitor mention policy, regulatory constraints, any past issues to be aware of
12. **Reporting Preferences** — frequency, format, recipients, priority metrics

**Posting frequency guidance note:** Where the client's expectation is unrealistic, flag it professionally. Recommended starting frequencies for Uganda/EA market:
- Facebook: 4–5 posts per week
- Instagram: 3–4 posts per week
- LinkedIn: 2–3 posts per week
- TikTok: 3–5 short videos per week
- WhatsApp: 1–2 broadcast messages per week (not daily)

---

### Output 2: Client At-a-Glance Card

Generate immediately after the full brief. Format as a compact one-page summary for the wider team. Include:

| Field | Content |
|---|---|
| **Business name** | |
| **Industry** | |
| **Location** | |
| **Active platforms** | *(list with handles)* |
| **Primary goal** | |
| **Secondary goals** | |
| **Tone in three words** | |
| **Approval contact** | *(name, role, turnaround time)* |
| **Content restrictions** | *(one line per restriction)* |
| **Posting targets** | *(per platform — recommended frequency)* |
| **Paid budget band** | |
| **Report recipient(s)** | |

Add a **Consultant Notes** field at the bottom: flag any ambiguities, missing information, or follow-up questions that need resolving before strategy work begins.

---

## Quality Criteria

- Both outputs are generated from the same completed questionnaire — no information is contradicted between the two documents
- The full brief covers all twelve sections; no section is skipped or left empty without a clear note explaining why
- Posting frequency recommendations are grounded in Uganda/EA platform norms, not generic global benchmarks
- Content restrictions are stated plainly and unambiguously so any team member can act on them without seeking clarification
- Tone adjectives are carried forward accurately and will be usable by the `04-brand-voice-intake` skill
- The at-a-glance card fits a single page; no section contains more detail than is needed for quick reference
- British English spelling is used throughout; tone follows the `east-african-english` skill
- The consultant notes field in the at-a-glance card identifies at least one follow-up item where information is missing or unclear

## Pre-brief filter (added 2026-05-04 from Levy + Deacon)

Three checks to apply during intake — before scoping or pricing:

### 1. Top-10 Not-UX-Strategies anti-pattern check (Levy)

See `docs/ux-foundations.md` Section 2 for the full list. During intake, score the client's stated goal against the Top-10. If the goal matches any anti-pattern, push back before scoping. Document the pushback in the brief itself under a "Brief filters applied" subsection so future audits can trace the conversation.

Most common matches in social-media intakes:
- "We need a killer Instagram strategy" → matches #1 (a killer idea) — push back, ask what problem the client is solving
- "We want viral content" → matches #5 (motivational generic) — push back, ask which persona for what action
- "We just need posts that look like [trending brand]" → matches #4 (buzzword permutation) — push back, ask what differentiated promise

### 2. Three Levels of UX Scope declaration (Deacon)

Every brief must declare which level the engagement targets:

- **Single Interaction** — one platform, one campaign, one task. Most engagements live here.
- **Journey** — multi-channel, multi-device, time-sequenced (e.g., social → email nurture → website). Opt-in upgrade.
- **Relationship** — overall brand experience across all touchpoints. Rare; treat as a separate engagement bundle.

Add the level declaration as a required field in the intake questionnaire and the at-a-glance card.

### 3. Field-of-Dreams flag (Levy)

If the brief contains no validated user research and no plan to acquire it, mark the brief as "speculative" rather than "execution-ready." This affects pricing — speculative work cannot be priced as a delivery engagement; it must be priced as a discovery engagement first.

If the client refuses discovery and demands execution-priced delivery on a speculative brief, decline the work or document the risk acceptance in writing.

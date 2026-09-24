---
name: playbook-pr-publicity
description: Use when designing or improving a Pr Publicity operating playbook with roles, ordered actions, controls and measures. Use platform skills for channel plans and strategy skills for upstream direction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# PR and Publicity Playbook

<!-- dual-compat-start -->
## Use When
- Build or improve a repeatable Pr Publicity workflow for a client or delivery team.
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
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Pr Publicity playbook plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| A story is promotional but lacks public relevance or proof | Rework the angle or do not pitch | Wasting journalist trust |
| Inputs and authority are complete | Produce an execution-ready playbook | Unowned actions and hidden assumptions |
| Evidence or tooling is incomplete | Produce the narrowest qualified draft and a gap list | Treating an unassessed check as passed |
| Action publishes, spends, contacts people or changes production state | Require explicit approval before action | Unauthorised external impact |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply the decision rules, preserve useful existing material and draft the Pr Publicity playbook.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Pr Publicity playbook | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
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

Before generating any deliverable, ask for:
- Client business name
- Industry / sector
- Country or city (default: Uganda / East Africa)
- Primary goal (e.g., launch coverage, sustained brand awareness, thought leadership)
- Any existing media relationships or past coverage

---

## Part 1 — What Counts as News

Apply this filter before writing anything.

**Worth pitching:**
- A new product, service or business launch
- A milestone (first client, a customer count, an anniversary, an award)
- A survey, study or data set the client ran or commissioned
- A provable "first" or "largest" in the category
- A link to a current national or regional story
- A human story (client change, founder origin, community impact)
- A well-argued contrarian view on a sector issue (handled carefully)
- A partnership, expansion or change that affects the public

**Not worth pitching:** routine promotions or price cuts; internal appointments with no public significance; "we're excited to announce" with no reason for the reader to care; routine product updates.

---

## Part 2 — The Standard News Release

    FOR IMMEDIATE RELEASE

    [HEADLINE — active voice, outcome-led, present tense]
    [SUBHEADLINE — one sentence adding what the headline leaves out]

    [City], [Date] — [Lead: who, what, when, where, why — most important fact first.
    Two sentences at most. Do not open with the company name.]

    [Paragraph 2: supporting detail and why it matters to the reader.]

    [Paragraph 3: a quote from a named spokesperson that adds information.]

    [Paragraph 4: further detail, data or background.]

    [About [Company Name]: two or three sentences.]

    For more information:
    [Contact name] · [Email] · [Phone] · [Website]

    ###

**Rules:** most important fact first, then descending importance; active voice; body under 400 words; one quote from a named person, never "a spokesperson said"; every claim verifiable; send as plain text in the email body or as a PDF, not an editable document; never write it as an advertisement.

---

## Part 3 — The Publicity Kit

| Component | Purpose |
|---|---|
| Biographical profile | Who the spokesperson is — third person, about 200 words |
| Company description | What the business does, for whom, since when — about 100 words |
| Product or service overview | One page on key offers and differences |
| Fact sheet | Founding date, team size, clients served, verified results |
| Photography | Headshot and product or service images at print resolution (300 dpi minimum) |
| Past coverage | Links or copies of published coverage |
| Story angles | Three to five headline-length ideas |
| Suggested questions | 10–15 questions a journalist might ask |

**Delivery:** one PDF or one tidy shared folder, never a string of separate attachments.

---

## Part 4 — Pitching Journalists

### Query Letter Structure

    Paragraph 1 — Hook: why this story, why now (a trend, season or issue). One or two sentences.
    Paragraph 2 — Story: the angle, and what the reader will learn or feel. Two or three sentences.
    Paragraph 3 — Why us: credentials or unique position to speak. One or two sentences.
    Paragraph 4 — Practicalities: length, interview availability, materials (data, cases, photos).
    Sign-off: name, title, phone, email.

The letter fits on one printed page.

### Media-Relations Operating Checklist

The engine's own grouping of standard publicity practice (drawing on Hahn, 2003; Pinskey, 1997; Edwards et al., 1991).

| Area | Practice |
|---|---|
| Target | Read the outlet before pitching; pitch the reporter who covers the beat, not the editor-in-chief; start with trade press before consumer press |
| Angle | Give every release a news hook; make the client the local or specialist angle on national news; turn client successes into human stories (with consent); plan anniversaries, milestones and firsts in advance |
| Create news | Publish original research or a survey; create a transparently judged award, index or ranking; host a panel, launch or public debate that is itself news |
| Format | Standard release format (Part 2) and inverted-pyramid writing; an always-current publicity kit (Part 3) |
| Timing | Match editorial calendars and news cycles; offer one outlet a 48–72-hour exclusive on a major story; answer journalists on deadline immediately |
| Relationships | Build them before you need them (read and share their work, attend media events); follow up once by phone about 48 hours after sending |
| Expert voice | Position the spokesperson as an on-call expert source; write signed opinion pieces of 600–800 words with no advertising; register with journalist-request services (check each service's current name and terms before recommending it) |
| Integrity | Never lie or spin; credibility with media takes years to build and one day to lose |

---

## Part 5 — Publicity Calendar

Build a 12-month calendar:

| Month | News hook or angle | Release / pitch type | Target media | Lead time |
|---|---|---|---|---|
| January | New-year plans and school-term opening | Opinion piece | Business press | 2 weeks |
| February | Seasonal campaign (Valentine's) | Feature pitch | Lifestyle / consumer | 3 weeks |
| ... | ... | ... | ... | ... |

**Rules:** at least two or three newsworthy moments per quarter; allow three to four weeks' lead time for print; mark national holidays, budget reading, sector events and other natural hooks.

---

## Part 6 — Earned Media Tracking

| Date | Outlet | Story type | Journalist | Status | Link / clip | Estimated reach |
|---|---|---|---|---|---|---|

Review monthly and calculate:
- **Earned impressions** = sum of reach for published coverage (state the source of each reach figure)
- **Advertising value equivalent** = cost of equivalent paid space at rate card — report only as context, never as a measure of outcome
- **Share of voice** = the client's mentions ÷ all category mentions in tracked outlets

---

## Quality Criteria

Good output from this skill:
1. Every release passes the "would a journalist run this?" test
2. Releases follow the standard format — inverted pyramid, no advertising language
3. The publicity kit contains all eight components at the stated lengths
4. The query letter fits on one page and has a genuine time-sensitive hook
5. The 12-month calendar names real, specific news moments, not generic "brand awareness"
6. Media targets are named outlets or outlet types relevant to the client's sector and geography
7. All content uses the professional register defined in `east-african-english`

---

## References

- Hahn, F.E. (2003) *Do-It-Yourself Advertising and Promotion*, 3rd edn. Hoboken: Wiley.
- Edwards, P., Edwards, S. and Douglas, L.C. (1991) *Getting Business to Come to You*. Los Angeles: Tarcher.
- Pinskey, R. (1997) *101 Ways to Promote Yourself*. New York: Avon Books.

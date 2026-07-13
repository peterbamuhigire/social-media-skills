---
name: playbook-employee-advocacy
description: Use when designing or improving a Employee Advocacy operating playbook with roles, ordered actions, controls and measures. Use platform skills for channel plans and strategy skills for upstream direction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Employee Advocacy Programme Playbook

<!-- dual-compat-start -->
## Use When
- Build or improve a repeatable Employee Advocacy workflow for a client or delivery team.
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
If accounts, files, network, rendering or current evidence are unavailable, return the narrowest useful qualified Employee Advocacy playbook plus an evidence-gap list. Mark each unavailable check `not assessed`; never convert it into a pass.

## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| Participation is pressured or the disclosure is unclear | Make participation voluntary and provide disclosure wording | Coerced or deceptive advocacy |
| Inputs and authority are complete | Produce an execution-ready playbook | Unowned actions and hidden assumptions |
| Evidence or tooling is incomplete | Produce the narrowest qualified draft and a gap list | Treating an unassessed check as passed |
| Action publishes, spends, contacts people or changes production state | Require explicit approval before action | Unauthorised external impact |

## Workflow
1. Confirm the consumer, objective, market, decision owner and permission boundary; stop if the objective or owner is missing.
2. Inspect supplied evidence and verify volatile claims; record missing inputs rather than filling them with assumptions.
3. Apply the decision rules, preserve useful existing material and draft the Employee Advocacy playbook.
4. Test each action against platform, privacy, safeguarding, brand and approval constraints; stop and escalate a blocking risk.
5. Run the quality and anti-slop gates. If a check fails, correct the draft and rerun it before handoff.

## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Employee Advocacy playbook | Client owner and delivery team | Uses named inputs, assigns actions, states decisions and contains no unverified specifics |
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

1. **Client business name and industry** — e.g. Kampala accounting firm, Nairobi logistics company, NGO
2. **Country/city** — default: Uganda / East Africa
3. **Number of employees and approximate social media activity level** — e.g. "30 staff, most active on WhatsApp and Facebook; 8 have LinkedIn profiles"
4. **Primary platform(s) where employees are active** — LinkedIn, Facebook personal profiles, WhatsApp, X/Twitter
5. **Business objective** — brand awareness, recruitment, thought leadership, sales support, or a combination
6. **Any existing social media policy for employees** — share if available; note if none exists
7. **Voluntary or part of job expectations** — this determines programme design, tone, and incentive structure

---

## Section 1 — The Case for Employee Advocacy

Employees' combined social networks typically reach 10× more people than the brand's owned channels. When an employee shares a company post, it reaches an audience that would never see the brand's official content — and it arrives with the social trust of a personal connection rather than the commercial intent of a brand advertisement. For a business with 20 employees each having 200–500 Facebook connections, the potential reach from one coordinated post exceeds 10,000 people — at zero additional ad cost. This positions employee advocacy firmly in the Earned Media category of the POEM model (Paid/Owned/Earned), making it one of the highest-ROI activities in a social media programme.

In Uganda and East Africa, professional reputation is deeply personal. A professional who is well-regarded on LinkedIn or active in WhatsApp professional networks carries institutional credibility that no brand page can replicate. Employee advocacy in this context is not just about reach — it is about credibility transfer. When a senior accountant shares the firm's thought leadership content, their network of fellow professionals takes it more seriously than any brand post. For B2B clients and professional services firms, this distinction is significant: advocacy by credible staff members directly supports the Reach and Act stages of the RACE framework (Chaffey, 2024).

---

## Section 2 — Programme Design

Make these five decisions before launching the programme.

### 1. Voluntary vs Required

Recommendation: voluntary participation with clear incentives is more sustainable than mandatory sharing. Mandatory advocacy tends to produce low-quality, unenthusiastic posts that damage rather than help the brand — audiences recognise compelled content. Make participation easy and rewarding, not compulsory. If the client insists on a requirement, frame it as a professional development expectation rather than a compliance rule.

### 2. Platform Focus

Match the programme to where employees are already active:

| Platform | Best fit |
|---|---|
| LinkedIn | B2B, professional services, NGOs, formal sector clients |
| Facebook personal profiles | Consumer brands, SMEs, retail, community-facing businesses |
| WhatsApp | Relationship-led sales, professional referral networks, warm outreach |
| X/Twitter | Employees who are opinion leaders, public sector professionals, journalists |

Do not ask employees to join a platform they do not currently use. Start where they already have an audience.

### 3. Content Provision

Never ask employees to create content from scratch — this is the single most common reason advocacy programmes fail. Provide ready-to-share content:

- Pre-written LinkedIn/Facebook post drafts in 2–3 versions per piece — let employees choose the tone that fits their voice
- Pre-approved images or graphics sized for each platform (note: image production is out of scope — brief the design team separately)
- A simple sharing instruction alongside each post: "Copy this, personalise the opening line if you wish, then post on LinkedIn"
- For WhatsApp: a short forwarding message suitable for professional groups, 2–3 sentences maximum

### 4. Incentive Structure

Include at least one non-monetary and one tangible option:

- **Recognition:** "Employee Advocate of the Month" — a public shout-out on the brand's page and at the monthly team meeting
- **Priority access:** Advocates receive early access to company news, new product launches, or internal training before the general announcement
- **Tangible reward:** UGX 20,000–50,000 airtime or data top-up for the top advocate each month — a meaningful, low-cost incentive in the Ugandan context
- **Career benefit:** Frame advocacy as a professional development activity. LinkedIn reach builds the employee's personal brand, not just the company's. Make this argument explicitly during the programme launch.

### 5. Measurement

Track monthly:

- Number of employees who shared at least one piece of content
- Total estimated reach of shares — sum of participating employees' connection/follower counts × 10% average organic reach factor
- Engagement on shared posts — likes, comments, shares/reposts
- Referral enquiries or leads attributed to employee shares (where trackable)

Set SMART objectives at launch (Bodnar and Cohen, 2012): e.g. "By Month 3, at least 10 of 30 employees share one piece of content per month, generating an estimated combined reach of 15,000 per post."

---

## Section 3 — Content Pack System

Prepare a monthly Advocacy Content Pack for all participating employees. Deliver it via the programme's shared WhatsApp group, a monthly email, or a shared Google Drive folder — whichever the client's team will actually use.

**Content Pack template:**

```
[COMPANY NAME] Employee Advocacy Pack — [Month YYYY]

This month's themes: [Theme 1], [Theme 2]

─────────────────────────────────────────
POST 1 — LinkedIn / Facebook

Option A (formal tone):
[Full post text, ready to copy. 100–150 words. Include a hook, body, and call to action.]

Option B (casual tone):
[Same message, warmer register. 80–100 words. More personal, conversational opener.]

Image: [Attach image file or share Canva link — brief design team separately]
Hashtags: #[BrandHashtag] #[Industry] #Uganda
Note: Add your personal perspective at the start if you wish — posts with a personal
opener consistently outperform straight brand shares.

─────────────────────────────────────────
POST 2 — LinkedIn / Facebook

Option A (formal tone):
[Full post text — 100–150 words]

Option B (casual tone):
[80–100 words]

Image: [Attach or link]
Hashtags: #[BrandHashtag] #[Industry] #Uganda

─────────────────────────────────────────
QUICK SHARE — WhatsApp (for professional networks and groups)

[Short forwarding message, 2–3 sentences. Suitable for dropping into a professional
WhatsApp group. No hashtags. Conversational. Ends with the company's contact or link.]

─────────────────────────────────────────
This month's advocate leaderboard will be shared on [Date].
Questions? Message [Advocacy Coordinator Name] on WhatsApp.
```

Generate a new Content Pack each month. Align themes with the broader content calendar produced in `11-content-calendar/SKILL.md`.

---

## Section 4 — LinkedIn-Specific Guidance

For B2B clients where LinkedIn is the primary advocacy platform, apply the following before and during the programme.

**Profile completion first.** Encourage all participating employees to complete their LinkedIn profiles before asking them to advocate. An incomplete or blank profile undermines the credibility the advocacy is intended to build. An employee sharing a thought leadership post from a profile with no photo and an empty summary does more harm than good.

**LinkedIn profile essentials for East African professionals:**

- Professional photo — a clear headshot, not a WhatsApp group photo cropped from a party
- Headline — not just the job title; include a value statement: "Helping SMEs grow through clean energy | Engineer, [Company Name]"
- Summary — 3–5 sentences covering expertise, professional passion, and what the employee brings to their sector
- Current role — with the company listed and the company page linked, so the logo appears and the connection to the brand is visible
- At least three skills endorsed and, where possible, one recommendation

**Algorithm note.** Personal posts on LinkedIn receive 3–5× more organic reach than equivalent posts from a company page. This is the structural reason why employee advocacy outperforms boosted brand content on LinkedIn — explain this clearly to the client and to participating employees. It is not a workaround; it is how the platform is designed.

**Engagement timing.** Advise employees to leave a comment on the post they have shared within the first hour of posting. LinkedIn's algorithm surfaces posts that attract early engagement; a comment from the author (or a colleague) in the first 60 minutes materially increases the post's reach to the employee's connections.

---

## Section 5 — Programme Launch

Introduce the programme to employees in this sequence:

1. **Brief the leadership team first.** Advocacy must be seen as a leadership initiative, not an HR or marketing task. If the managing director or country director is not visibly behind it, participation will be low.

2. **Run a 30-minute internal session.** Cover: what employee advocacy is, why it benefits employees personally (it builds their professional profile, not just the company's), what participation involves, how content will be provided, and how advocates will be recognised. Keep it practical and low-pressure.

3. **Start with a pilot group.** Identify 3–5 enthusiastic, social-media-active employees and run the programme with them for the first month before rolling out to all staff. Use their results as proof of concept for the wider team.

4. **Celebrate early wins publicly.** Share screenshots of high-engagement employee posts in the internal WhatsApp group or at team meetings. Name the employee and acknowledge the reach. This creates social proof inside the organisation.

5. **Review quarterly.** Assess: Is participation growing month on month? Which content types generate the most employee sharing and engagement? Are any departments or roles under-represented? Adjust the Content Pack format, incentive structure, or delivery method accordingly.

---

## Section 6 — Policy and Guidelines

Employee advocacy without clear guidelines creates reputational and legal risk. Provide a one-page guidelines document to all participants at programme launch. Include the following:

- Always clearly associate yourself with [Company Name] when posting about the company — do not share company content anonymously or without attribution
- Never share confidential client information, financial data, personnel matters, or unreleased product or service details
- Do not comment on legal disputes, regulatory investigations, or allegations involving competitors — refer any such enquiries immediately
- If a journalist, media outlet, or public figure contacts you via social media about the company, refer them to [Name and contact details] — do not respond on behalf of the company
- Your personal opinions are your own — make this clear when posting personal views alongside brand content; use phrases such as "My own view:" or "Speaking personally:"
- If in doubt about whether something is appropriate to share, ask [Advocacy Coordinator] before posting

For a full employee social media policy template, use `playbook-social-media-policy/SKILL.md`.

---

## Quality Criteria

Output from this skill meets the standard when:

- The voluntary vs required decision is explicitly addressed and the recommendation is justified with reference to content quality and employee motivation
- The platform selection is matched to where the client's employees are demonstrably active — not imposed based on consultant preference
- The Content Pack template is complete, correctly formatted, and ready to hand to the client for immediate use
- LinkedIn profile guidance includes the East African professional context and the specific algorithm explanation for why personal posts outperform company page posts
- The incentive structure includes at least one non-monetary option (recognition, early access, career framing) alongside any tangible reward
- The launch plan specifies a pilot group approach before full rollout, with a clear sequence of steps
- Policy guidelines are included with a cross-reference to `playbook-social-media-policy/SKILL.md`, and cover confidentiality, media enquiries, and personal opinion disclosure

---

## References

| Resource | When to use |
|---|---|
| `playbook-social-media-policy/SKILL.md` | Generate a full employee social media policy to accompany the advocacy guidelines |
| `strategy-personal-brand/SKILL.md` | When the client wants to develop individual employees as thought leaders, not just sharers |
| `platform-linkedin/SKILL.md` | For a full LinkedIn strategy when LinkedIn is the primary advocacy platform |
| `04-brand-voice-intake/SKILL.md` | Ensure Content Pack drafts are written in the client's approved brand voice |

**Cited works:**
- Bodnar, K. and Cohen, J. (2012) *The B2B Social Media Book*. Hoboken: Wiley.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. 8th edn. Harlow: Pearson.

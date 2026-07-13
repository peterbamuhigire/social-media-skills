---
name: 03-audience-personas
description: "Use when developing research-grounded audience personas after discovery and before channel planning. Produces persona cards and comparison matrix; use `04-brand-voice-intake` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Audience Persona Generator

Develop 2–4 audience personas for the client. Personas are the strategic foundation for every channel, content, and messaging decision. Base personas on the completed client brief, platform audit findings, and East African consumer behaviour knowledge. Where client data is thin, apply industry knowledge and flag every assumption explicitly. Apply the `east-african-english` skill for tone throughout.


<!-- dual-compat-start -->
## Use When

- Use this skill for developing research-grounded audience personas after discovery and before channel planning.
- Confirm that `04-brand-voice-intake` is not the closer route before proceeding.

## Do Not Use When

- Use `04-brand-voice-intake` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Approved client brief plus primary or cited secondary audience evidence | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Persona cards and comparison matrix | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified persona cards and comparison matrix. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Approved client brief plus primary or cited secondary audience evidence is current and attributable | Produce the full persona cards and comparison matrix and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `04-brand-voice-intake` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `04-brand-voice-intake` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the persona cards and comparison matrix, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the persona cards and comparison matrix without approved client brief plus primary or cited secondary audience evidence. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `04-brand-voice-intake` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified approved client brief plus primary or cited secondary audience evidence, the skill produces a persona cards and comparison matrix with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`04-brand-voice-intake`](../04-brand-voice-intake/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Input

Ask for the following before generating any personas:

- **Completed 01-client-brief** — essential; personas cannot be accurate without the audience demographics, tone preferences, and competitor context it contains
- **Client industry** — be specific (e.g. "private healthcare clinic", "mid-range restaurant chain", "B2B logistics software")
- **Target market** — B2C, B2B, or both; note any sub-segments if provided
- **Existing customer data** — even rough data is valuable: WhatsApp broadcast list size, past customer records, walk-in demographics, any survey results the client has conducted
- **Country / city** — defaults to Kampala, Uganda if not specified; adjust EA consumer behaviour notes for Kenya or Tanzania if relevant

If the client brief is unavailable, ask for: business name, industry, primary audience description, and the client's three brand tone adjectives before proceeding.

---

## Uganda / East Africa Consumer Behaviour — Apply to All Personas

Apply these EA-specific behavioural facts when building each persona. These are baseline truths, not stereotypes — adjust for income level, urban vs. rural, and age cohort as appropriate.

**Platform behaviour:**
- WhatsApp is the primary communication channel across all income levels. Business enquiries, referrals, and purchase decisions frequently happen via WhatsApp groups and direct messages.
- Facebook reaches the broadest demographic: urban and peri-urban, 18–55+, across all income levels.
- Instagram skews younger (18–35), urban, aspirational. Visual content and lifestyle imagery perform well.
- TikTok is fast-growing among 16–30 year olds. Entertainment-first; educational and behind-the-scenes content also performs.
- LinkedIn is used by professionals, NGO workers, senior management, and formal sector employees. B2B audiences are most reachable here.
- YouTube is a research and tutorial platform — how-to content, product reviews, and long-form storytelling.
- X/Twitter reaches journalists, public figures, opinion leaders, and politically engaged audiences.

**Consumption habits:**
- Mobile-first: the vast majority of content is consumed on smartphones. Assume small screens, vertical content, and limited data.
- Data consciousness: avoid recommending content formats that consume excessive data (long autoplay videos without captions).
- Peak usage times in Uganda: 7–9 am (morning commute or pre-work), 12–2 pm (lunch break), 7–10 pm (evening).

**Purchasing behaviour:**
- Trust is built through community endorsement, word-of-mouth, and social proof. A recommendation from a peer or a visible WhatsApp group member carries more weight than an advertisement.
- Price sensitivity is high across most consumer segments. Value messaging — what you get for what you pay — consistently outperforms aspirational status messaging for mass-market products.
- Premium and aspirational messaging is effective for upper-middle and high-income segments in specific categories: fashion, restaurants, travel, professional services.
- Localisation matters: content in local language (Luganda, Swahili) or referencing local places and events drives higher engagement than generic international content.

---

## Persona Structure — Complete All Fields for Each Persona

Generate one persona per section. Number each persona and give it a name and archetype before starting the detail.

---

### Persona [N]: [Name] — "[Archetype Label]"

**Archetype label examples:** "The Ambitious Professional", "The Cost-Conscious Household Manager", "The Growth-Minded SME Owner", "The Trend-Aware Young Urban", "The Cautious First-Time Buyer", "The Loyal Repeat Customer". Choose or create an archetype that is specific to the client's industry and market — do not use generic labels.

---

**Demographics**

| Field | Detail |
|---|---|
| Name | *(Ugandan/EA name — realistic for the market; e.g. Harriet, Brian, Fatuma, Ronald, Aisha)* |
| Age | *(Specific range, e.g. 28–35)* |
| Gender | *(State if relevant to the persona; note if gender is not a differentiating factor)* |
| Location | *(City and neighbourhood where relevant, e.g. "Kampala — Ntinda / Bukoto area")* |
| Income level | *(e.g. "UGX 1.5M–3M per month / middle income")* |
| Education | *(e.g. "University degree, Makerere or private university")* |
| Occupation | *(Specific role and sector, e.g. "Marketing officer at an NGO")* |
| Household | *(e.g. "Renting with one flatmate; not yet married")* |

---

**Platform Usage**

| Platform | Uses it? | Frequency | Peak time | How they use it |
|---|---|---|---|---|
| WhatsApp | | | | |
| Facebook | | | | |
| Instagram | | | | |
| TikTok | | | | |
| LinkedIn | | | | |
| YouTube | | | | |
| X / Twitter | | | | |

Note the one or two platforms where this persona is most reachable and most likely to act on content.

---

**Content They Engage With**

List 3–5 specific content types with concrete examples relevant to the client's industry:

1. [Content type] — [Example: "Before-and-after posts showing visible results from a skincare product"]
2. [Content type] — [Example: "Short how-to videos explaining how to use a banking app feature"]
3. [Content type] — [Example: "Customer testimonials from people who visibly resemble this persona"]
4. [Content type] *(optional)*
5. [Content type] *(optional)*

---

**Pain Points**

Three genuine frustrations related to the client's product or service category. Make these specific — not generic. A pain point for a private clinic persona is not "I want to be healthy"; it is "I waste a full morning at the government hospital for a condition that should take 20 minutes to treat."

1. [Specific, realistic frustration]
2. [Specific, realistic frustration]
3. [Specific, realistic frustration]

---

**Goals**

Three things this persona is actively trying to achieve — not aspirations, but concrete goals they would articulate themselves:

1. [Concrete, specific goal]
2. [Concrete, specific goal]
3. [Concrete, specific goal]

---

**Triggers to Follow a Brand**

What causes this persona to tap "Follow" or "Like" a page? List 3–5 specific triggers:

- [Trigger, e.g. "A friend or colleague has already liked the page — social proof from their network"]
- [Trigger]
- [Trigger]
- [Trigger] *(optional)*
- [Trigger] *(optional)*

---

**Triggers to Unfollow a Brand**

What causes this persona to leave? List 3–5 specific triggers:

- [Trigger, e.g. "Too many promotional posts in a row with no useful or entertaining content"]
- [Trigger]
- [Trigger]
- [Trigger] *(optional)*
- [Trigger] *(optional)*

---

**How the Client's Product or Service Fits Their Life**

Write one paragraph (4–6 sentences). Be specific to this persona's daily life and circumstances — do not write generic marketing copy. Explain what problem the client solves for this person, when in their week they would think about it, and what it would feel like to have that problem solved. Ground this in the Uganda/EA context.

---

**Messaging That Resonates**

- **Tone:** [e.g. "Warm, practical, peer-to-peer — as if advice from a trusted colleague"]
- **Vocabulary:** [e.g. "Plain language; avoids corporate speak; occasional Luganda word or local reference lands well"]
- **Platforms:** [Primary platforms for reaching this persona]
- **Content style:** [e.g. "Short captions, strong visual hook, clear call to action — avoid long paragraphs"]
- **Proof type:** [e.g. "Real customer stories with photos; numbers and guarantees; endorsements from recognisable community figures"]

---

**Messaging to Avoid**

- [What feels inauthentic, e.g. "Overly polished stock photography — looks foreign and unrelatable"]
- [What alienates, e.g. "Price anchoring against premium international brands — this persona is price-conscious and it feels tone-deaf"]
- [What loses trust, e.g. "Vague promises without proof — 'the best in Uganda' without any evidence"]

---

**Assumptions Flag**

If any part of this persona is inferred rather than drawn from provided client data, list the assumptions clearly:

> *Assumption: Income level estimated based on industry norms for [occupation] in Kampala. Client to validate against actual customer records.*

---

## Output 2: Persona Summary Matrix

Generate immediately after all persona cards. Present all personas side by side for quick reference.

| Field | [Persona 1 Name] | [Persona 2 Name] | [Persona 3 Name] | [Persona 4 Name] |
|---|---|---|---|---|
| Archetype | | | | |
| Age | | | | |
| Location | | | | |
| Primary platform | | | | |
| Peak usage time | | | | |
| Primary pain point | | | | |
| Primary goal | | | | |
| Key message | *(one sentence)* | | | |
| Content format that works | | | | |
| What causes them to follow | | | | |
| What causes them to unfollow | | | | |

After the matrix, add a **Strategic note** (3–5 sentences): explain which persona should receive the most content investment and why, note any tensions between personas (e.g. Persona 1 wants premium positioning; Persona 2 needs value messaging), and identify one platform where two or more personas overlap and can be reached with shared content.

---

## How Many Personas to Generate

- **B2C, single product/service:** 2 personas (primary buyer, secondary influencer or gifter)
- **B2C, multiple products or broad audience:** 3 personas
- **B2B:** 2 personas (decision-maker, influencer or budget holder)
- **B2B and B2C combined:** 4 personas (2 per side)
- **If client data is very thin:** generate 2 personas and flag that additional personas should be developed after a customer interview programme

---

## Technology Adoption Lens

**Technology Acceptance Model — TAM (Hanlon and Tuten, 2022):** Apply TAM as a diagnostic framework within the persona research process. For each persona, assess two adoption variables:

- **Perceived Usefulness:** Does this digital service or platform help the persona achieve something they genuinely value? In EA contexts, this must be evaluated against real-world objectives — not assumed from demographics alone.
- **Perceived Ease of Use:** Can the persona actually use this without frustration? In Uganda and East Africa, digital literacy levels, device quality, connectivity cost, and trust in digital transactions create genuine adoption barriers that Western frameworks do not account for.

For each persona, specify: (1) which digital services and platforms they are likely to adopt, (2) which they are unlikely to adopt despite demographic fit, and (3) what the primary barrier is — usefulness gap, ease-of-use gap, or trust gap. This prevents strategies that assume adoption based on income or age alone.

**Generational Digital Trust Spectrum (Rageh, 2026):** Where personas span multiple generations — common for EA clients targeting both urban professionals and older family decision-makers — add a generational trust calibration layer to each persona. For each generational cohort represented, specify: what does this persona need to see before they trust a brand digitally?

- Gen Z: brand activism and algorithmic transparency
- Millennials: data control and privacy signals
- Generation X: institutional credentials and third-party endorsements
- Baby Boomers: personal service access and traditional authority signals

Consult `strategy-multigenerational-digital` for the full generational trust spectrum when the client's audience spans three or more generational cohorts. Do not apply a single trust-building approach uniformly across a multi-generational persona set.

---

## Quality Criteria

- Each persona reads as a real, specific individual — not a demographic average or a marketing archetype
- Pain points are grounded in the client's specific industry and the Uganda/EA market context; no generic pain points
- Platform usage tables are completed with realistic EA usage patterns; peak times align with the morning/lunch/evening framework documented in this skill
- The "how the client's product fits their life" paragraph is specific to this persona — it could not be copied to a different persona without rewriting
- All inferred data is flagged explicitly in the Assumptions Flag field; no invented data is presented as fact
- The persona summary matrix enables a team member to make a quick content decision without reading the full cards
- British English spelling throughout; tone follows the `east-african-english` skill
- The strategic note after the matrix identifies at least one concrete implication for content or channel prioritisation

## Persona discipline (added 2026-05-04 from Branson)

Canonical reference: `docs/ux-foundations.md` Section 1.

For research-grounded persona work specifically (this skill), the following rules apply on top of the shared discipline:

- **Choose ONE Essential Persona per audience cluster.** A 4-persona deliverable means 4 Essential Personas, not a blurred average. Document the choice and the reasoning.
- **Reject "edge-cased to death" feature requests.** When stakeholders ask "what if a user wants X?", answer: "Persona <name> doesn't need X." Use the persona's name, not "the user."
- **"Clingy" tactic for East African client engagements.** Include the persona's full name, photo placeholder, and one memorable quote on every page that references the persona — not just the persona card itself.
- **Mechanics floor.** Every persona must have name, demographics, goals, motivations, social/technical/physical environment, pain points, stress points (Synechron list).

If a stakeholder pushes back on the Essential Persona choice, walk them through `docs/ux-foundations.md` Section 1 ("Choosing the Essential Persona" subsection) — the design specifically for the right Essential Persona will at least work for the others; a design for any other won't necessarily work for the Essential.

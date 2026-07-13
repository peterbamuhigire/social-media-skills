---
name: meta-social-proof-system
description: "Use when collecting, verifying, governing and placing testimonials, reviews and other proof. Produces social-proof asset register and collection protocol; use `04-brand-voice-intake` when that neighbouring contract is the closer match."
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Social Proof System

**Source:** Bly (2018) *The Digital Marketing Handbook*

---


<!-- dual-compat-start -->
## Use When

- Use this skill for collecting, verifying, governing and placing testimonials, reviews and other proof.
- Confirm that `04-brand-voice-intake` is not the closer route before proceeding.

## Do Not Use When

- Use `04-brand-voice-intake` when its narrower output is requested.
- Do not publish, spend, change a live account, certify compliance, or invent missing client evidence.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Consent-backed proof sources, claims, audience objections and placement points | Client, approved systems, or dated platform exports | Yes | Stop the affected decision; request it or mark the field unknown and narrow the output. |
| Purpose, audience and approval boundary | Client brief or accountable owner | Yes | Return discovery questions; do not infer approval. |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Social-proof asset register and collection protocol | Client lead and next workflow owner | Every recommendation traces to an input, names an owner or next action, and marks assumptions and unassessed checks. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision and source register | Table in the deliverable | Each material claim records its source/date or is labelled unverified; missing evidence never becomes a pass. |

<!-- dual-compat-end -->

## Capability and permission boundary

Read and search access to the supplied artefacts are required; calculation or file-rendering capability is optional. Planning and drafting are read-only with respect to client accounts and source records. Editing the deliverable requires explicit authorisation; publishing, production mutation, destructive action, spend, and certification claims require separate explicit authority and evidence.

## Degraded mode

If files, platform access, network, rendering, fonts, or calculation tools are unavailable, return the narrowest useful qualified social-proof asset register and collection protocol. Mark each blocked check `not assessed`, state the consequence, and provide the exact evidence needed to resume. Never convert an unavailable check into a pass.

## Decision rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Consent-backed proof sources, claims, audience objections and placement points is current and attributable | Produce the full social-proof asset register and collection protocol and cite the evidence used. | Decisions based on stale or unrelated evidence. |
| A material input is missing or contradictory | Stop that decision, request clarification, or issue a labelled partial result. | Fabricated precision and false confidence. |
| The requested outcome belongs to `04-brand-voice-intake` | Route there and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Workflow

1. Confirm the requested decision, consumer, market, period and permission boundary; route to `04-brand-voice-intake` if its contract is closer.
2. Inventory the required inputs and their provenance. Stop any decision whose critical evidence is absent; recover by requesting it or recording a bounded assumption.
3. Apply the domain method in the core sections below, following the decision table whenever evidence conflicts or scope changes.
4. Verify calculations, dates, named platforms and claims against the supplied sources; label inference and uncertainty.
5. Produce the social-proof asset register and collection protocol, decision/source register and explicit next owner. Do not mutate live systems without separate authority.
6. Run the repository anti-slop ship gate. If a blocking factual, permission or evidence defect remains, fix it or withhold release.

## Quality Standards

The output is client-specific, uses British English and the stated market/currency, distinguishes observed fact from inference, exposes gaps, and gives a checkable acceptance condition. Recommendations must be feasible within the confirmed budget, capacity and permissions.

## Anti-Patterns

- Using an undated benchmark as the client's result. Fix: use account evidence or label the benchmark as a provisional comparator.
- Producing the social-proof asset register and collection protocol without consent-backed proof sources. Fix: stop the affected decision or issue a clearly bounded partial output.
- Treating missing access or data as a successful check. Fix: record `not assessed`, its risk and the recovery input.
- Absorbing `04-brand-voice-intake` into this workflow. Fix: route the neighbouring output and hand over verified inputs.
- Publishing, spending or editing a live account during planning or review. Fix: obtain separate explicit authority and retain action evidence.

## Worked example

Given verified consent-backed proof sources, the skill produces a social-proof asset register and collection protocol with source dates and named assumptions. If that evidence cannot be accessed, it returns only the supported sections plus a recovery list; it does not fill gaps with East African defaults.

## Read next

- [`04-brand-voice-intake`](../../pipeline/04-brand-voice-intake/SKILL.md) for the neighbouring contract.
- [`anti-ai-slop`](../../ai-marketing/anti-ai-slop/SKILL.md) during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md) at the release checkpoint.

## References

- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md)
- Follow the directly linked repository skills above and any domain references named in the core sections below. Verify current platform, price, legal and regulatory claims before use.

## Required Inputs

Ask for the following before generating any deliverable:

1. **Client business name**
2. **Industry**
3. **Country / city** (defaults to Uganda / East Africa)
4. **Primary goal** (e.g. increase website conversion rate, reduce sales objections, build credibility for a new product)
5. **Existing proof available** (list any: testimonials, certifications, awards, media mentions, client logos, review platform ratings)
6. **Target audience** (B2C or B2B; generational mix if known — see `strategy-multigenerational-digital`)
7. **Key conversion points** (where do prospects currently drop off — pricing page, proposal stage, checkout, first WhatsApp message?)

---

## Why Social Proof Works

Buyers are uncertain. Social proof reduces uncertainty by showing that others — people like the prospect — have made the same decision and benefited. In East Africa, where digital commerce is newer and first-time buyers are more cautious, social proof is especially important: it bridges the trust gap before the first transaction, reducing the risk the prospect perceives in buying from a business they found online.

---

## Bly's Six-Source Social Proof Taxonomy

Apply all six sources where available. The goal is breadth — multiple proof types from multiple categories outperform any single strong testimonial (Bly, 2018).

### 1. Customer Testimonials
Written or video reviews from real clients, with full name, organisation, and photo. The most common and most trusted source for service businesses.

**Collect:** after every successfully completed project or positive service interaction.
**Format:** video (self-recorded on a smartphone is acceptable and often more authentic than polished production); written as a fallback.
**Content template:** "In 2–3 sentences, describe: (1) the problem you had before working with us, (2) what we did together, and (3) the specific result you achieved."

### 2. Expert Endorsements
Recommendations from recognised authorities in the client's field: an industry association, a professor, a respected publication, a well-known consultant, or a regulatory body.

**Most valuable for:** B2B clients, professional services, healthcare, education.
**Collect:** request a quote from an industry association president, a university department head, or a sector publication after a notable piece of work.

### 3. Celebrity and Influencer Endorsements
Recommendations from public figures with large, relevant audiences.

**For EA clients:** local celebrities (musicians, athletes, media personalities, respected business leaders) often outperform international names because their audiences trust their judgement on locally relevant purchases.
**Caution:** See `08-influencer-marketing-strategy` and `ai-influencer-strategy` for vetting process. Do not deploy celebrity endorsements without verifying audience alignment and engagement authenticity.

### 4. Crowd Proof (Large Numbers)
Statements that use volume to signal popularity and safety: "Over 500 businesses served", "Trusted by 12,000 subscribers", "4.8 stars from 300 reviews".

**Rules:** Numbers must be genuine and significant. Do not fabricate or inflate. Do not use crowd proof if the numbers are not yet impressive — wait until they are, or use a different proof type.
**EA context:** In markets where digital reviews are less common, even 50 genuine reviews is significant social proof. State the number with context: "50 verified Google reviews — more than any other [industry] provider in [city]."

### 5. Peer Recommendations
Referrals from friends, colleagues, or professional networks. The highest-trust source and the hardest to manufacture.

**Design referral mechanics to activate peer proof at scale:**
- Referral codes or introduction incentives
- Client advocacy programmes (recognition, exclusive access, early offers)
- WhatsApp referral prompts sent after a positive interaction: "If you know anyone who could benefit from [service], we'd love an introduction."

### 6. Third-Party Certifications and Awards
ISO certifications, industry association memberships, award badges, media features ("As featured in [publication]", "Winner of [award] 2024").

**Most valuable for:** Generation X and Baby Boomer audiences, who place high weight on institutional credibility signals (Rageh, 2026).
**Display:** logos on website header, footer, and proposals. Refresh annually — expired certifications undermine rather than build trust.

---

## The Multiplicity Principle

Multiple sources of proof from multiple categories outperform a single strong testimonial (Bly, 2018). A prospect who sees a customer testimonial, a crowd-proof number, and an expert endorsement on the same page is more confident than a prospect who sees only one — even if that one testimonial is excellent.

**Target:** Deploy at least three proof sources on every primary conversion page.

---

## Proof Placement Strategy

| Touchpoint | Recommended proof types | Placement |
|---|---|---|
| Homepage | Crowd proof (total clients, star rating) + 2–3 short testimonials | Above the fold; visible without scrolling on mobile |
| Service pages | Expert endorsements + testimonials specific to that service | Adjacent to the service description and CTA |
| Proposals and credentials | Case studies (full story with context and result) + certifications | After the proposed solution; before pricing |
| Email campaigns | One testimonial per email | After the main offer; before the CTA |
| WhatsApp sales conversations | Screenshot of a relevant testimonial or review | When handling a price or quality objection |
| Checkout / payment page | Star rating + "X clients served" + a short reassurance quote | Alongside the payment form |

---

## Testimonial Collection Protocol

1. **Timing:** Ask within 48 hours of a positive client interaction — before the emotion fades. Response rates drop by approximately 80% if the request comes more than 48 hours after the positive experience.
2. **Channel:** Send the request via WhatsApp (highest open rate in EA) with a direct Google review link or a short video prompt.
3. **Template:** "Hi [Name], I'm glad the [project/service] went well. Could I ask a small favour? In 2–3 sentences, could you describe: (1) the challenge you had before we worked together, (2) what we did, and (3) the result you got? I'd like to feature your words on our website."
4. **Video option:** Offer a guided prompt for video testimonials: "Just record a 30-second voice note or video on your phone answering those three questions — no need to be formal."
5. **Consent:** Confirm consent before publishing — include name, organisation, photo, and platform use permissions. Document consent in writing (WhatsApp message confirmation is sufficient).

---

## Proof Asset Register

Maintain a living register of all proof assets. Minimum fields:

| Field | Content |
|---|---|
| Proof type | Bly category (testimonial, expert, crowd, peer, cert, celebrity) |
| Source name | Full name and organisation |
| Date collected | DD/MM/YYYY |
| Format | Written / video / screenshot |
| Topics covered | Which service or product does this proof relate to? |
| Approved for use | Yes/No/Restricted |
| Placement | Where is it currently deployed? |

Review and refresh the register quarterly. Archive proof that is more than 2 years old unless it references a long-standing track record.

---

## Quality Criteria

Output meets the standard for this skill if:

- All six Bly proof sources are addressed — the output recommends which are currently available, which to actively collect, and which are not yet applicable
- The multiplicity principle is applied — the strategy deploys at least three proof types on primary conversion pages
- Placement recommendations are mapped to specific touchpoints — homepage, service pages, proposals, email, and WhatsApp
- The testimonial collection protocol includes timing, channel, template, video option, and consent documentation
- A Proof Asset Register structure is included so the client can manage proof as a living asset
- EA-specific adaptations are present: WhatsApp as primary request channel, local celebrity relevance, context for lower review volumes
- Language is British English throughout; imperative in all instructional sections

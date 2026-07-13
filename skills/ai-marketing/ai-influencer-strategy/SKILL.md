---
name: ai-influencer-strategy
description: Use when AI-Assisted Influencer Strategy is needed to produce a decision-ready strategy for social-media or digital-marketing work; use `ai-readiness-diagnostic` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# AI-Assisted Influencer Strategy

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **decision-ready strategy** and the supplied brief falls within ai-assisted influencer strategy.

## Do Not Use When
- Use `ai-readiness-diagnostic` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| AI marketing use-case brief, intended human control point and success measure | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Issue a qualified finding and identify the evidence needed. |

## Capability and Permission Boundaries
Default to read-only: inspect supplied material and report findings. Editing, publishing, contacting people, spending, or changing live systems requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified decision-ready strategy; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Data readiness, AI maturity and risk support the proposed operating level | Choose the lowest viable automation level and define its human approval gate. | Automating an unsafe or unevaluable marketing process. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact decision-ready strategy, consumer, market, channel and approval boundary; route to `ai-readiness-diagnostic` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete decision-ready strategy; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Decision-ready strategy | Requester, client reviewer or delivery team | The decision-ready strategy addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
| Decision and gap note | Approver or next workflow | Names the chosen route, evidence used, unresolved inputs and any action requiring authority. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Finding-to-source register and unassessed-check list | Inline table, checklist or linked source note | Every material claim, decision and unavailable check is traceable. |

## Quality Standards
- Preserve the domain guidance and East African market context below; replace it only when the requester names another market.
- Use British English unless the target language or market requires otherwise, and verify names, figures, quotations and platform rules before use.
- Make the key choice visible, cover failure and edge cases, and keep the result ready for its named consumer.
- Run the repository's `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested decision-ready strategy, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [ai-readiness-diagnostic](../ai-readiness-diagnostic/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

**Source:** Ltifi (Ed.) (2024) *Advances in Digital Marketing in the Era of Artificial Intelligence*

See also: `08-influencer-marketing-strategy` for the full influencer marketing strategy framework; `meta-social-proof-system` for integrating influencer content with the broader proof strategy.

## Required Inputs
Ask for the following before generating any deliverable:

1. **Client business name**
2. **Industry**
3. **Country / city** (defaults to Uganda / East Africa)
4. **Primary goal** (e.g. product launch awareness, brand credibility, Gen Z reach, community building)
5. **Target audience** (demographic, psychographic, and generational profile — see `03-audience-personas`)
6. **Influencer tier preference** (nano 1K–10K; micro 10K–100K; macro 100K–1M; mega 1M+; or open)
7. **Budget range** (determines which AI vetting tools are accessible; free vs. paid tiers differ significantly)
8. **Human or virtual influencer** (or confirm the client has not yet considered this choice — address it proactively)

## AI-Powered Influencer Identification
AI tools can scan millions of creator accounts to match audience demographics, engagement patterns, content topic affinity, and posting behaviour to a client's target profile. Use AI identification to build a longlist of 20–50 candidates, then apply human judgement for final selection.

**Recommended tools by access level:**

| Tool | Cost | Best for |
|---|---|---|
| Meta Audience Insights | Free (within Meta Business Suite) | Facebook and Instagram influencer research |
| HypeAuditor | Paid; free limited reports | Full audience demographics and fraud score |
| Modash | Paid | Discovery and vetting; EA creator coverage |
| Heepsy | Paid | Discovery with engagement quality filter |
| TikTok Creator Marketplace | Free (brand account required) | TikTok influencer discovery and analytics |
| Manual audit + Phlanx | Free engagement calculator | Micro and nano influencer vetting in EA |

**For EA clients on limited budgets:** Use Meta Audience Insights for Facebook and Instagram candidates. Use manual audit methodology (below) for vetting. Paid tools are justified for campaigns with a budget above UGX 5,000,000.

**Manual longlist process:**
1. Search relevant hashtags for the client's category in the target city or country
2. Review the top 20–30 posts by engagement (not just views)
3. Identify creators who appear consistently — not one viral post
4. Note follower count, engagement rate, content style, and audience comment quality
5. Add to the longlist for formal vetting

## Fraudulent Engagement Detection
Fraudulent engagement (purchased followers, bot activity, fake comments) is widespread across all markets including East Africa. Detect it using AI audit tools and manual signals before committing any campaign budget.

**Red flags detectable via AI tools:**

| Signal | Meaning |
|---|---|
| Irregular follower growth spikes | Sudden 10,000+ follower gain in 24–48 hours indicates purchased followers |
| Engagement rate anomaly | 100,000 followers with 0.1–0.5% engagement rate = significant purchased follower base |
| Comment quality index | Generic comments ("Great post!", emoji-only) at high volume indicate bot activity |
| Follower geography mismatch | Influencer claiming Ugandan audience but 80%+ of followers in South Asia or Eastern Europe |
| Sudden engagement spikes on old posts | Indicates engagement pod activity or purchased likes on specific posts |
| Like-to-comment ratio | Authentic content typically has 10–20 comments per 100 likes; ratio below 1:100 suggests artificial inflation |

**Manual vetting checklist:**
- Read the most recent 20 comments — are they specific and genuine, or generic?
- Check follower geography using a free tool (HypeAuditor free report, Social Blade) — does it match the claimed audience?
- Review follower account quality — click through 10 random followers; do they have real profiles, content, and their own followers?
- Check posting consistency — has the creator posted regularly over the past 6 months, or are there gaps followed by bursts?

**Rejection threshold:** Do not proceed with any influencer whose engagement rate is below 1% at the 100K+ follower level, or whose follower geography does not match the client's target market by at least 60%.

## Human vs. Virtual Influencer Decision
### Human Influencers
**Strengths:**
- Authenticity signals: audiences have parasocial relationships with human creators — they follow a person, not a brand proposition
- Community connection: human influencers carry existing trust with their audience
- Local market credibility: EA audiences are relationship-oriented; a trusted local voice outperforms an anonymous brand message

**Risks:**
- Human influencers have personal lives, opinions, and crises that can create brand risk
- Off-brand behaviour, personal controversies, or public disagreements can damage the client by association
- Message cannot be fully controlled — the creator's voice will shape delivery

**Best for:** Trust-building, community connection, local market penetration, EA campaigns of all types.

### Virtual / CGI Influencers (e.g. Lil Miquela, Shudu)
**Strengths:**
- Full message control: the brand controls every word, image, and position taken
- No scandal risk: no personal controversies, no off-brand behaviour, no fatigue
- Always available: no scheduling conflicts, production delays, or negotiation friction

**Risks:**
- **Uncanny valley effect:** If the CGI is almost-but-not-quite human, audiences reject the character as unsettling (Ltifi, 2024). The virtual influencer must either be fully realistic or clearly stylised — the middle ground fails.
- **Sarcasm and cynicism:** Audiences increasingly view virtual influencers as a corporate pretence rather than a genuine voice, particularly Gen X and Boomer audiences
- Higher production cost: quality CGI requires significant creative investment

**Best for:** Tech-forward brands, fashion and beauty, Gen Z audiences with high tolerance for digital innovation, and international campaigns that require strict brand consistency.

## The Parasocial Interaction Scale for Virtual Influencers (Ltifi, 2024)
Audiences evaluate virtual influencers on four dimensions. Assess each before recommending a virtual influencer campaign:

| Dimension | What it measures | Target |
|---|---|---|
| **Admiration** | Does the audience find the virtual influencer aspirational? | High |
| **Identification** | Does the audience see themselves in the virtual influencer? | High |
| **Uncanny valley rejection** | Does the almost-human appearance trigger discomfort? | Low |
| **Sarcasm** | Do audiences view the virtual influencer as a corporate pretence? | Low |

Virtual influencer campaigns succeed when admiration and identification are high and uncanny valley rejection and sarcasm are low. Assess using a small audience panel (10–20 members of the target demographic) before committing to full production.

## Decision Matrix
| Factor | Choose Human Influencer | Choose Virtual Influencer |
|---|---|---|
| Brand risk tolerance | Low | High |
| Message control requirement | Low to medium | High |
| Target audience age | 35+ | Under 30 |
| Brand positioning | Authentic, community-first | Innovative, tech-forward |
| Production budget | Lower | Higher (CGI cost) |
| Market maturity | Developing markets (EA) | Mature digital markets |
| Campaign geography | EA-focused | International or urban EA only |

**EA default recommendation:** For the vast majority of EA clients, human influencers — particularly local micro and nano influencers (1K–100K followers) — produce stronger results than virtual influencers. EA audiences are relationship-oriented, digital trust is still maturing, and virtual influencers have not yet established parasocial credibility in most EA markets.

## Campaign Design Principles
Once the influencer is selected and vetted, apply these design principles:

1. **Brief the brief:** Provide a creative brief — not a script. Define the message, the required claim accuracy, the mandatory disclosures ("#ad" or "#sponsored" as required by law), and what is off-limits. Do not write the creator's caption or dictate delivery style.
2. **Authentic integration:** The most effective influencer content integrates the brand into the creator's natural content style — it does not interrupt it. A food blogger filming their weekly meal prep naturally featuring the client's product outperforms a scripted testimonial.
3. **Disclose clearly:** Under Uganda's consumer protection framework and international advertising standards, paid influencer content must be disclosed. Require "#ad", "#sponsored", or equivalent in the creator's primary language, in the caption — not buried in hashtags.
4. **Content rights:** Agree in writing whether the client has the right to repurpose influencer content as paid social advertising. This is contractual — refer to a lawyer.
5. **Performance tracking:** Require UTM links for all influencer content linking to the client's website. Track reach, engagement, link clicks, and conversions. See `meta-utm-tracking` for UTM setup.

## Quality Criteria
Output meets the standard for this skill if:

- AI identification tools are recommended at appropriate cost tiers — free manual methods are provided for EA clients with limited budgets
- The fraud detection checklist includes both AI tool signals and manual verification steps
- The human vs. virtual influencer decision is addressed explicitly, not assumed
- The Parasocial Interaction Scale (Ltifi, 2024) is applied to virtual influencer evaluation
- The EA default recommendation (human, local, micro/nano) is stated with rationale
- Campaign design principles include mandatory disclosure and UTM tracking requirements
- Influencer contracts and payments are flagged as out of scope with referral to a lawyer
- Language is British English throughout; imperative in all instructional sections

---
name: ai-influencer-strategy
description: >
  AI-assisted influencer identification, vetting, and campaign design —
  including the strategic choice between human and virtual/CGI influencers and
  AI-powered fraud detection. Invoke when a client is planning an influencer
  campaign and needs a data-informed approach to influencer selection, when
  engagement fraud is suspected, or when the client is considering virtual
  influencers as part of a brand innovation initiative. Influencer contracts and
  payments are out of scope — refer to a lawyer for contractual matters.
---
# AI-Assisted Influencer Strategy

**Source:** Ltifi (Ed.) (2024) *Advances in Digital Marketing in the Era of Artificial Intelligence*

See also: `08-influencer-marketing-strategy` for the full influencer marketing strategy framework; `meta-social-proof-system` for integrating influencer content with the broader proof strategy.

---

<!-- dual-compat:start -->
## Use when
- AI-assisted influencer identification, vetting, and campaign design — including the strategic choice between human and virtual/CGI influencers and AI-powered fraud detection. Invoke when a client is planning an influencer campaign and needs a data-informed approach to influencer selection, when engagement fraud is suspected, or when the client is considering virtual influencers as part of a brand innovation initiative. Influencer contracts and payments are out of scope — refer to a lawyer for contractual matters.
- Use this skill when it is the closest match to the requested deliverable or workflow.

## Do not use when
- Do not use this skill for graphic design, video production, software development, or legal advice beyond the repository's stated scope.
- Do not use it when another skill in this repository is clearly more specific to the requested deliverable.

## Workflow
1. Collect the required inputs or source material before drafting, unless this skill explicitly generates the intake itself.
2. Follow the section order and decision rules in this `SKILL.md`; do not skip mandatory steps or required fields.
3. Review the draft against the quality criteria, then deliver the final output in markdown unless the skill specifies another format.

## Anti-Patterns
- Do not invent client facts, performance data, budgets, or approvals that were not provided or clearly inferred from evidence.
- Do not skip required inputs, mandatory sections, or quality checks just to make the output shorter.
- Do not drift into out-of-scope work such as code implementation, design production, or unsupported legal conclusions.

## Outputs
- An AI-focused strategy, audit, system design, or prompt asset in markdown with human review and control points.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

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

---

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

---

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

---

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

**Best for:** Tech-forward brands, fashion and beauty, Gen Z audiences with high tolerance for digital innovation, international campaigns where brand consistency is paramount.

---

## The Parasocial Interaction Scale for Virtual Influencers (Ltifi, 2024)

Audiences evaluate virtual influencers on four dimensions. Assess each before recommending a virtual influencer campaign:

| Dimension | What it measures | Target |
|---|---|---|
| **Admiration** | Does the audience find the virtual influencer aspirational? | High |
| **Identification** | Does the audience see themselves in the virtual influencer? | High |
| **Uncanny valley rejection** | Does the almost-human appearance trigger discomfort? | Low |
| **Sarcasm** | Do audiences view the virtual influencer as a corporate pretence? | Low |

Virtual influencer campaigns succeed when admiration and identification are high and uncanny valley rejection and sarcasm are low. Assess using a small audience panel (10–20 members of the target demographic) before committing to full production.

---

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

---

## Campaign Design Principles

Once the influencer is selected and vetted, apply these design principles:

1. **Brief the brief:** Provide a creative brief — not a script. Define the message, the required claim accuracy, the mandatory disclosures ("#ad" or "#sponsored" as required by law), and what is off-limits. Do not write the creator's caption or dictate delivery style.
2. **Authentic integration:** The most effective influencer content integrates the brand into the creator's natural content style — it does not interrupt it. A food blogger filming their weekly meal prep naturally featuring the client's product outperforms a scripted testimonial.
3. **Disclose clearly:** Under Uganda's consumer protection framework and international advertising standards, paid influencer content must be disclosed. Require "#ad", "#sponsored", or equivalent in the creator's primary language, in the caption — not buried in hashtags.
4. **Content rights:** Agree in writing whether the client has the right to repurpose influencer content as paid social advertising. This is contractual — refer to a lawyer.
5. **Performance tracking:** Require UTM links for all influencer content linking to the client's website. Track reach, engagement, link clicks, and conversions. See `meta-utm-tracking` for UTM setup.

---

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

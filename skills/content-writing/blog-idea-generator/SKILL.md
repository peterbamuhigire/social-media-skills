---
name: blog-idea-generator
description: Use when Blog Idea Generator is needed to produce a blog idea generator deliverable for social-media or digital-marketing work; use `caption-writer` when its narrower outcome is requested.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Blog Idea Generator

<!-- dual-compat-start -->
## Use When
- Use this skill when the requested outcome is specifically a **blog idea generator deliverable** and the supplied brief falls within blog idea generator.

## Do Not Use When
- Use `caption-writer` when its narrower output is the real deliverable; do not use this skill as a generic substitute.
- Do not use it to publish, send, spend, alter a live account, or make unsupported legal, platform, performance, or certification claims.

## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Content brief, channel, audience, message, format and call to action | Requester or approved brief | Yes | Stop and request the missing decision context. |
| Brand voice, offer facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions; do not invent names, prices, results or approvals. |
| Performance, platform or research evidence used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag the missing evidence. |

## Capability and Permission Boundaries
Drafting is permitted within the supplied brief. Publishing, sending, spending, changing live accounts, or claiming certification requires separate explicit authority. Minimum capabilities are read access to supplied files and search across the authorised evidence set. Use only the files, tools, accounts and evidence made available for the engagement, expose every unassessed check, and obtain explicit authority before any mutation.

## Degraded Mode
Fallback: if files, network access, platform data, language review or production tools are unavailable, return the narrowest useful qualified blog idea generator deliverable; mark unavailable checks `not assessed` and never convert them into a pass.

## Decision Rules
| Choice | Action | Failure or risk avoided |
|---|---|---|
| Channel, format and audience commitment level are known | Choose the hook, structure and call to action native to that context. | Copy that could be pasted unchanged onto any channel or brand. |
| A required fact or approval is missing | Stop that claim or action; request it or use an explicit placeholder. | Fabricated facts, implied consent or unauthorised publication. |
| Evidence is partial but a useful draft is possible | Deliver a qualified draft with gaps and the next verification step. | Treating an unassessed requirement as passed. |

## Workflow
1. Confirm the exact blog idea generator deliverable, consumer, market, channel and approval boundary; route to `caption-writer` if it is the closer match.
2. Inventory supplied facts, source provenance, constraints and missing inputs; stop if the objective, audience or authority is unknowable.
3. Select the domain method and record the material decision behind it before drafting.
4. Produce the smallest complete blog idea generator deliverable; keep facts traceable and placeholders visibly unresolved.
5. Test the result against the decision table, domain quality criteria and anti-slop gate; recover by narrowing or qualifying unsupported portions.
6. Deliver the artefact with evidence, assumptions, unassessed checks and the next approval or verification step.

## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Blog idea generator deliverable | Requester, client reviewer or delivery team | The blog idea generator deliverable addresses the named audience and objective, records assumptions, and passes the skill's domain checks without invented facts. |
| Decision and gap note | Approver or next workflow | Names the chosen route, evidence used, unresolved inputs and any action requiring authority. |

## Evidence Produced
| Evidence | Format | Acceptance condition |
|---|---|---|
| Source/assumption register and completed release checklist | Inline table, checklist or linked source note | Every material claim, decision and unavailable check is traceable. |

## Quality Standards
- Preserve the domain guidance and East African market context below; replace it only when the requester names another market.
- Use British English unless the target language or market requires otherwise, and verify names, figures, quotations and platform rules before use.
- Make the key choice visible, cover failure and edge cases, and keep the result ready for its named consumer.
- Run the repository's `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns
- Writing before the objective and audience are known. **Fix:** stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. **Fix:** route by the requested blog idea generator deliverable, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. **Fix:** verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. **Fix:** mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. **Fix:** obtain explicit action-specific authority and retain the approval record.

## References
- [caption-writer](../caption-writer/SKILL.md) is the nearest routing comparison for this skill.
- [Repository agent guide](../../../AGENTS.md) defines the engine-wide market, safety and anti-slop gates.
<!-- dual-compat-end -->

Generate 15-25 targeted blog post ideas, each presented as a 200-word hybrid summary with narrative brief + structured specs. The system adapts its ideation methods to the specific client and available information.

**Read `references/ideation-frameworks.md`** for the full 20-method library and selection logic.
**Read `references/content-formats.md`** for 20 content formats with structural templates.
**Read `sales-copywriting/references/headline-mastery.md`** for headline formulas and 4 U's scoring.

## Required Input
Read the client files listed in Step 1, then collect any missing audience, pain-point, and content-goal context before generating ideas.

## Step 1: Gather Context
### Read client docs (mandatory)
Read every available file to build a complete picture:

1. `docs/en/company-profile.md` (and all enabled language versions)
2. `docs/en/services.md` — service offerings, target customers
3. `docs/en/pages.md` — existing website pages and content
4. `docs/sector-brief.md` — industry context (if present)
5. `docs/style-brief.md` — brand voice and tone
6. `docs/blogs/topics.md` — existing topics (avoid duplicates)
7. `src/pages/en/blog/` — existing articles (avoid overlap)
8. All other `docs/en/` files — testimonials, FAQ, portfolio, about-story

Extract and note:
- What the business does (core services, products)
- Who they serve (audience segments, industries, company sizes)
- Where they operate (geographic focus, markets)
- What makes them different (competitive advantage, methodology)
- What expertise the author has (experience, credentials, stories)
- What problems customers face (pain points, challenges)
- What content already exists (published articles, covered topics)

### Guided interview (3-5 questions)
After reading docs, ask targeted questions to fill gaps. Ask one at a time. Skip questions already answered by docs.

**Core questions (ask what's missing):**

1. **Audience specifics** — "Who is your ideal reader? (Job title, company size, industry, location)"
2. **Top pain points** — "What are the top 3 problems your customers face that your business solves?"
3. **Content goals** — "What should readers DO after reading? (Contact you, book a demo, understand a concept?)"
4. **Competitor landscape** — "Name 2-3 competitors. What topics do they cover?"
5. **Unique knowledge** — "What do you know that competitors don't? What's your unfair advantage?"
6. **Customer questions** — "What questions do customers ask most before buying?"
7. **Content gaps** — "Topics you've wanted to write about but haven't?"
8. **Context/audience** — any additional context the user provides (specific themes, campaigns, seasonal needs)

If the user provides additional context (audience details, campaign goals, seasonal focus), incorporate it into the assessment.

## Step 2: Assess Available Information
Score each dimension to determine which ideation methods will work best:

| Dimension | Rich (3) | Moderate (2) | Sparse (1) |
|-----------|----------|--------------|------------|
| **Client docs** | Detailed company-profile, services, testimonials, stories | Basic company-profile and services | Minimal — just a business name and description |
| **Competitor visibility** | Named competitors with active blogs | Competitors named but blogs unknown | No competitor info |
| **Audience specificity** | Named segments with pain points | General audience description | Vague ("businesses") |
| **Industry dynamism** | Active news cycle, regulations, trends | Moderate change rate | Stable/static industry |
| **Existing content** | 5+ published articles to spin off | 1-4 articles | No existing content |
| **Customer interaction** | Direct customer questions available | Some FAQ data | No customer feedback |

## Step 3: Select Ideation Methods
Based on the assessment, select 5-7 methods from the 20-method library. **Always include Methods 1 and 2** as foundation.

### Selection Matrix
| Method | Best When | Min Score |
|--------|-----------|-----------|
| 1. Category Drilldown | Always | — (always include) |
| 2. Buyer Awareness Stages | Always | — (always include) |
| 3. Pain Point Mining | Client docs ≥ 2 or customer interaction ≥ 2 | — |
| 4. Competitor Gap Analysis | Competitor visibility ≥ 2 | Competitor 2+ |
| 5. Customer Question Mapping | Customer interaction ≥ 2 | Customer 2+ |
| 6. They Ask, You Answer | Customer interaction = 3 | Customer 3 |
| 7. Amazon/Review Mining | Product-based business | Client docs 2+ |
| 8. Spin-Off Posts | Existing content ≥ 2 | Content 2+ |
| 9. Media Mashup | Brand voice is informal/creative | Client docs 2+ |
| 10. Highlight Good/Bad | Industry has notable examples | Industry 2+ |
| 11. How-To/Tutorial Mining | Product/service has teachable processes | Client docs 2+ |
| 12. Success/Failure Stories | Client has real project stories | Client docs 3 |
| 13. Holiday/Event Mapping | Content calendar needs seasonal hooks | Any |
| 14. Newsjacking/Trends | Industry dynamism = 3 | Industry 3 |
| 15. Use Any Object | Need creative/lateral ideas | Any (creative fallback) |
| 16. Curated Roundups | Industry has notable resources | Industry 2+ |
| 17. Prediction Posts | Industry dynamism ≥ 2 | Industry 2+ |
| 18. Jargon/Glossary | Technical niche with newcomer audience | Audience 2+ |
| 19. Contrarian/Negative | Audience is sophisticated | Audience 3 |
| 20. Topic-Category Matrix | Need high volume quickly | Any (volume fallback) |

Announce: "Based on available information, I'm using methods: [list]. Here's why: [brief rationale]."

## Step 4: Generate Ideas
Run selected methods sequentially. Aim for 25-35 raw ideas, then filter to the best 15-25.

For each method, consult `references/ideation-frameworks.md` for detailed instructions and examples.

### Quality Filters
Remove any idea that fails:

| Filter | Test |
|--------|------|
| **High-value goal** | Does this help the reader make/save money, reduce risk, save time, or gain advantage? |
| **Unique angle** | Does this require knowledge that isn't commonly available? |
| **So-what test** | Would the target reader care enough to click? |
| **Longevity** | Will this still be relevant in 12 months? |
| **No overlap** | Not already published or in existing docs/blogs/topics.md? |
| **Searchable** | Would someone type this into a search engine? |

### Tier Classification
| Tier | Purpose | Target Count |
|------|---------|-------------|
| **Tier 1: SEO drivers** | Attract organic traffic via long-tail keywords | 6-8 ideas |
| **Tier 2: Authority builders** | Establish expertise with deep guides and analysis | 5-7 ideas |
| **Tier 3: Thought leadership** | Build brand with opinions, predictions, stories | 4-5 ideas |

## Step 5: Create 200-Word Hybrid Summaries
For each approved idea, produce a summary in this exact format:

```markdown
### [Number]. [Working Title]
[3-4 sentence narrative brief: What this article is about, who it serves,
why it matters now, and the unique angle that makes it worth reading. This
paragraph should make someone want to write — and read — this article. It
captures the creative direction and emotional tone.]

- **Audience:** [specific reader segment — job title, industry, company size]
- **Buyer Stage:** [Awareness / Consideration / Decision]
- **Format:** [How-to / Case study / List / Opinion / Guide / Story / Comparison / Interview / Roundup / FAQ]
- **Angle:** [the specific twist that differentiates from competitors — 1 sentence]
- **Key Points:**
  1. [what the article must cover — specific enough to outline from]
  2. [second key point]
  3. [third key point]
  4. [fourth key point — optional]
  5. [fifth key point — optional]
- **CTA Goal:** [what action the reader should take after reading]
- **SEO Keywords:** [primary keyword], [secondary keyword]
- **Tier:** [1: SEO driver / 2: Authority builder / 3: Thought leadership]
- **Est. Words:** [1,500-2,500]
```

### Summary Quality Rules
- The narrative must read like a creative brief — not a dry description
- Key points must be specific enough to outline section headings from
- Keywords must be realistic long-tail phrases someone would search
- The angle must be genuinely different from what a Google search would surface
- Every title must pass the 4 U's test (see `sales-copywriting/references/headline-mastery.md`): Useful, Unique, Urgent, Ultra-specific — score 3+ on at least 3 dimensions

## Step 6: Present and Refine
### Present to the User
Show ideas grouped by tier with full summaries. After presenting, ask:
- Which ideas excite you most?
- Any ideas to remove or modify?
- Any topics you expected but don't see?
- Any specific campaigns or seasonal needs to address?

Refine based on feedback. The user's input overrides the assessment.

## Step 7: Save Output
Save the final approved list to `docs/blogs/topics.md`:

```markdown
# Blog Topic Ideas — [Client Name]

Generated: YYYY-MM-DD
Methods used: [list of methods applied]
Target audience: [summary]
Content categories: [list]

## Tier 1: SEO Drivers
### 1. [Title]
[Full 200-word hybrid summary as above]

## Tier 2: Authority Builders
...

## Tier 3: Thought Leadership
...

## Content Calendar Suggestion
| Month | Article 1 (Tier) | Article 2 (Tier) |
|-------|-------------------|-------------------|
| Month 1 | [title] (T1) | [title] (T2) |
...
```

If the file already exists, merge new ideas — don't overwrite existing topics. Mark previously written topics as `[PUBLISHED]`.

## Quality Checklist
Before finalising:

- [ ] At least 15 ideas across all 3 tiers
- [ ] Each idea has a complete 200-word hybrid summary
- [ ] No duplicate angles (each idea is distinct)
- [ ] At least 2 ideas per buyer awareness stage
- [ ] Ideas span at least 3 content categories
- [ ] Every title passes the 4 U's test (3+ dimensions at 3+)
- [ ] No overlap with existing published articles
- [ ] Mix of content formats (not all lists, not all how-tos)
- [ ] At least 3 ideas that showcase the author's unique expertise
- [ ] At least 2 ideas based on real customer questions (if data available)
- [ ] Content calendar covers at least 6 months at 2 articles/month
- [ ] All SEO keywords are realistic long-tail phrases
- [ ] Narrative briefs are compelling — they make you want to write the article

After writing, verify line count is under 500: wc -l blog-idea-generator/SKILL.md

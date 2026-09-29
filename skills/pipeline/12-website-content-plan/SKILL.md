---
name: 12-website-content-plan
description: Use when a client's website or blog needs a 90-day content plan built from search intent and the questions customers ask, without building the site; produces the website content plan, twelve article briefs, FAQ library and internal-link map; not for writing the finished articles (use `blog-writer`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Website Content Plan Generator

Produces four planning outputs: 12 blog post briefs, an editorial calendar, an internal linking structure and lead magnet ideas. It does not produce finished articles (use `blog-writer` for article text); apply `east-african-english` for tone throughout.

<!-- dual-compat-start -->
## Use When

- The website blog is stale and the client wants a quarter's worth of articles planned around search intent and personas.
- Each article needs a brief with reader, keyword theme, key questions, structure, word count and call to action.
- Pages need an internal linking structure and lead magnet or content upgrade ideas.
- The questions customers ask staff, in DMs, in search and on sales calls should become a monthly question engine, FAQ library, Big 5 content priorities and assignment selling.

## Do Not Use When

- `blog-writer` for the finished article, whitepaper or eBook text.
- `seo-geo-optimisation` for making one page ready for search and AI citation.
- `11-content-calendar` for dated social posts.
- Stop at planning: do not design, build or edit the website; hand site work to the website engine.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client name, industry and country/city | Client brief or `01-client-brief` | Yes | Default the location to Kampala, Uganda; ask for the rest. |
| Named audience personas (minimum two) | `03-audience-personas` | Yes | Stop the briefs; list the personas that must be approved. |
| 3–5 primary topic areas and the dominant journey stage (Awareness, Consideration or Decision) | Client lead | Yes | Draft candidate topic areas from customer questions and ask the client to confirm them. |
| Blog publication frequency (1 per week or 2 per month) | Client lead | Yes | Plan 12 articles across 90 days and label the pace provisional. |
| Campaign windows to coordinate with | `09-campaign-strategy` or `11-content-calendar` | If campaigns run | Sequence awareness to decision without campaign alignment and note that none were supplied. |
| Current website state (homepage, Big 5 coverage, opt-ins, load time) | Client site or dated audit | Yes | Mark the seven-priority check `not assessed` and flag it before any traffic plan. |

## Workflow

1. Ask the intake questions in [content-plan-build-method](references/content-plan-build-method.md) § Intake questions; route dated social posts to `11-content-calendar` and single-page search work to `seo-geo-optimisation`.
2. Audit the site against the seven website content priorities (Sheridan, 2019) and brief the client; stop driving traffic to a site that fails Priorities 1, 2 or 7 and list the prerequisite actions.
3. Where topics must come from real customer questions, run the monthly harvest and Big 5 scoring in [buyer-question-content-plan](references/buyer-question-content-plan.md) before writing briefs.
4. Write 12 briefs (Article 1 of 12 through Article 12 of 12) with all nine elements, distributed across the topic areas.
5. Sequence the editorial calendar from awareness to decision, aligned to publication frequency and campaign windows.
6. Map internal links for all 12 articles and develop lead magnets for the 4 articles with the highest organic potential.
7. Check against the quality standards; correct failing briefs and rerun the check.
8. Run the anti-slop ship gate and pass the briefs, link map and lead magnet details to `blog-writer`; do not design, build or edit the website.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| 12 blog post briefs (nine elements each) | `blog-writer` | No element blank or marked TBC; titles under 60 characters. |
| Editorial calendar table | Client lead; `11-content-calendar` | All 12 articles sequenced by week, persona, intent, keyword theme and CTA. |
| Internal link map | `blog-writer` at the editing stage | Each article links to at least 2 articles and 1 service page with natural anchors, or states that no strong link exists. |
| Lead magnet ideas and website-priority findings | Client lead; `07-email-marketing-strategy` | 4 lead magnets with format, delivery, contents and value exchange; failed priorities flagged as prerequisites. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Seven-priority site audit | Table: priority, finding, source or measurement date | You:we ratio, Big 5 coverage and load time are measured or marked `not assessed`. |
| Topic-to-question trace | Table: article, persona, source question or topic area | Each brief traces to a persona need or a harvested customer question. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Site design, build and edits belong to the website engine.

## Degraded Mode

Without approved personas or access to the current website, return the narrowest qualified result and mark the affected checks `not assessed`. Topic clusters, draft briefs and an awareness-to-decision sequence can still be delivered, labelled as awaiting the site audit.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The site fails Priorities 1, 2 or 7 | Brief the client on the fixes first; do not drive traffic to it. | Content spend lost to a site that does not convert. |
| The site loads in more than 3 seconds | Flag speed as a prerequisite action (40% of visitors abandon beyond 3 seconds per Sheridan, 2019). | High traffic plus high bounce giving low return. |
| The site does not address all Big 5 categories | Prioritise articles filling those gaps before other blog content. | Buyers leaving with unanswered pre-contact questions. |
| Topics must come from real customer questions (FAQ library, Big 5, sales-call objections) | Run the monthly harvest, clustering and Big 5 scoring in [buyer-question-content-plan](references/buyer-question-content-plan.md) before writing briefs. | Briefs built on what the business wants to say rather than what buyers ask. |
| One topic area would exceed 40% of articles | Redistribute, or record the specific justification. | A plan clustered on one topic. |
| A campaign window falls in the plan | Align one article to the campaign theme in the week before launch; place Decision-stage articles near campaign windows. | Blog and campaign pulling in different directions. |
| A calculator or interactive tool is recommended | Flag that it requires a website developer. | Promising a tool nobody can build. |
| The work is dated social posts | Route to `11-content-calendar` and hand over the verified inputs already collected. | Neighbour collision and duplicated work. |

## Quality Standards

- All 12 article briefs are complete; no element within any brief is left blank or marked TBC.
- Articles are distributed across the 3–5 primary topic areas; no single topic receives more than 40% of articles unless specifically justified.
- Search intent is correctly classified and the article structure reflects it: a transactional brief looks different from an informational brief.
- The editorial calendar sequences articles in awareness-to-decision order unless a specific reason (campaign alignment, seasonal hook) justifies reordering.
- Internal link suggestions use natural anchor text: no keyword-stuffed anchor text, no links forced where a natural connection does not exist, and no more than 5 internal links per article.
- Lead magnets are specific to the client's industry and persona; no generic "download our newsletter" suggestions.
- Word count guidance is differentiated by article type: informational posts are not assigned the same word count as step-by-step guides.
- British English spelling is used throughout; Ugandan and East African context is applied to examples, titles and persona references.

## Anti-Patterns

- Clickbait titles. Fix: write specific, informative SEO titles under 60 characters in the client's industry language.
- Headings such as "Introduction" or "Conclusion". Fix: use 4–6 H2 headings that each answer one of the five key questions.
- Inventing keyword volumes. Fix: state the thematic territory; keyword tools are outside this skill's scope.
- A generic newsletter sign-up as the content upgrade. Fix: offer a lead magnet directly tied to the article, with WhatsApp opt-in for mobile-first audiences.
- Long, academic PDF lead magnets. Fix: keep PDFs under 8 pages; concise and practical wins in the EA market.
- Publishing two articles on the same topic area in consecutive weeks. Fix: alternate topic areas in the calendar.
- Editing or building the website during planning. Fix: hand site work to the website engine.

## References

- [Website content plan build method](references/content-plan-build-method.md): read when asking the intake questions, auditing the seven priorities, writing the nine brief elements, or building the editorial calendar, link map, lead magnets and coordination hand-offs.
- [buyer-question-content-plan](references/buyer-question-content-plan.md): read when content topics, an FAQ library or sales enablement must come from customer questions (five sources, Big 5, assignment selling).
- [`blog-writer`](../../content-writing/blog-writer/SKILL.md): read when briefs or lead magnets are ready to write.
- [`seo-geo-optimisation`](../../seo-discovery/seo-geo-optimisation/SKILL.md): read when one page must be made ready for search and AI citation.
- [`11-content-calendar`](../11-content-calendar/SKILL.md): read when aligning article dates with the pillar themes in the social calendar.
- [`07-email-marketing-strategy`](../07-email-marketing-strategy/SKILL.md): read when lead magnets feed an email list and nurture sequence.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read during production.
- [`ai-slop-audit`](../../ai-marketing/ai-slop-audit/SKILL.md): read at the release checkpoint.
<!-- dual-compat-end -->

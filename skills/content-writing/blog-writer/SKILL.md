---
name: blog-writer
description: Use when a topic or brief is agreed and the client needs the finished long-form piece, such as a sourced blog article, whitepaper or eBook lead magnet; produces publication-ready article copy with SEO frontmatter, or a gated document with executive summary and download landing page; not for choosing topics (use `content-ideas`).
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---
# Blog Writer

Writes a complete, professional blog post, whitepaper or eBook from an agreed brief: a finished markdown article ready to paste into a CMS, share with a client or hand to a web developer. Apply `east-african-english` for language and tone throughout.

<!-- dual-compat-start -->
## Use When
- We have the topic and search keywords and need the full article written with headings, cited sources and a meta description, ready to paste into WordPress or hand to the web developer.
- An existing post reads thin or generic and needs rewriting with sources, examples and a proper structure.
- We need a whitepaper or eBook as a gated lead magnet, with an executive summary, clear sections and a landing page for the download.
- A donor report or investor document needs writing for an outside reader, with a Theory of Change where it applies.

## Do Not Use When
- `content-ideas` for topic lists and briefs before anything is written.
- `12-website-content-plan` for a 90-day website and blog plan with article briefs and an internal-link map.
- `caption-writer` for the social posts that promote the article.
- Stop before publishing any statistic, quote or case figure without a traceable source; flag it rather than invent it.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---|---|
| Client business name, industry and country/city | Client brief | Yes | Default the market to Uganda/East Africa; ask for the business and industry before writing. |
| Topic or working title, target reader (role, situation, problem) and search intent (learn, compare or decide) | Approved brief or `content-ideas` output | Yes | Stop and ask; do not guess intent. |
| 3–5 key questions the article must answer, and the call to action | Client or account manager | Yes | Draft the questions from the verified SERP gaps and return them for approval before writing. |
| Word count target and tone | Client | No | Default to 1,200–1,800 words and a professional tone. |
| Brand voice, offer and service facts, constraints and approvals | Client source pack or authorised owner | Conditional | State assumptions in the gap note; never invent client names, prices, results or approvals in the article. |
| Statistics, quotations, case figures and research used for claims | Traceable export, URL, document or named source | Conditional | Draft the narrowest reviewable version and flag each unsourced claim. |

The full intake question list is in the [article build method](references/article-build-method.md#required-input).

## Workflow

1. Confirm the article, reader, market, channel and call to action; route to `caption-writer` for social posts or to `content-ideas` if the topic is not yet chosen.
2. Inventory the supplied facts, source provenance and missing inputs; stop if the objective, audience or authority is unknowable.
3. Run and retain the digital-research-engine's three-wave SEO/SERP study for every article: map 3–7 intent clusters, read the accessible top five results per cluster, and record content, evidence and AI-answer gaps; mark inaccessible results `UNASSESSED`. Treat search results and competitor copy as competitive evidence, not proof.
4. Choose the format and record the decision before drafting: a single article follows the [article build method](references/article-build-method.md); a whitepaper, eBook, gated lead magnet, donor report or investor document follows the [whitepaper and eBook structure](references/whitepaper-and-ebook-structure.md).
5. Write the frontmatter block, then the opening hook, nut paragraph, 4–7 H2 sections (one key question each, H3s for distinct sub-topics), a practical takeaway and a full-circle conclusion with a non-pushy call to action.
6. Place the primary and secondary keywords, mark 2–3 internal links as `[LINK: suggested anchor text → page type]` and suggest 1–2 authoritative external sources; add social cut-downs only if requested.
7. Run the `anti-ai-slop` humanising passes and the quality checks below; correct any failed passage by narrowing, sourcing or qualifying it, then rerun the checks until they pass.
8. Deliver the article with the dated research record, source register, assumptions, unassessed checks and the next approval step.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Frontmatter block (title under 60 characters, meta description under 155 characters with keyword and location, primary and 2–3 secondary keywords, read time at 200 words/min) | Web developer or CMS editor | Every field is filled; title and meta description contain the primary keyword. |
| Finished article in markdown | Client reviewer | Every H2 answers a named key question; at least one actionable section; the conclusion reconnects to the opening with a call to action. |
| Whitepaper or eBook with executive summary and download landing page | Client; lead-capture owner | Follows the section template for its use case and states a thesis. |
| Social cut-downs (LinkedIn 150 words, Facebook 80 words, X/Twitter opener 280 characters), only if requested | `caption-writer`; social team | Each is written for its platform, not pasted from the article. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Three-wave SEO/SERP research record | Dated table: intent cluster, results read, gaps | Every cluster lists the results read or marks them `UNASSESSED`. |
| Source and assumption register | Inline table or linked source note | Every statistic, quotation and case figure traces to a named source, or is flagged. |
| Release checklist | Checklist against the quality standards | Unavailable checks are marked `not assessed`, never passed. |

## Capability and Permission Boundaries

Read and search only; analysis is read-only. Publishing, spend, live account changes, outreach and personal-data processing need explicit, action-specific client authority. Drafting is permitted within the supplied brief; claiming certification or posting to the client's CMS needs separate authority.

## Degraded Mode

Without a confirmed reader, search intent or traceable sources, return the narrowest qualified result and mark the affected checks `not assessed`. An outline with frontmatter, H2 questions and flagged claim slots can still be delivered for approval.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The reader's channel and commitment level are known (cold search visitor, subscriber, prospect) | Choose the hook, structure and call to action native to that reader and site. | An article that could be pasted unchanged onto any site or brand. |
| A statistic, quotation, case figure or approval is missing | Stop that claim; request it or leave an explicit placeholder flagged in the source register. | Fabricated facts, implied consent or unauthorised publication. |
| The SERP study or source pack is partial but a useful article is possible | Deliver a qualified draft listing the gaps, unread clusters and the next verification step. | Treating an unassessed search gap or claim as covered. |
| The brief is a whitepaper, eBook, gated lead magnet, donor report or investor document rather than a single article | Apply the whitepaper/eBook decision rule, section templates and use-case variants in `references/whitepaper-and-ebook-structure.md`. | Padding a blog template into a thesis-free brochure or a reader-problem-free catalogue. |
| The opening uses a story or scenario | Follow it immediately with a nut paragraph stating what the article covers and why it matters. | A reader who does not know why they are reading. |
| The piece is premium thought leadership or lead generation | Also apply `premium-commercial-writing`: message spine, clear point of view, visible mechanism, proof density and an answer both readers and AI-search systems can extract. | Competent but forgettable copy. |

## Quality Standards

- The opening hook is a recognisable scenario, surprising fact, real question or short story; it never opens with a definition or generic statement.
- Every H2 section answers a real question the target reader would have; at least one section gives a checklist, decision framework or step-by-step.
- The primary keyword sits naturally in the title, first 100 words, at least one H2 and the conclusion; no keyword stuffing.
- British spelling; 90%+ active voice; no sentence over 35 words; paragraphs of 2–4 sentences; at least 2 clear positions taken.
- No banned vocabulary, filler phrases or weak modifiers from the [writing standards](references/article-build-method.md#writing-standards).
- Tone matches the client's industry and the East African professional register; names, figures, quotations and platform rules are verified before use.
- The article reads as written by a human with genuine expertise and passes the `anti-ai-slop` ship gate; a blocking factual, cultural, safety or permission defect stops release.

## Anti-Patterns

- Writing before the objective and audience are known. Fix: stop and obtain the missing brief fields.
- Reusing a neighbouring skill's template because the headings look similar. Fix: route by the requested publication-ready copy, not vocabulary overlap.
- Adding a price, result, quotation, platform limit or cultural claim without a traceable source. Fix: verify it or qualify/remove it.
- Treating missing access, evidence or native-language review as approval. Fix: mark the check `not assessed` and narrow the result.
- Publishing, sending, spending or changing a live account from drafting authority alone. Fix: obtain explicit action-specific authority and retain the approval record.
- Drafting from a keyword list or a single search result. Fix: complete the three-wave article study and write to the verified reader gap.
- Mass-producing near-identical articles (AI or templated) or placing sponsored third-party articles on a client's strong domain to rank. Fix: each article must add value for a reader; Google treats these as scaled content abuse and site reputation abuse (register `GOOGLE-SPAM-POLICIES`), so route the plan through `seo-geo-optimisation`.

## References

- [Article build method](references/article-build-method.md): read when asking the intake questions, laying out the frontmatter and body, or applying the writing, SEO, social cut-down and human-authenticity rules.
- [Whitepaper and eBook structure](references/whitepaper-and-ebook-structure.md): read when the deliverable is a whitepaper, eBook, gated lead magnet, donor report or investor document.
- [Human voice standards](references/human-voice-standards.md): read when the article risks sounding generic or AI-generated; run the voice checklist.
- [Writing craft](references/writing-craft.md): read when working on sentence structure, opening hook techniques or paragraph rhythm.
- [Editorial standards](references/editorial-standards.md): read when checking punctuation, capitalisation and grammar in the proofing pass.
- [Storytelling](references/storytelling.md): read when the opening or case material uses a story or personal experience.
- [Reader experience](references/reader-experience.md): read when treating the article as a product experience for clarity and value delivery.
- [Article design](references/article-design.md): read when designing the article page.
- [Content strategy](references/content-strategy.md): read when deciding the strategic purpose of the article and who it serves.
- [Ideation and research](references/ideation-and-research.md): read when generating topic ideas or planning the article research.
- [Topic ideas](references/topic-ideas.md): read when a project-specific topic list is needed.
- [Series and launch engine](references/series-and-launch-engine.md): read when the article must support discovery, warming, proof or a timed campaign.
- [`east-african-english`](../../language/east-african-english/SKILL.md): read when calibrating tone, the British English spelling list and courteous phrasing.
- [`premium-commercial-writing`](../premium-commercial-writing/SKILL.md): read when the piece needs premium positioning, proof density, value framing and SEO/GEO-aware authority structure.
- [`caption-writer`](../caption-writer/SKILL.md): read when routing is unclear; it is the nearest neighbour.
- [Repository agent guide](../../../AGENTS.md): read when checking the engine-wide market, safety and anti-slop gates.
- [Anti-AI slop production gate](../../ai-marketing/anti-ai-slop/SKILL.md): read when drafting and before client delivery.
- [Legal and market release gate](../../../docs/quality-gates/legal-market-release-gate.md): read when the article makes legal, health, financial or market claims.
<!-- dual-compat-end -->

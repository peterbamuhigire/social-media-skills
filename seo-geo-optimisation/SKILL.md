---
name: seo-geo-optimisation
description: Optimises individual pieces of content for Generative Engine Optimisation (GEO) — the discipline of making content findable and citable by AI-powered search engines including ChatGPT Search, Perplexity AI, and Google AI Overviews. Distinct from traditional keyword-based SEO. Invoke when creating or auditing a blog post, website page, or strategy document that must be cited as a trusted source in AI-generated answers. Cross-reference `ai-generative-search-optimisation` for full content audit and monitoring protocol.
---
# SEO and GEO Optimisation

<!-- dual-compat:start -->
## Use when
- Optimises individual pieces of content for Generative Engine Optimisation (GEO) — the discipline of making content findable and citable by AI-powered search engines including ChatGPT Search, Perplexity AI, and Google AI Overviews. Distinct from traditional keyword-based SEO. Invoke when creating or auditing a blog post, website page, or strategy document that must be cited as a trusted source in AI-generated answers. Cross-reference `ai-generative-search-optimisation` for full content audit and monitoring protocol.

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
- The primary deliverable requested by this skill, structured in markdown and ready for immediate use.

## References
- Use the inline instructions in this skill now. If a `references/` directory is added later, treat its files as the deeper source material and keep this `SKILL.md` execution-focused.

<!-- dual-compat:end -->

## Required Input

Ask for the following before optimising any content:

1. **Client business name** — the exact trading name used publicly
2. **Industry** — e.g. financial services, health, legal, consulting, retail
3. **Country/city** — default: Uganda/Kampala
4. **Primary goal** — what the content must achieve: brand visibility in AI search, thought leadership, local business discovery, lead generation
5. **Content type** — blog post, service page, homepage, FAQ page, case study
6. **Core query** — the exact question a potential customer would type into ChatGPT or Perplexity to find this content
7. **Current content** — paste the existing content for audit, or confirm this is new content to be created from scratch

---

## Why GEO Is a Distinct Discipline

Traditional SEO optimises for keyword matching and backlinks — factors that determine position in Google's ranked list of blue links. Generative Engine Optimisation (GEO) optimises for AI comprehension and credibility — the factors that determine whether an AI search engine chooses to cite a piece of content in its generated answer.

The mechanism is different. An AI search engine does not rank pages; it synthesises a single answer from multiple sources and presents it directly to the user. If the content is not cited in that answer, it is invisible — regardless of its Google ranking.

A study of 10,000+ search queries found GEO methods increase AI search visibility by 30–40% compared to traditionally structured content (Roth and neuroflash Team, 2024/2025). With AI-powered search handling an estimated 10% of all queries in 2025 and growing, GEO is a live commercial need for clients.

**Key difference:** SEO optimises for algorithms that rank pages. GEO optimises for LLMs that synthesise and cite content.

---

## The Five GEO Pillars

*Source: Roth, H. and neuroflash Team (2024/2025) AI Strategy 2025 for Marketing Teams*

Apply all five pillars to every piece of content intended for AI search visibility.

---

### Pillar 1 — Concise Opening Summary

Place a direct answer to the content's core query in the very first paragraph, in 50 words or fewer. AI search engines scan for the answer, not the introduction. If the answer is buried in paragraph four, the content will not be cited.

**Sentence structure:** [Specific answer to the query] because [brief reasoning]. For [audience], this means [practical implication].

**Example for an EA financial services firm:**
"A SACCO earns trust in Kampala by maintaining transparent loan terms, publishing member testimonials, and responding to enquiries on WhatsApp within 24 hours. For small business owners in Kampala, this means checking a SACCO's Facebook page reviews and WhatsApp response time before applying."

---

### Pillar 2 — Semantic Depth

Cover related topics, subtopics, synonyms, and adjacent questions within the same piece. AI search engines evaluate whether a piece demonstrates comprehensive knowledge of a subject — not just keyword density.

To identify which subtopics to cover:
- Check the "People Also Ask" box in Google for the core query
- Check Perplexity's related questions panel
- Search Reddit and Facebook community groups for recurring questions on the same topic
- For EA markets: review WhatsApp group discussions and community Facebook group questions

A piece with comprehensive semantic coverage is more likely to be cited across multiple related queries, not just the one it was written for.

---

### Pillar 3 — EEAT Signals

EEAT stands for Expertise, Authoritativeness, Trustworthiness, and Experience. AI search engines assess credibility before citing a source. Include all four signals in every piece:

- **Expertise:** Author attribution with credentials — name, title, organisation, and relevant experience
- **Authoritativeness:** Named external sources with dates — "According to the Uganda Bureau of Statistics (2024)..."
- **Trustworthiness:** Factual, verifiable statements — no marketing hyperbole; specific numbers preferred
- **Experience:** First-hand evidence — "In our work with hospitality clients in Kampala..." or a named case study

Content without an identifiable author and without named sources scores low on EEAT and is unlikely to be cited in AI answers.

---

### Pillar 4 — Conversational Long-Tail Structure

AI search users ask questions in natural language. Content that mirrors this structure is more likely to be cited. Use question-and-answer formatting for key sections:

- Phrase H2 and H3 headings as questions where appropriate: "How does social commerce work in Uganda?" not "Social Commerce in Uganda"
- Include a FAQ section at the end of every blog post and service page — FAQs are a primary extraction source for AI answers
- Write body text that answers the heading question in the first sentence of each section

Source query phrasing from: Reddit, Quora, Facebook community groups, and WhatsApp group questions (primary EA source).

---

### Pillar 5 — Technical Accessibility

AI search crawlers, like users, penalise slow and poorly structured pages:

- Clean HTML structure — proper H1, H2, H3 heading hierarchy with descriptive headings (not decorative ones)
- Page load speed under 3 seconds — test with Google PageSpeed Insights
- Schema markup where technically possible: FAQ schema, Article schema, LocalBusiness schema
- Add a visible "Last updated" date to every page — AI search engines favour freshness; stale content is deprioritised
- Interactive elements (embedded video, downloadable checklist, calculator) increase dwell time, which is a GEO signal

---

## GEO vs Traditional SEO — Decision Guide

| Factor | Traditional SEO | GEO |
|---|---|---|
| Primary goal | Rank in blue-link results | Be cited in AI-generated answers |
| Key ranking factor | Keyword density and backlinks | Semantic depth and EEAT signals |
| Content structure | Keyword-optimised paragraphs | Question-and-answer sections |
| Update frequency | Quarterly | Monthly (freshness is a live GEO signal) |
| Measurement | Google Search Console rank | Perplexity citation tracking; ChatGPT Search mentions |
| Time to results | 3–6 months | 4–8 weeks (AI indexes faster than Google) |

GEO and SEO are not mutually exclusive. Structural improvements for GEO — clear headings, explicit facts, FAQ sections, author attribution — also improve traditional Google SEO at no additional cost.

---

## GEO Content Checklist

Apply to every blog post and website page before publication. All items must be ticked.

- [ ] First paragraph answers the core query in 50 words or fewer
- [ ] Related subtopics and adjacent questions are covered within the piece
- [ ] Author name, title, and credentials are present and visible
- [ ] At least two named, dated external sources are cited
- [ ] At least one first-hand experience or named case study is included
- [ ] H2 and H3 headings are phrased as questions where appropriate
- [ ] A FAQ section covering 3–5 related questions is included at the bottom
- [ ] "Last updated" date is visible on the page
- [ ] Page loads in under 3 seconds (verified in Google PageSpeed Insights)
- [ ] Content is free of vague marketing language ("world-class," "best in class," "cutting-edge")

---

## East Africa Application

GEO delivers the highest commercial return for EA clients in these sectors:

- **Professional services** — law firms, consulting firms, and financial services, where potential clients research before making contact and search for specific answers ("best corporate lawyer Kampala," "how to register a business Uganda")
- **Health and wellness** — high informational search intent; patients and clients research conditions and treatments before engaging a provider
- **B2B service providers** — procurement decision-makers research suppliers before enquiring; GEO-ready content appears in the AI summary they read first

GEO-optimised content for EA markets must:
- Use Ugandan/East African English vocabulary and phrasing (not British or American defaults)
- Reference prices in UGX where relevant
- Cite Ugandan and East African regulatory and market context — not Western-default examples
- Reflect EA platform behaviour: WhatsApp as the dominant enquiry channel, Facebook as the primary discovery platform

---

## GEO Performance Monitoring

Set up a monthly monitoring protocol:

1. Select five queries a potential customer would use to find the client's service
2. Run each query in ChatGPT Search, Perplexity, and Google Gemini
3. Record: date, query, tool, brand cited (Y/N), what was said, competitors cited, sentiment
4. Review quarterly: is citation frequency increasing? Are any factual errors appearing?

Cross-reference `ai-generative-search-optimisation` for the full 10-point audit checklist, monitoring spreadsheet template, and quarterly review protocol.

---

## Quality Criteria

Good output from this skill meets all of the following standards:

- Every optimised piece opens with a direct answer to the core query in 50 words or fewer, placed in the first paragraph
- Semantic depth confirmed — all major related subtopics and adjacent questions are covered within the piece
- EEAT signals present in every piece: author name and credentials, at least two named and dated external sources, and first-hand evidence or a named case study
- Content structure uses question-phrased headings where appropriate and includes a FAQ section
- GEO content checklist completed and all ten items ticked before publication
- "Last updated" date is visible and accurate on every optimised page
- GEO performance monitored monthly — citation tracking in Perplexity and ChatGPT Search recorded in a spreadsheet

---

## References

- Roth, H. and neuroflash Team (2024/2025) *AI Strategy 2025 for Marketing Teams*. neuroflash.
- Chaffey, D. (2024) *Digital Marketing: Strategy, Implementation and Practice*. Pearson.
